import requests
from bs4 import BeautifulSoup

def Check(auth, mirrors):
    response = requests.get("https://ftp.gnu.org/gnu/wget/")
    html = response.content.decode("utf-8")
    parsedHtml = BeautifulSoup(html, "html.parser")

    table = parsedHtml.table
    rows = table.findChildren("tr")
    lastVersionRow = rows[-8]
    link = lastVersionRow.findChildren("a")

    version = link[0].text.split("-")[1].split(".tar.gz")[0]

    return version
