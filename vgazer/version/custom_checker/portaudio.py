import requests
from bs4 import BeautifulSoup

def Check(auth, mirrors):
    response = requests.get("http://www.portaudio.com/download.html")
    html = response.content.decode("utf-8")
    parsedHtml = BeautifulSoup(html, "html.parser")

    links = parsedHtml.find_all("a")

    for link in links:
        if link["href"].find("archives/pa_stable_") != -1:
            strongs = link.findChildren("strong")
            if len(strongs) == 1:
                versionText = strongs[0].text.split("_")[2];
                major = int(versionText[1:3])
                minor = int(versionText[3:5])
                patch = int(versionText[5:7])
                return "%i.%i.%i" % (major, minor, patch)
