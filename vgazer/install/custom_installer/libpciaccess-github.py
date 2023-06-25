import os

from vgazer.command              import GetCommandOutputUtf8
from vgazer.command              import RunCommand
from vgazer.exceptions           import CommandError
from vgazer.exceptions           import GithubApiError
from vgazer.exceptions           import InstallError
from vgazer.github_api_error_mgr import GithubApiErrorMgr
from vgazer.platform             import GetInstallPrefix
from vgazer.platform             import GetTriplet
from vgazer.store.temp           import StoreTemp
from vgazer.working_dir          import WorkingDir

def Install(auth, software, platform, platformData, mirrors, verbose):
    installPrefix = GetInstallPrefix(platformData)
    targetTriplet = GetTriplet(platformData["target"])

    storeTemp = StoreTemp()
    storeTemp.ResolveEmptySubdirectory(software)
    tempPath = storeTemp.GetSubdirectoryPath(software)

    try:
        tags = auth["github"].GetJson(
         "https://api.github.com/repos/freedesktop/xorg-libpciaccess/tags")
    except ConnectionError:
        print("VGAZER: Unable to know last version of", software)
        raise InstallError(software + " not installed")

    with GithubApiErrorMgr(tags, "freedesktop/xorg-libpciaccess") as errMgr:
        if errMgr.IsErrorOccured():
            raise GithubApiError(errMgr.GetErrorText())

    tagNum = 0
    for tag in tags:
        if tag["name"] in [
         "xf86-video-xgi-0.9.1",
        ]:
            tagNum = tagNum + 1
        else:
            break

    tarballUrl = tags[tagNum]["tarball_url"]
    tarballShortFilename = tarballUrl.split("/")[-1]

    try:
        with WorkingDir(tempPath):
            RunCommand(["wget", "-P", "./", tarballUrl], verbose)
            RunCommand(
             ["tar", "--verbose", "--extract", "--gzip", "--file",
              tarballShortFilename],
             verbose)
            output = GetCommandOutputUtf8(
             ["tar", "--list", "--file", tarballShortFilename]
            )
            extractedDir = os.path.join(tempPath,
             output.splitlines()[0].split("/")[0])
        with WorkingDir(extractedDir):
            RunCommand(
             ["./autogen.sh", "--host=" + targetTriplet,
              "--prefix=" + installPrefix],
             verbose)
            RunCommand(
             ["make", "-j{cores_count}".format(cores_count=os.cpu_count())],
             verbose)
            RunCommand(["make", "install"], verbose)
    except CommandError:
        print("VGAZER: Unable to install", software)
        raise InstallError(software + " not installed")

    print("VGAZER:", software, "installed")
