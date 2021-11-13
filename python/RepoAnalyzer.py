from github.PaginatedList import PaginatedList
from github.Repository import Repository
import main


def is_dead_fork(repo: Repository):
    print(repo.get_forks())


def analyze_repos(repos: PaginatedList) -> int:
    score: int = 0
    repo_num: int = repos.totalCount
    stars: int = 0
    contributors: int
    for repo in repos:
        repo: Repository
        stars += repo.stargazers_count
    return score


analyze_repos(main.g.get_user().get_repos())
