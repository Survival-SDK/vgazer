import os
from pathlib import Path

class WorkingDir:
    """Context manager for changing the current working directory"""
    def __init__(self, newPath, verbose=True):
        self.newPath = os.path.expanduser(newPath)
        self.verbose = verbose

    def __enter__(self):
        self.savedPath = os.getcwd()
        Path(self.newPath).mkdir(parents=True, exist_ok=True)
        if self.verbose:
            print("VGAZER: Entering to directory:", self.newPath)
        os.chdir(self.newPath)

    def __exit__(self, etype, value, traceback):
        if self.verbose:
            print("VGAZER: Returning to directory:", self.savedPath)
        os.chdir(self.savedPath)
