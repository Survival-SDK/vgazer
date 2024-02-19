import os

from libvgazer.command     import RunCommand
from libvgazer.exceptions  import CommandError
from libvgazer.exceptions  import InstallError
from libvgazer.platform    import GetAr
from libvgazer.platform    import GetCc
from libvgazer.platform    import GetInstallPrefix
from libvgazer.store.temp  import StoreTemp
from libvgazer.working_dir import WorkingDir

def Install(software, platform, platformData, verbose):
    installPrefix = GetInstallPrefix(platformData)
    ar = GetAr(platformData["target"])
    cc = GetCc(platformData["target"])

    storeTemp = StoreTemp()
    storeTemp.ResolveEmptySubdirectory(software)
    tempPath = storeTemp.GetSubdirectoryPath(software)

    try:
        with WorkingDir(tempPath):
            RunCommand(
             ["git", "clone", "https://github.com/jibsen/scv.git", "."],
             verbose)
            RunCommand([cc, "-O2", "-fPIC", "-o", "scv.o", "-c", "scv.c"],
             verbose)
            RunCommand([ar, "rcs", "libscv.a", "scv.o"], verbose)
            if not os.path.exists(
             "{prefix}/include".format(prefix=installPrefix)):
                RunCommand(
                 [
                  "mkdir", "-p",
                  "{prefix}/include".format(prefix=installPrefix)
                 ],
                 verbose
                )
            if not os.path.exists("{prefix}/lib".format(prefix=installPrefix)):
                RunCommand(
                 ["mkdir", "-p", "{prefix}/lib".format(prefix=installPrefix)],
                 verbose)
            RunCommand(
             ["cp", "./scv.h",
              "{prefix}/include".format(prefix=installPrefix)],
             verbose)
            RunCommand(
             ["cp", "./libscv.a", "{prefix}/lib".format(prefix=installPrefix)],
             verbose)
    except CommandError:
        print("VGAZER: Unable to install", software)
        raise InstallError(
         "{software} not installed".format(software=software))

    print("VGAZER:", software, "installed")
