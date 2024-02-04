import os
import requests
from bs4 import BeautifulSoup

from libvgazer.command     import RunCommand
from libvgazer.exceptions  import CommandError
from libvgazer.exceptions  import InstallError
from libvgazer.exceptions  import TarballLost
from libvgazer.platform    import GetAr
from libvgazer.platform    import GetCc
from libvgazer.platform    import GetInstallPrefix
from libvgazer.platform    import GetRanlib
from libvgazer.store.temp  import StoreTemp
from libvgazer.working_dir import WorkingDir

def GetTarballUrl():
    response = requests.get("http://www.lua.org/download.html")
    html = response.content
    parsedHtml = BeautifulSoup(html, "html.parser")

    links = parsedHtml.find_all("a")
    for link in links:
        if "ftp/lua-" in link["href"]:
            return "http://www.lua.org/" + link["href"]

    raise TarballLost(
     "Unable to find tarball with last stable release of Lua")

def Install(auth, software, platform, platformData, mirrors, verbose):
    installPrefix = GetInstallPrefix(platformData)
    ar = GetAr(platformData["target"]) + " rcu"
    cc = GetCc(platformData["target"]) + " -std=gnu99"
    ranlib = GetRanlib(platformData["target"])

    storeTemp = StoreTemp()
    storeTemp.ResolveEmptySubdirectory(software)
    tempPath = storeTemp.GetSubdirectoryPath(software)

    tarballUrl = GetTarballUrl()
    tarballShortFilename = tarballUrl.split("/")[-1]

    luaTarget = {
        "linux": "linux",
        "windows": "mingw",
    }[platformData["target"].GetOs()]

    try:
        with WorkingDir(tempPath):
            RunCommand(["wget", "-P", "./", tarballUrl], verbose)
            RunCommand(
             ["tar", "--verbose", "--extract", "--gzip", "--file",
              tarballShortFilename],
             verbose)
        extractedDir = os.path.join(tempPath,
         tarballShortFilename[0:-7])
        with WorkingDir(extractedDir):
            # We need not Lua commandline tools, because it depends on readline
            # library. We need not extra depends like it. We need unly lua
            # library. This arguments prevent building commandline tools:
            # TO_BIN=
            # LUA_T=
            # LUAC_T=
            # INSTALL_BIN=
            # INSTALL_EXEC=true
            RunCommand(
             [
              "make", "-j{cores_count}".format(cores_count=os.cpu_count()),
              luaTarget, "CC=" + cc, "AR=" + ar, "RANLIB=" + ranlib, "TO_BIN=",
              "LUA_T=", "LUAC_T="
             ],
             verbose
            )
            RunCommand(
             ["make", luaTarget, "install", "INSTALL_TOP=" + installPrefix,
              "TO_BIN=", "LUA_T=", "LUAC_T=", "INSTALL_BIN=",
              "INSTALL_EXEC=true"],
             verbose)
    except CommandError:
        print("VGAZER: Unable to install", software)
        raise InstallError(software + " not installed")

    print("VGAZER:", software, "installed")
