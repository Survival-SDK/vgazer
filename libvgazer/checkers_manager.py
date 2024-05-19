from libvgazer.exceptions        import UnknownVersionChecker
from libvgazer.version.apt_cache import CheckAptCache
from libvgazer.version.dnf       import CheckDnf
from libvgazer.version.git       import CheckGit
from libvgazer.version.pacman    import CheckPacman
from libvgazer.version.yolk3k    import CheckYolk3k
from libvgazer.version.yum       import CheckYum

class CheckersManager:
    def __init__(self):
        self.checkFuncs = {
            "apt-cache": lambda platform, checkerData: CheckAptCache(
                checkerData["package"],
                platform.GetArch()
            ),
            "dnf": lambda platform, checkerData: CheckDnf(
                checkerData["package"],
                checkerData["repo"] if "repo" in checkerData else None,
                platform.GetArch()
            ),
            "fixed": lambda platform, checkerData: checkerData["version"],
            "git": lambda platform, checkerData: CheckGit(
                checkerData["url"],
                checkerData["hint"] if "hint" in checkerData else None,
                checkerData["files"] if "files" in checkerData else None
            ),
            "pacman": lambda platform, checkerData: CheckPacman(
                checkerData["package"]
            ),
            "pypi": lambda platform, checkerData: CheckPypi(
                auth["base"],
                checkerData["package"]
            ),
            "yolk3k": lambda platform, checkerData: CheckYolk3k(
                checkerData["package"]
            ),
            "yum": lambda platform, checkerData: CheckYum(
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
