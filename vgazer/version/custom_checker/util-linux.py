import requests
from bs4 import BeautifulSoup

def GetPubSubdir():
    response = requests.get(
     "https://mirrors.edge.kernel.org/pub/linux/utils/util-linux/")
    html = response.content.decode("utf-8")
    parsedHtml = BeautifulSoup(html, "html.parser")

    links = parsedHtml.find_all("a")

    return ("https://mirrors.edge.kernel.org/pub/linux/utils/util-linux/"
     + links[-1]["href"] + "/")

def Check(auth):
    response = requests.get(GetPubSubdir())
    html = response.content.decode("utf-8")
    parsedHtml = BeautifulSoup(html, "html.parser")

    links = parsedHtml.find_all("a")

    maxVersionRc = -1
    for link in links:
        if ("util-linux-" in link.text and ".tar.gz" in link.text):
            versionMajor = int(link.text.split("-")[2].split(".")[0])
            versionMinor = int(link.text.split("-")[2].split(".")[1])
            if len(link.text.split("-")) == 3:
                return str(versionMajor) + "." + str(versionMinor)

            versionRc = int(
             link.text.split("-")[3].split(".")[0].split("rc")[1])

            if versionRc > maxVersionRc:
                maxVersionRc = versionRc

    return (
     str(versionMajor) + "." + str(versionMinor) + "-rc" + str(maxVersionRc))
