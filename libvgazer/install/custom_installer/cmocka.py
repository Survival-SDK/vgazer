import os
import requests
from bs4 import BeautifulSoup

from libvgazer.command      import GetCommandOutputUtf8
from libvgazer.command      import RunCommand
from libvgazer.config.cmake import ConfigCmake
from libvgazer.exceptions   import CommandError
from libvgazer.exceptions   import InstallError
from libvgazer.platform     import GetArFullPath
from libvgazer.platform     import GetInstallPrefix
from libvgazer.store.temp   import StoreTemp
from libvgazer.working_dir  import WorkingDir

def GetMinorVersionLink():
    response = requests.get("https://cmocka.org/files/")
    html = response.content.decode("utf-8")
    parsedHtml = BeautifulSoup(html, "html.parser")

    links = parsedHtml.find_all("a")

    lastVersionMajor = 0
    lastVersionMinor = 0

    for link in links:
        if (link["href"][-1] == "/" and link["href"] != "/"):
            linkVersionMajor = int(link.text.split(".")[0])
            linkVersionMinor = int(link.text.split(".")[1][:-1:])
            if linkVersionMinor > lastVersionMinor:
                lastVersionMinor = linkVersionMinor
                lastVersionLinkText = link["href"]
            if linkVersionMajor > lastVersionMajor:
                lastVersionMajor = linkVersionMajor
                lastVersionMinor = linkVersionMinor
                lastVersionLinkText = link["href"]
    return "https://cmocka.org/files/" + lastVersionLinkText

def Install(auth, software, platform, platformData, mirrors, verbose):
    configCmake = ConfigCmake(platformData)
    configCmake.GenerateCrossFile()

    installPrefix = GetInstallPrefix(platformData)
    ar = GetArFullPath(platformData["target"])

    storeTemp = StoreTemp()
    storeTemp.ResolveEmptySubdirectory(software)
    tempPath = storeTemp.GetSubdirectoryPath(software)

    minorVersionLink = GetMinorVersionLink()

    response = requests.get(minorVersionLink)
    html = response.content.decode("utf-8")
    parsedHtml = BeautifulSoup(html, "html.parser")

    links = parsedHtml.find_all("a")

    tarballUrl = minorVersionLink + "/" + links[-2]["href"]
    tarballShortFilename = tarballUrl.split("/")[-1]

    try:
        with WorkingDir(tempPath):
            RunCommand(["wget", "-P", "./", tarballUrl], verbose)
            RunCommand(
             ["tar", "--verbose", "--extract", "--xz", "--file",
              tarballShortFilename],
             verbose)
            output = GetCommandOutputUtf8(
             ["tar", "--list", "--file", tarballShortFilename]
            )
        extractedDir = os.path.join(tempPath,
         output.splitlines()[0].split("/")[0])
        with WorkingDir(extractedDir):
            RunCommand(["mkdir", "build"], verbose)
        buildDir = os.path.join(extractedDir, "build")
        with WorkingDir(buildDir):
            RunCommand(
             ["cmake", "..",
              "-DCMAKE_TOOLCHAIN_FILE=" + configCmake.GetCrossFileName(),
              "-DCMAKE_BUILD_TYPE=Debug",
              "-DCMAKE_INSTALL_PREFIX=" + installPrefix,
              "-DCMAKE_VERBOSE_MAKEFILE:BOOL=ON", "-DCMAKE_AR=" + ar,
              "-DWITH_STATIC_LIB=ON"],
             verbose)
            RunCommand(
             ["make", "-j{cores_count}".format(cores_count=os.cpu_count())],
             verbose)
            RunCommand(["make", "install"], verbose)
    except CommandError:
        print("VGAZER: Unable to install", software)
        raise InstallError(software + " not installed")

    print("VGAZER:", software, "installed")
