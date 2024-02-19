import os
import re

from libvgazer.command     import GetCommandOutputUtf8
from libvgazer.command     import RunCommand
from libvgazer.exceptions  import CommandError
from libvgazer.store.temp  import StoreTemp
from libvgazer.working_dir import WorkingDir

def GetLastTag(url, hint=None, files=None):
    if files is not None:
        return None

    storeTemp = StoreTemp()
    tempPath = storeTemp.GetDirectoryPath()

    try:
        with WorkingDir(tempPath, verbose=False):
            output = GetCommandOutputUtf8([
             "git", "-c", "versionsort.suffix=-", "ls-remote", "--tags", url]
            )

        if (output == ""):
            return None

        lines = output.splitlines()
        tags = []
        for line in lines:
            if line.endswith("^{}"):
                continue
            tag = line.split("/")[-1]
            if hint is None or re.fullmatch(hint, tag) is not None:
                tags.append(tag)

        tags.sort(reverse=True)
        return tags[0]

    except CommandError:
        return None

    return None

def GetLastCommit(url, hint=None, files=None):
    storeTemp = StoreTemp()
    tempPath = storeTemp.GetDirectoryPath()

    try:
        clonedDir = os.path.join(tempPath, "cloned")
        RunCommand(["rm", "-rf", clonedDir], False)
        RunCommand(["mkdir", "-p", clonedDir], False)

        with WorkingDir(clonedDir, verbose=False):
            RunCommand(["git", "clone", "--depth", "1", url, "."], False)

            if files is not None:
                mostRecent = ""
                for file in files:
                    if hint is None:
                        version = GetCommandOutputUtf8([
                         "git", "--no-pager", "log", "-1", "--format=%ai", file]
                        )[0:-6]
                        if version > mostRecent:
                            mostRecent = version
                    else:
                        with open(file) as openedFile:
                            content = openedFile.read()
                            matches = re.findall(hint, content)
                            for match in matches:
                                if match > mostRecent:
                                    mostRecent = match

                return mostRecent if mostRecent != "" else None

            output = GetCommandOutputUtf8([
             "git", "--no-pager", "log", "-1", "--format=%ai"]
            )
            splitted = output.split(" ")
            return "{date} {time}".format(date=splitted[0], time=splitted[1])
    except CommandError:
        return None

    return None

def CheckGit(url, hint=None, files=None):
    version = GetLastTag(url, hint, files)
    if version is None:
        version = GetLastCommit(url, hint, files)

    return version
