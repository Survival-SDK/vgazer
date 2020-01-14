import os
import requests
from bs4 import BeautifulSoup

from vgazer.command     import RunCommand
from vgazer.env_vars    import SetEnvVar
from vgazer.exceptions  import CommandError
from vgazer.exceptions  import InstallError
from vgazer.platform    import GetAr
from vgazer.platform    import GetCxx
from vgazer.platform    import GetSoFilename
from vgazer.platform    import GetInstallPrefix
from vgazer.platform    import GetSoPrefix
from vgazer.store.temp  import StoreTemp
from vgazer.working_dir import WorkingDir

def GetArchiveUrl(auth):
    response = requests.get("http://baical.net/downloads.html")
    html = response.content.decode("utf-8")
    parsedHtml = BeautifulSoup(html, "html.parser")

    links = parsedHtml.find_all("a")

    for link in links:
        if link["title"] == "P7 library":
            return "http://baical.net" + link["href"]

def Install(auth, software, platform, platformData, mirrors, verbose):
    installPrefix = GetInstallPrefix(platformData)
    soPrefix = GetSoPrefix(platformData)
    ar = GetAr(platformData["target"])
    cxx = GetCxx(platformData["target"])
    soFilename = GetSoFilename(platformData["target"], "P7")

    storeTemp = StoreTemp()
    storeTemp.ResolveEmptySubdirectory(software)
    tempPath = storeTemp.GetSubdirectoryPath(software)

    archiveUrl = GetArchiveUrl(auth)
    arhiveShortFilename = archiveUrl.split("/")[-1]

    try:
        with WorkingDir(tempPath):
            RunCommand(["mkdir", "build"], verbose)
        buildDir = os.path.join(tempPath, "build")
        with WorkingDir(buildDir):
            RunCommand(["wget", "-P", "./", archiveUrl], verbose)
            RunCommand(["unzip", arhiveShortFilename], verbose)
        sourcesDir = os.path.join(buildDir, "Sources")
        with WorkingDir(sourcesDir):
            RunCommand(
             ["sed", "-i", "-e", "s/g++/$(CXX)/g", "-e", "s/\\tar/\\t$(AR)/g",
              "-e", "s/libP7.so/" + soFilename + "/g", "./makefile"],
             verbose)
            SetEnvVar("CXX", cxx)
            SetEnvVar("AR", ar)
            RunCommand(["mkdir", "-p", "./../Binaries"], verbose)
            RunCommand(["mkdir", "-p", "./../Binaries/Temp"], verbose)
            RunCommand(["make", "./../Binaries/" + soFilename], verbose)
            RunCommand(["make", "./../Binaries/libP7.a"], verbose)
        with WorkingDir(buildDir):
            if not os.path.exists(installPrefix + "/include"):
                RunCommand(["mkdir", "-p", installPrefix + "/include"], verbose)
            if not os.path.exists(installPrefix + "/lib"):
                RunCommand(["mkdir", "-p", installPrefix + "/lib"], verbose)
            if not os.path.exists(soPrefix):
                RunCommand(["mkdir", "-p", soPrefix], verbose)
            RunCommand(
             ["sh", "-c", "cp ./Headers/*.h " + installPrefix + "/include"],
             verbose)
            RunCommand(["cp", "./Binaries/" + soFilename, soPrefix], verbose)
            RunCommand(["cp", "./Binaries/libP7.a", installPrefix + "/lib"],
             verbose)
    except CommandError:
        print("VGAZER: Unable to install", software)
        raise InstallError(software + " not installed")

    print("VGAZER:", software, "installed")
