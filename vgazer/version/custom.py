import importlib

def CheckCustom(auth, project):
    versionChecker = importlib.import_module(
     'vgazer.version.custom_checker.' + project)
    return versionChecker.Check(auth)
