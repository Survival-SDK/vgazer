import os
import requests
from bs4 import BeautifulSoup

from vgazer.command         import RunCommand
from vgazer.config.meson    import ConfigMeson
from vgazer.env_vars        import SetEnvVar
from vgazer.exceptions      import CommandError
from vgazer.exceptions      import InstallError
from vgazer.exceptions      import TarballLost
from vgazer.platform        import GetInstallPrefix
from vgazer.store.temp      import StoreTemp
from vgazer.working_dir     import WorkingDir

# Unable to get last versions via github API, because github API don't give
# info about all tags but info about small amount of prehistoric tags instead.
def GetTarballUrl():
    response = requests.get("https://github.com/freedesktop/mesa-drm/releases")
    html = response.content.decode("utf-8")
    parsedHtml = BeautifulSoup(html, "html.parser")

    links = parsedHtml.find_all("a")

    for link in links:
        if ("/freedesktop/mesa-drm/archive/libdrm-" in link["href"]
         and ".tar.gz" in link["href"]):
            return "github.com" + link["href"]

    raise TarballLost("Unable to find tarball of libdrm's last version")

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
             ["tar", "--verbose", "--extract", "--gzip", "--file",
              tarballShortFilename],
             verbose)
        extractedDir = os.path.join(tempPath,
         "mesa-drm-" + tarballShortFilename[0:-7])
        with WorkingDir(extractedDir):
            RunCommand(["mkdir", "build"], verbose)
        SetEnvVar("PKG_CONFIG_PATH", installPrefix + "/lib/pkgconfig")
        buildDir = os.path.join(extractedDir, "build")
        with WorkingDir(buildDir):
            RunCommand(
             ["meson", "--prefix=" + installPrefix,
              "--libdir=" + installPrefix + "/lib", "--cross-file",
              configMeson.GetCrossFileName(), "-Dudev=true",
              "-Dcairo-tests=false", "-Dman-pages=false"],
             verbose)
            RunCommand(["ninja"], verbose)
            RunCommand(["ninja", "install"], verbose)
    except CommandError:
        print("VGAZER: Unable to install", software)
        raise InstallError(software + " not installed")

    print("VGAZER:", software, "installed")
