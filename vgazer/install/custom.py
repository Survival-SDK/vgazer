import importlib

from vgazer.exceptions import MissingInstaller

class InstallCustom:
    def __init__(self, customInstallers = {}):
        self.customInstallers = customInstallers

    def AddData(self, customInstallers):
        self.customInstallers = {**self.customInstallers, **customInstallers}

    def Install(self, software, installerName, platform, hostPlatformData,
     targetPlatformData, verbose):
        try:
            installer = importlib.import_module(
             'vgazer.install.custom_installer.' + installerName)
        except ImportError:
            if len(self.customInstallers) == 0:
                raise MissingInstaller(
                 "Missing custom installer for project: " + software)
            for customInstaller in self.customInstallers:
                if customInstaller["name"] == installerName:
                    istaller = customInstaller["installer"]

        return istaller.Install()
