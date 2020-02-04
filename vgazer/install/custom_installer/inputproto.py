import os

from vgazer.command             import RunCommand
from vgazer.exceptions          import CommandError
from vgazer.exceptions          import InstallError
from vgazer.install.utils_xorg  import GetTarballUrl
from vgazer.platform            import GetInstallPrefix
from vgazer.platform            import GetTriplet
from vgazer.store.temp          import StoreTemp
from vgazer.working_dir         import WorkingDir

def Install(auth, software, platform, platformData, mirrors, verbose):
    installPrefix = GetInstallPrefix(platformData)
    targetTriplet = GetTriplet(platformData["target"])

    storeTemp = StoreTemp()
    storeTemp.ResolveEmptySubdirectory(software)
    tempPath = storeTemp.GetSubdirectoryPath(software)

    xorgMirrorsManager = mirrors["xorg"].CreateMirrorsManager(
     ["https", "http"])

    tarballUrl = GetTarballUrl(xorgMirrorsManager, suburl="individual/proto/",
     projectName="inputproto", linksMustHave=["inputproto-", ".tar.gz"],
     linksMustNotHave=[".sig"])
    tarballShortFilename = tarballUrl.split("/")[-1]

    try:
        with WorkingDir(tempPath):
            RunCommand(["wget", "-P", "./", tarballUrl], verbose)
            RunCommand(
             ["tar", "--verbose", "--extract", "--gzip", "--file",
              tarballShortFilename],
             verbose)
        extractedDir = os.path.join(tempPath, tarballShortFilename[0:-7])
        with WorkingDir(extractedDir):
            RunCommand(
             ["./configure", "--host=" + targetTriplet,
              "--prefix=" + installPrefix],
             verbose)
            RunCommand(["make", "install"], verbose)
    except CommandError:
        print("VGAZER: Unable to install", software)
        raise InstallError(software + " not installed")

    print("VGAZER:", software, "installed")
