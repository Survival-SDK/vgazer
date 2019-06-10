import requests
from bs4 import BeautifulSoup

def Check(auth):
    response = requests.get("https://ftp.gnu.org/pub/gnu/libiconv/")
    html = response.content.decode("utf-8")
    parsedHtml = BeautifulSoup(html, "html.parser")

    table = parsedHtml.table
    rows = table.findChildren("tr")
    lastVersionRow = rows[-3]
    link = lastVersionRow.findChildren("a")

    version = link[0].text.split("-")[1].split(".tar.gz")[0]

    return version
