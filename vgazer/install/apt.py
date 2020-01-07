from vgazer.command     import RunCommand
from vgazer.exceptions  import CommandError
from vgazer.exceptions  import InstallError

def InstallAptFromBackport(software, package, hostPlatform,
 showInstalledMessage, verbose):
    try:
        RunCommand(
         ["apt-get", "-t", hostPlatform.GetOsVersion() + "-backports",
          "install", "-y", package],
         verbose)
    except CommandError:
        print("VGAZER: Unable to install", software)
        raise InstallError(software + " not installed")

    if showInstalledMessage:
        print("VGAZER:", software, "installed")

def InstallApt(software, package, hostPlatform, showInstalledMessage, verbose):
    try:
        RunCommand(["apt-get", "install", "-y", package], verbose)
    except CommandError as e:
        if e.errorcode == 100 and hostPlatform.GetOs() == "debian":
            InstallAptFromBackport(software, package, hostPlatform, verbose)
        else:
            print("VGAZER: Unable to install", software)
            raise InstallError(software + " not installed")

    if showInstalledMessage:
        print("VGAZER:", software, "installed")
