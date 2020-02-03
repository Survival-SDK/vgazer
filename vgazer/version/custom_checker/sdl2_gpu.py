import requests

def Check(auth, mirrors):
    response = requests.get(
     "https://raw.githubusercontent.com/grimfang4/sdl-gpu/master/include/"
     "SDL_gpu.h"
    )
    source = response.content.decode("utf-8")

    lines = source.splitlines()

    for line in lines:
        if "#define SDL_GPU_VERSION_MAJOR" in line:
            versionMajor = line.split(" ")[2]
        if "#define SDL_GPU_VERSION_MINOR" in line:
            versionMinor = line.split(" ")[2]
        if "#define SDL_GPU_VERSION_PATCH" in line:
            versionPatch = line.split(" ")[2]

    return versionMajor + "." + versionMinor + "." + versionPatch
