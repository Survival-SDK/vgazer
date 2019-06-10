import os

class UnexpectedOsType(Exception):
    def __init__(self, message):
        super().__init__(message)

def GetHideDirectoryPrefix():
    if os.name == "posix":
        return "."
    else:
        raise UnexpectedOsType("Unexpected OS type: " + os.name)

def GetHomeDirectoryPath():
    if os.name == "posix":
        return os.path.expanduser("~")
    else:
        raise UnexpectedOsType("Unexpected OS type: " + os.name)

def GetTempDirectoryPath():
    if os.name == "posix":
        return "/tmp"
    else:
        raise UnexpectedOsType("Unexpected OS type: " + os.name)
