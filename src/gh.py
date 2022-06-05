"""
    gh.py: autoamtially generate project info from GitHub
"""
import requests
from github import Github


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
                    "created": repo.created_at,
                    "updated": repo.updated_at,
                    "commits": repo.get_commits().totalCount,
                    "topics": repo.get_topics(),
                    "languages": languages,
                }
                repos.append(repo)
    return repos
