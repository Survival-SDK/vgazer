import os
import platform

from libvgazer.exceptions import DebianReleaseDataNotFound
from libvgazer.exceptions import OsDataNotFound
from libvgazer.os_release import OsRelease

class HostDetector:
    @staticmethod
    def GetLinuxOs():
        with OsRelease() as osRelease:
            try:
                return osRelease.GetEntry("ID")
            except KeyError:
                raise OsDataNotFound(
                 "Unable to find data of host OS: " + os.name)

    @staticmethod
    def GetDebianVersion():
        with OsRelease() as osRelease:
            try:
                return osRelease.GetEntry("VERSION").split("(")[1][:-2:]
            except KeyError:
                raise DebianReleaseDataNotFound(
                 "Unable to find data of Debian version: " + os.name)

    def __init__(self):
        self.unknownOs = False
        self.errorMsg = "No error"
        self.arch = platform.machine()
        osType = platform.system()
        if osType == "Linux":
            self.os = HostDetector.GetLinuxOs()
            if self.os == "debian":
                self.osVersion = HostDetector.GetDebianVersion()
                self.abi = "gnu"
            if self.os == "steamrt":
                self.osVersion = "latest"
                self.abi = "gnu"
        else:
            self.unknownOs = True
            self.errorMsg = "Unexpected OS type: " + osType

    def __enter__(self):
        return self

    def __exit__(self, etype, value, traceback):
        pass

    def OsIsUnknown(self):
        return self.unknownOs

    def GetErrorMsg(self):
        return self.errorMsg

    def GetArch(self):
        return self.arch

    def GetOs(self):
        return self.os

    def GetOsVersion(self):
        return self.osVersion

    def GetAbi(self):
        return self.abi
