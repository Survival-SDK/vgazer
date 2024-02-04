import requests
from bs4 import BeautifulSoup

def CheckXiph(auth, project):
    response = requests.get("https://www.xiph.org/downloads/")
    html = response.content.decode("utf-8")
    parsedHtml = BeautifulSoup(html, "html.parser")

    tables = parsedHtml.find_all("table")

    rows = tables[1].findChildren("tr")
    for row in rows[1:]:
        cells = row.findChildren("td")
        if cells[0].text == project:
            return cells[1].text
