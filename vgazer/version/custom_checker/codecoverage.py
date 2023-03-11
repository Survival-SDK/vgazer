import re
import requests

def Check(auth, mirrors):
    response = requests.get(
     "https://raw.githubusercontent.com/bilke/cmake-modules/master/CodeCoverage.cmake"
    )

    source = response.content.decode("utf-8")

    result = re.findall("\d{4}-\d{2}-\d{2}", source)

    return result[-1]
