import os

from libvgazer.command     import RunCommand
from libvgazer.exceptions  import CommandError
from libvgazer.exceptions  import InstallError
from libvgazer.platform    import GetInstallPrefix
from libvgazer.store.temp  import StoreTemp
from libvgazer.working_dir import WorkingDir

def Install(software, platform, platformData, verbose):
    installPrefix = GetInstallPrefix(platformData)

    storeTemp = StoreTemp()
    storeTemp.ResolveEmptySubdirectory(software)
    tempPath = storeTemp.GetSubdirectoryPath(software)

    url = ("https://raw.githubusercontent.com/bilke/cmake-modules/master/"
     "CodeCoverage.cmake")

    try:
        with WorkingDir(tempPath):
            RunCommand(
             [
              "git", "clone", "https://github.com/bilke/cmake-modules.git", "."
             ],
             verbose)

            if not os.path.exists(installPrefix + "/lib/cmake/cmake-modules"):
                RunCommand(
                 ["mkdir", "-p", installPrefix + "/lib/cmake/cmake-modules"],
                 verbose)
            RunCommand(
             [
              "cp", "./CodeCoverage.cmake",
              installPrefix + "/lib/cmake/cmake-modules"
             ],
             verbose)
    except CommandError:
        print("VGAZER: Unable to install", software)
        raise InstallError(software + " not installed")

    print("VGAZER:", software, "installed")
