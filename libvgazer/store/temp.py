import os

from libvgazer.platform import GetTempDirectoryPath
from libvgazer.platform import GetHideDirectoryPrefix
from libvgazer.store.base import StoreBase

class StoreTemp(StoreBase):
    def __init__(self, subdirectory=None):
        tempDirPath = GetTempDirectoryPath()
        if subdirectory is None:
            subdirectory = GetHideDirectoryPrefix() + "vgazer"
        super().__init__(os.path.join(tempDirPath, subdirectory))
