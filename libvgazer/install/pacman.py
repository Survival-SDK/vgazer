from libvgazer.command    import RunCommand
from libvgazer.exceptions import CommandError
from libvgazer.exceptions import InstallError

def InstallPacman(software, packages, verbose):
    try:
        if isinstance(packages, list):
            for package in packages:
                RunCommand(
                 [
                  "pacman", "--noconfirm", "--disable-download-timeout", "-S",
                  package
                 ],
                 verbose
                )
        else:
            RunCommand(
             [
              "pacman", "--noconfirm", "--disable-download-timeout", "-S",
              packages
             ],
             verbose
            )
    except CommandError:
        print("VGAZER: Unable to install", software)
        raise InstallError(
         "{software}  not installed".format(software=software))

    print("VGAZER:", software, "installed")
