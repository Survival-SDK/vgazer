import requests
from bs4 import BeautifulSoup

from vgazer.version.utils import GetVersionFromTag

def Check(auth, mirrors):
    response = requests.get("http://xmlsoft.org/news.html")
    html = response.content.decode("utf-8")
    parsedHtml = BeautifulSoup(html, "html.parser")

    return GetVersionFromTag(parsedHtml.h3.text.split(":")[0])
