import requests
from bs4 import BeautifulSoup
import vgazer.version.utils as utils

def CheckSdl2Addon(auth, project):
    projectSuburl = project.replace("SDL2", "SDL") + "/"
    response = requests.get("https://www.libsdl.org/projects/" + projectSuburl)
    html = response.content
    parsedHtml = BeautifulSoup(html, "html.parser")

    links = parsedHtml.find_all("a")
    for link in links:
        if (link.text.find(".tar.gz") != -1 and link.text.find("devel") == -1):
            return utils.GetVersionFromFilename(link["href"])
