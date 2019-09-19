import requests
from bs4 import BeautifulSoup

def Check(auth):
    response = requests.get(
     "https://icculus.org/physfs/downloads/LATEST_VERSION.html")
    html = response.content.decode("utf-8")
    parsedHtml = BeautifulSoup(html, "html.parser")

    return parsedHtml.find_all("a")[0].text
