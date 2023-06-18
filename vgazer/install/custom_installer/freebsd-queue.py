import os

from vgazer.command     import RunCommand
from vgazer.exceptions  import CommandError
from vgazer.exceptions  import InstallError
from vgazer.platform    import GetInstallPrefix

def Install(auth, software, platform, platformData, mirrors, verbose):
    installPrefix = GetInstallPrefix(platformData)

    url = (
     "https://raw.githubusercontent.com/opensource-mirrors/freebsd-queue/"
     "master/queue.h"
    )

    try:
        if not os.path.exists(installPrefix + "/include"):
            RunCommand(["mkdir", "-p", installPrefix + "/include/sys"], verbose)
        RunCommand(["wget", "-P", installPrefix + "/include/sys", url], verbose)
    except CommandError:
        print("VGAZER: Unable to install", software)
        raise InstallError("{software} not installed".format(software=software))

    print("VGAZER:", software, "installed")
