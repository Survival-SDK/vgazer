from vgazer.exceptions import NoSuitableMirrors

class MirrorsManager():
    def __init__(self, mirrorsList, permittedProtocols):
        self.mirrorsList = mirrorsList
        self.permittedProtocols = permittedProtocols
        for protocol in permittedProtocols:
            if len(mirrorsList[protocol]) == 0:
                self.PermittedProtocols.remove(protocol)
        if len(self.permittedProtocols) == 0:
            raise NoSuitableMirrors(
             "No suitable mirrors for permitted protocols")
        self.currentProtocol = self.permittedProtocols[0]
        self.currentMirrorIndex = 0

    def GetMirrorUrl(self):
        return self.mirrorsList[self.currentProtocol][self.currentMirrorIndex]

    def ChangeMirror(self):
        if self.currentMirrorIndex < len(
         self.mirrorsList[self.currentProtocol]):
            self.currentMirrorIndex += 1
        else:
            protocolIndex = self.permittedProtocols.index[self.currentProtocol]
            if protocolIndex < len(self.PermittedProtocols):
                self.currentProtocol = self.PermittedProtocols[
                 protocolIndex + 1]
                self.currentMirrorIndex = 0
            else:
                raise NoSuitableMirrors(
                 "No suitable mirrors for permitted protocols")

    def GetNewMirrorUrl(self):
        self.ChangeMirror()
        return self.mirrorsList[self.currentProtocol][self.currentMirrorIndex]
