import importlib

class MissingChecker(Exception):
    def __init__(self, message):
        super().__init__(message)

class VersionCustom:
    def __init__(self, auth, customCheckers = {}):
        self.customCheckers = customCheckers
        self.auth = auth

    def AddData(self, customCheckers):
        self.customCheckers = {**self.customCheckers, **customCheckers}

    def Check(self, project):
        try:
            versionChecker = importlib.import_module(
             'vgazer.version.custom_checker.' + project)
        except ImportError:
            if len(self.customCheckers) == 0:
                raise MissingChecker(
                 "Missing custom checker for project: " + project)
            for customChecker in self.customCheckers:
                if customChecker["project"] == project:
                    versionChecker = customChecker["checker"]

        return versionChecker.Check(self.auth)
