import os
import os.path
import platform
from vgazer.command     import GetCommandOutputUtf8
from vgazer.exceptions  import AlpineReleaseDataNotFound
from vgazer.exceptions  import DebianReleaseDataNotFound
from vgazer.exceptions  import MissingArgument
from vgazer.exceptions  import OsDataNotFound
from vgazer.exceptions  import UnexpectedOsType
from vgazer.exceptions  import UnknownOs
from vgazer.exceptions  import UnknownTargetArch

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

    if arch in ["i386", "i486", "i586", "i686"]:
        return 32
    elif arch == "x86_64":
        return 64
    else:
        raise UnknownTargetArch(
         "Unknown target architecture: " + arch)

def GetTriplet(targetPlatformData):
    arch = targetPlatformData.GetArch()
    os = targetPlatformData.GetOs()
    abi = targetPlatformData.GetAbi()

    triplet = arch

    if os == "alpine":
        triplet += "-alpine"
    elif Platform.OsIsLinux(os):
        triplet += "-linux"
    elif os == "windows":
        triplet += "-w64"
    else:
        raise UnknownOs("Unknown OS: " + os)

    triplet += "-" + abi

    return triplet

def GetGenericTriplet(targetPlatformData):
    arch = targetPlatformData.GetArch()
    os = targetPlatformData.GetOs()
    abi = targetPlatformData.GetAbi()

    triplet = arch

    if Platform.OsIsLinux(os):
        triplet += "-linux"
    elif os == "windows":
        triplet += "-w64"
    else:
        raise UnknownOs("Unknown OS: " + os)

    triplet += "-" + abi

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

def GetCc(targetPlatformData):
    cc = GetTriplet(targetPlatformData) + "-gcc"
    if "i686" in cc:
        if not os.path.isfile(os.path.join("/usr/bin", cc)):
            cc.replace("i686", "i586")
    if "i586" in cc:
        if not os.path.isfile(os.path.join("/usr/bin", cc)):
            cc.replace("i586", "i486")
    if "i486" in cc:
        if not os.path.isfile(os.path.join("/usr/bin", cc)):
            cc.replace("i486", "i386")
    if os.path.isfile(os.path.join("/usr/bin", cc)):
        return cc
    else:
        return "gcc"

def GetCxx(targetPlatformData):
    return GetCc(targetPlatformData).replace("gcc", "g++")

def GetAr(targetPlatformData):
    triplet = GetTriplet(targetPlatformData)
    if "i686" in triplet:
        if not (os.path.isfile(os.path.join("/usr/bin", triplet + "-ar"))
         and os.path.isfile(os.path.join("/usr/bin", triplet + "-gcc-ar"))):
            triplet.replace("i686", "i586")
    if "i586" in triplet:
        if not (os.path.isfile(os.path.join("/usr/bin", triplet + "-ar"))
         and os.path.isfile(os.path.join("/usr/bin", triplet + "-gcc-ar"))):
            triplet.replace("i586", "i486")
    if "i486" in triplet:
        if not (os.path.isfile(os.path.join("/usr/bin", triplet + "-ar"))
         and os.path.isfile(os.path.join("/usr/bin", triplet + "-gcc-ar"))):
            triplet.replace("i486", "i386")
    if os.path.isfile(os.path.join("/usr/bin", triplet + "-ar")):
        return triplet + "-ar"
    elif os.path.isfile(os.path.join("/usr/bin", triplet + "-gcc-ar")):
        return triplet + "-gcc-ar"
    else:
        return "ar"

def GetArFullPath(targetPlatformData):
    ar = GetAr(targetPlatformData)
    if os.path.isfile(os.path.join("/usr/bin", ar)):
        return os.path.join("/usr/bin", ar)
    else:
        return ar

def GetRanlib(targetPlatformData):
    triplet = GetTriplet(targetPlatformData)
    if "i686" in triplet:
        if not os.path.isfile(
         os.path.join("/usr/bin", triplet + "-ranlib")
        ):
            triplet.replace("i686", "i586")
    if "i586" in triplet:
        if not os.path.isfile(
         os.path.join("/usr/bin", triplet + "-ranlib")
        ):
            triplet.replace("i586", "i486")
    if "i486" in triplet:
        if not os.path.isfile(
         os.path.join("/usr/bin", triplet + "-ranlib")
        ):
            triplet.replace("i486", "i386")
    if os.path.isfile(os.path.join("/usr/bin", triplet + "-ranlib")):
        return triplet + "-ranlib"
    else:
        return "ranlib"

def GetPkgConfig(targetPlatformData):
    triplet = GetTriplet(targetPlatformData)
    if "i686" in triplet:
        if not os.path.isfile(
         os.path.join("/usr/bin", triplet + "-pkg-config")
        ):
            triplet.replace("i686", "i586")
    if "i586" in triplet:
        if not os.path.isfile(
         os.path.join("/usr/bin", triplet + "-pkg-config")
        ):
            triplet.replace("i586", "i486")
    if "i486" in triplet:
        if not os.path.isfile(
         os.path.join("/usr/bin", triplet + "-pkg-config")
        ):
            triplet.replace("i486", "i386")
    if os.path.isfile(os.path.join("/usr/bin", triplet + "-pkg-config")):
        return triplet + "-pkg-config"
    else:
        return "pkg-config"

def GetStrip(targetPlatformData):
    triplet = GetTriplet(targetPlatformData)
    if "i686" in triplet:
        if not os.path.isfile(os.path.join("/usr/bin", triplet + "-strip")):
            triplet.replace("i686", "i586")
    if "i586" in triplet:
        if not os.path.isfile(os.path.join("/usr/bin", triplet + "-strip")):
            triplet.replace("i586", "i486")
    if "i486" in triplet:
        if not os.path.isfile(os.path.join("/usr/bin", triplet + "-strip")):
            triplet.replace("i486", "i386")
    if os.path.isfile(os.path.join("/usr/bin", triplet + "-strip")):
        return triplet + "-strip"
    else:
        return "strip"

def GetLlvmConfig(targetPlatformData):
    if os.path.isfile("/usr/bin/llvm-config"):
        return "/usr/bin/llvm-config"

    for llvmVersion in range(100)[::-1]:
        llvmFilename = "/usr/bin/llvm-config-" + str(llvmVersion)
        if os.path.isfile(llvmFilename):
            return llvmFilename

    return "llvm-config"

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
    def GetLinuxOs():
        osReleaseFile = open("/etc/os-release", "r")
        data = osReleaseFile.read()
        osReleaseFile.close()
        lines = data.splitlines()
        for line in lines:
            kv = line.split("=")
            if kv[0] == "ID":
                return kv[1]
        raise OsDataNotFound("Unable to find data of host OS: " + os.name)

    @staticmethod
    def GetDebianVersion():
        osReleaseFile = open("/etc/os-release", "r")
        data = osReleaseFile.read()
        osReleaseFile.close()
        lines = data.splitlines()
        for line in lines:
            kv = line.split("=")
            if kv[0] == "VERSION":
                return kv[1].split("(")[1][:-2:]
        raise DebianReleaseDataNotFound(
         "Unable to find data of Debian version: " + os.name)

    @staticmethod
    def GetAlpineVersion():
        osReleaseFile = open("/etc/os-release", "r")
        data = osReleaseFile.read()
        osReleaseFile.close()
        lines = data.splitlines()
        for line in lines:
            kv = line.split("=")
            if kv[0] == "VERSION_ID":
                return ".".join(kv[1].split(".")[0:2])
        raise AlpineReleaseDataNotFound(
         "Unable to find data of Alpine version: " + os.name)

    @staticmethod
    def OsIsLinux(os):
        return (os in ["linux", "alpine", "debian", "steamrt"])

    @staticmethod
    def GetGenericOs(os):
        if Platform.OsIsLinux(os):
            return "linux"
        elif os == "windows":
            return "windows"
        elif os == "any":
            return "any"
        else:
            raise UnknownOs("Unknown OS: " + os)

    def __init__(self, arch=None, os=None, osVersion=None, abi=None,
     suppressGenericFallback=False):
        if (arch is None or os is None or osVersion is None or abi is None):
            self.host = True
        else:
            self.host = False

        if self.host:
            self.arch = platform.machine()
            osType = platform.system()
            if osType == "Linux":
                self.os = Platform.GetLinuxOs()
                if self.os == "alpine":
                    self.osVersion = Platform.GetAlpineVersion()
                    self.abi = "musl"
                if self.os == "debian":
                    self.osVersion = Platform.GetDebianVersion()
                    self.abi = "gnu"
                if self.os == "steamrt":
                    self.osVersion = "latest"
                    self.abi = "gnu"
            else:
                raise UnexpectedOsType("Unexpected OS type: " + osType)
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
        if (
         (self.arch == "i686" and comparingArch in ["i586", "i486", "i386"])
         or (self.arch == "i586" and comparingArch in ["i486", "i386"])
         or (self.arch == "i486" and comparingArch == "i386")
        ):
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
