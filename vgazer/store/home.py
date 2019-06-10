import os
from vgazer.platform import GetHomeDirectoryPath
from vgazer.platform import GetHideDirectoryPrefix
from vgazer.store.base import StoreBase

class StoreHome(StoreBase):
    def __init__(self):
        homeDirPath = GetHomeDirectoryPath();
        hideDirPrefix = GetHideDirectoryPrefix();
        super().__init__(os.path.join(homeDirPath,
         hideDirPrefix + "vgazer"))

