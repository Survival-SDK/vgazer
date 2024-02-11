import os

from libvgazer.command    import RunCommand
from libvgazer.exceptions import CommandError
from libvgazer.exceptions import InstallError
from libvgazer.platform   import GetInstallPrefix

def Install(auth, software, platform, platformData, mirrors, verbose):
    installPrefix = GetInstallPrefix(platformData)

    url = (
     "https://raw.githubusercontent.com/Immediate-Mode-UI/Nuklear/master/"
     "nuklear.h"
    )

    try:
        if not os.path.exists(installPrefix + "/include"):
            RunCommand(["mkdir", "-p", installPrefix + "/include"], verbose)
        RunCommand(["wget", "-P", installPrefix + "/include", url], verbose)
    except CommandError:
        print("VGAZER: Unable to install", software)
        raise InstallError(software + " not installed")

    print("VGAZER:", software, "installed")