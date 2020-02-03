import requests
from bs4 import BeautifulSoup

def CheckOpusCodec(auth, project):
    response = requests.get("https://opus-codec.org/news/")
    html = response.content
    parsedHtml = BeautifulSoup(html, "html.parser")

    links = parsedHtml.find_all("a")
    for link in links:
        if project + " " in link.text:
            return link.text.split(" ")[1]
