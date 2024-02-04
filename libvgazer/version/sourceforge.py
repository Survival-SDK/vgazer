import requests

import libvgazer.version.utils as utils
from libvgazer.exceptions import SourceforgeReleaseArchiveLost

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
        raise SourceforgeReleaseArchiveLost(
         "Release not contain archive for project: " + project)

    return utils.GetVersionFromFilename(filename)
