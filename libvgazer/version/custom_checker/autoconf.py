import requests
from bs4 import BeautifulSoup

def Check():
    response = requests.get("https://ftp.gnu.org/gnu/autoconf/")
    html = response.content.decode("utf-8")
    parsedHtml = BeautifulSoup(html, "html.parser")

    links = parsedHtml.find_all("a")

    maxMajor = -1
    maxMinor = -1
    for link in links:
        if ("autoconf" in link.text and ".tar.gz" in link.text
         and ".sig" not in link.text and "-latest" not in link.text):
            version = link.text.split("-")[1].split(".tar.gz")[0]
            splitedVersion = version.split(".")
            if int(splitedVersion[0]) > maxMajor:
                maxMajor = int(splitedVersion[0])
                maxMinor = int(splitedVersion[1])
            elif (int(splitedVersion[0]) == maxMajor
             and int(splitedVersion[1]) > maxMinor):
                maxMinor = int(splitedVersion[1])

    return "{major}.{minor}".format(major=maxMajor, minor=maxMinor)
