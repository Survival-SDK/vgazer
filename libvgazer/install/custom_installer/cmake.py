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
    response = requests.get("https://cmake.org/download/")
    html = response.content.decode("utf-8")
    parsedHtml = BeautifulSoup(html, "html.parser")

    headers3 = parsedHtml.find_all("h3")
    for header in headers3:
        if header.text.find("Latest Release") != -1:
            version = header.text.split("(")[1][:-1:]
            return ("https://github.com/Kitware/CMake/releases/download/"
             "v{version}/cmake-{version}.tar.gz").format(version=version)

    raise TarballLost("Tarball url not found")

def Install(auth, software, platform, platformData, mirrors, verbose):
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
             [
              "./bootstrap",
              "--parallel={cores_count}".format(cores_count=os.cpu_count()),
              "--",
              "-DCMAKE_USE_OPENSSL=OFF",
             ],
             verbose)
            RunCommand(["make"], verbose)
            RunCommand(["make", "install"], verbose)
    except CommandError:
        print("VGAZER: Unable to install", software)
        raise InstallError(software + " not installed")

    print("VGAZER:", software, "installed")
