import os
import requests
from bs4 import BeautifulSoup

from vgazer.command         import RunCommand
from vgazer.config.meson    import ConfigMeson
from vgazer.env_vars        import SetEnvVar
from vgazer.exceptions      import CommandError
from vgazer.exceptions      import InstallError
from vgazer.platform        import GetInstallPrefix
from vgazer.store.temp      import StoreTemp
from vgazer.working_dir     import WorkingDir

def GetTarballUrl():
    response = requests.get("https://mesa.freedesktop.org/archive/")
    html = response.content.decode("utf-8")
    parsedHtml = BeautifulSoup(html, "html.parser")

    links = parsedHtml.find_all("a")

    maxVersionMajor = -1
    maxVersionMinor = -1
    maxVersionPatch = -1
    maxVersionRc = -1
    for link in links:
        if ("mesa-" in link.text and ".tar.xz" in link.text
         and ".sig" not in link.text):
            if "rc" in link.text:
                version = link.text.split("-")[1].split(".")
                versionMajor = int(version[0])
                versionMinor = int(version[1])
                try:
                    versionPatch = int(version[2])
                except IndexError:
                    versionPatch = int(link.text.split("-")[2])
                versionRc = int(link.text.split("rc")[1][0])
            else:
                version = link.text.split("-")[1].split(".tar.xz")[0].split(
                 ".")
                versionMajor = int(version[0])
                versionMinor = int(version[1])
                versionPatch = int(version[2])
                versionRc = 0

            if versionMajor > maxVersionMajor:
                maxVersionMajor = versionMajor
                maxVersionMinor = versionMinor
                maxVersionPatch = versionPatch
                maxVersionRc = versionRc
                url = "https://mesa.freedesktop.org/archive/" + link["href"]
            elif (versionMajor == maxVersionMajor
             and versionMinor > maxVersionMinor):
                maxVersionMinor = versionMinor
                maxVersionPatch = versionPatch
                maxVersionRc = versionRc
                url = "https://mesa.freedesktop.org/archive/" + link["href"]
            elif (versionMajor == maxVersionMajor
             and versionMinor == maxVersionMinor
             and versionPatch > maxVersionPatch):
                maxVersionPatch = versionPatch
                maxVersionRc = versionRc
                url = "https://mesa.freedesktop.org/archive/" + link["href"]
            elif (versionMajor == maxVersionMajor
             and versionMinor == maxVersionMinor
             and versionPatch == maxVersionPatch
             and (
              versionRc != 0 and maxVersionRc != 0 and versionRc > maxVersionRc
               or versionRc == 0 and maxVersionRc != 0
             )
            ):
                maxVersionRc = versionRc
                url = "https://mesa.freedesktop.org/archive/" + link["href"]

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

    try:
        with WorkingDir(tempPath):
            RunCommand(["wget", "-P", "./", tarballUrl], verbose)
            RunCommand(
             ["tar", "--verbose", "--extract", "--xz", "--file",
              tarballShortFilename],
             verbose)
        SetEnvVar(
         "PKG_CONFIG_PATH",
         "{prefix}/share/pkgconfig:{prefix}/lib/pkgconfig".format(
          prefix=installPrefix)
        )
        extractedDir = os.path.join(tempPath, tarballShortFilename[0:-7])
        with WorkingDir(extractedDir):
            RunCommand(
             ["meson", "build/", "--prefix=" + installPrefix,
              "--libdir=" + installPrefix + "/lib",
              "--cross-file", configMeson.GetCrossFileName(),
              "-Dplatforms=x11,wayland,drm,surfaceless"],
             verbose)
            RunCommand(["ninja", "-C", "build/"], verbose)
            RunCommand(["ninja", "-C", "build/", "install"], verbose)
    except CommandError:
        print("VGAZER: Unable to install", software)
        raise InstallError(software + " not installed")

    print("VGAZER:", software, "installed")
