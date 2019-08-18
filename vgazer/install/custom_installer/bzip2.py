import os
import requests

from vgazer.command     import RunCommand
from vgazer.exceptions  import CommandError
from vgazer.exceptions  import InstallError
from vgazer.exceptions  import TarballLost
from vgazer.platform    import GetInstallPrefix
from vgazer.store.temp  import StoreTemp
from vgazer.working_dir import WorkingDir

def Install(auth, software, platform, platformData, verbose):
    installPrefix = GetInstallPrefix(platformData)

    storeTemp = StoreTemp()
    storeTemp.ResolveEmptySubdirectory(software)
    tempPath = storeTemp.GetSubdirectoryPath(software)

    tarballUrl = requests.get(
     "https://sourceforge.net/projects/bzip2/best_release.json"
    ).json()["release"]["url"]
    tarballShortFilename = tarballUrl.split("/")[-2]

    try:
        with WorkingDir(tempPath):
            RunCommand(["wget", "-P", "./", "-O", tarballShortFilename, tarballUrl], verbose)
            RunCommand(
             ["tar", "--verbose", "--extract", "--gzip", "--file",
              tarballShortFilename],
             verbose)
        extractedDir = os.path.join(tempPath, tarballShortFilename[0:-7])
        with WorkingDir(extractedDir):
            RunCommand(["make", "CFLAGS=-Wall -Winline -O2 -g -D_FILE_OFFSED_BITS=64 -fPIC"], verbose)
            RunCommand(["make", "install", "PREFIX=" + installPrefix], verbose)
            RunCommand(["make", "-f", "Makefile-libbz2_so"], verbose)
            RunCommand(["cp", "./libbz2.so.1.0.6", installPrefix + "/lib"], verbose)
    except CommandError:
        print("Unable to install", software)
        raise InstallError(software + " not installed")

    print(software, "installed")
