from libvgazer.command    import RunCommand
from libvgazer.exceptions import CommandError
from libvgazer.exceptions import InstallError

def InstallCmd(software, cmds, verbose):
    for cmd in cmds:
        try:
            RunCommand(cmd, verbose)
        except CommandError:
            print("VGAZER: Unable to install", software)
            raise InstallError(
             "{software}  not installed".format(software=software))

    print("VGAZER:", software, "installed")
