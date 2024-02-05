import os

from libvgazer.exceptions import FileNotFound

def GetKeyByValue(dictionary, value):
    keys = list(dictionary.keys())
    values = list(dictionary.values())
    return keys[values.index(value)]

def FindFileInDir(directories, filenames):
    for directory in directories:
        for filename in filenames:
            if os.path.isfile(os.path.join(directory, filename)):
                return filename
    raise FileNotFound(
     "Unable to find any file from list: " + ", ".join(filenames))

def OneOfIsNone(*args):
    for arg in args:
        if arg is None:
            return True

    return False
