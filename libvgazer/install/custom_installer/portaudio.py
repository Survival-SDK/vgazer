import os
import requests
from bs4 import BeautifulSoup

from libvgazer.command     import RunCommand
from libvgazer.exceptions  import CommandError
from libvgazer.exceptions  import InstallError
from libvgazer.exceptions  import TarballLost
from libvgazer.platform    import GetInstallPrefix
from libvgazer.platform    import GetTriplet
from libvgazer.store.temp  import StoreTemp
from libvgazer.working_dir import WorkingDir

def GetTarballUrl():
    response = requests.get("http://www.portaudio.com/download.html")
    html = response.content.decode("utf-8")
    parsedHtml = BeautifulSoup(html, "html.parser")

    links = parsedHtml.find_all("a")

    for link in links:
        if link["href"].find("archives/pa_stable_") != -1:
            strongs = link.findChildren("strong")
            if len(strongs) == 1:
                return "http://www.portaudio.com/" + link["href"]

    raise TarballLost(
     "Unable to find tarball with last stable release of portaudio")

def Install(auth, software, platform, platformData, mirrors, verbose):
    installPrefix = GetInstallPrefix(platformData)
    targetTriplet = GetTriplet(platformData["target"])

    storeTemp = StoreTemp()
    storeTemp.ResolveEmptySubdirectory(software)
    tempPath = storeTemp.GetSubdirectoryPath(software)

    tarballUrl = GetTarballUrl()
    tarballShortFilename = tarballUrl.split("/")[-1]

    libs = {
        "linux": "LIBS=-lasound",
        "windows": "",
    }[platformData["target"].GetOs()]

    try:
        with WorkingDir(tempPath):
            RunCommand(["wget", "-P", "./", tarballUrl], verbose)
            RunCommand(
             ["tar", "--verbose", "--extract", "--gzip", "--file",
              tarballShortFilename],
             verbose)
        extractedDir = os.path.join(tempPath, "portaudio")
        with WorkingDir(extractedDir):
            RunCommand(
             ["./configure", "--host=" + targetTriplet,
              "--prefix=" + installPrefix, "--disable-shared",
              "--with-alsa=yes", "--with-oss=yes",
              "--with-winapi=wmme,directx,wdmks",
              "LDFLAGS=-L" + installPrefix + "/lib", libs,
              "CPPFLAGS=-I" + installPrefix + "/include"],
             verbose)
            RunCommand(
             ["sed", "-i", "-e",
              "s#CFLAGS = #CFLAGS = -I" + installPrefix + "/include #g",
              "./Makefile"],
             verbose)
            RunCommand(
             ["make", "-j{cores_count}".format(cores_count=os.cpu_count())],
             verbose)
            RunCommand(["make", "install"], verbose)
    except CommandError:
        print("VGAZER: Unable to install", software)
        raise InstallError(software + " not installed")

    print("VGAZER:", software, "installed")
