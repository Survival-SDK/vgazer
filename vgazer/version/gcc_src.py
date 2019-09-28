import requests
from bs4 import BeautifulSoup

def CheckGccSrc(auth):
    response = requests.get("https://ftp.gnu.org/gnu/gcc/")
    html = response.content.decode("utf-8")
    parsedHtml = BeautifulSoup(html, "html.parser")

    links = parsedHtml.find_all("a")

    maxVersionMajor = -1
    maxVersionMinor = -1
    maxVersionPatch = -1
    for link in links:
        if ("gcc" in link.text and "/" in link.text):
            version = link.text.split("-")[1].split("/")[0].split(".")
            versionMajor = int(version[0])
            versionMinor = int(version[1])
            if len(version) == 2:
                versionPatch = 0
            else:
                versionPatch = int(version[2])

            if versionMajor > maxVersionMajor:
                maxVersionMajor = versionMajor
                maxVersionMinor = versionMinor
                maxVersionPatch = versionPatch
            elif (versionMajor == maxVersionMajor
             and versionMinor > maxVersionMinor):
                maxVersionMinor = versionMinor
                maxVersionPatch = versionPatch
            elif (versionMajor == maxVersionMajor
             and versionMinor == maxVersionMinor
             and versionPatch > maxVersionPatch):
                maxVersionPatch = versionPatch

    return str(maxVersionMajor) + "." + str(maxVersionMinor) + "." + str(maxVersionPatch)
