import requests
from bs4 import BeautifulSoup

def Check(auth, mirrors):
    response = requests.get("https://alsa-project.org/wiki/Main_Page")
    html = response.content.decode("utf-8")
    parsedHtml = BeautifulSoup(html, "html.parser")

    links = parsedHtml.find_all("a")
    for link in links:
        if "alsa-lib" in link.text:
            return link.text.split("-")[2]
