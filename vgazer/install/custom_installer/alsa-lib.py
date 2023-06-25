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
    response = requests.get("https://alsa-project.org/wiki/Main_Page")
    html = response.content.decode("utf-8")
    parsedHtml = BeautifulSoup(html, "html.parser")

    links = parsedHtml.find_all("a")
    for link in links:
        if "alsa-lib" in link.text:
            return link["href"]

    raise TarballLost("Unable to find tarball of alsa-lib's last version")

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
             ["tar", "--verbose", "--extract", "--bzip2", "--file",
              tarballShortFilename],
             verbose)
        extractedDir = os.path.join(tempPath, tarballShortFilename[0:-8])
        with WorkingDir(extractedDir):
            RunCommand(
             ["./configure", "--host=" + targetTriplet,
              "--prefix=" + installPrefix, "--enable-symbolic-functions",
              "--disable-python"],
             verbose)
            RunCommand(
             ["make", "-j{cores_count}".format(cores_count=os.cpu_count())],
             verbose)
            RunCommand(["make", "install"], verbose)
    except CommandError:
        print("VGAZER: Unable to install", software)
        raise InstallError(software + " not installed")

    print("VGAZER:", software, "installed")
