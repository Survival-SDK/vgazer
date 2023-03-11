import requests

from vgazer.exceptions           import GithubApiError
from vgazer.github_api_error_mgr import GithubApiErrorMgr

def CheckMuslCrossMake(auth):
    tags = auth.GetJson(
     "https://api.github.com/repos/richfelker/musl-cross-make/tags")

    with GithubApiErrorMgr(tags, "richfelker/musl-cross-make") as errMgr:
        if errMgr.IsErrorOccured():
            raise GithubApiError(errMgr.GetErrorText())

    lastVersionCommitSha = tags[0]["commit"]["sha"]

    lastVersionCommitMakefileUrl = (
     "https://raw.githubusercontent.com/richfelker/musl-cross-make/"
     + lastVersionCommitSha + "/Makefile"
    )

    response = requests.get(lastVersionCommitMakefileUrl)
    html = response.content.decode("utf-8")
    lines = html.splitlines()
    for line in lines:
        if line.startswith("GCC_VER"):
            return line.split("=")[1][1:]
