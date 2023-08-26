import os

from vgazer.command     import RunCommand
from vgazer.exceptions  import CommandError
from vgazer.exceptions  import InstallError
from vgazer.platform    import GetAr
from vgazer.platform    import GetCc
from vgazer.platform    import GetInstallPrefix
from vgazer.store.temp  import StoreTemp
from vgazer.working_dir import WorkingDir

def Install(auth, software, platform, platformData, mirrors, verbose):
    installPrefix = GetInstallPrefix(platformData)
    ar = GetAr(platformData["target"])
    cc = GetCc(platformData["target"])

    storeTemp = StoreTemp()
    storeTemp.ResolveEmptySubdirectory(software)
    tempPath = storeTemp.GetSubdirectoryPath(software)

    try:
        with WorkingDir(tempPath):
            RunCommand(
             ["git", "clone", "https://github.com/jibsen/scv.git"],
             verbose)
        clonedDir = os.path.join(tempPath, "scv")
        with WorkingDir(clonedDir):
            RunCommand([cc, "-O2", "-fPIC", "-o", "scv.o", "-c", "scv.c"],
             verbose)
            RunCommand([ar, "rcs", "libscv.a", "scv.o"], verbose)
            if not os.path.exists(
             "{prefix}/include".format(prefix=installPrefix)):
                RunCommand(
                 [
                  "mkdir", "-p", "{prefix}/include".format(prefix=installPrefix)
                 ],
                 verbose
                )
            if not os.path.exists("{prefix}/lib".format(prefix=installPrefix)):
                RunCommand(
                 ["mkdir", "-p", "{prefix}/lib".format(prefix=installPrefix)],
                 verbose)
            RunCommand(
             ["cp", "./scv.h", "{prefix}/include".format(prefix=installPrefix)],
             verbose)
            RunCommand(
             ["cp", "./libscv.a", "{prefix}/lib".format(prefix=installPrefix)],
             verbose)
    except CommandError:
        print("VGAZER: Unable to install", software)
        raise InstallError("{software} not installed".format(software=software))

    print("VGAZER:", software, "installed")
