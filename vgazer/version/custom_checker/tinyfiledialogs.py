import requests

def Check(auth):
    description = requests.get(
     "https://sourceforge.net/rest/p/tinyfiledialogs"
    ).json()["short_description"]
    return description.split("\r\n")[0].split("v")[1]
