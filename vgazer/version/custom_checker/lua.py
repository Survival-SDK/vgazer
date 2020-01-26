import requests
from bs4 import BeautifulSoup

def Check(auth, mirrors):
    response = requests.get("http://www.lua.org/")
    html = response.content
    parsedHtml = BeautifulSoup(html, "html.parser")

    links = parsedHtml.find_all("a")
    for link in links:
        href = link["href"]
        if href.find("versions.html") != -1:
            return link.text.split(" ")[1]
