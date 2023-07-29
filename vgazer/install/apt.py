from vgazer.command     import RunCommand
from vgazer.exceptions  import CommandError
from vgazer.exceptions  import InstallError

def InstallPackageDebian(software, package, hostPlatform, verbose):
    try:
        RunCommand(
         ["apt-get", "-t",
          "{osver}-backports".format(osver=hostPlatform.GetOsVersion()),
          "install", "-y", package
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
        RunCommand(["apt-get", "install", "-y", package], verbose)
    except CommandError:
        print("VGAZER: Unable to install", software)
        raise InstallError(
         "{software}  not installed".format(software=software))

def InstallPackage(software, package, hostPlatform, verbose):
    if hostPlatform.GetOs() == "debian":
        InstallPackageDebian(software, package, hostPlatform, verbose);
    else:
        InstallPackageOther(software, package, hostPlatform, verbose);

def InstallApt(software, packages, postInstallCommands, hostPlatform, verbose):
    if isinstance(packages, list):
        for package in packages:
            InstallPackage(software, package, hostPlatform, verbose)
    else:
        InstallPackage(software, packages, hostPlatform, verbose)

    if postInstallCommands is not None:
        for command in postInstallCommands:
            RunCommand(command, verbose)

    print("VGAZER:", software, "installed")
