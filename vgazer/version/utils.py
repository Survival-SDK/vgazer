def GetVersionFromTag(tag):
    if tag[0] == "v":
        return tag.split("v")[1]
    return tag

def GetVersionFromFilename(filename):
    VersionAndExt = filename.split("-")[-1]

    for i in range(0, 4):
        if VersionAndExt.split(".")[i].isalpha():
            return ".".join(VersionAndExt.split(".")[0:i])
