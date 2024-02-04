import os
from libvgazer.platform import GetHomeDirectoryPath
from libvgazer.platform import GetHideDirectoryPrefix
from libvgazer.store.base import StoreBase

class StoreHome(StoreBase):
    def __init__(self, subdirectory=None):
        homeDirPath = GetHomeDirectoryPath()
        if subdirectory is None:
            subdirectory = GetHideDirectoryPrefix() + "vgazer"
        super().__init__(os.path.join(homeDirPath, subdirectory))
