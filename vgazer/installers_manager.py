from vgazer.exceptions              import UnknownInstaller
from vgazer.install.apk             import InstallApk
from vgazer.install.apt             import InstallApt
from vgazer.install.gcc_src         import InstallGccSrc
from vgazer.install.linux_headers   import InstallLinuxHeaders
from vgazer.install.musl_cross_make import InstallMuslCrossMake
from vgazer.install.pip             import InstallPip
from vgazer.install.pip3            import InstallPip3
from vgazer.install.pkg_config      import InstallPkgConfig
from vgazer.install.stb             import InstallStb

class InstallersManager:
    def __init__(self):
        self.installFuncs = {
            "apk": lambda software, auth, platformData, installerData, mirrors,
             verbose:
                InstallApk(software, installerData["package"], verbose),
            "apt": lambda software, auth, platformData, installerData, mirrors,
             verbose:
                InstallApt(software, installerData["package"],
                 installerData["postInstallCommands"] if "postInstallCommands"
                  in installerData else None,
                 platformData["host"],
                 verbose),
            "gcc-src": lambda software, auth, platformData, installerData,
             mirrors, verbose:
                InstallGccSrc(auth["base"], software,
                 installerData["languages"], installerData["triplet"],
                 platformData, mirrors["gnu"], verbose),
            "linux-headers": lambda software, auth, platformData,
             installerData, mirrors, verbose:
                InstallLinuxHeaders(auth["base"], platformData, verbose),
            "musl-cross-make": lambda software, auth, platformData,
             installerData, mirrors, verbose:
                InstallMuslCrossMake(auth["github"], software,
                 installerData["languages"], installerData["triplet"],
                 platformData, verbose),
            "not_needed": lambda software, auth, platformData, installerData,
             mirrors, verbose:
                True,
            "pip": lambda software, auth, platformData, installerData, mirrors,
             verbose:
                InstallPip(software, installerData["package"], verbose),
            "pip3": lambda software, auth, platformData, installerData,
             mirrors, verbose:
                InstallPip3(software, installerData["package"], verbose),
            "pkg-config": lambda software, auth, platformData, installerData,
             mirrors, verbose:
                InstallPkgConfig(software, installerData["triplet"],
                 platformData, verbose),
            "stb": lambda software, auth, platformData, installerData, mirrors,
             verbose:
                InstallStb(installerData["library"], platformData, verbose),
        }

    def GetInstallFunc(self, installerType):
        if installerType in self.installFuncs:
            return self.installFuncs[installerType]
        else:
            raise UnknownInstaller(
             "Unknown installer: " + installerType)
