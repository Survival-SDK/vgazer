import os
import requests

from vgazer.command         import RunCommand
from vgazer.exceptions      import CommandError
from vgazer.exceptions      import InstallError
from vgazer.install.utils   import SourceforgeDownloadTarballWhileErrorcodeFour
from vgazer.platform        import GetAr
from vgazer.platform        import GetCc
from vgazer.platform        import GetInstallPrefix
from vgazer.platform        import GetRanlib
from vgazer.store.temp      import StoreTemp
from vgazer.working_dir     import WorkingDir

def Install(auth, software, platform, platformData, mirrors, verbose):
    installPrefix = GetInstallPrefix(platformData)
    cc = GetCc(platformData["target"])
    ar = GetAr(platformData["target"])
    ranlib = GetRanlib(platformData["target"])

    storeTemp = StoreTemp()
    storeTemp.ResolveEmptySubdirectory(software)
    tempPath = storeTemp.GetSubdirectoryPath(software)

    sourceforgeMirrorsManager = mirrors["sourceforge"].CreateMirrorsManager(
     ["https", "http"])

    filename = requests.get(
     "https://sourceforge.net/projects/bzip2/best_release.json"
    ).json()["release"]["filename"]
    tarballShortFilename = filename.split("/")[-1]

    try:
        with WorkingDir(tempPath):
            SourceforgeDownloadTarballWhileErrorcodeFour(
             sourceforgeMirrorsManager, "bzip2", filename, verbose)
            RunCommand(
             ["tar", "--verbose", "--extract", "--gzip", "--file",
              tarballShortFilename],
             verbose)
        extractedDir = os.path.join(tempPath, tarballShortFilename[0:-7])
        with WorkingDir(extractedDir):
            RunCommand(
             ["make", "CC=" + cc, "AR=" + ar, "RANLIB=" + ranlib,
              "CFLAGS=-Wall -Winline -O2 -g -D_FILE_OFFSED_BITS=64 -fPIC"],
             verbose)
            RunCommand(["make", "install", "PREFIX=" + installPrefix], verbose)
            RunCommand(
             ["make", "-f", "Makefile-libbz2_so", "CC=" + cc],
             verbose)
            RunCommand(
             ["sh", "-c", "ln -s ./libbz2.so.?.? ./libbz2.so"],
             verbose)
            RunCommand(["cp", "./libbz2.so", installPrefix + "/lib"],
             verbose)
    except CommandError:
        print("VGAZER: Unable to install", software)
        raise InstallError(software + " not installed")

    print("VGAZER:", software, "installed")
