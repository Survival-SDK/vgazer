import importlib
from vgazer.exceptions import MissingChecker

class VersionCustom:
    def __init__(self, auth, customCheckers = {}):
        self.customCheckers = customCheckers
        self.auth = auth

    def AddData(self, customCheckers):
        self.customCheckers = {**self.customCheckers, **customCheckers}

    def Check(self, checker):
        try:
            versionChecker = importlib.import_module(
             'vgazer.version.custom_checker.' + checker)
        except ImportError:
            if len(self.customCheckers) == 0:
                raise MissingChecker(
                 "Missing custom checker : " + checker)
            for customChecker in self.customCheckers:
                if customChecker["name"] == checker:
                    versionChecker = customChecker["checker"]

        return versionChecker.Check(self.auth)
