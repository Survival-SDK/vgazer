from libvgazer.exceptions          import UnknownVersionChecker
from libvgazer.version.debian      import CheckDebian
from libvgazer.version.git         import CheckGit
from libvgazer.version.github      import CheckGithub
from libvgazer.version.gitlab      import CheckGitlab
from libvgazer.version.pypi        import CheckPypi
from libvgazer.version.sourceforge import CheckSourceforge
from libvgazer.version.stb         import CheckStb
from libvgazer.version.xiph        import CheckXiph

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
             checkerData["hint"] if "hint" in checkerData else None),
            "github": lambda auth, platform, checkerData: CheckGithub(
             auth["github"],
             checkerData["user"],
             checkerData["repo"],
             "ignoreReleases" in checkerData,
             (
              checkerData["ignoredTags"] if "ignoredTags" in checkerData
              else []
             ),
            ),
            "gitlab": lambda auth, platform, checkerData: CheckGitlab(
             auth["base"],
             checkerData["host"],
             checkerData["id"]
            ),
            "pypi": lambda auth, platform, checkerData: CheckPypi(
             auth["base"],
             checkerData["package"]
            ),
            "sourceforge": lambda auth, platform, checkerData:
             CheckSourceforge(auth["base"], checkerData["project"]),
            "stb": lambda auth, platform, checkerData: CheckStb(
             auth["base"],
             checkerData["library"]
            ),
            "xiph": lambda auth, platform, checkerData: CheckXiph(
             auth["base"],
             checkerData["project"]
            ),
        }

    def GetCheckFunc(self, checkerType):
        if checkerType in self.checkFuncs:
            return self.checkFuncs[checkerType]
        else:
            raise UnknownVersionChecker(
             "Unknown version checker: " + checkerType)
