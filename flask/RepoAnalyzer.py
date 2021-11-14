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
            print(f"Looking through... {repo.name}")
            self.contributors += repo.get_contributors().totalCount
            self.good_repos += is_good_repo(repo)
            self.dead_forks += is_dead_fork(repo)
            self.stars += repo.stargazers_count

    # 0-150
    def score_stars(self) -> int:
        stars = min(self.stars, 250)
        return int(62.6 * math.log((stars + 1), 10))

    # 0-100
    def score_number_of_repos(self) -> int:
        repo_num = min(self.repos.totalCount, 100)
        return int(50 * math.log((repo_num + 1), 10))

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

    def calculate_score(self) -> int:
        contributors = self.score_contributors()
        stars = self.score_stars()
        number = self.score_number_of_repos()
        dead = self.score_dead_forks()
        good = self.score_good_repos()
        print(f'Contributor score: {contributors}\n'
              f'Stars score: {stars}\n'
              f'Repo amount score: {number}\n'
              f'Dead Fork score: {dead}\n'
              f'Good Repo score: {good}')
        return contributors + stars + number + dead + good


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
