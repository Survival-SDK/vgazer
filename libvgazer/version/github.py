import libvgazer.version.utils as utils
from libvgazer.exceptions           import GithubApiError
from libvgazer.github_api_error_mgr import GithubApiErrorMgr

def CheckLastCommit(auth, user, repo):
    commits = auth.GetJson(
     "https://api.github.com/repos/" + user + "/" + repo + "/commits")

    with GithubApiErrorMgr(commits, user + "/" + repo) as errMgr:
        if errMgr.IsErrorOccured():
            raise GithubApiError(errMgr.GetErrorText())

    lastCommitDateTime = commits[0]["commit"]["author"]["date"]

    date = lastCommitDateTime.split("T")[0]
    time = lastCommitDateTime.split("T")[1].split("Z")[0]

    return "commit on " + date + " " + time

def CheckGithub(auth, user, repo, ignoreReleases, ignoredTags):
    if ignoreReleases:
        return CheckLastCommit(auth, user, repo)

    releases = auth.GetJson(
     "https://api.github.com/repos/" + user + "/" + repo + "/releases")

    with GithubApiErrorMgr(releases, user + "/" + repo) as errMgr:
        if errMgr.IsErrorOccured():
            raise GithubApiError(errMgr.GetErrorText())

    if len(releases) != 0:
        return utils.GetVersionFromTag(releases[0]["tag_name"])

    tags = auth.GetJson(
     "https://api.github.com/repos/" + user + "/" + repo + "/tags")

    with GithubApiErrorMgr(tags, user + "/" + repo) as errMgr:
        if errMgr.IsErrorOccured():
            raise GithubApiError(errMgr.GetErrorText())

    tagNum = 0
    for tag in tags:
        if tag["name"] in ignoredTags:
            tagNum = tagNum + 1
        else:
            break

    if len(tags) != 0:
        return utils.GetVersionFromTag(tags[tagNum]["name"])

    return CheckLastCommit(auth, user, repo)
