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
             [
              "git", "clone", "https://gitlab.kitware.com/cmake/cmake.git", "."
             ],
             verbose)
            RunCommand(
             [
              "git", "checkout",
              GetLastTag("https://gitlab.kitware.com/cmake/cmake.git",
               hint=r'v3\.\d\d\.\d+')
             ],
             verbose)
            RunCommand(
             [
              "./bootstrap",
              "--parallel={cores_count}".format(cores_count=os.cpu_count()),
              "--",
              "-DCMAKE_USE_OPENSSL=OFF",
             ],
             verbose)
            RunCommand(["make"], verbose)
            RunCommand(["make", "install"], verbose)
    except CommandError:
        print("VGAZER: Unable to install", software)
        raise InstallError(software + " not installed")

    print("VGAZER:", software, "installed")
