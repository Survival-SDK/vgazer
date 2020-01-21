import requests
import vgazer.version.utils as utils

def Check(auth):
    response = requests.get(
     "https://raw.githubusercontent.com/criptych/physfs/master/src/physfs.h"
    )
    source = response.content.decode("utf-8")

    lines = source.splitlines()

    for line in lines:
        if "#define PHYSFS_VER_MAJOR" in line:
            versionMajor = line.split(" ")[2]
        if "#define PHYSFS_VER_MINOR" in line:
            versionMinor = line.split(" ")[2]
        if "#define PHYSFS_VER_PATCH" in line:
            versionPatch = line.split(" ")[2]

    return versionMajor + "." + versionMinor + "." + versionPatch
