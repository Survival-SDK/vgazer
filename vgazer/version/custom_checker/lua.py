import requests
from bs4 import BeautifulSoup

from vgazer.version.utils import GetVersionFromFilename

def Check(auth, mirrors):
    response = requests.get("http://www.lua.org/download.html")
    html = response.content
    parsedHtml = BeautifulSoup(html, "html.parser")

    links = parsedHtml.find_all("a")
    for link in links:
        if "ftp/lua-" in link["href"]:
            return GetVersionFromFilename(link["href"])
