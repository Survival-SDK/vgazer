import os
import requests
from bs4 import BeautifulSoup

from vgazer.command     import RunCommand
from vgazer.exceptions  import CommandError
from vgazer.exceptions  import InstallError
from vgazer.exceptions  import TarballLost
from vgazer.platform    import GetTriplet
from vgazer.store.temp  import StoreTemp
from vgazer.working_dir import WorkingDir

def GetTarballUrl():
    response = requests.get("https://ftp.gnu.org/gnu/automake/")
    html = response.content.decode("utf-8")
    parsedHtml = BeautifulSoup(html, "html.parser")

    links = parsedHtml.find_all("a")

    maxVersion = "-1"
    maxUrl = ""
    for link in links:
        if ("automake-1.11" in link.text and ".tar.gz" in link.text
         and ".sig" not in link.text):
            version = link.text.split("-")[1].split(".tar.gz")[0]
            splitedVersion = version.split(".")
            if len(splitedVersion) == 2:
                patchVersion = 0
            else:
                patchVersion = splitedVersion[2]
            if int(patchVersion) > int(maxVersion):
                maxVersion = patchVersion
                maxUrl = "https://ftp.gnu.org/gnu/automake/" + link["href"]

    if maxUrl != "":
        return maxUrl
    else:
        raise TarballLost("Tarball url not found")

def Install(auth, software, platform, platformData, verbose):
    hostTriplet = GetTriplet(platformData["host"])

    storeTemp = StoreTemp()
    storeTemp.ResolveEmptySubdirectory(software)
    tempPath = storeTemp.GetSubdirectoryPath(software)

    tarballUrl = GetTarballUrl()
    tarballShortFilename = tarballUrl.split("/")[-1]

    try:
        with WorkingDir(tempPath):
            RunCommand(["wget", "-P", "./", tarballUrl], verbose)
            RunCommand(
             ["tar", "--verbose", "--extract", "--gzip", "--file",
              tarballShortFilename],
             verbose)
        extractedDir = os.path.join(tempPath,
         ".".join(tarballShortFilename.split(".")[0:-2]))
        with WorkingDir(extractedDir):
            RunCommand(
             ["wget", "-O", "./lib/config.guess",
              "https://git.savannah.gnu.org/gitweb/?p=config.git;a=blob_plain;f=config.guess;hb=HEAD"],
             verbose)
            RunCommand(
             ["wget", "-O", "./lib/config.sub",
              "https://git.savannah.gnu.org/gitweb/?p=config.git;a=blob_plain;f=config.sub;hb=HEAD"],
             verbose)
            RunCommand(
             ["./configure", "--prefix=/usr/local"],
             verbose
            )
            RunCommand(["make"], verbose)
            RunCommand(["make", "install"], verbose)
    except CommandError:
        print("Unable to install", software)
        raise InstallError(software + " not installed")

    print(software, "installed")
