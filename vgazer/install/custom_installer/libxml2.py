import os
import requests
from bs4 import BeautifulSoup

from vgazer.command         import RunCommand
from vgazer.exceptions      import CommandError
from vgazer.exceptions      import InstallError
from vgazer.platform        import GetInstallPrefix
from vgazer.platform        import GetTriplet
from vgazer.store.temp      import StoreTemp
from vgazer.version.utils   import GetVersionFromTag
from vgazer.working_dir     import WorkingDir

def GetTarballUrl():
    response = requests.get("http://xmlsoft.org/news.html")
    html = response.content.decode("utf-8")
    parsedHtml = BeautifulSoup(html, "html.parser")

    version = GetVersionFromTag(parsedHtml.h3.text.split(":")[0])

    return "ftp://xmlsoft.org/libxml2/libxml2-" + version + ".tar.gz"

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
            RunCommand(["wget", "-P", "./", tarballUrl], verbose)
            RunCommand(
             ["tar", "--verbose", "--extract", "--gzip", "--file",
              tarballShortFilename],
             verbose)
        extractedDir = os.path.join(tempPath, tarballShortFilename[0:-7])
        with WorkingDir(extractedDir):
            RunCommand(
             ["./configure", "--host=" + targetTriplet,
              "--prefix=" + installPrefix, "--without-python",
              "LDFLAGS=-L" + installPrefix + "/lib",
              "LIBS=-lz -llzma",
              "CPPFLAGS=-I" + installPrefix + "/include"],
             verbose)
            RunCommand(
             ["make", "-j{cores_count}".format(cores_count=os.cpu_count())],
             verbose)
            RunCommand(["make", "install"], verbose)
    except CommandError:
        print("VGAZER: Unable to install", software)
        raise InstallError(software + " not installed")

    print("VGAZER:", software, "installed")
