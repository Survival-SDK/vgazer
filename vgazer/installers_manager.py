from vgazer.exceptions         import UnknownInstaller
from vgazer.install.apt        import InstallApt
from vgazer.install.pip        import InstallPip
from vgazer.install.pip3       import InstallPip3
from vgazer.install.pkg_config import InstallPkgConfig
from vgazer.install.stb        import InstallStb

class InstallersManager:
    def __init__(self):
        self.installFuncs = {
            "apt": lambda software, auth, platformData, installerData, mirrors,
             verbose:
                InstallApt(software, installerData["package"],
                 installerData["postInstallCommands"] if "postInstallCommands"
                  in installerData else None,
                 platformData["host"],
                 verbose),
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
