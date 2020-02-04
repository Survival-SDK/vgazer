from vgazer.command     import RunCommand
from vgazer.exceptions  import CommandError
from vgazer.exceptions  import InstallError

def InstallPackageFromBackport(software, package, hostPlatform,
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

def InstallPackage(software, package, hostPlatform, showInstalledMessage,
 verbose):
    try:
        RunCommand(["apt-get", "install", "-y", package], verbose)
    except CommandError as e:
        if e.errorcode == 100 and hostPlatform.GetOs() == "debian":
            InstallPackageFromBackport(software, package, hostPlatform,
             showInstalledMessage, verbose)
        else:
            print("VGAZER: Unable to install", software)
            raise InstallError(software + " not installed")

    if showInstalledMessage:
        print("VGAZER:", software, "installed")

def InstallApt(software, packages, hostPlatform, verbose):
    if isinstance(packages, list):
        for package in packages:
            InstallPackage(software, package, hostPlatform,
             package is packages[-1], verbose)
    else:
        InstallPackage(software, packages, hostPlatform, True, verbose)
