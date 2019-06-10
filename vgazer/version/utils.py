def GetExtensionDotsCount(filename):
    splitedFilename = filename.split(".")
    firtsExt = splitedFilename[-1]
    if firtsExt == "gz" or firtsExt == "bz2" or firtsExt == "xz":
        if splitedFilename[-2] == "tar":
            return 1

    return 0

def GetVersionNumbers(VersionAndExt, dotsCount):
    splitedVersionAndExt = VersionAndExt.split(".")
    while dotsCount >= 0:
        splitedVersionAndExt.pop(-1)
        dotsCount -= 1
    return splitedVersionAndExt

def GetVersionFromTag(tag):
    if tag[0] == "v":
        return tag.split("v")[1]
    return tag

def GetVersionFromFilename(filename):
    dotsCount = GetExtensionDotsCount(filename)

    VersionAndExt = filename.split("-")[-1]

    return '.'.join(GetVersionNumbers(VersionAndExt, dotsCount))
