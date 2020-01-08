import requests
from bs4 import BeautifulSoup

def Check(auth):
    response = requests.get("https://wayland.freedesktop.org/releases.html")
    html = response.content.decode("utf-8")
    parsedHtml = BeautifulSoup(html, "html.parser")

    links = parsedHtml.find_all("a")

    maxVersionMajor = -1
    maxVersionMinor = -1
    maxVersionPatch = -1
    for link in links:
        if ("wayland-" in link.text and ".tar.xz" in link.text and "-protocols"
         not in link.text):
            version = link.text.split("-")[1].split(".tar.xz")[0].split(".")
            versionMajor = int(version[0])
            versionMinor = int(version[1])
            versionPatch = int(version[2])

            if versionMajor > maxVersionMajor:
                maxVersionMajor = versionMajor
                maxVersionMinor = versionMinor
                maxVersionPatch = versionPatch
                versionText = link.text.split("-")[1].split(".tar.xz")[0]
            elif (versionMajor == maxVersionMajor
             and versionMinor > maxVersionMinor):
                maxVersionMinor = versionMinor
                maxVersionPatch = versionPatch
                versionText = link.text.split("-")[1].split(".tar.xz")[0]
            elif (versionMajor == maxVersionMajor
             and versionMinor == maxVersionMinor
             and versionPatch > maxVersionPatch):
                maxVersionPatch = versionPatch
                versionText = link.text.split("-")[1].split(".tar.xz")[0]

    return versionText
