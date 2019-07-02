import importlib

class MissingInstaller(Exception):
    def __init__(self, message):
        super().__init__(message)

class InstallCustom:
    def __init__(self, customInstallers = {}):
        self.customInstallers = customInstallers

    def AddData(self, customInstallers):
        self.customInstallers = {**self.customInstallers, **customInstallers}

    def Install(self, project, verbose):
        try:
            installer = importlib.import_module(
             'vgazer.install.custom_installer.' + project)
        except ImportError:
            if len(self.customInstallers) == 0:
                raise MissingChecker(
                 "Missing custom installer for project: " + project)
            for customInstaller in self.customInstallers:
                if customInstaller["project"] == project:
                    istaller = customInstaller["checker"]

        return istaller.Install()
