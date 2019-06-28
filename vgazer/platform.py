import os
import platform

class UnexpectedOsType(Exception):
    def __init__(self, message):
        super().__init__(message)

class OsDataNotFound(Exception):
    def __init__(self, message):
        super().__init__(message)

class DebianReleaseDataNotFound(Exception):
    def __init__(self, message):
        super().__init__(message)

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

class Platform:
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

    def __init__(self, arch = None, os = None, version = None, compiler = None):
        if (arch is None or os is None or version is None or compiler is None):
            self.host = True
        else:
            self.host = False

        if self.host:
            self.arch = platform.machine()
            osType = platform.system()
            if osType == "Linux":
                self.os = Platform.GetLinuxOs()
                if self.os == "debian":
                    self.version = Platform.GetDebianVersion()
            else:
                raise UnexpectedOsType("Unexpected OS type: " + osType)
            self.compiler = "gcc"
        else:
            self.arch = arch
            self.os = os
            self.version = version
            self.compiler = compiler

    def GetArch(self):
        return self.arch

    def GetOs(self):
        return self.os

    def GetOsVersion(self):
        return self.version

    def GetCompiler(self):
        return self.compiler

    def PlatformsEqual(self, platform):
        return (self.arch == platform.arch and self.os == platform.os
         and self.version == platform.version
         and self.compiler == platform.compiler)
