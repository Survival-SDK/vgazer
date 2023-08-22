import os

from vgazer.command    import RunCommand
from vgazer.exceptions import CommandError
from vgazer.exceptions import InstallError
from vgazer.platform   import GetInstallPrefix

def Install(auth, software, platform, platformData, mirrors, verbose):
    installPrefix = GetInstallPrefix(platformData)

    url = (
     "https://raw.githubusercontent.com/Malvineous/cfgpath/master/cfgpath.h")

    try:
        if not os.path.exists("{prefix}/include".format(prefix=installPrefix)):
            RunCommand(
             ["mkdir", "-p", "{prefix}/include".format(prefix=installPrefix)],
             verbose)
        RunCommand(
         [
          "wget", "--read-timeout=10", "-P",
          "{prefix}/include".format(prefix=installPrefix), url
         ],
         verbose)
    except CommandError:
        print("VGAZER: Unable to install", software)
        raise InstallError("{software} not installed".format(software=software))

    print("VGAZER:", software, "installed")
