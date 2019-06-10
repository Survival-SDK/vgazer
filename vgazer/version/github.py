import configparser
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
        if (responseJson["documentation_url"] == "https://developer.github.com/v3/#rate-limiting"):
            return True
    return False

def CheckLastCommit(auth, user, repo):
    commits = auth.GetJson(
     "https://api.github.com/repos/" + user + "/" + repo + "/commits")

    if ApiRateLimitExceeded(commits):
        raise GithubApiRateLimitExceeded(
         "Github API rate limit reached while searching last commit info of resource: "
         + project
        )

    lastCommitDateTime = commits[0]["commit"]["author"]["date"]

    date = lastCommitDateTime.split("T")[0]
    time = lastCommitDateTime.split("T")[1].split("Z")[0]

    return "commit on " + date + " " + time

def CheckGithub(auth, project):
    config = configparser.ConfigParser()
    config.read("github_projects.ini")

    if project not in config:
        raise LostConfigEntry(
         "There is not entry in configfile for project: " + project)

    user = config[project]["user"]
    repo = config[project]["repo"]

    if "ignore_releases" in config[project].keys():
        return CheckLastCommit(auth, user, repo)

    releases = auth.GetJson(
     "https://api.github.com/repos/" + user + "/" + repo + "/releases")

    if ApiRateLimitExceeded(releases):
        raise GithubApiRateLimitExceeded(
         "Github API rate limit reached while searching last version of resource: "
         + project
        )

    if len(releases) == 0:
        return CheckLastCommit(auth, user, repo)

    return utils.GetVersionFromTag(releases[0]["tag_name"])
