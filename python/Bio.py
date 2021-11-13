# import gevent.threading
# from github.PaginatedList import PaginatedList
# from github.Repository import Repository
from github import Github
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')
g = Github(TOKEN)

def follow_ratio(username: str) -> int:
    followers = g.get_user(username).followers
    following = g.get_user(username).following
    # if (followers / following == 2 / 3):
    #     # credit score uppity up
    # if (followers > 20 and following > 30):
    #     # uppity

def starring_repos(username: str) -> int:
    starringRepos = g.get_user(username).has_in_starred()
    print(starringRepos)

starring_repos("rbccawang")

