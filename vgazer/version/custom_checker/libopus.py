import requests
from bs4 import BeautifulSoup
import vgazer.version.utils as utils

def Check(auth, mirrors):
    response = requests.get("https://opus-codec.org/news/")
    html = response.content
    parsedHtml = BeautifulSoup(html, "html.parser")

    links = parsedHtml.find_all("a")
    for link in links:
        if "libopus " in link.text:
            return link.text.split(" ")[1]
