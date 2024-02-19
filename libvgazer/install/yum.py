from libvgazer.command    import RunCommand
from libvgazer.exceptions import CommandError
from libvgazer.exceptions import InstallError

def InstallYum(software, packages, repo, postInstallCommands, verbose):
    cmd = ["yum", "-y", "install"]
    if repo is not None:
        cmd.append("--enablerepo={repo}".format(repo=repo))

    try:
        if isinstance(packages, list):
            for package in packages:
                cmd.append(package)
        else:
            cmd.append(packages)
        RunCommand(cmd, verbose)
    except CommandError:
        print("VGAZER: Unable to install", software)
        raise InstallError(
         "{software}  not installed".format(software=software))

    if postInstallCommands is not None:
        for command in postInstallCommands:
            RunCommand(command, verbose)

    print("VGAZER:", software, "installed")
