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
    includeDir = "{prefix}/include".format(prefix=installPrefix)
    libDir = "{prefix}/lib".format(prefix=installPrefix)
    ar = GetAr(platformData["target"])
    cc = GetCc(platformData["target"])

    storeTemp = StoreTemp()
    storeTemp.ResolveEmptySubdirectory(software)
    tempPath = storeTemp.GetSubdirectoryPath(software)

    try:
        with WorkingDir(tempPath):
            RunCommand(
             [
              "git", "clone", "https://github.com/takatak/path_normalize.git",
              "."
             ],
             verbose)
            RunCommand(
             [
              cc, "-O2", "-fPIC", "-c", "path_normalize.c",
              "-o", "path_normalize.o"
             ],
             verbose)
            RunCommand([ar, "rcs", "libpath_normalize.a", "path_normalize.o"],
             verbose)
            if not os.path.exists(includeDir):
                RunCommand(["mkdir", "-p", includeDir], verbose)
            if not os.path.exists(libDir):
                RunCommand(["mkdir", "-p", libDir], verbose)
            RunCommand(["cp", "./path_normalize.h", includeDir], verbose)
            RunCommand(["cp", "./libpath_normalize.a", libDir], verbose)
    except CommandError:
        print("VGAZER: Unable to install", software)
        raise InstallError(
         "{software} not installed".format(software=software))

    print("VGAZER:", software, "installed")
