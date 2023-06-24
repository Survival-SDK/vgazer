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
             ["git", "clone", "https://github.com/anholt/hash_table.git"],
             verbose)
        clonedDir = os.path.join(tempPath, "hash_table")
        with WorkingDir(clonedDir):
            RunCommand([cc, "-O2", "-c", "hash_table.c", "-o", "hash_table.o"],
             verbose)
            RunCommand([ar, "rcs", "libhash_table.a", "hash_table.o"], verbose)
            if not os.path.exists(includeDir):
                RunCommand(["mkdir", "-p", includeDir], verbose)
            if not os.path.exists(libDir):
                RunCommand(["mkdir", "-p", libDir], verbose)
            RunCommand(["cp", "./hash_table.h", includeDir], verbose)
            RunCommand(["cp", "./libhash_table.a", libDir], verbose)
    except CommandError:
        print("VGAZER: Unable to install", software)
        raise InstallError("{softare} not installed".format(software=software))

    print("VGAZER:", software, "installed")
