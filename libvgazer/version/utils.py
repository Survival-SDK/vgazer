import re

def GetVersionFromTag(tag):
    if "-" in tag:
        # if tag is something like "V3-6-0"
        if (tag.lower()[0] == "v"
         and re.search('[a-zA-Z]', tag.lower().split("v")[1]) is None):
            return tag.lower().split("v")[1].replace("-", ".")
        else:
            return tag.split("-")[-1]
    elif tag[0] == "v":
        return tag.split("v")[1]
    return tag

def GetVersionFromFilename(filename):
    VersionAndExt = filename.split("-")[-1]

    if "beta" in VersionAndExt:
        VersionAndExt = filename.split("-")[-2] + "-" + filename.split("-")[-1]

    for i in range(0, 5):
        if VersionAndExt.split(".")[i].isalpha():
            return ".".join(VersionAndExt.split(".")[0:i])
