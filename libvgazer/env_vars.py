import os

def PrintMessage(varName):
    if varName in os.environ:
        print("VGAZER: Changed environment variable:", varName)
        print("VGAZER: New value:", os.environ[varName])
    else:
        print("VGAZER: Removed environment variable:", varName)

def SetEnvVar(name, value):
    os.environ[name] = value
    PrintMessage(name)

class EnvVar:
    def __init__(self, name, value):
        self.name = name
        self.newValue = value

    def __enter__(self):
        if self.name not in os.environ:
            self.oldValue = None
        else:
            self.oldValue = os.environ[self.name]

        os.environ[self.name] = self.newValue
        PrintMessage(self.name)

    def __exit__(self, etype, value, traceback):
        if self.oldValue is None:
            os.environ.pop(self.name)
        else:
            os.environ[self.name] = self.oldValue
        PrintMessage(self.name)
