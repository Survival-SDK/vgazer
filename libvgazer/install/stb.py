import os

from libvgazer.command    import RunCommand
from libvgazer.exceptions import CommandError
from libvgazer.exceptions import InstallError
from libvgazer.platform   import GetInstallPrefix

def InstallStb(library, platformData, verbose):
    installPrefix = GetInstallPrefix(platformData)

    url = (
     "https://raw.githubusercontent.com/nothings/stb/master/" + library + ".h"
    )

    try:
        if not os.path.exists(installPrefix + "/include"):
            RunCommand(["mkdir", "-p", installPrefix + "/include"], verbose)
        RunCommand(["wget", "-P", installPrefix + "/include", url], verbose)
    except CommandError:
        print("VGAZER: Unable to install", library)
        raise InstallError(library + " not installed")

    print("VGAZER:", library, "installed")
