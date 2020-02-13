import os
import requests

from vgazer.command         import RunCommand
from vgazer.exceptions      import CommandError
from vgazer.exceptions      import InstallError
from vgazer.install.utils   import SourceforgeDownloadTarballWhileErrorcodeFour
from vgazer.platform        import GetAr
from vgazer.platform        import GetCc
from vgazer.platform        import GetInstallPrefix
from vgazer.store.temp      import StoreTemp
from vgazer.working_dir     import WorkingDir

def Install(auth, software, platform, platformData, mirrors, verbose):
    installPrefix = GetInstallPrefix(platformData)

    cc = GetCc(platformData["target"])
    ar = GetAr(platformData["target"])

    storeTemp = StoreTemp()
    storeTemp.ResolveEmptySubdirectory(software)
    tempPath = storeTemp.GetSubdirectoryPath(software)

    sourceforgeMirrorsManager = mirrors["sourceforge"].CreateMirrorsManager(
     ["https", "http"])

    filename = requests.get(
     "https://sourceforge.net/projects/tinyfiledialogs/best_release.json"
    ).json()["release"]["filename"]
    archiveShortFilename = filename.split("/")[-1]

    try:
        with WorkingDir(tempPath):
            SourceforgeDownloadTarballWhileErrorcodeFour(
             sourceforgeMirrorsManager, "tinyfiledialogs", filename, verbose)
            RunCommand(["unzip", archiveShortFilename], verbose)
        extractedDir = os.path.join(tempPath, archiveShortFilename[0:-4])
        with WorkingDir(extractedDir):
            RunCommand(
             [cc, "-c", "tinyfiledialogs.c", "-o", "tinyfiledialogs.o", "-O2",
              "-Wall", "-fPIC"],
             verbose)
            RunCommand(
             [ar, "rcs", "libtinyfiledialogs.a", "tinyfiledialogs.o"],
             verbose)
            if not os.path.exists(installPrefix + "/include"):
                RunCommand(["mkdir", "-p", installPrefix + "/include"],
                 verbose)
            if not os.path.exists(installPrefix + "/lib"):
                RunCommand(["mkdir", "-p", installPrefix + "/lib"], verbose)
            RunCommand(
             ["cp", "./tinyfiledialogs.h", installPrefix + "/include"],
             verbose)
            RunCommand(
             ["cp", "./libtinyfiledialogs.a", installPrefix + "/lib"],
             verbose)
    except CommandError:
        print("VGAZER: Unable to install", software)
        raise InstallError(software + " not installed")

    print("VGAZER:", software, "installed")
