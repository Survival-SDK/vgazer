import os
from vgazer.platform import GetHomeDirectoryPath
from vgazer.platform import GetHideDirectoryPrefix
from vgazer.store.base import StoreBase

class StoreHome(StoreBase):
    def __init__(self, subdirectory=None):
        homeDirPath = GetHomeDirectoryPath()
        if subdirectory is None:
            subdirectory = GetHideDirectoryPrefix() + "vgazer"
        super().__init__(os.path.join(homeDirPath, subdirectory))
