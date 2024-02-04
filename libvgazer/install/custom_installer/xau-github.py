import os
import requests

from libvgazer.command              import GetCommandOutputUtf8
from libvgazer.command              import RunCommand
from libvgazer.exceptions           import CommandError
from libvgazer.exceptions           import GithubApiError
from libvgazer.exceptions           import InstallError
from libvgazer.github_api_error_mgr import GithubApiErrorMgr
from libvgazer.platform             import GetInstallPrefix
from libvgazer.platform             import GetTriplet
from libvgazer.store.temp           import StoreTemp
from libvgazer.working_dir          import WorkingDir

def Install(auth, software, platform, platformData, mirrors, verbose):
    installPrefix = GetInstallPrefix(platformData)
    targetTriplet = GetTriplet(platformData["target"])

    storeTemp = StoreTemp()
    storeTemp.ResolveEmptySubdirectory(software)
    tempPath = storeTemp.GetSubdirectoryPath(software)

    try:
        tags = auth["github"].GetJson(
         "https://api.github.com/repos/freedesktop/xorg-libXau/tags")
    except requests.exceptions.ConnectionError:
        print("VGAZER: Unable to know last version of", software)
        raise InstallError("{software} not installed".format(software=software))

    with GithubApiErrorMgr(tags, "freedesktop/xorg-libXau") as errMgr:
        if errMgr.IsErrorOccured():
            raise GithubApiError(errMgr.GetErrorText())

    tagNum = 0
    for tag in tags:
        if tag["name"] in [
         "xo-6_7_0",
         "xf86-012804-2330",
         "xf86-4_4_99_1",
         "xf86-4_4_0",
         "xf86-4_3_99_903",
         "xf86-4_3_99_903_special",
         "xf86-4_3_99_902",
         "xf86-4_3_99_901",
         "xf86-4_3_99_16",
         "xf86-4_3_0_1",
         "sco_port_update-base",
         "rel-0-6-1",
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
             ["./configure", "--host={triplet}".format(triplet=targetTriplet),
              "--prefix={prefix}".format(prefix=installPrefix),
              "PKG_CONFIG_PATH={prefix}/lib/pkgconfig".format(
               prefix=installPrefix)
             ],
             verbose)
            RunCommand(
             ["make", "-j{cores_count}".format(cores_count=os.cpu_count())],
             verbose)
            RunCommand(["make", "install"], verbose)

    except CommandError:
        print("VGAZER: Unable to install", software)
        raise InstallError("{software} not installed".format(software=software))

    print("VGAZER:", software, "installed")
