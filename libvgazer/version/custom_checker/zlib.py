import requests
from bs4 import BeautifulSoup

def Check(auth, mirrors):
    response = requests.get("http://zlib.net/")
    html = response.content.decode("utf-8")
    parsedHtml = BeautifulSoup(html, "html.parser")

    fonts = parsedHtml.find_all("font")
    for font in fonts:
        if font["size"] == "+2":
            return font.text.split(" ")[2]
