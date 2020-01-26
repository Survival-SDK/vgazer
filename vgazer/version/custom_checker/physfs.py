import requests
from bs4 import BeautifulSoup

from vgazer.exceptions import VersionCheckError

def Check(auth, mirrors):
    try:
        response = requests.get(
         "https://icculus.org/physfs/downloads/LATEST_VERSION.html")
    except requests.exceptions.ConnectionError:
        raise VersionCheckError("Version of physfs is not checked")
    html = response.content.decode("utf-8")
    parsedHtml = BeautifulSoup(html, "html.parser")

    return parsedHtml.find_all("a")[0].text
