import os

def SetEnvVar(name, value):
    os.environ[name] = value

def AppendEnvVar(name, value):
    if name not in os.environ:
        os.environ[name] = ""
    os.environ[name] = os.environ[name] + value

def PrependEnvVar(name, value):
    if name not in os.environ:
        os.environ[name] = ""
    os.environ[name] = value + os.environ[name]

def AppendEnvVarItem(name, value, separator):
    if name not in os.environ:
        os.environ[name] = ""
    else:
        os.environ[name] = os.environ[name] + separator
    os.environ[name] = os.environ[name] + value

def PrependEnvVarItem(name, value, separator):
    if name not in os.environ:
        os.environ[name] = ""
    else:
        os.environ[name] = separator + os.environ[name]
    os.environ[name] = value + os.environ[name]
