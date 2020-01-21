import requests
from bs4 import BeautifulSoup

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
    elif (versionInfo["versionMajor"] == versionInfo["maxVersionMajor"]
     and versionInfo["versionMinor"] > versionInfo["maxVersionMinor"]):
        versionInfo["maxVersionMinor"] = versionInfo["versionMinor"]
        versionInfo["maxVersionPatch"] = versionInfo["versionPatch"]
    elif (versionInfo["versionMajor"] == versionInfo["maxVersionMajor"]
     and versionInfo["versionMinor"] == versionInfo["maxVersionMinor"]
     and versionInfo["versionPatch"] > versionInfo["maxVersionPatch"]):
        versionInfo["maxVersionPatch"] = versionInfo["versionPatch"]

def GetLastKernelVersionInSubdir(majorVersion):
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

    return "{versionMajor}.{versionMinor}.{versionPatch}".format(
     versionMajor=versionInfo["maxVersionMajor"],
     versionMinor=versionInfo["maxVersionMinor"],
     versionPatch=versionInfo["maxVersionPatch"])

def CheckLinuxHeaders(auth):
    response = requests.get("https://www.kernel.org/pub/linux/kernel/")
    html = response.content.decode("utf-8")
    parsedHtml = BeautifulSoup(html, "html.parser")

    links = parsedHtml.find_all("a")

    maxVersionMajor = -1
    for link in links:
        if "v" in link.text and "." in link.text:
            versionMajor = int(link.text[1:-1].split(".")[0])
            if versionMajor > maxVersionMajor:
                maxVersionMajor = versionMajor

    version = GetLastKernelVersionInSubdir(maxVersionMajor)
    if version is None:
        return GetLastKernelVersionInSubdir(maxVersionMajor - 1)
    else:
        return version
