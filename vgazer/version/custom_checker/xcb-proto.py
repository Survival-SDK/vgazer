import requests
from bs4 import BeautifulSoup

import vgazer.version.utils as utils

def Check(auth):
    response = requests.get("https://xcb.freedesktop.org/dist/")
    html = response.content.decode("utf-8")
    parsedHtml = BeautifulSoup(html, "html.parser")

    links = parsedHtml.find_all("a")

    for link in links:
        if link.text.startswith("xcb-proto"):
            version = utils.GetVersionFromFilename(link.text)

    return version
