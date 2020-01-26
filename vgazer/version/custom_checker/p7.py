import requests
from bs4 import BeautifulSoup

import vgazer.version.utils as utils

def Check(auth, mirrors):
    response = requests.get("http://baical.net/downloads.html")
    html = response.content.decode("utf-8")
    parsedHtml = BeautifulSoup(html, "html.parser")

    links = parsedHtml.find_all("a")

    for link in links:
        if link["title"] == "P7 library":
            return link.text.split(" ")[-1][1::]
