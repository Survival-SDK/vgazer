import os
from pathlib import Path

class WorkingDir:
    """Context manager for changing the current working directory"""
    def __init__(self, newPath):
        self.newPath = os.path.expanduser(newPath)

    def __enter__(self):
        self.savedPath = os.getcwd()
        print("VGAZER: Entering to directory:", self.newPath)
        Path(self.newPath).mkdir(parents=True, exist_ok=True)
        os.chdir(self.newPath)

    def __exit__(self, etype, value, traceback):
        os.chdir(self.savedPath)
