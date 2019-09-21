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

    hostArch = gazer.GetHostPlatform().GetArch()
    hostOs = gazer.GetHostPlatform().GetOs()
    hostOsVersion = gazer.GetHostPlatform().GetOsVersion()

    if hostOs == "alpine" and hostOsVersion != "edge":
        gazer.Install(hostArch + "-linux-musl-gcc", verbose=True)
        gazer.Install(hostArch + "-linux-musl-g++", verbose=True)
        gazer.Install("make", verbose=True)
        gazer.Install("cmake", verbose=True)
        fallbackPreinstall = ["git"]
    else:
        fallbackPreinstall = None
    gazer.Install("physfs", verbose=True,
     fallbackPreinstallList=fallbackPreinstall)

if __name__ == "__main__":
    main()