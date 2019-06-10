import requests
import vgazer.version.utils as utils

def Check(auth):
    response = requests.get(
     "https://raw.githubusercontent.com/nothings/stb/master/README.md"
    )
    readme = response.content.decode("utf-8")

    lines = readme.splitlines()
    for line in lines:
        if line.startswith("**[stb_rect_pack.h](stb_rect_pack.h)**"):
            return line.split("|")[1].split(" ")[1]
