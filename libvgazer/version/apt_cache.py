import os
import re

from libvgazer.command     import GetCommandOutputUtf8
from libvgazer.command     import RunCommand
from libvgazer.exceptions  import CommandError
from libvgazer.store.temp  import StoreTemp
from libvgazer.working_dir import WorkingDir

def ArchToDebianArch(arch):
    return {
        "x86_64": "amd64",
    }[arch]

def CheckAptCache(package, arch):
    output = GetCommandOutputUtf8(["apt-cache", "madison", package])
    lines = output.splitlines()
    maxVersion = ""

    for line in lines:
        columns = line.split("|")
        version = columns[1].strip()
        repoArch = columns[2].strip().split(" ", 2)[2]
        if ((repoArch == "{arch} Packages".format(arch=ArchToDebianArch(arch))
         or repoArch == "Sources") and (version > maxVersion)):
            maxVersion = version

    return maxVersion
