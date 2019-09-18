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

    hostArch = gazer.GetTargetPlatform().GetArch()
    hostOs = gazer.GetTargetPlatform().GetOs()
    hostOsVersion = gazer.GetTargetPlatform().GetOsVersion()

    if not (
     (hostOs == "debian") and (hostOsVersion in ["buster", "bullseye", "sid"])
    ):
        if hostOs == "alpine":
            gazer.Install(hostArch + "-linux-musl-gcc", verbose=True)
            gazer.Install("musl", verbose=True)
            gazer.Install("make", verbose=True)
        if hostOs == "debian":
            gazer.Install("wget", verbose=True)
        gazer.Install("cmake", verbose=True)
    gazer.Install("cjson", verbose=True)

if __name__ == "__main__":
    main()
