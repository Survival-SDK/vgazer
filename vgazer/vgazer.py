from vgazer.auth.base           import AuthBase
from vgazer.auth.github         import AuthGithub
from vgazer.config.software     import ConfigSoftware
from vgazer.platform            import Platform
from vgazer.version.custom      import VersionCustom
from vgazer.version.github      import CheckGithub
from vgazer.version.sourceforge import CheckSourceforge
from vgazer.version.xiph        import CheckXiph
from vgazer.version.debian      import CheckDebian
from vgazer.install.custom      import InstallCustom
from vgazer.install.debian      import InstallDebian
from vgazer.exceptions          import DebianPackageUnavailable
from vgazer.exceptions          import UnknownSoftware

class Vgazer:
    def __init__(self, arch = None, os = None, osVersion = None,
     compiler = None, customCheckers = {}, customInstallers = {},
     customSoftwareData = {}):
        self.authBase = AuthBase()
        self.authGithub = AuthGithub()
        self.configSoftware = ConfigSoftware(customSoftwareData)
        self.hostPlatform = Platform()
        self.targetPlatform = Platform(arch, os, osVersion, compiler)
        self.versionCustom = VersionCustom(self.authBase, customCheckers)
        self.installCustom = InstallCustom(customInstallers)

    def CheckVersionCrossplatform(self, software):
        softwareData = self.configSoftware.GetData()
        projects = softwareData[software]["projects"]
        if "github" in projects:
            return CheckGithub(self.authGithub, projects["github"])
        elif "sourceforge" in projects:
            return CheckSourceforge(self.authBase, projects["sourceforge"])
        elif "xiph" in projects:
            return CheckXiph(self.authBase, projects["xiph"])
        elif "custom" in projects:
            return self.versionCustom.Check(projects["custom"])

    def CheckVersionDebian(self, software, debianVersion):
        softwareData = self.configSoftware.GetData()
        projects = softwareData[software]["projects"]
        if "debian" not in projects:
            return self.CheckVersionCrossplatform(software)
        try:
            return CheckDebian(self.authBase, debianVersion, projects["debian"])
        except DebianPackageUnavailable:
            return self.CheckVersionCrossplatform(software)

    def CheckVersion(self, software):
        crossplatform = not self.targetPlatform.PlatformsEqual(
         self.hostPlatform)
        softwareData = self.configSoftware.GetData()
        if software not in softwareData:
            raise UnknownSoftware("Unknown software: " + software)

        if crossplatform:
            return self.CheckVersionCrossplatform(software)
        elif self.targetPlatform.GetOs() == "debian":
            return self.CheckVersionDebian(software,
             self.targetPlatform.GetOsVersion())

    def InstallCustom(self, software, verbose):
        softwareData = self.configSoftware.GetData()
        self.installCustom.Install(software, softwareData[software],
         self.hostPlatform, self.targetPlatform, verbose)

    def InstallDebian(self, software, debianVersion, verbose):
        softwareData = self.configSoftware.GetData()
        projects = softwareData[software]["projects"]
        if "debian" not in projects:
            return self.InstallCustom(software, verbose)
        try:
            return InstallDebian(software, debianVersion, projects["debian"],
             verbose)
        except DebianPackageUnavailable:
            return self.InstallCustom(software, verbose)

    def Install(self, software, verbose = False):
        crossplatform = not self.targetPlatform.PlatformsEqual(
         self.hostPlatform)
        softwareData = self.configSoftware.GetData()
        if software not in softwareData:
            raise UnknownSoftware("Unknown software: " + software)

        if crossplatform:
            return self.InstallCustom(software, verbose)
        elif self.targetPlatform.GetOs() == "debian":
            return self.InstallDebian(software,
             self.targetPlatform.GetOsVersion(), verbose)
