from libvgazer.command    import RunCommand
from libvgazer.exceptions import CommandError
from libvgazer.exceptions import InstallError

aptUpdateCalled = False

def InstallPackageDebian(software, package, hostPlatform, verbose):
    try:
        RunCommand(
         [
          "apt-get", "-t",
          "{osver}-backports".format(osver=hostPlatform.GetOsVersion()),
          "install", "-y", "--no-install-recommends", "--no-install-suggests",
          package
         ],
         verbose)
    except CommandError as e:
        if e.errorcode == 100:
            InstallPackageOther(software, package, hostPlatform, verbose)
        else:
            print("VGAZER: Unable to install", software)
            raise InstallError(
             "{software} not installed".format(software=software))

def InstallPackageOther(software, package, hostPlatform, verbose):
    try:
        RunCommand(
         ["apt-get", "install", "-y", "--no-install-recommends",
          "--no-install-suggests", package],
         verbose)
    except CommandError:
        print("VGAZER: Unable to install", software)
        raise InstallError(
         "{software}  not installed".format(software=software))

def InstallPackage(software, package, hostPlatform, verbose):
    if hostPlatform.GetOs() == "debian":
        InstallPackageDebian(software, package, hostPlatform, verbose)
    else:
        InstallPackageOther(software, package, hostPlatform, verbose)

def InstallApt(software, packages, postInstallCommands, hostPlatform, verbose):
    global aptUpdateCalled

    if not aptUpdateCalled:
        RunCommand(["apt-get", "update"], verbose)
        aptUpdateCalled = True

    if isinstance(packages, list):
        for package in packages:
            InstallPackage(software, package, hostPlatform, verbose)
    else:
        InstallPackage(software, packages, hostPlatform, verbose)

    if postInstallCommands is not None:
        for command in postInstallCommands:
            RunCommand(command, verbose)

    print("VGAZER:", software, "installed")
