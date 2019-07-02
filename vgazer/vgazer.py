from vgazer.auth.base               import AuthBase
from vgazer.auth.github             import AuthGithub
from vgazer.config.software         import ConfigSoftware
from vgazer.platform                import Platform
from vgazer.version.custom          import VersionCustom
from vgazer.version.github          import CheckGithub
from vgazer.version.sourceforge     import CheckSourceforge
from vgazer.version.xiph            import CheckXiph
from vgazer.version.debian          import CheckDebian
from vgazer.version.debian          import InstallCustom
from vgazer.install.debian      import InstallDebian
from vgazer.exceptions          import DebianPackageUnavailable
from vgazer.exceptions          import UnknownSoftware

class Vgazer:
    def __init__(self, arch = None, os = None, osVersion = None,
     compiler = None, customSoftwareData = {}):
        self.authBase = AuthBase()
        self.authGithub = AuthGithub()
        self.configSoftware = ConfigSoftware(customSoftwareData)
        self.hostPlatform = Platform()
        self.targetPlatform = Platform(arch, os, osVersion, compiler)
        self.versionCustom = VersionCustom(self.authBase, customCheckers)

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
            raise GithubApiRateLimitExceeded("Unknown software: " + software)

        if crossplatform:
            return self.CheckVersionCrossplatform(software)
        elif self.targetPlatform.GetOs() == "debian":
            return self.CheckVersionDebian(software,
             self.targetPlatform.GetOsVersion())

    #def AddGithubProjectsData(self, data):
        #self.configGithubProjects.AddData(data)

    #def AddSoftwareData(self, data):
        #self.ConfigSoftware.AddData(data)

