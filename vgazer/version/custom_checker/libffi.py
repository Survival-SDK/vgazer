import requests
from bs4 import BeautifulSoup

def Check(auth, mirrors):
    response = requests.get("https://sourceware.org/libffi/")
    html = response.content.decode("utf-8")
    parsedHtml = BeautifulSoup(html, "html.parser")

    return parsedHtml.b.text.split("-")[1]
