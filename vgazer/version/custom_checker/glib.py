import requests
from bs4 import BeautifulSoup

def Check(auth, mirrors):
    response = requests.get("https://developer.gnome.org/glib/")
    html = response.content.decode("utf-8")
    parsedHtml = BeautifulSoup(html, "html.parser")

    versions = parsedHtml.body.find("ul", attrs={"class": "versions"})
    links = versions.find_all("a")
    for link in links:
        if link.parent.name == "strong":
            return link.text
