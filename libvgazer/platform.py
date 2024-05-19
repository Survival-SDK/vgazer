import os.path

from libvgazer.command       import GetCommandOutputUtf8
from libvgazer.exceptions    import FileNotFound
from libvgazer.exceptions    import MissingArgument
from libvgazer.exceptions    import UnexpectedOsType
from libvgazer.exceptions    import UnknownOs
from libvgazer.exceptions    import UnknownTargetArch
from libvgazer.host_detector import HostDetector
from libvgazer.utils         import FindFileInDir
from libvgazer.utils         import OneOfIsNone

def GetFilesystemType(path):
    output = GetCommandOutputUtf8(["df", "-T", path])
    lines = output.splitlines()
    if len(lines) == 1:
        raise UnexpectedOsType('Directory "' + path + '" unavailable')

    return lines[1].split()[1]

def GetHideDirectoryPrefix():
    if os.name == "posix":
        return "."
    else:
        raise UnexpectedOsType("Unexpected OS type: " + os.name)

def GetHomeDirectoryPath():
    if os.name == "posix":
        return os.path.expanduser("~")
    else:
        raise UnexpectedOsType("Unexpected OS type: " + os.name)

def GetTempDirectoryPath():
    if os.name == "posix":
        return "/tmp"
    else:
        raise UnexpectedOsType("Unexpected OS type: " + os.name)

def GetBitness(targetPlatformData):
    arch = targetPlatformData.GetArch()

    if arch == "x86_64":
        return 64
    else:
        raise UnknownTargetArch(
         "Unknown target architecture: " + arch)

def GetTriplet(targetPlatformData):
    arch = targetPlatformData.GetArch()
    os = targetPlatformData.GetOs()
    abi = targetPlatformData.GetAbi()

    triplet = arch

    if Platform.OsIsLinux(os):
        triplet += "-linux-" + abi
    elif os == "windows":
        triplet += "-w64-mingw32"
    else:
        raise UnknownOs("Unknown OS: " + os)

    return triplet

def GetGenericTriplet(targetPlatformData):
    arch = targetPlatformData.GetArch()
    os = targetPlatformData.GetOs()
    abi = targetPlatformData.GetAbi()

    triplet = arch

    if Platform.OsIsLinux(os):
        triplet += "-linux-" + abi
    elif os == "windows":
        triplet += "-w64-mingw32"
    else:
        raise UnknownOs("Unknown OS: " + os)

    return triplet

def GetInstallPrefix(platformData):
    if platformData["target"].PlatformsEqual(platformData["host"]):
        return "/usr/local"
    else:
        return ("/usr/local/" + GetTriplet(platformData["target"]))

def GetSoPrefix(platformData):
    if Platform.OsIsLinux(platformData["target"].GetOs()):
        return GetInstallPrefix(platformData) + "/lib"
    elif platformData["target"].GetOs() == "windows":
        return GetInstallPrefix(platformData) + "/bin"
    else:
        raise UnknownOs("Unknown OS: " + platformData["target"].GetOs())

def GetTripletFilenames(triplet, suffixes):
    filenames = []
    for suffix in suffixes:
        filenames.append(triplet + suffix)

    return filenames

def GetUtility(targetPlatformData, directories, suffixes, fallbackFilenames):
    triplet = GetGenericTriplet(targetPlatformData)
    vendoredTriplet = GetTriplet(targetPlatformData)

    filenames = GetTripletFilenames(triplet, suffixes)
    filenames.extend(GetTripletFilenames(vendoredTriplet, suffixes))
    try:
        return FindFileInDir(directories, filenames)
    except FileNotFound:
        return FindFileInDir(directories, fallbackFilenames)

def GetCc(targetPlatformData):
    return GetUtility(
     targetPlatformData,
     directories=["/usr/bin", "/usr/local/bin"],
     suffixes=["-gcc-posix", "-gcc"],
     fallbackFilenames=["gcc"]
    )

def GetCxx(targetPlatformData):
    return GetUtility(
     targetPlatformData,
     directories=["/usr/bin", "/usr/local/bin"],
     suffixes=["-g++-posix", "-g++"],
     fallbackFilenames=["g++"]
    )

def GetAr(targetPlatformData):
    return GetUtility(
     targetPlatformData,
     directories=["/usr/bin", "/usr/local/bin"],
     suffixes=["-ar-posix", "-gcc-ar-posix", "-ar", "-gcc-ar"],
     fallbackFilenames=["ar"]
    )

def GetArFullPath(targetPlatformData):
    return os.path.join("/usr/bin", GetAr(targetPlatformData))

def GetRanlib(targetPlatformData):
    return GetUtility(
     targetPlatformData,
     directories=["/usr/bin", "/usr/local/bin"],
     suffixes=["-ranlib-posix", "-gcc-ranlib-posix", "-ranlib", "-gcc-ranlib"],
     fallbackFilenames=["ranlib"]
    )

def GetPkgConfig(targetPlatformData):
    try:
        return GetUtility(
         targetPlatformData,
         directories=["/usr/bin", "/usr/local/bin"],
         suffixes=["-pkg-config"],
         fallbackFilenames=["pkg-config"]
        )
    except FileNotFound:
        return "pkg-config"

def GetStrip(targetPlatformData):
    return GetUtility(
     targetPlatformData,
     directories=["/usr/bin", "/usr/local/bin"],
     suffixes=["-strip"],
     fallbackFilenames=["strip"]
    )

def GetCmake(targetPlatformData):
    if os.path.isfile("/usr/bin/cmake"):
        return "/usr/bin/cmake"

    if os.path.isfile("/usr/local/bin/cmake"):
        return "/usr/local/bin/cmake"

    return "cmake"

def GetSoFilename(targetPlatformData, name):
    if Platform.OsIsLinux(targetPlatformData.GetOs()):
        return "lib" + name + ".so"
    elif targetPlatformData.GetOs() == "windows":
        return name + ".dll"
    else:
        raise UnknownOs("Unknown OS: " + targetPlatformData.GetOs())

class Platform:
    # Platforms comparing ratings
    COMP_INCOMPATIBLE = -1000
    COMP_COMPATIBLE = 0
    COMP_EQUAL = 1

    @staticmethod
    def OsIsLinux(os):
        return (os in ["linux", "archlinux", "fedora", "oraclelinux", "debian"])

    @staticmethod
    def GetGenericOs(os):
        if Platform.OsIsLinux(os):
            return "linux"
        elif os == "windows" or os == "any":
            return os
        else:
            raise UnknownOs("Unknown OS: " + os)

    def __init__(self, arch=None, os=None, osVersion=None, abi=None,
     suppressGenericFallback=False):
        self.isHost = OneOfIsNone(arch, os, osVersion, abi)

        if self.isHost:
            with HostDetector() as hostDetector:
                if hostDetector.OsIsUnknown():
                    raise UnexpectedOsType(hostDetector.GetErrorMsg)

                self.arch = hostDetector.GetArch()
                self.os = hostDetector.GetOs()
                self.osVersion = hostDetector.GetOsVersion()
                self.abi = hostDetector.GetAbi()

        elif not suppressGenericFallback:
            self.arch = arch
            self.os = Platform.GetGenericOs(os)
            self.osVersion = "any"
            self.abi = abi
        else:
            self.arch = arch
            self.os = os
            self.osVersion = osVersion
            self.abi = abi

    def IsHost(self):
        return self.isHost

    def GetArch(self):
        return self.arch

    def GetOs(self):
        return self.os

    def GetOsVersion(self):
        return self.osVersion

    def GetAbi(self):
        return self.abi

    def ArchsCompatible(self, platform=None, arch=None):
        if platform is None:
            if arch is None:
                raise MissingArgument("Missing value for argument 'arch'")
            comparingArch = arch
        else:
            comparingArch = platform.arch
        if self.arch == "any" or comparingArch == "any":
            return True
        if self.arch == comparingArch:
            return True

        return False

    def ArchsEqual(self, platform=None, arch=None):
        if platform is None:
            if arch is None:
                raise MissingArgument("Missing value for argument 'arch'")
            comparingArch = arch
        else:
            comparingArch = platform.arch
        if (self.arch == comparingArch and self.arch != "any" and
         comparingArch != "any"):
            return True
        return False

    def OsesCompatible(self, platform=None, os=None):
        if platform is None:
            if os is None:
                raise MissingArgument("Missing value for argument 'os'")
            comparingOs = os
        else:
            comparingOs = platform.os
        if self.os == "any" or comparingOs == "any":
            return True
        if self.os == comparingOs:
            return True
        if Platform.OsIsLinux(self.os) and comparingOs == "linux":
            return True
        return False

    def OsesEqual(self, platform=None, os=None):
        if platform is None:
            if os is None:
                raise MissingArgument("Missing value for argument 'os'")
            comparingOs = os
        else:
            comparingOs = platform.os
        if (self.os == comparingOs and self.os != "any"
         and comparingOs != "any"):
            return True
        return False

    def OsVersionsCompatible(self, platform=None, osVersion=None):
        if platform is None:
            if osVersion is None:
                raise MissingArgument("Missing value for argument 'osVersion'")
            comparingOsVersion = osVersion
        else:
            comparingOsVersion = platform.osVersion
        if self.osVersion == "any" or comparingOsVersion == "any":
            return True
        if self.osVersion == comparingOsVersion:
            return True
        return False

    def OsVersionsEqual(self, platform=None, osVersion=None):
        if platform is None:
            if osVersion is None:
                raise MissingArgument("Missing value for argument 'osVersion'")
            comparingOsVersion = osVersion
        else:
            comparingOsVersion = platform.osVersion
        if (self.osVersion == comparingOsVersion and self.osVersion != "any"
         and comparingOsVersion != "any"):
            return True
        return False

    def AbisCompatible(self, platform=None, abi=None):
        if platform is None:
            if abi is None:
                raise MissingArgument("Missing value for argument 'abi'")
            comparingAbi = abi
        else:
            comparingAbi = platform.abi
        if self.abi == "any" or comparingAbi == "any":
            return True
        if self.abi == comparingAbi:
            return True
        return False

    def AbisEqual(self, platform=None, abi=None):
        if platform is None:
            if abi is None:
                raise MissingArgument("Missing value for argument 'abi'")
            comparingAbi = abi
        else:
            comparingAbi = platform.abi
        if (self.abi == comparingAbi and self.abi != "any" and
         comparingAbi != "any"):
            return True
        return False

    def GetArchsCompareRating(self, platform=None, arch=None):
        if platform is None:
            if arch is None:
                raise MissingArgument("Missing value for argument 'arch'")
            comparingArch = arch
        else:
            comparingArch = platform.arch
        if self.ArchsEqual(arch=comparingArch):
            return Platform.COMP_EQUAL
        elif self.ArchsCompatible(arch=comparingArch):
            return Platform.COMP_COMPATIBLE
        else:
            return Platform.COMP_INCOMPATIBLE

    def GetOsesCompareRating(self, platform=None, os=None):
        if platform is None:
            if os is None:
                raise MissingArgument("Missing value for argument 'os'")
            comparingOs = os
        else:
            comparingOs = platform.os
        if self.OsesEqual(os=comparingOs):
            return Platform.COMP_EQUAL
        elif self.OsesCompatible(os=comparingOs):
            return Platform.COMP_COMPATIBLE
        else:
            return Platform.COMP_INCOMPATIBLE

    def GetOsVersionsCompareRating(self, platform=None, osVersion=None):
        if platform is None:
            if osVersion is None:
                raise MissingArgument("Missing value for argument 'osVersion'")
            comparingOsVersion = osVersion
        else:
            comparingOsVersion = platform.osVersion
        if self.OsVersionsEqual(osVersion=comparingOsVersion):
            return Platform.COMP_EQUAL
        elif self.OsVersionsCompatible(osVersion=comparingOsVersion):
            return Platform.COMP_COMPATIBLE
        else:
            return Platform.COMP_INCOMPATIBLE

    def GetAbisCompareRating(self, platform=None, abi=None):
        if platform is None:
            if abi is None:
                raise MissingArgument("Missing value for argument 'abi'")
            comparingAbi = abi
        else:
            comparingAbi = platform.abi
        if self.AbisEqual(abi=comparingAbi):
            return Platform.COMP_EQUAL
        elif self.AbisCompatible(abi=comparingAbi):
            return Platform.COMP_COMPATIBLE
        else:
            return Platform.COMP_INCOMPATIBLE

    def PlatformsEqual(self, platform):
        return (self.ArchsEqual(platform) and self.OsesEqual(platform)
         and self.OsVersionsEqual(platform) and self.AbisEqual(platform))

    def GetCompatibilityRating(self, archs, oses, osVersions, abis):
        archMaxRating = Platform.COMP_INCOMPATIBLE
        osMaxRating = Platform.COMP_INCOMPATIBLE
        osVersionMaxRating = Platform.COMP_INCOMPATIBLE
        abiMaxRating = Platform.COMP_INCOMPATIBLE
        for comparingArch in archs:
            archRating = self.GetArchsCompareRating(arch=comparingArch)
            if archRating > archMaxRating:
                archMaxRating = archRating
        for comparingOs in oses:
            osRating = self.GetOsesCompareRating(os=comparingOs)
            if osRating > osMaxRating:
                osMaxRating = osRating
        for comparingOsVersion in osVersions:
            osVersionRating = self.GetOsVersionsCompareRating(
             osVersion=comparingOsVersion)
            if osVersionRating > osVersionMaxRating:
                osVersionMaxRating = osVersionRating
        for comparingAbi in abis:
            abiRating = self.GetAbisCompareRating(abi=comparingAbi)
            if abiRating > abiMaxRating:
                abiMaxRating = abiRating

        return (archMaxRating + osMaxRating * 2 + osVersionMaxRating * 4 +
         abiMaxRating * 8)
