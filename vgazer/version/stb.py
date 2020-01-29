import requests

def CheckStb(auth, library):
    response = requests.get(
     "https://raw.githubusercontent.com/nothings/stb/master/README.md"
    )
    readme = response.content.decode("utf-8")

    lines = readme.splitlines()
    for line in lines:
        if line.startswith("**[" + library + ".h](" + library + ".h)**"):
            return line.split("|")[1].split(" ")[1]
