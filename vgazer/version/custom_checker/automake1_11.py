import requests
from bs4 import BeautifulSoup

def Check(auth, mirrors):
    response = requests.get("https://ftp.gnu.org/gnu/automake/")
    html = response.content.decode("utf-8")
    parsedHtml = BeautifulSoup(html, "html.parser")

    links = parsedHtml.find_all("a")

    maxVersion = "-1"
    for link in links:
        if ("automake-1.11" in link.text and ".tar.gz" in link.text
         and ".sig" not in link.text):
            version = link.text.split("-")[1].split(".tar.gz")[0]
            splitedVersion = version.split(".")
            if len(splitedVersion) == 2:
                patchVersion = 0
            else:
                patchVersion = splitedVersion[2]
            if int(patchVersion) > int(maxVersion):
                maxVersion = patchVersion

    if maxVersion == 0:
        return "1.11"
    else:
        return "1.11." + maxVersion
