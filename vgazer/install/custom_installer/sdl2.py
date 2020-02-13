import os
import requests
from bs4 import BeautifulSoup

from vgazer.command     import RunCommand
from vgazer.exceptions  import CommandError
from vgazer.exceptions  import InstallError
from vgazer.exceptions  import TarballLost
from vgazer.platform    import GetInstallPrefix
from vgazer.platform    import GetTriplet
from vgazer.store.temp  import StoreTemp
from vgazer.working_dir import WorkingDir

def GetTarballUrl():
    response = requests.get("https://www.libsdl.org/")
    html = response.content.decode("utf-8")
    parsedHtml = BeautifulSoup(html, "html.parser")

    links = parsedHtml.find_all("a")
    for link in links:
        href = link["href"]
        if href == "download-2.0.php":
            return ("https://www.libsdl.org/release/SDL2-"
             + link.text.split(" ")[2] + ".tar.gz")

    raise TarballLost(
     "Unable to find tarball with last stable release of SDL2")

def Install(auth, software, platform, platformData, mirrors, verbose):
    installPrefix = GetInstallPrefix(platformData)
    targetTriplet = GetTriplet(platformData["target"])

    storeTemp = StoreTemp()
    storeTemp.ResolveEmptySubdirectory(software)
    tempPath = storeTemp.GetSubdirectoryPath(software)

    tarballUrl = GetTarballUrl()
    tarballShortFilename = tarballUrl.split("/")[-1]

    try:
        with WorkingDir(tempPath):
            RunCommand(
             ["wget", "-P", "./", "-O", tarballShortFilename, tarballUrl],
             verbose)
            RunCommand(
             ["tar", "--verbose", "--extract", "--gzip", "--file",
              tarballShortFilename],
             verbose)
        extractedDir = os.path.join(tempPath, tarballShortFilename[0:-7])
        with WorkingDir(extractedDir):
            RunCommand(["mkdir", "build"], verbose)
        with WorkingDir(extractedDir + "/build"):
            RunCommand(
             ["../configure", "--host=" + targetTriplet,
              "--prefix=" + installPrefix,
              "--disable-alsatest", "--enable-jack=no", "--enable-esd=no",
              "--enable-pulseaudio=no", "--enable-arts=no", "--enable-nas=no",
              "--enable-libsamplerate=no",
              "CPPFLAGS=-I" + installPrefix + "/include",
              "LDFLAGS=-L" + installPrefix + "/lib"],
             verbose)
            RunCommand(["make"], verbose)
            RunCommand(["make", "install"], verbose)
    except CommandError:
        print("VGAZER: Unable to install", software)
        raise InstallError(software + " not installed")

    print("VGAZER:", software, "installed")
