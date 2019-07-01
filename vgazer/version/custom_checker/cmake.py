import requests
from bs4 import BeautifulSoup

def Check(auth):
    response = requests.get("https://cmake.org/download/")
    html = response.content.decode("utf-8")
    parsedHtml = BeautifulSoup(html, "html.parser")

    headers3 = parsedHtml.find_all("h3")
    for header in headers3:
        if header.text.find("Latest Release") != -1:
            return header.text.split("(")[1][:-1:]
