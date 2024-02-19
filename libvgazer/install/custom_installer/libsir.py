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
             ["git", "clone", "https://github.com/aremmell/libsir.git", "."],
             verbose)
            RunCommand(
             [
              "git", "checkout",
              GetLastTag("https://github.com/aremmell/libsir.git")
             ],
             verbose)
            RunCommand(
             [
              "make", "-j{cores_count}".format(cores_count=os.cpu_count()),
              "static", "CC={cc}".format(cc=cc), "AR={ar}".format(ar=ar)
             ],
             verbose
            )
            RunCommand(
             [
              "make", "install", "PREFIX={prefix}".format(prefix=installPrefix)
             ],
             verbose
            )
    except CommandError:
        print("VGAZER: Unable to install", software)
        raise InstallError(
         "{software} not installed".format(software=software))

    print("VGAZER:", software, "installed")
