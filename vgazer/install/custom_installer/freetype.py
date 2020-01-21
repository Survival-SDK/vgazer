import os
import os.path
import requests

from vgazer.command     import RunCommand
from vgazer.exceptions  import CommandError
from vgazer.exceptions  import InstallError
from vgazer.platform    import GetInstallPrefix
from vgazer.platform    import GetTriplet
from vgazer.store.temp  import StoreTemp
from vgazer.working_dir import WorkingDir

def Install(auth, software, platform, platformData, mirrors, verbose):
    installPrefix = GetInstallPrefix(platformData)
    targetTriplet = GetTriplet(platformData["target"])

    storeTemp = StoreTemp()
    storeTemp.ResolveEmptySubdirectory(software)
    tempPath = storeTemp.GetSubdirectoryPath(software)

    tarballUrl = requests.get(
     "https://sourceforge.net/projects/freetype/best_release.json"
    ).json()["release"]["url"]
    tarballShortFilename = tarballUrl.split("/")[-2]

    if os.path.exists(installPrefix + "/lib/libharfbuzz.a"):
        withHarfbuzz = "yes"
    else:
        withHarfbuzz = "no"

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
            RunCommand(
             ["./configure", "--host=" + targetTriplet,
              "--prefix=" + installPrefix,
              "--with-zlib=yes", "--with-bzip2=yes", "--with-png=yes",
              "--with-harfbuzz=" + withHarfbuzz, "--with-old-mac-fonts",
              "PKG_CONFIG_PATH=" + installPrefix + "/lib/pkgconfig",
              "BZIP2_CFLAGS=-I" + installPrefix + "/include",
              "BZIP2_LIBS=-L" + installPrefix + "/lib -lbz2",
              "HARFBUZZ_CFLAGS=-I" + installPrefix + "/include/harfbuzz",
              "HARFBUZZ_LIBS=-L" + installPrefix + "/lib -lharfbuzz"],
             verbose)
            RunCommand(["make"], verbose)
            RunCommand(["make", "install"], verbose)
    except CommandError:
        print("VGAZER: Unable to install", software)
        raise InstallError(software + " not installed")

    print("VGAZER:", software, "installed")
