"""
    gh.py: autoamtially generate project info from GitHub
"""
import json
from datetime import datetime, timedelta
from functools import lru_cache, wraps

import requests
from github import Github, GithubException


def timed_lru_cache(seconds: int, maxsize: int = None):
    """
    Timed lru cache decorator that takes a seconds arg
    in addition to a maxsize arg

    Args
    ----
        - seconds (int): expiration window in secondds
        - maxsize (int): cache size
    """

    def wrapper_cache(func):
        """timed cache implementation"""
        func = lru_cache(maxsize=maxsize)(func)
        func.lifetime = timedelta(seconds=seconds)
        func.expiration = datetime.utcnow() + func.lifetime

        @wraps(func)
        def wrapped_func(*args, **kwargs):
            # check expiration
            if datetime.utcnow() >= func.expiration:
                func.cache_clear()
                func.expiration = datetime.utcnow() + func.lifetime
            return func(*args, **kwargs)

        return wrapped_func

    return wrapper_cache


@timed_lru_cache(3600)
def github_content(pat: str, username: str, saved: str = None):
    """
    Automatically pull project info from GitHub using

    PAT & V3 API

    Args
    ----
        - pat (str): github access token if none will return empty dict
    """
    if saved:
        with open(saved, "r", encoding="utf8") as github_file:
            return json.load(github_file)
    repos = []
    if pat is not None:
        gcli = Github(pat)
        try:
            github_repos = list(gcli.get_user().get_repos())
        except GithubException:
            return []
        for repo in github_repos:
            if (
                repo.owner.login == username
                and not repo.private
                and repo.name != username
                and not repo.fork
            ):
                headers = {"Authorization": f"token {pat}"}
                resp = requests.get(repo.languages_url, headers=headers, timeout=30)
                languages = []
                if resp.status_code == 200:
                    languages = list(resp.json().keys())
                repo = {
                    "name": repo.name,
                    "created": repo.created_at.strftime("%m-%d-%Y"),
                    "updated": repo.updated_at.strftime("%m-%d-%Y"),
                    "commits": repo.get_commits().totalCount,
                    "topics": repo.get_topics(),
                    "languages": languages,
                    "description": repo.description,
                    "link": repo.html_url,
                }
                repos.append(repo)
    with open(saved, "w", encoding="utf8") as github_file:
        json.dump(repos, github_file)
    return repos
