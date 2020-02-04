import requests
from bs4 import BeautifulSoup

from vgazer.command         import RunCommand
from vgazer.exceptions      import CommandError
from vgazer.exceptions      import TarballLost
from vgazer.install.utils   import GetVersionNumbers

def GetMirrorUrlFunc(mirrorsManager, firstTry):
    if firstTry:
        return mirrorsManager.GetMirrorUrl
    else:
        return mirrorsManager.GetNewMirrorUrl

def IsLinkTextCorrect(link, linksMustHave, linksMustNotHave):
    for mustHave in linksMustHave:
        if mustHave not in link.text:
            return False
    for mustNotHave in linksMustNotHave:
        if mustNotHave in link.text:
            return False
    return True

def GetTarballUrl(mirrorsManager, suburl, projectName, linksMustHave,
 linksMustNotHave, firstTry=True):
    getMirrorUrl = GetMirrorUrlFunc(mirrorsManager, firstTry)

    try:
        response = requests.get(getMirrorUrl() + "/" + suburl)
    except requests.exceptions.ConnectionError:
        return GetTarballUrl(mirrorsManager, suburl, projectName,
         linksMustHave, linksMustNotHave, firstTry=False)
    html = response.content.decode("utf-8")
    parsedHtml = BeautifulSoup(html, "html.parser")

    links = parsedHtml.find_all("a")

    maxVersionMajor = -1
    maxVersionMinor = -1
    maxVersionPatch = -1
    maxVersionSubpatch = -1
    for link in links:
        if not IsLinkTextCorrect(link, linksMustHave, linksMustNotHave):
            continue

        versionText = link.text.split("-")[1].split(".tar.gz")[0].split(".")
        version = GetVersionNumbers(versionText)

        if version["major"] > maxVersionMajor:
            maxVersionMajor = version["major"]
            maxVersionMinor = version["minor"]
            maxVersionPatch = version["patch"]
            maxVersionSubpatch = version["subpatch"]
            url = (getMirrorUrl() + "/" + suburl + link["href"])
        elif (version["major"] == maxVersionMajor
         and version["minor"] > maxVersionMinor):
            maxVersionMinor = version["minor"]
            maxVersionPatch = version["patch"]
            maxVersionSubpatch = version["subpatch"]
            url = (getMirrorUrl() + "/" + suburl + link["href"])
        elif (version["major"] == maxVersionMajor
         and version["minor"] == maxVersionMinor
         and version["patch"] > maxVersionPatch):
            maxVersionPatch = version["patch"]
            maxVersionSubpatch = version["subpatch"]
            url = (getMirrorUrl() + "/" + suburl + link["href"])
        elif (version["major"] == maxVersionMajor
         and version["minor"] == maxVersionMinor
         and version["patch"] == maxVersionPatch
         and version["subpatch"] > maxVersionSubpatch):
            maxVersionSubpatch = version["subpatch"]
            url = (getMirrorUrl() + "/" + suburl + link["href"])

    try:
        return url
    except UnboundLocalError:
        raise TarballLost(
         "Unable to find tarball of {project}'s last version".format(
          project=projectName)
        )
