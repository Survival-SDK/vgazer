import requests
from bs4 import BeautifulSoup
import vgazer.version.utils as utils

def Check(auth, mirrors):
    response = requests.get(
     "https://developers.google.com/speed/webp/download")
    html = response.content.decode("utf-8")
    parsedHtml = BeautifulSoup(html, "html.parser")

    links = parsedHtml.find_all("a")
    for link in links:
        href = link["href"]
        if (href.find("releases") != -1 and href.find("windows") == -1
         and href.find("linux") == -1 and href.find("mac") == -1
         and href.find("ios") == -1 and href.find("index") == -1):
            return utils.GetVersionFromFilename(link["href"])
