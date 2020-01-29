import os
import requests
from bs4 import BeautifulSoup

from vgazer.command     import RunCommand
from vgazer.exceptions  import CommandError
from vgazer.exceptions  import InstallError
#from vgazer.exceptions  import UnknownTargetArch
from vgazer.platform    import GetFilesystemType
from vgazer.platform    import GetInstallPrefix
from vgazer.store.temp  import StoreTemp
from vgazer.working_dir import WorkingDir

def InitVersionInfo():
    return {
        "maxVersionMajor": -1,
        "maxVersionMinor": -1,
        "maxVersionPatch": -1,
    }

def UpdateVersionInfo(versionInfo, splitedVersion, versionFilename):
    versionInfo["versionMajor"] = int(splitedVersion[0])
    versionInfo["versionMinor"] = int(splitedVersion[1])
    if len(splitedVersion) == 2:
        versionInfo["versionPatch"] = 0
    elif "a" in splitedVersion[2]:
        versionInfo["versionPatch"] = int(splitedVersion[2][:-1])
    else:
        versionInfo["versionPatch"] = int(splitedVersion[2])

    if versionInfo["versionMajor"] > versionInfo["maxVersionMajor"]:
        versionInfo["maxVersionMajor"] = versionInfo["versionMajor"]
        versionInfo["maxVersionMinor"] = versionInfo["versionMinor"]
        versionInfo["maxVersionPatch"] = versionInfo["versionPatch"]
        versionInfo["maxVersionFilename"] = versionFilename
    elif (versionInfo["versionMajor"] == versionInfo["maxVersionMajor"]
     and versionInfo["versionMinor"] > versionInfo["maxVersionMinor"]):
        versionInfo["maxVersionMinor"] = versionInfo["versionMinor"]
        versionInfo["maxVersionPatch"] = versionInfo["versionPatch"]
        versionInfo["maxVersionFilename"] = versionFilename
    elif (versionInfo["versionMajor"] == versionInfo["maxVersionMajor"]
     and versionInfo["versionMinor"] == versionInfo["maxVersionMinor"]
     and versionInfo["versionPatch"] > versionInfo["maxVersionPatch"]):
        versionInfo["maxVersionPatch"] = versionInfo["versionPatch"]
        versionInfo["maxVersionFilename"] = versionFilename

def GetLastKernelUrlInSubdir(auth, majorVersion):
    VersionDirUrl = ("https://mirrors.edge.kernel.org/pub/linux/kernel/v"
     + str(majorVersion) + ".x/")

    response = requests.get(VersionDirUrl)
    html = response.content.decode("utf-8")
    parsedHtml = BeautifulSoup(html, "html.parser")

    links = parsedHtml.find_all("a")

    versionInfo = InitVersionInfo()
    for link in links:
        if ("linux" in link.text and ".tar.gz" in link.text):
            version = link.text.split("-")[1].split(".tar.gz")[0].split(".")
            UpdateVersionInfo(versionInfo, version, link.text)

    if versionInfo["maxVersionMajor"] == -1:
        return None

    return VersionDirUrl + versionInfo["maxVersionFilename"]

def GetLastKernelUrl(auth):
    response = requests.get("https://www.kernel.org/pub/linux/kernel/")
    html = response.content.decode("utf-8")
    parsedHtml = BeautifulSoup(html, "html.parser")

    links = parsedHtml.find_all("a")

    maxVersion = -1
    for link in links:
        if "v" in link.text and "." in link.text:
            version = int(link.text[1:-1].split(".")[0])
            if version > maxVersion:
                maxVersion = version

    url = GetLastKernelUrlInSubdir(auth, maxVersion)
    if url is None:
        return GetLastKernelUrlInSubdir(auth, maxVersion - 1)
    else:
        return url

def InstallLinuxHeaders(auth, platformData, verbose):
    installPrefix = GetInstallPrefix(platformData)
    kernelArch = platformData["target"].GetArch()

    storeTemp = StoreTemp()
    storeTemp.ResolveEmptySubdirectory(
     "linux-headers-" + platformData["target"].GetArch())
    tempPath = storeTemp.GetSubdirectoryPath(
     "linux-headers-" + platformData["target"].GetArch())

    if (GetFilesystemType(tempPath) == "overlay"
     and platformData["host"].GetOs() == "debian"):
        kernelTar = "bsdtar"
    else:
        kernelTar = "tar"

    kernelTarballUrl = GetLastKernelUrl(auth)
    kernelTarballShortFilename = kernelTarballUrl.split("/")[-1]
    kernelExtractedDir = kernelTarballShortFilename[0:-7]

    try:
        with WorkingDir(tempPath):
            RunCommand(["wget", "-P", "./", kernelTarballUrl], verbose)
            RunCommand(
             [kernelTar, "--verbose", "--extract", "--file",
              kernelTarballShortFilename],
             verbose)
        linuxHeadersDir = os.path.join(tempPath, kernelExtractedDir)
        with WorkingDir(linuxHeadersDir):
            RunCommand(
             ["make", "ARCH=" + kernelArch,
              "INSTALL_HDR_PATH=" + installPrefix, "headers_install"],
             verbose)

    except CommandError:
        print("VGAZER: Unable to install",
         "linux-headers-" + platformData["target"].GetArch())
        raise InstallError(
         "linux-headers-" + platformData["target"].GetArch() + " not installed"
        )

    print("VGAZER:", "linux-headers-" + platformData["target"].GetArch(),
     "installed")
