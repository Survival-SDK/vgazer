import requests
from vgazer.exceptions import DebianPackageUnavailable

def GetPackageVersion(sourceInfo, debianRelease):
    versions = sourceInfo["versions"]

    for version in versions:
        suites = version["suites"]
        for suit in suites:
            if suit == debianRelease:
                return version["version"]

    for version in versions:
        suites = version["suites"]
        for suit in suites:
            if suit == debianRelease + "-backports":
                return version["version"]

    return None

def CheckDebian(auth, debianRelease, source):
    #for key, data in projects.items():
        #if (key == debianRelease or key == "generic"):
            #source = data["source"]
            #break

    sourceInfo = auth.GetJson(
     "https://sources.debian.org/api/src/" + source + "/")

    version = GetPackageVersion(sourceInfo, debianRelease)

    if version is None:
        raise DebianPackageUnavailable("There is not package " + source
         + " in " + debianRelease + " Debian release")

    return version
