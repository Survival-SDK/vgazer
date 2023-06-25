import os
import requests

from vgazer.command     import RunCommand
from vgazer.exceptions  import CommandError
from vgazer.exceptions  import InstallError
from vgazer.exceptions  import UnknownTargetArch
from vgazer.platform    import GetInstallPrefix
from vgazer.platform    import GetTriplet
from vgazer.store.temp  import StoreTemp
from vgazer.working_dir import WorkingDir

def Install(auth, software, platform, platformData, mirrors, verbose):
    installPrefix = GetInstallPrefix(platformData)
    targetTriplet = GetTriplet(platformData["target"])

    storeTemp = StoreTemp()
    storeTemp.ResolveEmptySubdirectory(software)
    tempPath = storeTemp.GetSubdirectoryPath(software)

    tarballUrl = requests.get(
     "https://sourceforge.net/projects/mpg123/best_release.json"
    ).json()["release"]["url"]
    tarballShortFilename = tarballUrl.split("/")[-2]

    if platformData["target"].GetArch() == "i386":
        cpu = "i386_fpu"
    elif platformData["target"].GetArch() == "i486":
        cpu = "i486"
    elif platformData["target"].GetArch() in ["i586", "i686"]:
        cpu = "i586_dither"
    elif platformData["target"].GetArch() == "x86_64":
        cpu = "x86-64"
    else:
        raise UnknownTargetArch(
         "Unknown target architecture: " + platformData["target"].GetArch())

    try:
        with WorkingDir(tempPath):
            RunCommand(
             ["wget", "-P", "./", "-O", tarballShortFilename, tarballUrl],
             verbose)
            RunCommand(
             ["tar", "--verbose", "--extract", "--bzip2", "--file",
              tarballShortFilename],
             verbose)
        extractedDir = os.path.join(tempPath, tarballShortFilename[0:-8])
        with WorkingDir(extractedDir):
            RunCommand(
             ["./configure", "--host=" + targetTriplet,
              "--prefix=" + installPrefix,
              "--enable-nagging=no", "--enable-ipv6=yes",
              "--enable-network=yes", "--with-cpu=" + cpu,
              "--with-audio=dummy", "--with-default-audio=dummy"],
             verbose)
            RunCommand(
             ["make", "-j{cores_count}".format(cores_count=os.cpu_count())],
             verbose)
            RunCommand(["make", "install"], verbose)
    except CommandError:
        print("VGAZER: Unable to install", software)
        raise InstallError(software + " not installed")

    print("VGAZER:", software, "installed")
