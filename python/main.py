
from github import Github
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')
g = Github(TOKEN)



def main(user: str):
    print(type(g.get_user().get_repos()))


if __name__ == "__main__":
    main(input("Which user would you like to evaluate?"))
