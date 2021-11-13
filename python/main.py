from github import Github
import os
from dotenv import load_dotenv

load_dotenv()


def main():
    TOKEN = os.getenv('TOKEN')
    g = Github(TOKEN)
    for repo in g.get_user("kchandra423").get_repos():
        print(repo)


if __name__ == "__main__":
    main()
