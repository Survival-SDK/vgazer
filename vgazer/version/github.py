import requests
import vgazer.version.utils as utils
from vgazer.github_common import GithubCheckApiRateLimitExceeded
from vgazer.exceptions import GithubApiRateLimitExceeded

def CheckLastCommit(auth, user, repo):
    commits = auth.GetJson(
     "https://api.github.com/repos/" + user + "/" + repo + "/commits")

    if GithubCheckApiRateLimitExceeded(commits):
        raise GithubApiRateLimitExceeded(
         "Github API rate limit reached while searching last commit info of "
         "repo: " + user + "/" + repo
        )

    lastCommitDateTime = commits[0]["commit"]["author"]["date"]

    date = lastCommitDateTime.split("T")[0]
    time = lastCommitDateTime.split("T")[1].split("Z")[0]

    return "commit on " + date + " " + time

def CheckGithub(auth, user, repo, ignoreReleases):
    if ignoreReleases == True:
        return CheckLastCommit(auth, user, repo)

    releases = auth.GetJson(
     "https://api.github.com/repos/" + user + "/" + repo + "/releases")

    if GithubCheckApiRateLimitExceeded(releases):
        raise GithubApiRateLimitExceeded(
         "Github API rate limit reached while searching last version of "
         "repo: " + user + "/" + repo
        )

    if len(releases) != 0:
        return utils.GetVersionFromTag(releases[0]["tag_name"])

    tags = auth.GetJson(
     "https://api.github.com/repos/" + user + "/" + repo + "/tags")

    if GithubCheckApiRateLimitExceeded(tags):
        raise GithubApiRateLimitExceeded(
         "Github API rate limit reached while searching last version of "
         "repo: " + user + "/" + repo
        )

    if len(tags) != 0:
        return utils.GetVersionFromTag(tags[0]["name"])

    return CheckLastCommit(auth, user, repo)

