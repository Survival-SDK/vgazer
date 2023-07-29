import os

def PrintMessage(varName):
    print("VGAZER: Changed environment variable:", varName)
    print("VGAZER: New value:", os.environ[varName])

def SetEnvVar(name, value):
    os.environ[name] = value
    PrintMessage(name)




