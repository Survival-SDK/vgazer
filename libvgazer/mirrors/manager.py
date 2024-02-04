from libvgazer.exceptions import NoSuitableMirrors

class MirrorsManager():
    def __init__(self, mirrorsList, permittedProtocols):
        self.mirrorsList = mirrorsList
        self.permittedProtocols = permittedProtocols
        for protocol in permittedProtocols:
            if len(mirrorsList[protocol]) == 0:
                self.permittedProtocols.remove(protocol)
        if len(self.permittedProtocols) == 0:
            raise NoSuitableMirrors(
             "No suitable mirrors for permitted protocols")
        self.currentProtocol = self.permittedProtocols[0]
        self.currentMirrorIndex = 0

    def GetMirrorUrl(self):
        return self.mirrorsList[self.currentProtocol][self.currentMirrorIndex]

    def ChangeMirror(self):
        if self.currentMirrorIndex < len(
         self.mirrorsList[self.currentProtocol]) - 1:
            self.currentMirrorIndex += 1
        else:
            protocolIndex = self.permittedProtocols.index(self.currentProtocol)
            if protocolIndex < len(self.permittedProtocols) - 1:
                self.currentProtocol = self.permittedProtocols[
                 protocolIndex + 1]
                self.currentMirrorIndex = 0
            else:
                raise NoSuitableMirrors(
                 "No suitable mirrors for permitted protocols")

    def GetNewMirrorUrl(self):
        self.ChangeMirror()
        return self.mirrorsList[self.currentProtocol][self.currentMirrorIndex]
