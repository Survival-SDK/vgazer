import os
import requests
from bs4 import BeautifulSoup

from vgazer.command      import RunCommand
from vgazer.config.meson import ConfigMeson
from vgazer.exceptions   import CommandError
from vgazer.exceptions   import InstallError
from vgazer.platform     import GetInstallPrefix
from vgazer.store.temp   import StoreTemp
from vgazer.working_dir  import WorkingDir

def GetTarballUrl():
    response = requests.get("https://dri.freedesktop.org/libdrm/")
    html = response.content.decode("utf-8")
    parsedHtml = BeautifulSoup(html, "html.parser")

    links = parsedHtml.find_all("a")

    maxVersionMajor = -1
    maxVersionMinor = -1
    maxVersionPatch = -1
    for link in links:
        if ("libdrm-" in link.text
         and (".tar.gz" in link.text or ".tar.xz" in link.text)
         and ".sig" not in link.text):
            version = link.text.split("-")[1].split(".tar.gz")[0].split(".")
            versionMajor = int(version[0])
            versionMinor = int(version[1])
            if len(version) == 2:
                versionPatch = 0
            else:
                versionPatch = int(version[2])

            if versionMajor > maxVersionMajor:
                maxVersionMajor = versionMajor
                maxVersionMinor = versionMinor
                maxVersionPatch = versionPatch
                url = "https://dri.freedesktop.org/libdrm/{link}".format(
                 link=link["href"])
            elif (versionMajor == maxVersionMajor
             and versionMinor > maxVersionMinor):
                maxVersionMinor = versionMinor
                maxVersionPatch = versionPatch
                url = "https://dri.freedesktop.org/libdrm/{link}".format(
                 link=link["href"])
            elif (versionMajor == maxVersionMajor
             and versionMinor == maxVersionMinor
             and versionPatch > maxVersionPatch):
                maxVersionPatch = versionPatch
                url = "https://dri.freedesktop.org/libdrm/{link}".format(
                 link=link["href"])

    return url

def Install(auth, software, platform, platformData, mirrors, verbose):
    configMeson = ConfigMeson(platformData)
    configMeson.GenerateCrossFile()

    installPrefix = GetInstallPrefix(platformData)

    storeTemp = StoreTemp()
    storeTemp.ResolveEmptySubdirectory(software)
    tempPath = storeTemp.GetSubdirectoryPath(software)

    tarballUrl = GetTarballUrl()
    tarballShortFilename = tarballUrl.split("/")[-1]
    tarrballExtension = tarballShortFilename.split(".")[-1]

    try:
        with WorkingDir(tempPath):
            RunCommand(["wget", "-P", "./", tarballUrl], verbose)
            RunCommand(
             ["tar", "--verbose", "--extract",
              "--gzip" if tarrballExtension == ".gz" else "--xz", "--file",
              tarballShortFilename
             ],
             verbose)
        extractedDir = os.path.join(tempPath, tarballShortFilename[0:-7])
        with WorkingDir(extractedDir):
            RunCommand(["mkdir", "build"], verbose)
        buildDir = os.path.join(extractedDir, "build")
        with WorkingDir(buildDir):
            RunCommand(
             ["meson", "setup",
              "--prefix={prefix}".format(prefix=installPrefix),
              "--libdir={prefix}/lib".format(prefix=installPrefix),
              "--cross-file", configMeson.GetCrossFileName(), "-Dudev=true",
              "-Dcairo-tests=disabled", "-Dman-pages=disabled",
              "-Dvalgrind=disabled", "-Dtests=false"
             ],
             verbose)
            RunCommand(["ninja"], verbose)
            RunCommand(["ninja", "install"], verbose)
    except CommandError:
        print("VGAZER: Unable to install", software)
        raise InstallError("{software} not installed".format(software=software))

    print("VGAZER:", software, "installed")
