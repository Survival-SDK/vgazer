from libvgazer.exceptions     import UnknownInstaller
from libvgazer.install.apt    import InstallApt
from libvgazer.install.cmd    import InstallCmd
from libvgazer.install.dnf    import InstallDnf
from libvgazer.install.pacman import InstallPacman
from libvgazer.install.pip3   import InstallPip3
from libvgazer.install.yum    import InstallYum

class InstallersManager:
    def __init__(self):
        self.installFuncs = {
            "apt": lambda software, platformData, installerData, verbose:
                InstallApt(software, installerData["package"],
                 installerData["postInstallCommands"] if "postInstallCommands"
                  in installerData else None,
                 platformData["host"],
                 verbose),
            "cmd": lambda software, platformData, installerData, verbose:
                InstallCmd(software, installerData["cmds"], verbose),
            "dnf": lambda software, platformData, installerData, verbose:
                InstallDnf(software, installerData["package"],
                 installerData["repo"] if "repo" in installerData else None,
                 installerData["postInstallCommands"] if "postInstallCommands"
                  in installerData else None,
                 verbose),
            "not-needed": lambda software, platformData, installerData,
             verbose:
                True,
            "pacman": lambda software, platformData, installerData, verbose:
                InstallPacman(software, installerData["package"], verbose),
            "pip3": lambda software, platformData, installerData,
             verbose:
                InstallPip3(software, installerData["package"], verbose),
            "yum": lambda software, platformData, installerData, verbose:
                InstallYum(software, installerData["package"],
                 installerData["repo"] if "repo" in installerData else None,
                 installerData["postInstallCommands"] if "postInstallCommands"
                  in installerData else None,
                 verbose),
        }

    def GetInstallFunc(self, installerType):
        if installerType in self.installFuncs:
            return self.installFuncs[installerType]
        else:
            raise UnknownInstaller(
             "Unknown installer: " + installerType)
