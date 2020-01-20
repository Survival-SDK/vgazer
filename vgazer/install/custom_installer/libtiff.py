import os
import requests
from bs4 import BeautifulSoup

import vgazer.version.utils as utils

from vgazer.command     import RunCommand
from vgazer.exceptions  import CommandError
from vgazer.exceptions  import InstallError
from vgazer.exceptions  import TarballLost
from vgazer.platform    import GetInstallPrefix
from vgazer.platform    import GetTriplet
from vgazer.store.temp  import StoreTemp
from vgazer.working_dir import WorkingDir

def GetTarballUrl():
    response = requests.get("http://libtiff.maptools.org/")
    html = response.content.decode("utf-8")
    parsedHtml = BeautifulSoup(html, "html.parser")

    table = parsedHtml.table
    link = table.findChildren("a")[3]

    return ("https://download.osgeo.org/libtiff/tiff-"
     + utils.GetVersionFromTag(link.text) + ".tar.gz")

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
            RunCommand(
             ["./configure", "--host=" + targetTriplet,
              "--prefix=" + installPrefix, "--disable-jbig",
              "--with-zlib-include-dir=" + installPrefix + "/include",
              "--with-zlib-lib-dir=" + installPrefix + "/lib",
              "--with-jpeg-include-dir=" + installPrefix + "/include",
              "--with-jpeg-lib-dir=" + installPrefix + "/lib",
              "--with-lzma-include-dir=" + installPrefix + "/include",
              "--with-lzma-lib-dir=" + installPrefix + "/lib",
              "--with-zstd-include-dir=" + installPrefix + "/include",
              "--with-zstd-lib-dir=" + installPrefix + "/lib",
              "--with-webp-include-dir=" + installPrefix + "/include",
              "--with-webp-lib-dir=" + installPrefix + "/lib",
              ],
             verbose)
            RunCommand(["make"], verbose)
            RunCommand(["make", "install"], verbose)
    except CommandError:
        print("VGAZER: Unable to install", software)
        raise InstallError(software + " not installed")

    print("VGAZER:", software, "installed")
