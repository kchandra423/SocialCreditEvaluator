from RepoAnalyzer import RepoAnalyzer
from github import Github
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')
g = Github(TOKEN)



def main(user: str):
    scorer = RepoAnalyzer(usr=g.get_user(user))
    print(scorer.calculate_score())


if __name__ == "__main__":
    main(input("Which user would you like to evaluate?"))
