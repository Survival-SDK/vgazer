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

    try:
        with WorkingDir(tempPath):
            RunCommand(
             ["git", "clone", "https://github.com/compuphase/minIni.git"],
            verbose)
        clonedDir = os.path.join(tempPath, "minIni")
        with WorkingDir(clonedDir + "/dev"):
            RunCommand(
             [cc, "-O2", "-Wall", "-fPIC", "-c", "minIni.c", "-o", "minIni.o"],
             verbose)
            RunCommand(
             [ar, "rcs", "libminini.a", "minIni.o"],
             verbose)
            if not os.path.exists(installPrefix + "/include"):
                RunCommand(["mkdir", "-p", installPrefix + "/include"], verbose)
            if not os.path.exists(installPrefix + "/lib"):
                RunCommand(["mkdir", "-p", installPrefix + "/lib"], verbose)
            RunCommand(["mkdir", "-p", installPrefix + "/include/minINI"],
             verbose)
            RunCommand(
             ["bash", "-c",
              "cp ./*.h " + installPrefix + "/include/minINI"],
             verbose)
            RunCommand(["cp", "./libminini.a", installPrefix + "/lib"],
             verbose)
    except CommandError:
        print("Unable to install", software)
        raise InstallError(software + " not installed")

    print(software, "installed")
