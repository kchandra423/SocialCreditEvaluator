import math

from github.PaginatedList import PaginatedList
from github.Repository import Repository
import main


# 0-150
def score_stars(stars: int) -> int:
    return int(math.pow(1.010086, stars) - 1)


# 0-100
def score_number_of_repos(repos: int) -> int:
    if repos > 100:
        repos = 100
    return int(50 * math.log((repos + 1)))


def calculate_score(repos: int, stars: int, dead_forks: int, contributors: int) -> int:


def is_dead_fork(repo: Repository) -> bool:
    if repo.parent is not None:
        if repo.get_commits().totalCount < repo.parent.get_commits().totalCount:
            return True
    return False


def analyze_repos(repos: PaginatedList) -> int:
    repo_num: int = repos.totalCount
    stars: int = 0
    dead_forks: int = 0
    contributors: int = 0
    for repo in repos:
        repo: Repository
        contributors += repo.get_contributors().totalCount
        dead_forks += is_dead_fork(repo)
        stars += repo.stargazers_count
    return calculate_score(repo_num, stars, dead_forks, contributors)


analyze_repos(main.g.get_user().get_repos())
