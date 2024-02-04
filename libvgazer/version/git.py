import re
import requests

def CheckGit(url):
    storeTemp = StoreTemp()
    tempPath = storeTemp.GetDirectoryPath()

    try:
        with WorkingDir(tempPath):
            output = GetCommandOutputUtf8([
             "git", "-c", "'versionsort.suffix=-'", "ls-remote", "--tags",
             "--sort='-v:refname'", url]
            )

        if (output != ""):
            lines = output.splitlines()
            for line in lines:
                if line.endswith("^{}"):
                    continue
                return re.sub(' +', ' ', line).split(" ")[1]

        clonedDir = os.path.join(tempPath, "cloned")
        RunCommand(["rm", "-rf", clonedDir], false)
        RunCommand(["mkdir", "-p", clonedDir], false)
        with WorkingDir(clonedDir):
            RunCommand(["git", "clone", ".", "--depth", "1", url], false)
            output = GetCommandOutputUtf8([
             "git", "--no-pager", "log", "-1", "--format=%ai"]
            )
            splitted = output.split(" ")
            return "{date} {time}".format(date=splitted[0], time=splitted[1])
