import requests
from bs4 import BeautifulSoup

from vgazer.version.utils import GetVersionFromFilename

def Check(auth, mirrors):
    response = requests.get("http://luajit.org/download.html")
    html = response.content
    parsedHtml = BeautifulSoup(html, "html.parser")

    links = parsedHtml.find_all("a")
    for link in links:
        if "download/LuaJIT-" in link["href"]:
            return GetVersionFromFilename(link["href"])
