import os

from vgazer.command     import RunCommand
from vgazer.exceptions  import CommandError
from vgazer.exceptions  import InstallError
from vgazer.platform    import GetAr
from vgazer.platform    import GetCc
from vgazer.platform    import GetInstallPrefix
from vgazer.store.temp  import StoreTemp
from vgazer.working_dir import WorkingDir

def Install(auth, software, platform, platformData, verbose):
    installPrefix = GetInstallPrefix(platformData)

    cc = GetCc(platformData["target"])
    ar = GetAr(platformData["target"])

    storeTemp = StoreTemp()
    storeTemp.ResolveEmptySubdirectory(software)
    tempPath = storeTemp.GetSubdirectoryPath(software)

    sourceUrl = "https://sourceforge.net/projects/tinyfiledialogs/files/tinyfiledialogs.c/download"
    headerUrl = "https://sourceforge.net/projects/tinyfiledialogs/files/tinyfiledialogs.h/download"

    try:
        with WorkingDir(tempPath):
            RunCommand(
             ["wget", "-P", "./", "-O", "tinyfiledialogs.c", sourceUrl], verbose
            )
            RunCommand(
             ["wget", "-P", "./", "-O", "tinyfiledialogs.h", headerUrl], verbose
            )
            RunCommand(
             [cc, "-c", "tinyfiledialogs.c", "-o", "tinyfiledialogs.o", "-O2",
              "-Wall", "-fPIC"],
             verbose)
            RunCommand(
             [cc, "-shared", "-s", "-o", "libtinyfiledialogs.so",
              "tinyfiledialogs.o"],
             verbose)
            RunCommand(
             [ar, "rcs", "libtinyfiledialogs.a", "tinyfiledialogs.o"],
             verbose)
            if not os.path.exists(installPrefix + "/include"):
                RunCommand(["mkdir", "-p", installPrefix + "/include"], verbose)
            if not os.path.exists(installPrefix + "/lib"):
                RunCommand(["mkdir", "-p", installPrefix + "/lib"], verbose)
            RunCommand(
             ["cp", "./tinyfiledialogs.h", installPrefix + "/include"],
             verbose)
            RunCommand(["cp", "./libtinyfiledialogs.a", installPrefix + "/lib"],
             verbose)
            RunCommand(
             ["cp", "./libtinyfiledialogs.so", installPrefix + "/lib"],
             verbose)
    except CommandError:
        print("Unable to install", software)
        raise InstallError(software + " not installed")

    print(software, "installed")
