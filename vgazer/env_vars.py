import os

def PrintMessage(varName):
    print("VGAZER: Changed environment variable:", varName)
    print("VGAZER: New value:", os.environ[varName])

def SetEnvVar(name, value):
    os.environ[name] = value
    PrintMessage(name)

def AppendEnvVar(name, value):
    if name not in os.environ:
        os.environ[name] = ""
    os.environ[name] = os.environ[name] + value
    PrintMessage(name)

def PrependEnvVar(name, value):
    if name not in os.environ:
        os.environ[name] = ""
    os.environ[name] = value + os.environ[name]
    PrintMessage(name)

def AppendEnvVarItem(name, value, separator):
    if name not in os.environ:
        os.environ[name] = ""
    else:
        os.environ[name] = os.environ[name] + separator
    os.environ[name] = os.environ[name] + value
    PrintMessage(name)

def PrependEnvVarItem(name, value, separator):
    if name not in os.environ:
        os.environ[name] = ""
    else:
        os.environ[name] = separator + os.environ[name]
    os.environ[name] = value + os.environ[name]
    PrintMessage(name)
