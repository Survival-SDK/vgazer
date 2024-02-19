import os

from libvgazer.command     import RunCommand
from libvgazer.exceptions  import CommandError
from libvgazer.exceptions  import InstallError
from libvgazer.store.temp  import StoreTemp
from libvgazer.version.git import GetLastTag
from libvgazer.working_dir import WorkingDir

def Install(software, platform, platformData, verbose):
    storeTemp = StoreTemp()
    storeTemp.ResolveEmptySubdirectory(software)
    tempPath = storeTemp.GetSubdirectoryPath(software)

    try:
        with WorkingDir(tempPath):
            RunCommand(
             ["git", "clone", "git://git.savannah.gnu.org/libtool.git"],
             verbose)
        clonedDir = os.path.join(tempPath, "libtool")
        with WorkingDir(clonedDir):
            RunCommand(
             [
              "git", "checkout",
              GetLastTag("git://git.savannah.gnu.org/libtool.git")
             ],
             verbose)
            RunCommand(["./bootstrap"], verbose)
            RunCommand(["./configure", "--prefix=/usr/local"], verbose)
            RunCommand(
             ["make", "-j{cores_count}".format(cores_count=os.cpu_count())],
             verbose)
            RunCommand(["make", "install"], verbose)
    except CommandError:
        print("VGAZER: Unable to install", software)
        raise InstallError(
         "{software} not installed".format(software=software))

    print("VGAZER:", software, "installed")
