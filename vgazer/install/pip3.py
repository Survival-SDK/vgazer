from vgazer.command     import RunCommand
from vgazer.exceptions  import CommandError
from vgazer.exceptions  import InstallError

def InstallPip3(software, package, verbose):
    try:
        RunCommand(["pip3", "install", package, "--no-cache-dir"], verbose)
    except CommandError:
        print("Unable to install", software)
        raise InstallError(software + " not installed")

    print(software, "installed")
