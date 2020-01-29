import requests
from vgazer.github_common import GithubCheckApiRateLimitExceeded
from vgazer.exceptions import GithubApiRateLimitExceeded

def CheckMuslCrossMake(auth):
    tags = auth.GetJson(
     "https://api.github.com/repos/richfelker/musl-cross-make/tags")

    if GithubCheckApiRateLimitExceeded(tags):
        raise GithubApiRateLimitExceeded(
         "Github API rate limit reached while searching last version of gcc in"
         "repo: richfelker/musl-cross-make"
        )

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
