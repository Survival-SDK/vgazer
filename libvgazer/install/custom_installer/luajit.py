import os

from libvgazer.command     import RunCommand
from libvgazer.exceptions  import CommandError
from libvgazer.exceptions  import InstallError
from libvgazer.platform    import GetInstallPrefix
from libvgazer.platform    import GetTriplet
from libvgazer.store.temp  import StoreTemp
from libvgazer.version.git import GetLastTag
from libvgazer.working_dir import WorkingDir

def Install(software, platform, platformData, verbose):
    installPrefix = GetInstallPrefix(platformData)
    triplet = GetTriplet(platformData["target"])

    storeTemp = StoreTemp()
    storeTemp.ResolveEmptySubdirectory(software)
    tempPath = storeTemp.GetSubdirectoryPath(software)

    try:
        with WorkingDir(tempPath):
            RunCommand(
             ["git", "clone", "https://luajit.org/git/luajit.git", "."],
             verbose)
            RunCommand(
             [
              "git", "checkout",
              GetLastTag("https://luajit.org/git/luajit.git")
             ],
             verbose)
            RunCommand(
             [
              "make", "-j{cores_count}".format(cores_count=os.cpu_count()),
              "CFLAGS=-fPIC", "BUILDMODE=static",
              "CROSS={triplet}-".format(triplet=triplet),
              "TARGET_SYS={os}".format(
               os=platformData["target"].GetOs().capitalize()),
              "TARGET_AR={triplet}-gcc-ar rcus".format(triplet=triplet),
              "E=@:", "Q="
             ],
             verbose)
            RunCommand(
             ["make", "install",
              "PREFIX={prefix}".format(prefix=installPrefix)],
             verbose)
    except CommandError:
        print("VGAZER: Unable to install", software)
        raise InstallError(
         "{software} not installed".format(software=software))

    print("VGAZER:", software, "installed")
