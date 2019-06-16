import requests
from bs4 import BeautifulSoup

def Check(auth):
    response = requests.get("https://www.libsdl.org/")
    html = response.content.decode("utf-8")
    parsedHtml = BeautifulSoup(html, "html.parser")

    links = parsedHtml.find_all("a")
    for link in links:
        href = link["href"]
        if href == "download-2.0.php":
            return link.text.split(" ")[2]
