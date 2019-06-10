import requests
import vgazer.version.utils as utils

class LostReleaseArchive(Exception):
    def __init__(self, message):
        super().__init__(message)

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

    return utils.GetVersionFromFilename(filename)
