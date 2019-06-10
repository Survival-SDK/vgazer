import requests
from bs4 import BeautifulSoup

def Check(auth):
    response = requests.get("https://www.gnu.org/software/gettext/")
    html = response.content.decode("utf-8")
    parsedHtml = BeautifulSoup(html, "html.parser")

    paragraphs = parsedHtml.find_all("p")

    for paragraph in paragraphs:
        if paragraph.text.startswith("\nThe latest release is"):
            lines = paragraph.text.splitlines()
            return lines[1].split(" ")[4][:-1]
