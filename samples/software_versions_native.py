#!/usr/bin/env python3

import os
import sys
import inspect

currentFrame = inspect.currentframe()
currentFile = os.path.abspath(inspect.getfile(currentFrame))
currentDir = os.path.dirname(currentFile)
parentDir = os.path.dirname(currentDir)

sys.path.insert(0, parentDir)

from vgazer.vgazer                      import Vgazer

from samples.samples_common             import PrintPlatformData
from samples.software_versions_common   import PrintSoftwareVersions

def main():
    gazer = Vgazer()
    PrintPlatformData(gazer)
    PrintSoftwareVersions(gazer)

if __name__ == "__main__":
    main()
