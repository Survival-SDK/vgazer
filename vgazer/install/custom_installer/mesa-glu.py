import os
import requests
from bs4     import BeautifulSoup
from pathlib import Path

from vgazer.command      import RunCommand
from vgazer.config.meson import ConfigMeson
from vgazer.exceptions   import CommandError
from vgazer.exceptions   import InstallError
from vgazer.exceptions   import TarballLost
from vgazer.platform     import GetInstallPrefix
from vgazer.store.temp   import StoreTemp
from vgazer.working_dir  import WorkingDir

def GetTarballUrl():
    response = requests.get("https://mesa.freedesktop.org/archive/glu")
    html = response.content.decode("utf-8")
    parsedHtml = BeautifulSoup(html, "html.parser")

    links = parsedHtml.find_all("a")

    maxVersionMajor = -1
    maxVersionMinor = -1
    maxVersionPatch = -1
    for link in links:
        if ("glu-" in link.text
         and (".tar.gz" in link.text or ".tar.xz" in link.text)
         and ".sig" not in link.text):
            arfmt = ".tar.gz" if ".tar.gz" in link.text else ".tar.xz";

            version = link.text.split("-")[1].split(arfmt)[0].split(".")
            versionMajor = int(version[0])
            versionMinor = int(version[1])
            versionPatch = int(version[2])

            if versionMajor > maxVersionMajor:
                maxVersionMajor = versionMajor
                maxVersionMinor = versionMinor
                maxVersionPatch = versionPatch
                url = "https://mesa.freedesktop.org/archive/glu/{href}".format(
                 href=link["href"])
            elif (versionMajor == maxVersionMajor
             and versionMinor > maxVersionMinor):
                maxVersionMinor = versionMinor
                maxVersionPatch = versionPatch
                url = "https://mesa.freedesktop.org/archive/glu/{href}".format(
                 href=link["href"])
            elif (versionMajor == maxVersionMajor
             and versionMinor == maxVersionMinor
             and versionPatch > maxVersionPatch):
                maxVersionPatch = versionPatch
                url = "https://mesa.freedesktop.org/archive/glu/{href}".format(
                 href=link["href"])

    if url is not None:
        return url

    raise TarballLost("Unable to find tarball of mesa-glu last version")

def Install(auth, software, platform, platformData, mirrors, verbose):
    configMeson = ConfigMeson(platformData)
    configMeson.GenerateCrossFile()

    installPrefix = GetInstallPrefix(platformData)

    storeTemp = StoreTemp()
    storeTemp.ResolveEmptySubdirectory(software)
    tempPath = storeTemp.GetSubdirectoryPath(software)

    tarballUrl = GetTarballUrl()
    tarballShortFilename = tarballUrl.split("/")[-1]
    ext = Path(tarballShortFilename).suffix

    try:
        with WorkingDir(tempPath):
            RunCommand(["wget", "-P", "./", tarballUrl], verbose)
            RunCommand(
             [
              "tar", "--verbose", "--extract",
              "--gzip" if ext == "gz" else "--xz", "--file",
              tarballShortFilename
             ],
             verbose)
        extractedDir = os.path.join(tempPath, tarballShortFilename[0:-7])
        with WorkingDir(extractedDir):
            RunCommand(
             ["meson", "setup", "build/",
              "--prefix={prefix}".format(prefix=installPrefix),
              "--cross-file", configMeson.GetCrossFileName(),
              "-Dgl_provider=gl"
             ],
             verbose)
            RunCommand(["ninja", "-C", "build/"], verbose)
            RunCommand(["ninja", "-C", "build/", "install"], verbose)
    except CommandError:
        print("VGAZER: Unable to install", software)
        raise InstallError("{software} not installed".format(software=software))

    print("VGAZER:", software, "installed")
