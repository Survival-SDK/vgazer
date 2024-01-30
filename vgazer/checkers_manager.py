from vgazer.exceptions          import UnknownVersionChecker
from vgazer.version.alpine      import CheckAlpine
from vgazer.version.debian      import CheckDebian
from vgazer.version.github      import CheckGithub
from vgazer.version.gitlab      import CheckGitlab
from vgazer.version.pypi        import CheckPypi
from vgazer.version.sourceforge import CheckSourceforge
from vgazer.version.stb         import CheckStb
from vgazer.version.xiph        import CheckXiph

class CheckersManager:
    def __init__(self):
        self.checkFuncs = {
            "alpine": lambda auth, platform, checkerData: CheckAlpine(
             auth["base"],
             platform.GetArch(),
             platform.GetOsVersion(),
             checkerData["repo"],
             checkerData["package"]
            ),
            "debian": lambda auth, platform, checkerData: CheckDebian(
             auth["base"],
             platform.GetOsVersion(),
             checkerData["source"]
            ),
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
