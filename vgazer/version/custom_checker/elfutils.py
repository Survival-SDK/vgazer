import requests
from bs4 import BeautifulSoup

def Check(auth):
    response = requests.get("https://sourceware.org/elfutils/ftp/")
    html = response.content.decode("utf-8")
    parsedHtml = BeautifulSoup(html, "html.parser")

    links = parsedHtml.find_all("a")

    maxVersionMajor = -1
    maxVersionMinor = -1
    for link in links:
        if ("." in link.text and "/" in link.text):
            version = link.text.split("/")[0].split(".")
            versionMajor = int(version[0])
            versionMinor = int(version[1])

            if versionMajor > maxVersionMajor:
                maxVersionMajor = versionMajor
                maxVersionMinor = versionMinor
                versionText = link.text.split("/")[0]
            elif (versionMajor == maxVersionMajor
             and versionMinor > maxVersionMinor):
                maxVersionMinor = versionMinor
                versionText = link.text.split("/")[0]

    return versionText
