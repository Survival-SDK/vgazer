def GetVersionFromTag(tag):
    if "-" in tag:
        return tag.split("-")[-1]
    elif tag[0] == "v":
        return tag.split("v")[1]
    return tag

def GetVersionFromFilename(filename):
    VersionAndExt = filename.split("-")[-1]

    for i in range(0, 5):
        if VersionAndExt.split(".")[i].isalpha():
            return ".".join(VersionAndExt.split(".")[0:i])
