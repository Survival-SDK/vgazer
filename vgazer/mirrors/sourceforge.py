import requests
from bs4 import BeautifulSoup

from vgazer.mirrors.base import MirrorsBase

fallbackMirrorsList = {
    "http": [
        "http://downloads.sourceforge.net",
        "http://astuteinternet.dl.sourceforge.net",
        "http://ayera.dl.sourceforge.net",
        "http://cfhcable.dl.sourceforge.net",
        "http://freefr.dl.sourceforge.net",
        "http://gigenet.dl.sourceforge.net",
        "http://iweb.dl.sourceforge.net",
        "http://jaist.dl.sourceforge.net",
        "http://liquidtelecom.dl.sourceforge.net",
        "http://managedway.dl.sourceforge.net",
        "http://nchc.dl.sourceforge.net",
        "http://netcologne.dl.sourceforge.net",
        "http://netix.dl.sourceforge.net",
        "http://newcontinuum.dl.sourceforge.net",
        "http://phoenixnap.dl.sourceforge.net",
        "http://pilotfiber.dl.sourceforge.net",
        "http://razaoinfo.dl.sourceforge.net",
        "http://svwh.dl.sourceforge.net",
        "http://tenet.dl.sourceforge.net",
        "http://ufpr.dl.sourceforge.net",
        "http://versaweb.dl.sourceforge.net",
    ],
    "https": [
        "https://downloads.sourceforge.net",
        "https://astuteinternet.dl.sourceforge.net",
        "https://ayera.dl.sourceforge.net",
        "https://cfhcable.dl.sourceforge.net",
        "https://freefr.dl.sourceforge.net",
        "https://gigenet.dl.sourceforge.net",
        "https://iweb.dl.sourceforge.net",
        "https://jaist.dl.sourceforge.net",
        "https://liquidtelecom.dl.sourceforge.net",
        "https://managedway.dl.sourceforge.net",
        "https://nchc.dl.sourceforge.net",
        "https://netcologne.dl.sourceforge.net",
        "https://netix.dl.sourceforge.net",
        "https://newcontinuum.dl.sourceforge.net",
        "https://phoenixnap.dl.sourceforge.net",
        "https://pilotfiber.dl.sourceforge.net",
        "https://razaoinfo.dl.sourceforge.net",
        "https://svwh.dl.sourceforge.net",
        "https://tenet.dl.sourceforge.net",
        "https://ufpr.dl.sourceforge.net",
        "https://versaweb.dl.sourceforge.net",
    ],
    "ftp": [
    ],
    "rsync": [
    ],
}

def GetMirrorsList(noFallback=False):
    print("VGAZER: Retrieving mirrors list for downloads.sourceforge.net...")

    mirrorsList = {
        "http": [
            "http://downloads.sourceforge.net",
        ],
        "https": [
            "https://downloads.sourceforge.net",
        ],
        "ftp": [
        ],
        "rsync": [
        ],
    }
    try:
        response = requests.get(
         "https://sourceforge.net/p/forge/documentation/Mirrors/")
    except requests.exceptions.ConnectionError:
        if noFallback:
            print("VGAZER: Unable to retrieve mirrors list")
            return None
        else:
            print(
             "VGAZER: Unable to retrieve mirrors list. Using fallback mirrors "
             "list"
            )
            return fallbackMirrorsList
    html = response.content.decode("utf-8")
    parsedHtml = BeautifulSoup(html, "html.parser")

    rows = parsedHtml.find_all("tr")
    for row in rows:
        cells = row.findChildren("td", recursive=False)
        if len(cells) < 4:
            continue

        mirrorsList["http"].append(
         "http://" + cells[1].text + ".dl.sourceforge.net")
        mirrorsList["https"].append(
         "https://" + cells[1].text + ".dl.sourceforge.net")

    return mirrorsList

class MirrorsSourceforge(MirrorsBase):
    def __init__(self):
        super().__init__("downloads.sourceforge.net", GetMirrorsList)
