def GetKeyByValue(dictionary, value):
    keys = list(dictionary.keys())
    values = list(dictionary.values())
    return keys[values.index(value)]
