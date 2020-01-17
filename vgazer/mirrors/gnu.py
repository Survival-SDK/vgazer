import requests
from bs4 import BeautifulSoup

from vgazer.exceptions      import UnknownProtocol
from vgazer.mirrors.base    import MirrorsBase

fallbackMirrorsList = {
    "http": [
        "http://ftpmirror.gnu.org",
        "http://ftp.gnu.org/gnu",
        "http://mirrors.kernel.org/gnu",
        "http://ftp.club.cc.cmu.edu/pub/gnu",
        "http://ftp.azc.uam.mx/mirrors/gnu",
        "http://ftp.belnet.be/mirror/ftp.gnu.org/gnu",
        "http://mirrors.sunsite.dk/gnu",
        "http://ftp-stud.fht-esslingen.de/pub/Mirrors/ftp.gnu.org",
        "http://ftp.heanet.ie/mirrors/ftp.gnu.org/gnu",
        "http://rm.mirror.garr.it/mirrors/gnuftp",
    ],
    "https": [
        "https://ftpmirror.gnu.org",
        "https://ftp.gnu.org/gnu",
        "https://mirrors.kernel.org/gnu",
        "https://ftp.belnet.be/mirror/ftp.gnu.org/gnu",
        "https://mirrors.sunsite.dk/gnu",
        "https://ftp.heanet.ie/mirrors/ftp.gnu.org/gnu",
        "https://rm.mirror.garr.it/mirrors/gnuftp",
    ],
    "ftp": [
        "ftp://ftp.gnu.org/gnu",
        "ftp://mirrors.kernel.org/gnu",
        "ftp://ftp.keystealth.org/pub/gnu",
        "ftp://ftp.cise.ufl.edu/pub/mirrors/GNU/gnu",
        "ftp://ftp.cse.ohio-state.edu/mirror/gnu",
        "ftp://ftp.club.cc.cmu.edu/gnu",
        "ftp://ftp.sun.ac.za/pub/mirrorsites/ftp.gnu.org",
        "ftp://ftp.unicamp.br/pub/gnu",
        "ftp://core.ring.gr.jp/pub/GNU",
        "ftp://ftp.belnet.be/mirror/ftp.gnu.org/gnu",
        "ftp://ftp.fi.muni.cz/pub/gnu/gnu",
        "ftp://ftp.funet.fi/pub/gnu/prep",
        "ftp://ftp-stud.fht-esslingen.de/pub/Mirrors/ftp.gnu.org",
        "ftp://ftp.ntua.gr/pub/gnu",
        "ftp://ftp.nluug.nl/pub/gnu",
        "ftp://ftp.mirror.nl/pub/mirror/gnu",
        "ftp://ftp.task.gda.pl/pub/gnu",
        "ftp://sunsite.icm.edu.pl/pub/gnu",
        "ftp://ftp.man.poznan.pl/pub/gnu",
        "ftp://ftp.arnes.si/software/gnu",
        "ftp://ftp.gnu.org.ua/gnu",
    ],
    "rsync": [
    ],
}

def GetMirrorsList(noFallback = False):
    print("VGAZER: Retrieving mirrors list for ftp.gnu.org...")

    mirrorsList = {
        "http": [
            "http://ftpmirror.gnu.org",
            "http://ftp.gnu.org/gnu",
        ],
        "https": [
            "https://ftpmirror.gnu.org",
            "https://ftp.gnu.org/gnu",
        ],
        "ftp": [
            "ftp://ftp.gnu.org/gnu",
        ],
        "rsync": [
        ],
    }
    try:
        response = requests.get(
         "http://download.savannah.gnu.org/mirmon/allgnu/")
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
        cells = row.findChildren("td" , recursive=False)
        if len(cells) < 2:
            continue
        if cells[1].text not in ["http", "https", "ftp", "rsync"]:
            continue
        protocol = cells[1].text
        if protocol in ["http", "https", "ftp"]:
            links = cells[0].findChildren("a" , recursive=False)
            mirrorUrl = links[0]["href"][:-1]
        elif protocol == "rsync":
            mirrorUrl = "rsync://" + cells[0].text.split("\xa0\xa0")[0]
        else:
            raise UnknownProtocol(
             "VGAZER: Found mirror's url with unknown protocol: " + protocol)
        mirrorsList[protocol].append(mirrorUrl)

    return mirrorsList

class MirrorsGnu(MirrorsBase):
    def __init__(self):
        super().__init__("ftp.gnu.org", GetMirrorsList)
