from vgazer.exceptions              import UnknownVersionChecker
from vgazer.version.alpine          import CheckAlpine
from vgazer.version.debian          import CheckDebian
from vgazer.version.gcc_src         import CheckGccSrc
from vgazer.version.github          import CheckGithub
from vgazer.version.gitlab          import CheckGitlab
from vgazer.version.linux_headers   import CheckLinuxHeaders
from vgazer.version.musl_cross_make import CheckMuslCrossMake
from vgazer.version.opus_codec      import CheckOpusCodec
from vgazer.version.pypi            import CheckPypi
from vgazer.version.sdl2_addon      import CheckSdl2Addon
from vgazer.version.sourceforge     import CheckSourceforge
from vgazer.version.stb             import CheckStb
from vgazer.version.xiph            import CheckXiph

class CheckersManager:
    def __init__(self, auth):
        self.checkFuncs = {
            "alpine": lambda auth, platform, checkerData : CheckAlpine(
             auth["base"],
             platform.GetArch(),
             platform.GetOsVersion(),
             checkerData["repo"],
             checkerData["package"]
            ),
            "debian": lambda auth, platform, checkerData : CheckDebian(
             auth["base"],
             platform.GetOsVersion(),
             checkerData["source"]
            ),
            "gcc-src": lambda auth, platform, checkerData : CheckGccSrc(
             auth["base"]
            ),
            "github": lambda auth, platform, checkerData : CheckGithub(
             auth["github"],
             checkerData["user"],
             checkerData["repo"],
             "ignoreReleases" in checkerData,
             (
              checkerData["ignoredTags"] if "ignoredTags" in checkerData
              else []
             ),
            ),
            "gitlab": lambda auth, platform, checkerData : CheckGitlab(
             auth["base"],
             checkerData["host"],
             checkerData["id"]
            ),
            "linux-headers": lambda auth, platform, checkerData :
             CheckLinuxHeaders(auth["base"]),
            "musl-cross-make": lambda auth, platform, checkerData :
             CheckMuslCrossMake(auth["github"]),
            "opus-codec": lambda auth, platform, checkerData : CheckOpusCodec(
             auth["base"],
             checkerData["project"]
            ),
            "pypi": lambda auth, platform, checkerData : CheckPypi(
             auth["base"],
             checkerData["package"]
            ),
            "sdl2-addon": lambda auth, platform, checkerData : CheckSdl2Addon(
             auth["base"],
             checkerData["project"]
            ),
            "sourceforge": lambda auth, platform, checkerData :
             CheckSourceforge(auth["base"], checkerData["project"]),
            "stb": lambda auth, platform, checkerData : CheckStb(
             auth["base"],
             checkerData["library"]
            ),
            "xiph": lambda auth, platform, checkerData : CheckXiph(
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
