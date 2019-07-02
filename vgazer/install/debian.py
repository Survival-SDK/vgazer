from vgazer.command     import RunCommand
from vgazer.exceptions  import CommandError
from vgazer.exceptions  import InstallError

def InstallDebian(software, debianRelease, projects, verbose):
    package = None

    for key, data in projects.items():
        if (key == debianRelease or key == "generic"):
            package = data["package"]
            break

    if package is None:
        raise DebianPackageUnavailable("There is not package " + package
         + " in " + debianRelease + " Debian release")

    try:
        RunCommand(["apt-get", "install", "-y", package], verbose)
    except CommandError:
        print("Unable to install", software)
        raise InstallError(software + " not installed")

    print(software, "installed")
