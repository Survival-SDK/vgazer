import requests

class LostReleaseArchive(Exception):
    def __init__(self, message):
        super().__init__(message)

def GetExtensionDotsCount(filename):
    splitedFilename = filename.split(".")
    if splitedFilename[-1] == "gz":
        if splitedFilename[-2] == "tar":
            return 1

    return 0

def GetVersionNumbers(VersionAndExt, dotsCount):
    splitedVersionAndExt = VersionAndExt.split(".")
    while dotsCount >= 0:
        splitedVersionAndExt.pop(-1)
        dotsCount -= 1
    return splitedVersionAndExt

def CheckSourceforge(auth, project):
    fullFilename = requests.get(
     "https://sourceforge.net/projects/" + project + "/best_release.json"
    ).json()["release"]["filename"]

    filename = fullFilename.split("/")[-1]
    extension = filename.split(".")[-1]
    if extension == "txt":
        raise LostReleaseArchive(
         "Release not contain archive for project: " + project)

    dotsCount = GetExtensionDotsCount(filename)

    VersionAndExt = filename.split("-")[-1]

    return '.'.join(GetVersionNumbers(VersionAndExt, dotsCount))
