"""
    gh.py: autoamtially generate project info from GitHub
"""
from functools import lru_cache, wraps
from datetime import datetime, timedelta

import requests
from github import Github


def timed_lru_cache(seconds: int, maxsize: int = None):
    """
    timed lru cache decorator that takes a seconds arg
    in addition to a maxsize arg

    params:

    :param seconds (int): expiration window in secondds
    :param maxsize (int): cache size
    """

    def wrapper_cache(func):
        """timed cache implementation"""
        # using lru_cache
        func = lru_cache(maxsize=maxsize)(func)
        # set lifetime
        func.lifetime = timedelta(seconds=seconds)
        # set expiration
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
def github_projects(pat: str, username: str):
    """
    automatically pull project info from GitHub using

    PAT & V3 API

    params:

    :param pat (str): github access token if none will return empty dict
    """
    repos = []
    if pat is not None:
        gcli = Github(pat)
        for repo in gcli.get_user().get_repos():
            if (
                repo.owner.login == username
                and not repo.private
                and repo.name != username
            ):
                headers = {"Authorization": f"token {pat}"}
                resp = requests.get(repo.languages_url, headers=headers)
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
    return repos
