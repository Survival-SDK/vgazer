import requests

import libvgazer.version.utils as utils

def Check(auth, mirrors):
    response = requests.get(
     "https://raw.githubusercontent.com/mackron/dr_libs/master/dr_wav.h"
    )
    source = response.content.decode("utf-8")

    lines = source.splitlines()

    return utils.GetVersionFromTag(lines[2].split(" ")[2])
