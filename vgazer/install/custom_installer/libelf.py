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

def GetTarballUrl():
    response = requests.get("https://sourceware.org/elfutils/ftp/")
    html = response.content.decode("utf-8")
    parsedHtml = BeautifulSoup(html, "html.parser")

    links = parsedHtml.find_all("a")

    maxVersionMajor = -1
    maxVersionMinor = -1
    for link in links:
        if ("." in link.text and "/" in link.text):
            version = link.text.split("/")[0].split(".")
            versionMajor = int(version[0])
            versionMinor = int(version[1])

            if versionMajor > maxVersionMajor:
                maxVersionMajor = versionMajor
                maxVersionMinor = versionMinor
                url = ("https://sourceware.org/elfutils/ftp/" + link["href"]
                 + "elfutils-" + str(versionMajor) + "." + str(versionMinor)
                 + ".tar.bz2")
            elif (versionMajor == maxVersionMajor
             and versionMinor > maxVersionMinor):
                maxVersionMinor = versionMinor
                url = ("https://sourceware.org/elfutils/ftp/" + link["href"]
                 + "elfutils-" + str(versionMajor) + "." + str(versionMinor)
                 + ".tar.bz2")

    return url

def Install(auth, software, platform, platformData, verbose):
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
             ["tar", "--verbose", "--extract", "--bzip2", "--file",
              tarballShortFilename],
             verbose)
        extractedDir = os.path.join(tempPath, tarballShortFilename[0:-8])
        with WorkingDir(extractedDir):
            RunCommand(
             ["./configure", "--host=" + targetTriplet,
              "--prefix=" + installPrefix, "--enable-debugpred",
              "--enable-gprof", "--enable-gcov", "--enable-install-elfh",
              "--disable-debuginfod",
              "CPPFLAGS=-I" + installPrefix + "/include",
              "LDFLAGS=-L" + installPrefix + "/lib"],
             verbose)
        with WorkingDir(extractedDir + "/lib"):
            RunCommand(["make"], verbose)
        with WorkingDir(extractedDir + "/libelf"):
            RunCommand(["make"], verbose)
            RunCommand(["make", "install"], verbose)
        with WorkingDir(extractedDir + "/config"):
            RunCommand(["make", "install"], verbose)
    except CommandError:
        print("VGAZER: Unable to install", software)
        raise InstallError(software + " not installed")

    print("VGAZER:", software, "installed")
