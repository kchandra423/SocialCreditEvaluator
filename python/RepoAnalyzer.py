import math

from github.AuthenticatedUser import AuthenticatedUser
from github.Repository import Repository


class RepoAnalyzer:

    def __init__(self, usr: AuthenticatedUser):
        self.repos = usr.get_repos()
        self.good_repos = 0
        self.stars: int = 0
        self.dead_forks: int = 0
        self.contributors: int = 0
        for repo in self.repos:
            repo: Repository
            self.contributors += repo.get_contributors().totalCount
            self.good_repos += is_good_repo(repo)
            self.dead_forks += is_dead_fork(repo)
            self.stars += repo.stargazers_count

    # 0-150
    def score_stars(self) -> int:
        return int(math.pow(1.010086, self.stars) - 1)

    # 0-100
    def score_number_of_repos(self) -> int:
        repo_num = min(self.repos.totalCount, 100)
        return int(50 * math.log((repo_num + 1)))

    # 0-50
    def score_dead_forks(self) -> int:
        percentage = self.dead_forks / self.repos.totalCount
        return int((1 - percentage) * 50)

    # 0-50
    def score_contributors(self) -> int:
        contributors = min(self.contributors, 50)
        return contributors

    # 0-150
    def score_good_repos(self) -> int:
        percentage = self.good_repos / self.repos.totalCount
        return int((1 - percentage) * 150)

    def calculate_score(self):
        contributors =
        return self.score_contributors() + self.score_stars() + self.score_number_of_repos() + self.score_dead_forks() \
               + self.score_good_repos()


def is_dead_fork(repo: Repository) -> bool:
    if repo.parent is not None:
        if repo.get_commits().totalCount < repo.parent.get_commits().totalCount:
            return True
    return False


def is_good_repo(repo: Repository) -> bool:
    try:
        repo.get_readme()
        repo.get_tags()
        repo.get_license()
    except Exception:
        return False
    if repo.description is None:
        return False
    return True
