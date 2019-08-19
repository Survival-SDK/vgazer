import os
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

    triplet = arch

    if os == "linux":
        triplet += "-linux-gnu"
    elif os == "windows":
        triplet += "-w64-mingw32"

    return triplet

def GetInstallPrefix(platformData):
    if platformData["target"].PlatformsEqual(platformData["host"]):
        return "/usr/local"
    else:
        return ("/usr/local/" + GetTriplet(platformData["target"]))

def GetCc(targetPlatformData):
    return GetTriplet(targetPlatformData) + "-gcc"

def GetAr(targetPlatformData):
    return GetTriplet(targetPlatformData) + "-ar"

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
    def OsIsLinux(os):
        if os == "linux" or os == "debian":
            return True
        else:
            return False

    @staticmethod
    def GetGenericOs(os):
        if os in ["linux", "debian"]:
            return "linux"
        else:
            raise UnknownOs("Unknown OS: " + os)

    def __init__(self, arch = None, os = None, osVersion = None, compiler = None):
        if (arch is None or os is None or osVersion is None or compiler is None):
            self.host = True
        else:
            self.host = False

        if self.host:
            self.arch = platform.machine()
            osType = platform.system()
            if osType == "Linux":
                self.os = Platform.GetLinuxOs()
                if self.os == "debian":
                    self.osVersion = Platform.GetDebianVersion()
            else:
                raise UnexpectedOsType("Unexpected OS type: " + osType)
            self.compiler = "gcc"
        else:
            self.arch = arch
            self.os = Platform.GetGenericOs(os) #os
            self.osVersion = "any" #osVersion
            self.compiler = compiler

    def GetArch(self):
        return self.arch

    def GetOs(self):
        return self.os

    def GetOsVersion(self):
        return self.osVersion

    def GetCompiler(self):
        return self.compiler

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

    def CompilersCompatible(self, platform = None, compiler = None):
        if platform is None:
            if compiler is None:
                raise MissingArgument("Missing value for argument 'compiler'")
            comparingCompiler = compiler
        else:
            comparingCompiler = platform.compiler
        if self.compiler == "any" or comparingCompiler == "any":
            return True
        if self.compiler == comparingCompiler:
            return True
        return False

    def CompilersEqual(self, platform = None, compiler = None):
        if platform is None:
            if compiler is None:
                raise MissingArgument("Missing value for argument 'compiler'")
            comparingCompiler = compiler
        else:
            comparingCompiler = platform.compiler
        if (self.compiler == comparingCompiler and self.compiler != "any" and
         comparingCompiler != "any"):
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

    def GetCompilersCompareRating(self, platform = None, compiler = None):
        if platform is None:
            if compiler is None:
                raise MissingArgument("Missing value for argument 'compiler'")
            comparingCompiler = compiler
        else:
            comparingCompiler = platform.compiler
        if self.CompilersEqual(compiler = comparingCompiler):
            return Platform.COMP_EQUAL
        elif self.CompilersCompatible(compiler = comparingCompiler):
            return Platform.COMP_COMPATIBLE
        else:
            return Platform.COMP_INCOMPATIBLE

    def PlatformsEqual(self, platform):
        return (self.ArchsEqual(platform) and self.OsesEqual(platform)
         and self.OsVersionsEqual(platform) and self.CompilersEqual(platform))

    def GetCompatibilityRating(self, archs, oses, osVersions, compilers):
        archMaxRating = Platform.COMP_INCOMPATIBLE
        osMaxRating = Platform.COMP_INCOMPATIBLE
        osVersionMaxRating = Platform.COMP_INCOMPATIBLE
        compilerMaxRating = Platform.COMP_INCOMPATIBLE
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
        for comparingCompiler in compilers:
            compilerRating = self.GetCompilersCompareRating(
             compiler = comparingCompiler)
            if compilerRating > compilerMaxRating:
                compilerMaxRating = compilerRating

        return (archMaxRating + osMaxRating * 2 + osVersionMaxRating * 4 +
         compilerMaxRating * 8)
