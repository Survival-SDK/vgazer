import re

from libvgazer.command import GetCommandOutputUtf8

def CheckYum(package, repo, arch):
    cmd = ["yum", "list", package]
    if repo is not None:
        cmd.append("--enablerepo={repo}".format(repo=repo))
    output = GetCommandOutputUtf8(cmd)
    lines = output.splitlines()
    maxVersion = ""

    for line in lines:
        if package in line:
            columns = re.split(' +', line)
            version = columns[1]
            pkgArch = columns[0].split(".")[-1]
            if pkgArch in [arch, "noarch"] and (version > maxVersion):
                maxVersion = version

    return maxVersion
