def GetVersionFromTag(tag):
    if tag[0] == "v":
        return tag.split("v")[1]
    return tag
