import requests
from bs4 import BeautifulSoup

def Check(auth, mirrors):
    response = requests.get("https://www.x.org/releases/individual/proto/")
    html = response.content.decode("utf-8")
    parsedHtml = BeautifulSoup(html, "html.parser")

    links = parsedHtml.find_all("a")

    maxVersionMajor = -1
    maxVersionMinor = -1
    maxVersionPatch = -1
    maxVersionSubpatch = -1
    for link in links:
        if ("randrproto-" in link.text and ".tar.gz" in link.text
         and ".sig" not in link.text):
            version = link.text.split("-")[1].split(".tar.gz")[0].split(".")
            versionMajor = int(version[0])
            versionMinor = int(version[1])
            versionPatch = int(version[2])
            if len(version) == 3:
                versionSubpatch = 0
            else:
                versionSubpatch = int(version[3])

            if versionMajor > maxVersionMajor:
                maxVersionMajor = versionMajor
                maxVersionMinor = versionMinor
                maxVersionPatch = versionPatch
                maxVersionSubpatch = versionSubpatch
                maxVersionText = link.text.split("-")[1].split(".tar.gz")[0]
            elif (versionMajor == maxVersionMajor
             and versionMinor > maxVersionMinor):
                maxVersionMinor = versionMinor
                maxVersionPatch = versionPatch
                maxVersionSubpatch = versionSubpatch
                maxVersionText = link.text.split("-")[1].split(".tar.gz")[0]
            elif (versionMajor == maxVersionMajor
             and versionMinor == maxVersionMinor
             and versionPatch > maxVersionPatch):
                maxVersionPatch = versionPatch
                maxVersionSubpatch = versionSubpatch
                maxVersionText = link.text.split("-")[1].split(".tar.gz")[0]
            elif (versionMajor == maxVersionMajor
             and versionMinor == maxVersionMinor
             and versionPatch > maxVersionPatch
             and versionSubpatch > maxVersionSubpatch):
                maxVersionSubpatch = versionSubpatch
                maxVersionText = link.text.split("-")[1].split(".tar.gz")[0]

    return maxVersionText
