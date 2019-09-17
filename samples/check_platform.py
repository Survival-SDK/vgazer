#!/usr/bin/env python3

import os
import sys
import inspect

currentFrame = inspect.currentframe()
currentFile = os.path.abspath(inspect.getfile(currentFrame))
currentDir = os.path.dirname(currentFile)
parentDir = os.path.dirname(currentDir)

sys.path.insert(0, parentDir)

from vgazer.vgazer          import Vgazer
from samples.samples_common import PrintHostPlatformData

def main():
    gazer = Vgazer()
    PrintHostPlatformData(gazer)

if __name__ == "__main__":
    main()
