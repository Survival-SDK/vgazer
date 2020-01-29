import requests
from bs4 import BeautifulSoup

def Check(auth, mirrors):
    response = requests.get("https://mesa.freedesktop.org/archive/")
    html = response.content.decode("utf-8")
    parsedHtml = BeautifulSoup(html, "html.parser")

    links = parsedHtml.find_all("a")

    maxVersionMajor = -1
    maxVersionMinor = -1
    maxVersionPatch = -1
    maxVersionRc = -1
    for link in links:
        if ("mesa-" in link.text and ".tar.xz" in link.text
         and ".sig" not in link.text):
            if "rc" in link.text:
                version = link.text.split("-")[1].split(".")
                versionMajor = int(version[0])
                versionMinor = int(version[1])
                try:
                    versionPatch = int(version[2])
                except IndexError:
                    versionPatch = int(link.text.split("-")[2])
                versionRc = int(link.text.split("rc")[1][0])
            else:
                version = link.text.split("-")[1].split(".tar.xz")[0].split(
                 ".")
                versionMajor = int(version[0])
                versionMinor = int(version[1])
                versionPatch = int(version[2])
                versionRc = 0

            if versionMajor > maxVersionMajor:
                maxVersionMajor = versionMajor
                maxVersionMinor = versionMinor
                maxVersionPatch = versionPatch
                maxVersionRc = versionRc
                versionText = link.text.split("-")[1].split(".tar.xz")[0]
            elif (versionMajor == maxVersionMajor
             and versionMinor > maxVersionMinor):
                maxVersionMinor = versionMinor
                maxVersionPatch = versionPatch
                maxVersionRc = versionRc
                versionText = link.text.split("-")[1].split(".tar.xz")[0]
            elif (versionMajor == maxVersionMajor
             and versionMinor == maxVersionMinor
             and versionPatch > maxVersionPatch):
                maxVersionPatch = versionPatch
                maxVersionRc = versionRc
                versionText = link.text.split("-")[1].split(".tar.xz")[0]
            elif (versionMajor == maxVersionMajor
             and versionMinor == maxVersionMinor
             and versionPatch == maxVersionPatch
             and (
              versionRc != 0 and maxVersionRc != 0 and versionRc > maxVersionRc
               or versionRc == 0 and maxVersionRc != 0
             )
            ):
                maxVersionRc = versionRc
                versionText = link.text.split("-")[1].split(".tar.xz")[0]

    return versionText
