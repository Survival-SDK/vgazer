import os

from libvgazer.command     import RunCommand
from libvgazer.exceptions  import CommandError
from libvgazer.exceptions  import InstallError
from libvgazer.platform    import GetAr
from libvgazer.platform    import GetCc
from libvgazer.platform    import GetInstallPrefix
from libvgazer.store.temp  import StoreTemp
from libvgazer.version.git import GetLastTag
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
             ["git", "clone", "https://github.com/XadillaX/xmempool.git", "."],
             verbose)
            RunCommand(
             [
              "git", "checkout",
              GetLastTag("https://github.com/XadillaX/xmempool.git")
             ],
             verbose)
            RunCommand(
             ["sed", "-i",
              "s/(unsigned int)pool->start,/pool->start,/g; "
              "s/(unsigned int)pool->end);/pool->end);/g",
              "xmempool.c"],
             verbose)
            RunCommand(
             [
              "make", "-j{cores_count}".format(cores_count=os.cpu_count()),
              "static", "CC=" + cc, "AR=" + ar
             ],
             verbose
            )
            if not os.path.exists(installPrefix + "/include"):
                RunCommand(["mkdir", "-p", installPrefix + "/include"],
                 verbose)
            if not os.path.exists(installPrefix + "/lib"):
                RunCommand(["mkdir", "-p", installPrefix + "/lib"], verbose)
            RunCommand(
             ["cp", "xmempool.a", installPrefix + "/lib/libxmempool.a"],
             verbose)
            RunCommand(["cp", "xmempool.h", installPrefix + "/include"],
             verbose)
    except CommandError:
        print("VGAZER: Unable to install", software)
        raise InstallError(software + " not installed")

    print("VGAZER:", software, "installed")
