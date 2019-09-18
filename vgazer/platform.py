import os
import os.path
import platform
from vgazer.exceptions import DebianReleaseDataNotFound
from vgazer.exceptions import MissingArgument
from vgazer.exceptions import OsDataNotFound
from vgazer.exceptions import UnexpectedOsType
from vgazer.exceptions import UnknownOs
from vgazer.exceptions import UnknownPlatform

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

def GetTriplet(targetPlatformData):
    arch = targetPlatformData.GetArch()
    os = targetPlatformData.GetOs()
    abi = targetPlatformData.GetAbi()

    triplet = arch

    if os == "alpine":
        triplet += "-alpine"

    if Platform.OsIsLinux(os):
        triplet += "-linux"
    elif os == "windows":
        triplet += "-w64"

    triplet += "-" + abi

    return triplet

def GetInstallPrefix(platformData):
    if platformData["target"].PlatformsEqual(platformData["host"]):
        return "/usr/local"
    else:
        return ("/usr/local/" + GetTriplet(platformData["target"]))

def GetCc(targetPlatformData):
    if (targetPlatformData.GetOs() == "debian"
     and targetPlatformData.GetAbi() == "musl"):
        return "musl-gcc"
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
    return cc

def GetAr(targetPlatformData):
    if (targetPlatformData.GetOs() == "debian"
     and targetPlatformData.GetAbi() == "musl"):
        return "ar"
    ar = GetTriplet(targetPlatformData) + "-ar"
    if "i686" in ar:
        if not os.path.isfile(os.path.join("/usr/bin", ar)):
            ar.replace("i686", "i586")
    if "i586" in ar:
        if not os.path.isfile(os.path.join("/usr/bin", ar)):
            ar.replace("i586", "i486")
    if "i486" in ar:
        if not os.path.isfile(os.path.join("/usr/bin", ar)):
            ar.replace("i486", "i386")
    return ar

class Platform:
    # Platforms comparing ratings
    COMP_INCOMPATIBLE   = -1000
    COMP_COMPATIBLE     =  0
    COMP_EQUAL          =  1

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
        raise DebianReleaseDataNotFound(
         "Unable to find data of Debian version: " + os.name)

    @staticmethod
    def OsIsLinux(os):
        return (os in ["linux", "alpine", "debian"])

    @staticmethod
    def GetGenericOs(os):
        if Platform.OsIsLinux(os):
            return "linux"
        elif os == "any":
            return "any"
        else:
            raise UnknownOs("Unknown OS: " + os)

    def __init__(self, arch = None, os = None, osVersion = None, abi = None,
     suppressGenericFallback = False):
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

    def ArchsCompatible(self, platform = None, arch = None):
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
         (self.arch == "i686" and (comparingArch == "i586"
          or comparingArch == "i486" or comparingArch == "i386")
         )
         or (self.arch == "i586" and (comparingArch == "i486"
          or comparingArch == "i386")
         )
         or (self.arch == "i486" and comparingArch == "i386")
        ):
            return True
        return False

    def ArchsEqual(self, platform = None, arch = None):
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

    def OsesCompatible(self, platform = None, os = None):
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

    def OsesEqual(self, platform = None, os = None):
        if platform is None:
            if os is None:
                raise MissingArgument("Missing value for argument 'os'")
            comparingOs = os
        else:
            comparingOs = platform.os
        if self.os == comparingOs and self.os != "any" and comparingOs != "any":
            return True
        return False

    def OsVersionsCompatible(self, platform = None, osVersion = None):
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

    def OsVersionsEqual(self, platform = None, osVersion = None):
        if platform is None:
            if osVersion is None:
                raise MissingArgument("Missing value for argument 'osVersion'")
            comparingOsVersion = osVersion
        else:
            comparingOsVersion = platform.osVersion
        if (self.osVersion == comparingOsVersion and self.osVersion != "any" and
         comparingOsVersion != "any"):
            return True
        return False

    def AbisCompatible(self, platform = None, abi = None):
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

    def AbisEqual(self, platform = None, abi = None):
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

    def GetArchsCompareRating(self, platform = None, arch = None):
        if platform is None:
            if arch is None:
                raise MissingArgument("Missing value for argument 'arch'")
            comparingArch = arch
        else:
            comparingArch = platform.arch
        if self.ArchsEqual(arch = comparingArch):
            return Platform.COMP_EQUAL
        elif self.ArchsCompatible(arch = comparingArch):
            return Platform.COMP_COMPATIBLE
        else:
            return Platform.COMP_INCOMPATIBLE

    def GetOsesCompareRating(self, platform = None, os = None):
        if platform is None:
            if os is None:
                raise MissingArgument("Missing value for argument 'os'")
            comparingOs = os
        else:
            comparingOs = platform.os
        if self.OsesEqual(os = comparingOs):
            return Platform.COMP_EQUAL
        elif self.OsesCompatible(os = comparingOs):
            return Platform.COMP_COMPATIBLE
        else:
            return Platform.COMP_INCOMPATIBLE

    def GetOsVersionsCompareRating(self, platform = None, osVersion = None):
        if platform is None:
            if osVersion is None:
                raise MissingArgument("Missing value for argument 'osVersion'")
            comparingOsVersion = osVersion
        else:
            comparingOsVersion = platform.osVersion
        if self.OsVersionsEqual(osVersion = comparingOsVersion):
            return Platform.COMP_EQUAL
        elif self.OsVersionsCompatible(osVersion = comparingOsVersion):
            return Platform.COMP_COMPATIBLE
        else:
            return Platform.COMP_INCOMPATIBLE

    def GetAbisCompareRating(self, platform = None, abi = None):
        if platform is None:
            if abi is None:
                raise MissingArgument("Missing value for argument 'abi'")
            comparingAbi = abi
        else:
            comparingAbi = platform.abi
        if self.AbisEqual(abi = comparingAbi):
            return Platform.COMP_EQUAL
        elif self.AbisCompatible(abi = comparingAbi):
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
            archRating = self.GetArchsCompareRating(arch = comparingArch)
            if archRating > archMaxRating:
                archMaxRating = archRating
        for comparingOs in oses:
            osRating = self.GetOsesCompareRating(os = comparingOs)
            if osRating > osMaxRating:
                osMaxRating = osRating
        for comparingOsVersion in osVersions:
            osVersionRating = self.GetOsVersionsCompareRating(
             osVersion = comparingOsVersion)
            if osVersionRating > osVersionMaxRating:
                osVersionMaxRating = osVersionRating
        for comparingAbi in abis:
            abiRating = self.GetAbisCompareRating(
             abi = comparingAbi)
            if abiRating > abiMaxRating:
                abiMaxRating = abiRating

        return (archMaxRating + osMaxRating * 2 + osVersionMaxRating * 4 +
         abiMaxRating * 8)
