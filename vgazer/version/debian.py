import requests

class DebianPackageUnavailable(Exception):
    def __init__(self, message):
        super().__init__(message)

def GetPackageVersion(packageInfo, debianRelease, package):
    versions = packageInfo["versions"]

    for version in versions:
        suites = version["suites"]
        for suit in suites:
            if (suit == debianRelease or suit == debianRelease + "-backports"):
                return version["version"]

    return None

def CheckDebian(auth, debianRelease, projects):
    for key, data in projects.items():
        if (key == debianRelease or key == "generic"):
            source = data["source"]
            break

    sourceInfo = auth.GetJson(
     "https://sources.debian.org/api/src/" + source + "/")

    version = GetPackageVersion(sourceInfo, debianRelease, source)

    if version is None:
        raise DebianPackageUnavailable("There is not package " + source
         + " in " + debianRelease + " Debian release")

    return version
