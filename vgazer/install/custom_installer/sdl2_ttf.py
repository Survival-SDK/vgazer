import os
import requests
from bs4 import BeautifulSoup

from vgazer.command     import RunCommand
from vgazer.exceptions  import CommandError
from vgazer.exceptions  import InstallError
from vgazer.exceptions  import TarballLost
from vgazer.platform    import GetInstallPrefix
from vgazer.platform    import GetTriplet
from vgazer.store.temp  import StoreTemp
from vgazer.working_dir import WorkingDir

def GetTarballUrl():
    response = requests.get("https://www.libsdl.org/projects/SDL_ttf/")
    html = response.content
    parsedHtml = BeautifulSoup(html, "html.parser")

    links = parsedHtml.find_all("a")
    for link in links:
        if (link.text.find(".tar.gz") != -1 and link.text.find("devel") == -1):
            return "https://www.libsdl.org/projects/SDL_ttf/" + link["href"]

    raise TarballLost(
     "Unable to find tarball with last stable release of SDL2_ttf")

def Install(auth, software, platform, platformData, mirrors, verbose):
    installPrefix = GetInstallPrefix(platformData)
    targetTriplet = GetTriplet(platformData["target"])

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
            try:
                RunCommand(
                 ["./configure", "--host=" + targetTriplet,
                  "--prefix=" + installPrefix, "--disable-sdltest",
                  "--disable-freetypetest",
                  "--with-sdl-prefix=" + installPrefix,
                  "CPPFLAGS=-I" + installPrefix + "/include/SDL2",
                  "LDFLAGS=-L" + installPrefix + "/lib -W1,-rpath-link,"
                  + installPrefix + "/lib",
                  "LIBS=-lSDL2 -lglib-2.0 -lgraphite2",
                  ],
                 verbose)
            except CommandError as e:
                try:
                    RunCommand(["cat", "./config.log"], verbose)
                except CommandError:
                    print("VGAZER: 'config.log' not found")
                finally:
                    raise e
            RunCommand(["make"], verbose)
            RunCommand(["make", "install"], verbose)
    except CommandError:
        print("VGAZER: Unable to install", software)
        raise InstallError(software + " not installed")

    print("VGAZER:", software, "installed")
