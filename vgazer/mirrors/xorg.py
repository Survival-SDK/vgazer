import requests
from bs4 import BeautifulSoup

from vgazer.exceptions      import UnknownProtocol
from vgazer.mirrors.base    import MirrorsBase

fallbackMirrorsList = {
    "http": [
        "http://xorg.freedesktop.org/releases/",
        "http://www.x.org/pub/",
        "http://mirror.csclub.uwaterloo.ca/x.org/",
        "http://xorg.mirrors.pair.com/",
        "http://mirrors.ircam.fr/pub/x.org/",
        "http://www.mirrorservice.org/sites/ftp.x.org/pub/",
        "http://ftp.yz.yamagata-u.ac.jp/pub/X11/x.org/",
    ],
    "https": [
        "https://www.x.org/releases",
    ],
    "ftp": [
        "ftp://ftp.freedesktop.org/pub/xorg/",
        "ftp://ftp.x.org/pub/",
        "ftp://mirror.csclub.uwaterloo.ca/x.org/",
        "ftp://xorg.mirrors.pair.com/",
        "ftp://ftp.fu-berlin.de/unix/X11/FTP.X.ORG/",
        "ftp://ftp.gwdg.de/pub/x11/x.org/",
        "ftp://ftp.mirrorservice.org/sites/ftp.x.org/pub/",
        "ftp://ftp.yz.yamagata-u.ac.jp/pub/X11/x.org/",
    ],
    "rsync": [
    ],
}

def GetMirrorsList(noFallback = False):
    print("VGAZER: Retrieving mirrors list for www.x.org/releases...")

    mirrorsList = {
        "http": [
            "http://xorg.freedesktop.org/releases/",
            "http://www.x.org/pub/",
        ],
        "https": [
            "https://www.x.org/releases",
        ],
        "ftp": [
            "ftp://ftp.freedesktop.org/pub/xorg/",
            "ftp://ftp.x.org/pub/",
        ],
        "rsync": [
        ],
    }
    try:
        response = requests.get(
         "https://www.x.org/wiki/Releases/Download/")
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

    listItems = parsedHtml.find_all("li")

    for listItem in listItems:
        if listItem.a is not None:
            if listItem.a.text in [
             "Edit", "Page History", "Repo Info", "HTTP", "FTP", "Releases"
            ]:
                continue
            protocol = listItem.a.text.split(":")[0]
            url = listItem.a.text
        else:
            if "no known active mirror." in listItem.text:
                continue
            protocol = listItem.text.split(":")[0]
            url = listItem.text
        if protocol not in ["http", "https", "ftp", "rsync"]:
            raise UnknownProtocol(
             "VGAZER: Found mirror's url with unknown protocol: " + protocol)
        mirrorsList[protocol].append(url)

    return mirrorsList

class MirrorsXorg(MirrorsBase):
    def __init__(self):
        super().__init__("www.x.org", GetMirrorsList)
