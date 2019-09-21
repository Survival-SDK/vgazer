#!/usr/bin/env python3

import os
import sys
import inspect

currentFrame = inspect.currentframe()
currentFile = os.path.abspath(inspect.getfile(currentFrame))
currentDir = os.path.dirname(currentFile)
parentDir = os.path.dirname(currentDir)

sys.path.insert(0, parentDir)

from vgazer.vgazer import Vgazer

def main():
    gazer = Vgazer()

    print("host:", gazer.GetHostPlatform().GetArch(),
     gazer.GetHostPlatform().GetOs(), gazer.GetHostPlatform().GetOsVersion(),
     gazer.GetHostPlatform().GetAbi())
    print("target:", gazer.GetTargetPlatform().GetArch(),
     gazer.GetTargetPlatform().GetOs(),
     gazer.GetTargetPlatform().GetOsVersion(),
     gazer.GetTargetPlatform().GetAbi())

    if gazer.GetHostPlatform().GetOs() == "alpine":
        gazer.Install(gazer.GetHostPlatform().GetArch() + "-linux-musl-gcc",
         verbose=True)
        gazer.Install(gazer.GetHostPlatform().GetArch() + "-linux-musl-g++",
         verbose=True)
        gazer.Install("make", verbose=True)
    if gazer.GetHostPlatform().GetOs() == "debian":
        gazer.Install("wget", verbose=True)
    gazer.Install("git", verbose=True)
    gazer.Install("cmake", verbose=True)
    gazer.Install("sdl2", verbose=True)
    gazer.Install("glew", verbose=True)
    gazer.Install("stb_image", verbose=True)
    gazer.Install("stb_image_write", verbose=True)
    gazer.Install("sdl2_gpu", verbose=True)

if __name__ == "__main__":
    main()
