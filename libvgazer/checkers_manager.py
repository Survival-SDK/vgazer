from libvgazer.exceptions        import UnknownVersionChecker
from libvgazer.version.apt_cache import CheckAptCache
from libvgazer.version.git       import CheckGit
from libvgazer.version.pacman    import CheckPacman
from libvgazer.version.pypi      import CheckPypi
from libvgazer.version.yum       import CheckYum

class CheckersManager:
    def __init__(self):
        self.checkFuncs = {
            "apt-cache": lambda auth, platform, checkerData: CheckAptCache(
                checkerData["package"],
                platform.GetArch()
            ),
            "fixed": lambda auth, platform, checkerData: checkerData["version"],
            "git": lambda auth, platform, checkerData: CheckGit(
                checkerData["url"],
                checkerData["hint"] if "hint" in checkerData else None,
                checkerData["files"] if "files" in checkerData else None
            ),
            "pacman": lambda auth, platform, checkerData: CheckPacman(
                checkerData["package"]
            ),
            "pypi": lambda auth, platform, checkerData: CheckPypi(
                auth["base"],
                checkerData["package"]
            ),
            "yum": lambda auth, platform, checkerData: CheckYum(
                checkerData["package"],
                checkerData["repo"] if "repo" in checkerData else None,
                platform.GetArch()
            ),
        }

    def GetCheckFunc(self, checkerType):
        if checkerType in self.checkFuncs:
            return self.checkFuncs[checkerType]
        else:
            raise UnknownVersionChecker(
             "Unknown version checker: " + checkerType)
