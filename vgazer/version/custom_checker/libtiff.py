import requests
from bs4 import BeautifulSoup
import vgazer.version.utils as utils

def Check(auth):
    response = requests.get("http://libtiff.maptools.org/")
    html = response.content.decode("utf-8")
    parsedHtml = BeautifulSoup(html, "html.parser")

    table = parsedHtml.table
    link = table.findChildren("a")[3]

    return utils.GetVersionFromTag(link.text)
