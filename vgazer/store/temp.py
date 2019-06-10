import os
from vgazer.platform import GetTempDirectoryPath
from vgazer.platform import GetHideDirectoryPrefix
from vgazer.store.base import StoreBase

class StoreTemp(StoreBase):
    def __init__(self):
        tempDirPath = GetTempDirectoryPath();
        tempDirPrefix = GetHideDirectoryPrefix();
        super().__init__(os.path.join(tempDirPath,
         tempDirPrefix + "vgazer"))
