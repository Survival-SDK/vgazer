import os
import requests
from bs4 import BeautifulSoup

from libvgazer.command      import RunCommand
from libvgazer.config.cmake import ConfigCmake
from libvgazer.exceptions   import CommandError
from libvgazer.exceptions   import InstallError
from libvgazer.platform     import GetAr
from libvgazer.platform     import GetCxx
from libvgazer.platform     import GetInstallPrefix
from libvgazer.store.temp   import StoreTemp
from libvgazer.working_dir  import WorkingDir

def GetArchiveUrl(auth):
    response = requests.get("http://baical.net/downloads.html")
    html = response.content.decode("utf-8")
    parsedHtml = BeautifulSoup(html, "html.parser")

    links = parsedHtml.find_all("a")

    for link in links:
        if link["title"] == "P7 library":
            return "http://baical.net{link}".format(link=link["href"])

def Install(auth, software, platform, platformData, mirrors, verbose):
    configCmake = ConfigCmake(platformData)
    configCmake.GenerateCrossFile()
    toolchainFile = configCmake.GetCrossFileName()

    installPrefix = GetInstallPrefix(platformData)
    ar = GetAr(platformData["target"])
    cxx = GetCxx(platformData["target"])

    storeTemp = StoreTemp()
    storeTemp.ResolveEmptySubdirectory(software)
    tempPath = storeTemp.GetSubdirectoryPath(software)

    archiveUrl = GetArchiveUrl(auth)
    arhiveShortFilename = archiveUrl.split("/")[-1]

    try:
        with WorkingDir(tempPath):
            RunCommand(["wget", "-P", "./", archiveUrl], verbose)
            RunCommand(["unzip", arhiveShortFilename], verbose)
            RunCommand(["mkdir", "build"], verbose)
        buildDir = os.path.join(tempPath, "build")
        with WorkingDir(buildDir):
            RunCommand(
             ["cmake", "..",
              "-DCMAKE_TOOLCHAIN_FILE={file}".format(file=toolchainFile),
              "-DCMAKE_INSTALL_PREFIX={prefix}".format(prefix=installPrefix),
              "-DCMAKE_VERBOSE_MAKEFILE:BOOL=ON", "-DP7_BUILD_SHARED=ON",
              "-DBUILD_TESTS=OFF", "-DBUILD_EXAMPLES=OFF"],
             verbose)
            RunCommand(
             ["make", "-j{cores_count}".format(cores_count=os.cpu_count())],
             verbose)
            RunCommand(["make", "install"], verbose)
    except CommandError:
        print("VGAZER: Unable to install", software)
        raise InstallError("{software} not installed".format(software=software))

    print("VGAZER:", software, "installed")
