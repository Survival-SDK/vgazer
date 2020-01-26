import requests
from bs4 import BeautifulSoup
import vgazer.version.utils as utils

def GetMinorVersionLink(auth):
    response = requests.get("https://cmocka.org/files/")
    html = response.content.decode("utf-8")
    parsedHtml = BeautifulSoup(html, "html.parser")

    links = parsedHtml.find_all("a")

    lastVersionMajor = 0
    lastVersionMinor = 0

    for link in links:
        if (link["href"][-1] == "/" and link["href"] != "/"):
            linkVersionMajor = int(link.text.split(".")[0])
            linkVersionMinor = int(link.text.split(".")[1][:-1:])
            if linkVersionMinor > lastVersionMinor:
                lastVersionMinor = linkVersionMinor
                lastVersionLinkText = link["href"]
            if linkVersionMajor > lastVersionMajor:
                lastVersionMajor = linkVersionMajor
                lastVersionMinor = linkVersionMinor
                lastVersionLinkText = link["href"]
    return "https://cmocka.org/files/" + lastVersionLinkText

def Check(auth, mirrors):
    minorVersionLink = GetMinorVersionLink(auth)

    response = requests.get(minorVersionLink)
    html = response.content.decode("utf-8")
    parsedHtml = BeautifulSoup(html, "html.parser")

    links = parsedHtml.find_all("a")

    return utils.GetVersionFromFilename(links[-2]["href"])
