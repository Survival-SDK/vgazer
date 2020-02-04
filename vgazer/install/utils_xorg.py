import requests
from bs4 import BeautifulSoup

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

def UpdateMaxVersion(maxVersion, version):
    result = maxVersion

    if version["major"] > maxVersion["major"]:
        result["major"] = version["major"]
        result["minor"] = version["minor"]
        result["patch"] = version["patch"]
        result["subpatch"] = version["subpatch"]
    elif (version["major"] == maxVersion["major"]
     and version["minor"] > maxVersion["minor"]):
        result["minor"] = version["minor"]
        result["patch"] = version["patch"]
        result["subpatch"] = version["subpatch"]
    elif (version["major"] == maxVersion["major"]
     and version["minor"] == maxVersion["minor"]
     and version["patch"] > maxVersion["patch"]):
        result["patch"] = version["patch"]
        result["subpatch"] = version["subpatch"]
    elif (version["major"] == maxVersion["major"]
     and version["minor"] == maxVersion["minor"]
     and version["patch"] == maxVersion["patch"]
     and version["subpatch"] > maxVersion["subpatch"]):
        result["subpatch"] = version["subpatch"]

    return result

def UpdateUrl(oldUrl, maxVersion, version, getMirrorUrl, suburl, link):
    if (version["major"] > maxVersion["major"]
    or (
     version["major"] == maxVersion["major"]
     and version["minor"] > maxVersion["minor"]
    )
    or (
     version["major"] == maxVersion["major"]
     and version["minor"] == maxVersion["minor"]
     and version["patch"] > maxVersion["patch"]
    )
    or (
     version["major"] == maxVersion["major"]
     and version["minor"] == maxVersion["minor"]
     and version["patch"] == maxVersion["patch"]
     and version["subpatch"] > maxVersion["subpatch"]
    )):
        return getMirrorUrl() + "/" + suburl + link["href"]

    return oldUrl

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

    maxVersion = {
        "major": -1,
        "minor": -1,
        "patch": -1,
        "subpatch": -1,
    }
    url = None
    for link in links:
        if not IsLinkTextCorrect(link, linksMustHave, linksMustNotHave):
            continue

        versionText = link.text.split("-")[1].split(".tar.gz")[0].split(".")
        version = GetVersionNumbers(versionText)

        url = UpdateUrl(url, maxVersion, version, getMirrorUrl, suburl, link)
        maxVersion = UpdateMaxVersion(maxVersion, version)

    if url is not None:
        return url
    else:
        raise TarballLost(
         "Unable to find tarball of {project}'s last version".format(
          project=projectName)
        )
