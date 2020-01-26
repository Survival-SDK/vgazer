import requests
from bs4 import BeautifulSoup

def Check(auth, mirrors):
    response = requests.get("http://site.icu-project.org/download")
    html = response.content.decode("utf-8")
    parsedHtml = BeautifulSoup(html, "html.parser")

    tbodies = parsedHtml.body.find_all("tbody")
    tbodiesVersions = tbodies[1]
    rows = tbodiesVersions.findChildren("tr" , recursive=False)
    cells = rows[1].findChildren("td" , recursive=False)
    links = cells[1].findChildren("a")

    return links[0].text
