import os
import requests
from bs4 import BeautifulSoup

from vgazer.command         import RunCommand
from vgazer.exceptions      import CommandError
from vgazer.exceptions      import InstallError
from vgazer.exceptions      import TarballLost
from vgazer.install.utils   import GetVersionNumbers
from vgazer.platform        import GetInstallPrefix
from vgazer.platform        import GetTriplet
from vgazer.store.temp      import StoreTemp
from vgazer.working_dir     import WorkingDir

def GetMirrorUrlFunc(mirrorsManager, firstTry):
    if firstTry:
        return mirrorsManager.GetMirrorUrl
    else:
        return mirrorsManager.GetNewMirrorUrl

def GetTarballUrl(mirrorsManager, firstTry=True):
    getMirrorUrl = GetMirrorUrlFunc(mirrorsManager, firstTry)

    try:
        response = requests.get(getMirrorUrl() + "/individual/lib/")
    except requests.exceptions.ConnectionError:
        return GetTarballUrl(mirrorsManager, firstTry=False)
    html = response.content.decode("utf-8")
    parsedHtml = BeautifulSoup(html, "html.parser")

    links = parsedHtml.find_all("a")

    maxVersionMajor = -1
    maxVersionMinor = -1
    maxVersionPatch = -1
    maxVersionSubpatch = -1
    for link in links:
        if ("libX11-" in link.text and ".tar.gz" in link.text
         and ".sig" not in link.text):
            versionText = link.text.split("-")[1].split(".tar.gz")[0].split(
             ".")
            version = GetVersionNumbers(versionText)

            if version["major"] > maxVersionMajor:
                maxVersionMajor = version["major"]
                maxVersionMinor = version["minor"]
                maxVersionPatch = version["patch"]
                maxVersionSubpatch = version["subpatch"]
                url = (getMirrorUrl() + "/individual/lib/" + link["href"])
            elif (version["major"] == maxVersionMajor
             and version["minor"] > maxVersionMinor):
                maxVersionMinor = version["minor"]
                maxVersionPatch = version["patch"]
                maxVersionSubpatch = version["subpatch"]
                url = (getMirrorUrl() + "/individual/lib/" + link["href"])
            elif (version["major"] == maxVersionMajor
             and version["minor"] == maxVersionMinor
             and version["patch"] > maxVersionPatch):
                maxVersionPatch = version["patch"]
                maxVersionSubpatch = version["subpatch"]
                url = (getMirrorUrl() + "/individual/lib/" + link["href"])
            elif (version["major"] == maxVersionMajor
             and version["minor"] == maxVersionMinor
             and version["patch"] == maxVersionPatch
             and version["subpatch"] > maxVersionSubpatch):
                maxVersionSubpatch = version["subpatch"]
                url = (getMirrorUrl() + "/individual/lib/" + link["href"])

    if url is not None:
        return url

    raise TarballLost("Unable to find tarball of xlib's last version")

def Install(auth, software, platform, platformData, mirrors, verbose):
    installPrefix = GetInstallPrefix(platformData)
    targetTriplet = GetTriplet(platformData["target"])

    storeTemp = StoreTemp()
    storeTemp.ResolveEmptySubdirectory(software)
    tempPath = storeTemp.GetSubdirectoryPath(software)

    xorgMirrorsManager = mirrors["xorg"].CreateMirrorsManager(
     ["https", "http"])

    tarballUrl = GetTarballUrl(xorgMirrorsManager)
    tarballShortFilename = tarballUrl.split("/")[-1]

    try:
        with WorkingDir(tempPath):
            RunCommand(["wget", "-P", "./", tarballUrl], verbose)
            RunCommand(
             ["tar", "--verbose", "--extract", "--gzip", "--file",
              tarballShortFilename],
             verbose)
        extractedDir = os.path.join(tempPath, tarballShortFilename[0:-7])
        with WorkingDir(extractedDir):
            RunCommand(
             ["./configure", "--host=" + targetTriplet,
              "--prefix=" + installPrefix,
              "CPPFLAGS=-I" + installPrefix + "/include",
              "PKG_CONFIG_PATH=" + installPrefix + "/lib/pkgconfig:"
               + installPrefix + "/share/pkgconfig"
             ],
             verbose)
            RunCommand(["make"], verbose)
            RunCommand(["make", "install"], verbose)
    except CommandError:
        print("VGAZER: Unable to install", software)
        raise InstallError(software + " not installed")

    print("VGAZER:", software, "installed")
