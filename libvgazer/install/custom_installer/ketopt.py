import os

from libvgazer.command    import RunCommand
from libvgazer.exceptions import CommandError
from libvgazer.exceptions import InstallError
from libvgazer.platform   import GetInstallPrefix

def Install(auth, software, platform, platformData, mirrors, verbose):
    installPrefix = GetInstallPrefix(platformData)

    url = (
     "https://raw.githubusercontent.com/attractivechaos/klib/master/"
     "ketopt.h"
    )

    try:
        if not os.path.exists(
         "{prefix}/include/klib".format(prefix=installPrefix)):
            RunCommand(
             [
              "mkdir", "-p",
              "{prefix}/include/klib".format(prefix=installPrefix)
             ],
             verbose
            )
        RunCommand(
         [
          "wget", "--read-timeout=10", "-P",
          "{prefix}/include/klib".format(prefix=installPrefix), url
         ],
         verbose)
    except CommandError:
        print("VGAZER: Unable to install", software)
        raise InstallError("{software} not installed".format(software=software))

    print("VGAZER:", software, "installed")
