import os

import dotenv
from github import Github

import Bio
from RepoAnalyzer import RepoAnalyzer

dotenv.load_dotenv()
TOKEN = os.getenv('TOKEN')
g = Github(TOKEN)


def analyze(user: str) -> int:
    usr = g.get_user(user)
    scorer = RepoAnalyzer(usr=usr)
    social_credits = 0
    social_credits += scorer.calculate_score()
    social_credits += Bio.starring_repos(usr)
    social_credits += Bio.follow_ratio(usr)
    social_credits += Bio.getREADME(usr, user)
    print(social_credits)

    return social_credits
