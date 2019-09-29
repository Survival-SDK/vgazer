import time

from vgazer.mirrors.manager import MirrorsManager
from vgazer.store.home      import StoreHome

class MirrorsBase():
    @staticmethod
    def ResolveHomeDirsAndFiles(storeHome, siteName):
        if not storeHome.ResolveSubdirectory(siteName):
            return False

        filesResolved = storeHome.ResolveSubdirectoryFile(siteName, "mirrors")

        if not filesResolved:
            return False
        return True

    @staticmethod
    def MirrorsListToText(mirrorsList):
        data = ""
        data += str(time.time()) + "\n"
        for protocol in mirrorsList:
            for mirror in mirrorsList[protocol]:
                data += protocol + " " + mirror + "\n"
        return data

    @staticmethod
    def MirrorsListFromText(data):
        mirrorsList = {"http": [], "https": [], "ftp": [], "rsync": []}
        for line in data.splitlines()[1:]:
            protocol = line.split(" ")[0]
            mirror = line.split(" ")[1]
            mirrorsList[protocol].append(mirror)
        return mirrorsList

    @staticmethod
    def MirrorsDataOutOfTime(data):
        return float(data.splitlines()[0]) + 86400 < time.time()

    def __init__(self, siteName, getMirrorsList):
        print("VGAZER: Checking mirrors list for " + siteName + "...")
        self.storeHome = StoreHome()
        if self.storeHome.ResolveDirectory():
            if self.ResolveHomeDirsAndFiles(self.storeHome, siteName):
                data = self.storeHome.SubdirectoryReadTextFile(siteName,
                 "mirrors")
                if data == "":
                    print(
                     "VGAZER: Stored mirrors list for " + siteName
                      + " not found")
                    self.mirrorsList = getMirrorsList()
                    data = self.MirrorsListToText(self.mirrorsList)
                    self.storeHome.SubdirectoryWriteTextFile(siteName,
                     "mirrors", data)
                elif self.MirrorsDataOutOfTime(data):
                    print(
                     "VGAZER: Stored mirrors list for " + siteName
                      + " out of date")
                    self.mirrorsList = getMirrorsList(noFallback = True)
                    if self.mirrorsList is None:
                        self.mirrorsList = self.MirrorsListFromText(data)
                    else:
                        data = self.MirrorsListToText(self.mirrorsList)
                        self.storeHome.SubdirectoryWriteTextFile(siteName,
                         "mirrors", data)
                else:
                    print(
                     "VGAZER: Found up to date mirrors list for " + siteName)
                    self.mirrorsList = self.MirrorsListFromText(data)
            else:
                print(
                 "VGAZER: Unable to load stored mirrors list for " + siteName)
                self.mirrorsList = getMirrorsList()
        else:
            print("VGAZER: Unable to load stored mirrors list for " + siteName)
            self.mirrorsList = getMirrorsList()

    def CreateMirrorsManager(self, permittedProtocols):
        return MirrorsManager(self.mirrorsList, permittedProtocols)
