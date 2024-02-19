import os
import requests
from bs4 import BeautifulSoup

from libvgazer.command     import RunCommand
from libvgazer.exceptions  import CommandError
from libvgazer.exceptions  import InstallError
from libvgazer.exceptions  import TarballLost
from libvgazer.store.temp  import StoreTemp
from libvgazer.working_dir import WorkingDir

def GetTarballUrl():
    response = requests.get("https://ftp.gnu.org/gnu/autoconf/")
    html = response.content.decode("utf-8")
    parsedHtml = BeautifulSoup(html, "html.parser")

    links = parsedHtml.find_all("a")

    maxMajor = -1
    maxMinor = -1
    for link in links:
        if ("autoconf" in link.text and ".tar.gz" in link.text
         and ".sig" not in link.text and "-latest" not in link.text):
            version = link.text.split("-")[1].split(".tar.gz")[0]
            splitedVersion = version.split(".")
            if int(splitedVersion[0]) > maxMajor:
                maxMajor = int(splitedVersion[0])
                maxMinor = int(splitedVersion[1])
            elif (int(splitedVersion[0]) == maxMajor
             and int(splitedVersion[1]) > maxMinor):
                maxMinor = int(splitedVersion[1])

    if (maxMajor != -1 and maxMinor != -1):
        return ("http://ftp.gnu.org/gnu/autoconf/autoconf-"
         "{major}.{minor}.tar.gz".format(major=maxMajor, minor=maxMinor))

    raise TarballLost("Tarball url not found")

def Install(software, platform, platformData, verbose):
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
             ["./configure", "--prefix=/usr/local"],
             verbose
            )
            RunCommand(
             ["make", "-j{cores_count}".format(cores_count=os.cpu_count())],
             verbose)
            RunCommand(["make", "install"], verbose)
    except CommandError:
        print("VGAZER: Unable to install", software)
        raise InstallError(
         "{software} not installed".format(software=software))

    print("VGAZER:", software, "installed")
