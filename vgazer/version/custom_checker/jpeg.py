import requests

def Check(auth, mirrors):
    response = requests.get("http://www.ijg.org/")
    html = response.content.decode("utf-8")
    lines = html.splitlines()
    for line in lines:
        if line.startswith("The current version is release"):
            return line.split(" ")[5]
