import requests
from bs4 import BeautifulSoup

def CheckAlpine(auth, arch, alpineRelease, repo, package):
    if alpineRelease != "edge":
        alpineRelease = "v" + alpineRelease
    response = requests.get(
     "https://pkgs.alpinelinux.org/package/" + alpineRelease + "/" + repo + "/"
     + arch + "/" + package
    )
    html = response.content.decode("utf-8")
    parsedHtml = BeautifulSoup(html, "html.parser")

    trs = parsedHtml.find_all("tr")
    for tr in trs:
        ths = tr.findChildren("th" , recursive=False)
        if ths[0].text == "Version":
            tds = tr.findChildren("td" , recursive=False)
            return tds[0].text.strip()
