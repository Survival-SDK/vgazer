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
from vgazer.exceptions          import CompatibleProjectNotFound
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
        self.platform = {}
        self.platform["host"] = self.hostPlatform
        self.platform["target"] = self.targetPlatform
        self.versionCustom = VersionCustom(self.authBase, customCheckers)
        self.installCustom = InstallCustom(customInstallers)

    def ChooseProject(self, projects, platform):
        maxRatingProject = None
        maxRating = Platform.COMP_INCOMPATIBLE
        for project in projects:
            projectRating = platform.GetCompatibilityRating(project["arch"],
             project["os"], project["osVersion"], project["compiler"])
            if projectRating > maxRating:
                maxRating = projectRating
                maxRatingProject = project
        if maxRating >= Platform.COMP_COMPATIBLE:
            return maxRatingProject
        else:
            return None

    def CheckVersion(self, software):
        softwareData = self.configSoftware.GetData()
        if software not in softwareData:
            raise UnknownSoftware("Unknown software: " + software)

        softwarePlatform = softwareData[software]["platform"]
        softwareProjects = softwareData[software]["projects"]
        project = self.ChooseProject(softwareProjects,
         self.platform[softwarePlatform])
        if project is None:
            raise CompatibleProjectNotFound(
             "Unable to find compatible project for sowtware: " + software)

        checker = project["checker"]
        if checker["type"] == "github":
            if "ignoreReleases" in checker:
                ignoreReleases = True
            else:
                ignoreReleases = False
            return CheckGithub(self.authGithub, checker["user"],
             checker["repo"], ignoreReleases)
        elif checker["type"] == "sourceforge":
            return CheckSourceforge(self.authBase, checker["project"])
        elif checker["type"] == "xiph":
            return CheckXiph(self.authBase, checker["project"])
        elif checker["type"] == "debian":
            return CheckDebian(self.authBase,
             self.platform[softwarePlatform].GetOsVersion(), checker["source"])
        elif checker["type"] == "custom":
            return self.versionCustom.Check(checker["name"])

    #def InstallCustom(self, software, verbose):
        #softwareData = self.configSoftware.GetData()
        #self.installCustom.Install(software, softwareData[software],
         #self.hostPlatform, self.targetPlatform, verbose)

    #def InstallDebian(self, software, debianVersion, verbose):
        #softwareData = self.configSoftware.GetData()
        #projects = softwareData[software]["projects"]
        #if "debian" not in projects:
            #return self.InstallCustom(software, verbose)
        #try:
            #return InstallDebian(software, debianVersion, projects["debian"],
             #verbose)
        #except DebianPackageUnavailable:
            #return self.InstallCustom(software, verbose)

    def Install(self, software, verbose = False):
        #crossplatform = not self.targetPlatform.PlatformsEqual(
         #self.hostPlatform)
        #softwareData = self.configSoftware.GetData()
        #if software not in softwareData:
            #raise UnknownSoftware("Unknown software: " + software)

        #if crossplatform:
            #return self.InstallCustom(software, verbose)
        #elif self.targetPlatform.GetOs() == "debian":
            #return self.InstallDebian(software,
             #self.targetPlatform.GetOsVersion(), verbose)

        softwareData = self.configSoftware.GetData()
        if software not in softwareData:
            raise UnknownSoftware("Unknown software: " + software)

        softwarePlatform = softwareData[software]["platform"]
        softwareProjects = softwareData[software]["projects"]
        project = self.ChooseProject(softwareProjects,
         self.platform[softwarePlatform])
        if project is None:
            raise CompatibleProjectNotFound(
             "Unable to find compatible project for sowtware: " + software)

        installer = project["installer"]
        if installer["type"] == "debian":
            return InstallDebian(software, installer["package"], verbose)
        elif installer["type"] == "custom":
            return self.installCustom.Install(software, installer["name"],
             softwarePlatform, self.hostPlatform, self.targetPlatform, verbose)
