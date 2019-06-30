#import configparser
import requests
import vgazer.version.utils as utils

class GithubApiRateLimitExceeded(Exception):
    def __init__(self, message):
        super().__init__(message)

class LostConfigEntry(Exception):
    def __init__(self, message):
        super().__init__(message)

def ApiRateLimitExceeded(responseJson):
    if "message" in responseJson:
        if (responseJson["documentation_url"]
         == "https://developer.github.com/v3/#rate-limiting"):
            return True
    return False

def CheckLastCommit(auth, user, repo):
    commits = auth.GetJson(
     "https://api.github.com/repos/" + user + "/" + repo + "/commits")

    if ApiRateLimitExceeded(commits):
        raise GithubApiRateLimitExceeded(
         "Github API rate limit reached while searching last commit info of "
         "resource: "
         + project
        )

    lastCommitDateTime = commits[0]["commit"]["author"]["date"]

    date = lastCommitDateTime.split("T")[0]
    time = lastCommitDateTime.split("T")[1].split("Z")[0]

    return "commit on " + date + " " + time

def CheckGithub(auth, project):
    user = project["user"]
    repo = project["repo"]

    if "ignore_releases" in project.keys():
        return CheckLastCommit(auth, user, repo)

    releases = auth.GetJson(
     "https://api.github.com/repos/" + user + "/" + repo + "/releases")

    if ApiRateLimitExceeded(releases):
        raise GithubApiRateLimitExceeded(
         "Github API rate limit reached while searching last version of "
         "resource: "
         + project
        )

    if len(releases) != 0:
        return utils.GetVersionFromTag(releases[0]["tag_name"])

    tags = auth.GetJson(
     "https://api.github.com/repos/" + user + "/" + repo + "/tags")

    if ApiRateLimitExceeded(tags):
        raise GithubApiRateLimitExceeded(
         "Github API rate limit reached while searching last version of "
         "resource: "
         + project
        )

    if len(tags) != 0:
        return utils.GetVersionFromTag(tags[0]["name"])

    return CheckLastCommit(auth, user, repo)

