import requests
from bs4 import BeautifulSoup

def Check(auth):
    response = requests.get("https://www.freetype.org/")
    html = response.content.decode("utf-8")
    parsedHtml = BeautifulSoup(html, "html.parser")

    news = parsedHtml.body.find("div", attrs={"id": "news"})
    newsHeaders = news.find_all("h4")

    for newHeader in newsHeaders:
        if newHeader.text.startswith("FreeType"):
            return newHeader.text.split(" ")[1]
