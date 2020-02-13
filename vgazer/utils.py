import os

from vgazer.exceptions  import FileNotFound

def GetKeyByValue(dictionary, value):
    keys = list(dictionary.keys())
    values = list(dictionary.values())
    return keys[values.index(value)]

def NewListWithReplace(array, oldText, newText):
    for element in array:
        array.replace(oldText, newText)

def FindFileInDir(directories, filenames):
    for directory in directories:
        for filename in filenames:
            if os.path.isfile(os.path.join(directory, filename)):
                return filename
    raise FileNotFound(
     "Unable to find any file from list: " + ", ".join(filenames))
