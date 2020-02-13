import os
import requests
from bs4 import BeautifulSoup

from vgazer.command     import GetCommandOutputUtf8
from vgazer.command     import RunCommand
from vgazer.exceptions  import CommandError
from vgazer.exceptions  import InstallError
from vgazer.exceptions  import TarballLost
from vgazer.platform    import GetInstallPrefix
from vgazer.platform    import GetPkgConfig
from vgazer.platform    import GetTriplet
from vgazer.store.temp  import StoreTemp
from vgazer.working_dir import WorkingDir

def GetTarballUrl():
    response = requests.get("https://www.libsdl.org/projects/SDL_image/")
    html = response.content
    parsedHtml = BeautifulSoup(html, "html.parser")

    links = parsedHtml.find_all("a")
    for link in links:
        if (link.text.find(".tar.gz") != -1 and link.text.find("devel") == -1):
            return "https://www.libsdl.org/projects/SDL_image/" + link["href"]

    raise TarballLost(
     "Unable to find tarball with last stable release of SDL2_image")

def Install(auth, software, platform, platformData, mirrors, verbose):
    installPrefix = GetInstallPrefix(platformData)
    targetTriplet = GetTriplet(platformData["target"])
    pkgConfig = GetPkgConfig(platformData["target"])

    storeTemp = StoreTemp()
    storeTemp.ResolveEmptySubdirectory(software)
    tempPath = storeTemp.GetSubdirectoryPath(software)

    tarballUrl = GetTarballUrl()
    tarballShortFilename = tarballUrl.split("/")[-1]

    try:
        with WorkingDir(tempPath):
            RunCommand(
             ["wget", "-P", "./", "-O", tarballShortFilename, tarballUrl],
             verbose)
            RunCommand(
             ["tar", "--verbose", "--extract", "--gzip", "--file",
              tarballShortFilename],
             verbose)
        extractedDir = os.path.join(tempPath, tarballShortFilename[0:-7])
        with WorkingDir(extractedDir):
            #tiffLibs = GetCommandOutputUtf8(
             #[pkgConfig, "--libs", "--static", "libtiff-4"], verbose=False)
            #RunCommand(
             #["sed", "-i",
              #"-e", "s/"
              #"AC_CHECK_LIB("
              #"[tiff], [TIFFClientOpen], [have_tif_lib=yes], [], [-lz]"
              #")/"
              #"AC_CHECK_LIB("
              #"[tiff], [TIFFClientOpen], [have_tif_lib=yes], [], "
              #"[" + tiffLibs + "]"
              #")/g",
              #"./configure.in"],
             #verbose)
            #RunCommand(["./autogen.sh"], verbose)
            RunCommand(
             ["./configure", "--host=" + targetTriplet,
              "--prefix=" + installPrefix, "--disable-sdltest",
              "CPPFLAGS=-I" + installPrefix + "/include",
              "LDFLAGS=-L" + installPrefix + "/lib"],
             verbose)
            RunCommand(["make"], verbose)
            RunCommand(["make", "install"], verbose)
    except CommandError:
        print("VGAZER: Unable to install", software)
        raise InstallError(software + " not installed")

    print("VGAZER:", software, "installed")
