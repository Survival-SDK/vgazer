import requests
import json
from libvgazer.store.home import StoreHome

class AuthBase:
    @staticmethod
    def GetAuthData(storeHome, homeSubdir, filename, dataName):
        data = storeHome.SubdirectoryReadTextFile(homeSubdir, filename)
        if data == "":
            data = input("Input your " + dataName + ": ")
            storeHome.SubdirectoryWriteTextFile(homeSubdir, filename, data)
        if data[-1] == "\n":
            data = data[:-1]
        return data

    def __init__(self):
        self.session = requests.Session()
        self.storeHome = StoreHome()
        self.useAuth = True
        if not self.storeHome.ResolveDirectory():
            self.useAuth = False

    def GetSession(self):
        return self.session

    def GetJson(self, url):
        return json.loads(self.session.get(url).text)
