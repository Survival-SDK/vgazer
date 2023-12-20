import requests
from bs4 import BeautifulSoup

def Check(auth, mirrors):
    response = requests.get("https://ftp.gnu.org/gnu/automake/")
    html = response.content.decode("utf-8")
    parsedHtml = BeautifulSoup(html, "html.parser")

    links = parsedHtml.find_all("a")

    maxMajor = -1
    maxMinor = -1
    maxPatch = 0
    for link in links:
        if ("automake" in link.text and ".tar.gz" in link.text
         and ".sig" not in link.text):
            version = link.text.split("-")[1].split(".tar.gz")[0]
            splitedVersion = version.split(".")
            if len(splitedVersion) == 2:
                patch = 0
            else:
                patch = splitedVersion[2]
            if int(splitedVersion[0]) > maxMajor:
                maxMajor = int(splitedVersion[0])
                maxMinor = int(splitedVersion[1])
                maxPatch = int(patch)
            elif (int(splitedVersion[0]) == maxMajor
             and int(splitedVersion[1]) > maxMinor):
                maxMinor = int(splitedVersion[1])
                maxPatch = int(patch)
            elif (int(splitedVersion[0]) == maxMajor
             and int(splitedVersion[1]) == maxMinor
             and int(patch) > maxPatch):
                maxPatch = int(patch)

    return "{major}.{minor}.{patch}".format(major=maxMajor, minor=maxMinor,
     patch=maxPatch)
