import json
import urllib.request

def CheckPyPi(package):
    with urllib.request.urlopen(f"https://pypi.org/pypi/{package}/json") as resp:
        data = json.load(resp)

    return data["info"]["version"]
