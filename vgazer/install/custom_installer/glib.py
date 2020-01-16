import os
import requests
from bs4 import BeautifulSoup

from vgazer.command     import RunCommand
from vgazer.config.meson    import ConfigMeson
from vgazer.env_vars    import SetEnvVar
from vgazer.exceptions  import CommandError
from vgazer.exceptions  import InstallError
from vgazer.exceptions  import ProjectPubNotFound
from vgazer.exceptions  import TarballLost
from vgazer.platform    import GetInstallPrefix
from vgazer.store.temp  import StoreTemp
from vgazer.working_dir import WorkingDir

def GetVersionPubUrl():
    response = requests.get("https://developer.gnome.org/glib/")
    html = response.content.decode("utf-8")
    parsedHtml = BeautifulSoup(html, "html.parser")

    versions = parsedHtml.body.find("ul", attrs={"class": "versions"})
    links = versions.find_all("a")
    for link in links:
        if link.parent.name == "strong":
            versionMajor = link.text.split(".")[0]
            versionMinor = link.text.split(".")[1]
            return ("https://ftp.gnome.org/pub/gnome/sources/glib/" +
             versionMajor + "." + versionMinor + "/")

    raise ProjectPubNotFound("Unable to find pub of glib's last version")

def GetTarballUrl():
    versionPubUrl = GetVersionPubUrl()
    response = requests.get(versionPubUrl)
    html = response.content.decode("utf-8")
    parsedHtml = BeautifulSoup(html, "html.parser")

    links = parsedHtml.find_all("a")
    for link in links:
        if link["href"].startswith("LATEST-IS"):
            latest = link["href"].split("-")[2]
            return versionPubUrl + "/glib-" + latest + ".tar.xz"

    raise TarballLost("Unable to find tarball of glib's last version")

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
            RunCommand(
             ["wget", "-P", "./", "-O", tarballShortFilename, tarballUrl],
             verbose
            )
            RunCommand(
             ["tar", "--verbose", "--extract", "--xz", "--file",
              tarballShortFilename],
             verbose
            )
        SetEnvVar("PKG_CONFIG_PATH", installPrefix + "/lib/pkgconfig")
        extractedDir = os.path.join(tempPath, tarballShortFilename[0:-7])
        with WorkingDir(extractedDir):
            RunCommand(
             ["meson", "_build", "-Dprefix=" + installPrefix,
              "--libdir=" + installPrefix + "/lib", "--cross-file",
              configMeson.GetCrossFileName(), "-Dbuildtype=release",
              "-Ddefault_library=shared", "-Doptimization=2", "-Dstrip=true",
              "-Dforce_posix_threads=true", "-Dinternal_pcre=false",
              "-Dgtk_doc=false", "-Dman=false", "-Db_coverage=false",
              "-Dlibmount=true", "-Dxattr=true"],
             verbose)
            RunCommand(["ninja", "-C", "_build"], verbose)
            RunCommand(["ninja", "-C", "_build", "install"], verbose)
    except CommandError:
        print("VGAZER: Unable to install", software)
        raise InstallError(software + " not installed")

    print("VGAZER:", software, "installed")
