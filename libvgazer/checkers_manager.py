from libvgazer.exceptions     import UnknownVersionChecker
from libvgazer.version.debian import CheckDebian
from libvgazer.version.git    import CheckGit
from libvgazer.version.pypi   import CheckPypi

class CheckersManager:
    def __init__(self):
        self.checkFuncs = {
            "debian": lambda auth, platform, checkerData: CheckDebian(
             auth["base"],
             platform.GetOsVersion(),
             checkerData["source"]
            ),
            "git": lambda auth, platform, checkerData: CheckGit(
             checkerData["url"],
             checkerData["hint"] if "hint" in checkerData else None,
             checkerData["files"] if "files" in checkerData else None),
            "pypi": lambda auth, platform, checkerData: CheckPypi(
             auth["base"],
             checkerData["package"]
            ),
        }

    def GetCheckFunc(self, checkerType):
        if checkerType in self.checkFuncs:
            return self.checkFuncs[checkerType]
        else:
            raise UnknownVersionChecker(
             "Unknown version checker: " + checkerType)
