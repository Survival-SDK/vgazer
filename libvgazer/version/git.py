import os
import re

from libvgazer.command     import GetCommandOutputUtf8
from libvgazer.command     import RunCommand
from libvgazer.exceptions  import CommandError
from libvgazer.store.temp  import StoreTemp
from libvgazer.working_dir import WorkingDir

def CheckGit(url):
    storeTemp = StoreTemp()
    tempPath = storeTemp.GetDirectoryPath()

    try:
        with WorkingDir(tempPath, verbose=False):
            output = GetCommandOutputUtf8([
             "git", "-c", "versionsort.suffix=-", "ls-remote", "--tags",
             "--sort=-v:refname", url]
            )

        if (output != ""):
            lines = output.splitlines()
            for line in lines:
                if line.endswith("^{}"):
                    continue
                return re.sub(' +', ' ', line).split(" ")[1]

        clonedDir = os.path.join(tempPath, "cloned")
        RunCommand(["rm", "-rf", clonedDir], False)
        RunCommand(["mkdir", "-p", clonedDir], False)
        with WorkingDir(clonedDir, verbose=False):
            RunCommand(["git", "clone", "--depth", "1", url, "."], False)
            output = GetCommandOutputUtf8([
             "git", "--no-pager", "log", "-1", "--format=%ai"]
            )
            splitted = output.split(" ")
            return "{date} {time}".format(date=splitted[0], time=splitted[1])
    except CommandError:
        return "N/A"
