from github import Github
import os
import requests 
from dotenv import load_dotenv

credits2 = 0 # max is 400

def follow_ratio(username: str) -> int:
    followers = g.get_user(username).followers
    following = g.get_user(username).following
    if (followers / following == 2 / 3):
        credit += 70
    else:
        credit -= 70
    if (followers > 20 and following > 30):
        credit += 50
    else:
        credit -= 50

def starring_repos(username: str) -> int:
   starringRepos = g.get_user(username).get_starred().totalCount

   if (starringRepos > 50):
       credit -= 50
   else:
       credit += 50


def getREADME(username: str):
    repo = g.get_user(username).get_repo(username)
    file = repo.get_readme()
    file_lower = file.lower()
    # print(file.decoded_content)
    bad_words = ["founder", "ceo", "non-profit", "high school", "metaverse", "dogecoin", "taiwan"]
    for i in range:
        if (bad_words[i] in file_lower):
            credit -= 100
        else:
            credit += 200
