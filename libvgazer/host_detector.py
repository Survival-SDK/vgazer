import os
import platform

from libvgazer.exceptions import OsDataNotFound
from libvgazer.exceptions import ReleaseDataNotFound
from libvgazer.exceptions import UnknownOsVersion
from libvgazer.os_release import OsRelease

class HostDetector:
    @staticmethod
    def GetLinuxOs():
        with OsRelease() as osRelease:
            try:
                return {
                    "arch":   "archlinux",
                    "ol":     "oraclelinux",
                    "debian": "debian",
                }[osRelease.GetEntry("ID")]
            except KeyError:
                raise OsDataNotFound(
                 "Unable to find data of host OS: " + os.name)

    @staticmethod
    def GetOracleLinuxVersion():
        with OsRelease() as osRelease:
            try:
                return osRelease.GetEntry("VERSION").strip("\"").split(".")[0]
            except KeyError:
                raise ReleaseDataNotFound(
                 "Unable to find data of Debian version: " + os.name)

    @staticmethod
    def GetDebianVersion():
        with OsRelease() as osRelease:
            try:
                return osRelease.GetEntry("VERSION").split("(")[1][:-2:]
            except KeyError:
                raise ReleaseDataNotFound(
                 "Unable to find data of Debian version: " + os.name)

    @staticmethod
    def GetSteamRtVersion():
        # TODO
        # May be reference - https://gitlab.steamos.cloud/steamrt/steam-runtime-tools/-/blob/main/docs/distro-assumptions.md#environment-variables
        raise UnknownOsVersion(
                 "Unable to detect version of Steam Runtime")

    def __init__(self):
        self.unknownOs = False
        self.errorMsg = "No error"
        self.arch = platform.machine()
        osType = platform.system()
        if osType == "Linux":
            # TODO steamrt not being detected by HostDetector.GetLinuxOs()
            self.os = HostDetector.GetLinuxOs()
            if self.os == "archlinux":
                self.osVersion = "latest"
                self.abi = "gnu"
            if self.os == "oraclelinux":
                self.osVersion = HostDetector.GetOracleLinuxVersion()
                self.abi = "gnu"
            if self.os == "debian":
                self.osVersion = HostDetector.GetDebianVersion()
                self.abi = "gnu"
            if self.os == "steamrt":
                self.osVersion = HostDetector.GetSteamRtVersion()
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
