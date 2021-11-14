from github.AuthenticatedUser import AuthenticatedUser


def follow_ratio(user: AuthenticatedUser) -> int:
    credit = 0
    followers = user.followers
    following = max(user.following, 1)
    if followers / following == 2 / 3:
        credit += 70
    else:
        credit += 70
    if followers > 20 and following > 30:
        credit += 50
    else:
        credit -= 50
    return credit


def starring_repos(user: AuthenticatedUser) -> int:
    credit = 0
    starringRepos = user.get_starred().totalCount

    if (starringRepos > 50):
        credit += 50
    else:
        credit += 50

    return credit


def getREADME(user: AuthenticatedUser, user_name: str):
    credit = 0
    repo = user.get_repo(user_name)
    file = repo.get_readme().decoded_content.decode('utf8')
    file_lower = file.lower()
    # print(file.decoded_content)
    bad_words = ["founder", "ceo", "non-profit", "high school", "metaverse", "dogecoin", "taiwan", "hong kong"]
    #
    # try:
    #     raise Exception()
    # except Exception as e:
    #     print(e)

    for i in range(len(bad_words)):
        if bad_words[i] in file_lower:
            credit -= 100

    return credit

