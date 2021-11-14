from RepoAnalyzer import RepoAnalyzer
from github import Github
import os
import Bio
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')
g = Github(TOKEN)


def main(user: str):
    usr = g.get_user(user)
    scorer = RepoAnalyzer(usr=usr)
    social_credits = 0
    social_credits += scorer.calculate_score()
    social_credits += Bio.starring_repos(usr)
    social_credits += Bio.follow_ratio(usr)
    social_credits += Bio.getREADME(usr, user)
    print(social_credits)

    if (social_credits >= 400):
        print("Kumar approves! https://cloud-ew8i9hhs9-hack-club-bot.vercel.app/0image_from_ios.jpg")
    else:
        print("Kumar does not approve. https://cloud-6sg94z1h0-hack-club-bot.vercel.app/0image_from_ios.jpg")


if __name__ == "__main__":
    main(input("Which user would you like to evaluate?"))
