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
             ["git", "clone", "https://github.com/ninja-build/ninja.git", "."],
             verbose)
            RunCommand(
             [
              "git", "checkout",
              GetLastTag("https://github.com/ninja-build/ninja.git",
               hint=r'v1\.\d\d\.\d+')
             ],
             verbose)
            RunCommand(
             ["./configure.py", "--bootstrap", "--verbose"],
             verbose)
            if not os.path.exists("/usr/local/bin"):
                RunCommand(["mkdir", "-p", "/usr/local/bin"], verbose)
            RunCommand(["cp", "./ninja", "/usr/local/bin/ninja"], verbose)
    except CommandError:
        print("VGAZER: Unable to install", software)
        raise InstallError(
         "{software} not installed".format(software=software))

    print("VGAZER:", software, "installed")
