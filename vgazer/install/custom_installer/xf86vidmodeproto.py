import os
import requests
from bs4 import BeautifulSoup

from vgazer.command     import RunCommand
from vgazer.exceptions  import CommandError
from vgazer.exceptions  import InstallError
from vgazer.platform    import GetInstallPrefix
from vgazer.platform    import GetTriplet
from vgazer.store.temp  import StoreTemp
from vgazer.working_dir import WorkingDir

def GetMirrorUrlFunc(mirrorsManager, firstTry):
    if firstTry:
        return mirrorsManager.GetMirrorUrl
    else:
        return mirrorsManager.GetNewMirrorUrl

def GetTarballUrl(mirrorsManager, firstTry=True):
    getMirrorUrl = GetMirrorUrlFunc(mirrorsManager, firstTry)

    try:
        response = requests.get(getMirrorUrl() + "/individual/proto/")
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
        if ("xf86vidmodeproto-" in link.text and ".tar.gz" in link.text):
            version = link.text.split("-")[1].split(".tar.gz")[0].split(".")
            versionMajor = int(version[0])
            versionMinor = int(version[1])
            if len(version) == 2:
                versionPatch = 0
                versionSubpatch = 0
            elif len(version) == 3:
                versionPatch = int(version[2])
                versionSubpatch = 0
            else:
                versionPatch = int(version[2])
                versionSubpatch = int(version[3])

            if versionMajor > maxVersionMajor:
                maxVersionMajor = versionMajor
                maxVersionMinor = versionMinor
                maxVersionPatch = versionPatch
                maxVersionSubpatch = versionSubpatch
                maxVersionText = link.text.split("-")[1].split(".tar.gz")[0]
            elif (versionMajor == maxVersionMajor
             and versionMinor > maxVersionMinor):
                maxVersionMinor = versionMinor
                maxVersionPatch = versionPatch
                maxVersionSubpatch = versionSubpatch
                maxVersionText = link.text.split("-")[1].split(".tar.gz")[0]
            elif (versionMajor == maxVersionMajor
             and versionMinor == maxVersionMinor
             and versionPatch > maxVersionPatch):
                maxVersionPatch = versionPatch
                maxVersionSubpatch = versionSubpatch
                maxVersionText = link.text.split("-")[1].split(".tar.gz")[0]
            elif (versionMajor == maxVersionMajor
             and versionMinor == maxVersionMinor
             and versionPatch > maxVersionPatch
             and versionSubpatch > maxVersionSubpatch):
                maxVersionSubpatch = versionSubpatch
                maxVersionText = link.text.split("-")[1].split(".tar.gz")[0]

    return (getMirrorUrl() + "/individual/proto/xf86vidmodeproto-"
     + maxVersionText + ".tar.gz")

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
              "--prefix=" + installPrefix],
             verbose)
            RunCommand(["make", "install"], verbose)
    except CommandError:
        print("VGAZER: Unable to install", software)
        raise InstallError(software + " not installed")

    print("VGAZER:", software, "installed")
