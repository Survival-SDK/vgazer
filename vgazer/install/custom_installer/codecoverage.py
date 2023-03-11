import os

from vgazer.command     import RunCommand
from vgazer.exceptions  import CommandError
from vgazer.exceptions  import InstallError
from vgazer.platform    import GetInstallPrefix

def Install(auth, software, platform, platformData, mirrors, verbose):
    installPrefix = GetInstallPrefix(platformData)

    url = "https://raw.githubusercontent.com/bilke/cmake-modules/master/CodeCoverage.cmake"

    try:
        if not os.path.exists(installPrefix + "/lib/cmake/cmake-modules"):
            RunCommand(
             ["mkdir", "-p", installPrefix + "/lib/cmake/cmake-modules"],
             verbose)
        RunCommand(
         ["wget", "-P", installPrefix + "/lib/cmake/cmake-modules", url],
         verbose)
    except CommandError:
        print("VGAZER: Unable to install", software)
        raise InstallError(software + " not installed")

    print("VGAZER:", software, "installed")
