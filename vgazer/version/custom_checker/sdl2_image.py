import requests
from bs4 import BeautifulSoup
import vgazer.version.utils as utils

def Check(auth):
    response = requests.get("https://www.libsdl.org/projects/SDL_image/")
    html = response.content
    parsedHtml = BeautifulSoup(html, "html.parser")

    links = parsedHtml.find_all("a")
    for link in links:
        if (link.text.find(".tar.gz") != -1 and link.text.find("devel") == -1):
            return utils.GetVersionFromFilename(link["href"])
