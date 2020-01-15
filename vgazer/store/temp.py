import os
from vgazer.platform import GetTempDirectoryPath
from vgazer.platform import GetHideDirectoryPrefix
from vgazer.store.base import StoreBase

class StoreTemp(StoreBase):
    def __init__(self, subdirectory=None):
        tempDirPath = GetTempDirectoryPath();
        if subdirectory is None:
            subdirectory = GetHideDirectoryPrefix() + "vgazer";
        super().__init__(os.path.join(tempDirPath, subdirectory))
