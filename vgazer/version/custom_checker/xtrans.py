import requests
from bs4 import BeautifulSoup

def Check(auth):
    response = requests.get("https://www.x.org/releases/individual/lib/")
    html = response.content.decode("utf-8")
    parsedHtml = BeautifulSoup(html, "html.parser")

    links = parsedHtml.find_all("a")

    maxVersionMajor = -1
    maxVersionMinor = -1
    maxVersionPatch = -1
    for link in links:
        if ("xtrans-" in link.text and ".tar.gz" in link.text
         and ".sig" not in link.text):
            version = link.text.split("-")[1].split(".tar.gz")[0].split(".")
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
                versionText = link.text.split("-")[1].split(".tar.gz")[0]
            elif (versionMajor == maxVersionMajor
             and versionMinor > maxVersionMinor):
                maxVersionMinor = versionMinor
                maxVersionPatch = versionPatch
                versionText = link.text.split("-")[1].split(".tar.gz")[0]
            elif (versionMajor == maxVersionMajor
             and versionMinor == maxVersionMinor
             and versionPatch > maxVersionPatch):
                maxVersionPatch = versionPatch
                versionText = link.text.split("-")[1].split(".tar.gz")[0]

    return versionText
