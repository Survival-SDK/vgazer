from vgazer.auth.base               import AuthBase
from vgazer.auth.github             import AuthGithub
from vgazer.config.software         import ConfigSoftware
from vgazer.exceptions              import CompatibleProjectNotFound
from vgazer.exceptions              import DebianPackageUnavailable
from vgazer.exceptions              import InstallError
from vgazer.exceptions              import UnknownSoftware
from vgazer.exceptions              import VersionCheckError
from vgazer.install.custom          import InstallCustom
from vgazer.install.apk             import InstallApk
from vgazer.install.apt             import InstallApt
from vgazer.install.gcc_src         import InstallGccSrc
from vgazer.install.musl_cross_make import InstallMuslCrossMake
from vgazer.install.pip             import InstallPip
from vgazer.install.pip3            import InstallPip3
from vgazer.install.stb             import InstallStb
from vgazer.mirrors.gnu             import MirrorsGnu
from vgazer.platform                import GetGenericTriplet
from vgazer.platform                import Platform
from vgazer.version.custom          import VersionCustom
from vgazer.version.alpine          import CheckAlpine
from vgazer.version.debian          import CheckDebian
from vgazer.version.gcc_src         import CheckGccSrc
from vgazer.version.github          import CheckGithub
from vgazer.version.musl_cross_make import CheckMuslCrossMake
from vgazer.version.pypi            import CheckPypi
from vgazer.version.sourceforge     import CheckSourceforge
from vgazer.version.stb             import CheckStb
from vgazer.version.xiph            import CheckXiph

class Vgazer:
    def __init__(self, arch = None, os = None, osVersion = None,
     abi = None, customCheckers = {}, customInstallers = {},
     customSoftwareData = {}, supportOnly = False):
        if not supportOnly:
            self.auth = {
                "base": AuthBase(),
                "github": AuthGithub(),
            }
            self.versionCustom = VersionCustom(self.auth["base"],
             customCheckers)
            self.mirrors = {
                "gnu": MirrorsGnu()
            }
            self.installCustom = InstallCustom(customInstallers)
            self.installedSoftware = []
        self.configSoftware = ConfigSoftware(customSoftwareData)
        self.platform = {
            "host":   Platform(),
            "target": Platform(arch, os, osVersion, abi),
        }

    def GetHostPlatform(self):
        return self.platform["host"]

    def GetTargetPlatform(self):
        return self.platform["target"]

    def GetSoftwareData(self):
        return self.configSoftware

    def ChooseProject(self, projects, platform):
        maxRatingProject = None
        maxRating = Platform.COMP_INCOMPATIBLE
        for project in projects:
            projectRating = platform.GetCompatibilityRating(project["arch"],
             project["os"], project["osVersion"], project["abi"])
            if projectRating > maxRating:
                maxRating = projectRating
                maxRatingProject = project
        if maxRating >= Platform.COMP_COMPATIBLE:
            return maxRatingProject
        else:
            return None

    def UseChecker(self, software, checker):
        softwareData = self.configSoftware.GetData()
        softwarePlatform = softwareData[software]["platform"]

        try:
            if checker["type"] == "alpine":
                return CheckAlpine(self.auth["base"],
                 self.platform[softwarePlatform].GetArch(),
                 self.platform[softwarePlatform].GetOsVersion(),
                 checker["repo"], checker["package"])
            elif checker["type"] == "debian":
                return CheckDebian(self.auth["base"],
                 self.platform[softwarePlatform].GetOsVersion(), checker["source"])
            elif checker["type"] == "gcc-src":
                return CheckGccSrc(self.auth["base"])
            elif checker["type"] == "github":
                return CheckGithub(self.auth["github"], checker["user"],
                 checker["repo"], "ignoreReleases" in checker)
            elif checker["type"] == "musl-cross-make":
                return CheckMuslCrossMake(self.auth["github"])
            elif checker["type"] == "pypi":
                return CheckPypi(self.auth["base"], checker["package"])
            elif checker["type"] == "sourceforge":
                return CheckSourceforge(self.auth["base"], checker["project"])
            elif checker["type"] == "stb":
                return CheckStb(self.auth["base"], checker["library"])
            elif checker["type"] == "xiph":
                return CheckXiph(self.auth["base"], checker["project"])
            elif checker["type"] == "custom":
                return self.versionCustom.Check(checker["name"])
        except VersionCheckError as versionCheckError:
            if "fallback" in checker:
                return self.UseChecker(software, checker["fallback"])
            else:
                raise versionCheckError

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
             "Unable to find compatible project for software: " + software)

        checker = project["checker"]

        return self.UseChecker(software, checker)

    def UseInstaller(self, software, installer, verbose,
     fallbackPreinstallList):
        softwareData = self.configSoftware.GetData()
        softwarePlatform = softwareData[software]["platform"]

        if software in self.installedSoftware:
            return

        try:
            if installer["type"] == "apk":
                InstallApk(software, installer["package"], verbose)
            elif installer["type"] == "apt":
                InstallApt(software, installer["package"], verbose)
            elif installer["type"] == "custom":
                self.installCustom.Install(self.auth, software,
                 installer["name"], softwarePlatform, self.platform, verbose)
            elif installer["type"] == "gcc-src":
                InstallGccSrc(self.auth["base"], software,
                 installer["languages"], installer["triplet"], self.platform,
                 self.mirrors["gnu"], verbose)
            elif installer["type"] == "musl-cross-make":
                InstallMuslCrossMake(self.auth["github"], software,
                 installer["languages"], installer["triplet"], self.platform,
                 verbose)
            elif installer["type"] == "pip":
                InstallPip(software, installer["package"], verbose)
            elif installer["type"] == "pip3":
                InstallPip3(software, installer["package"], verbose)
            elif installer["type"] == "stb":
                InstallStb(installer["library"], self.platform, verbose)
        except InstallError as installError:
            if "fallback" in installer:
                print("VGAZER: Trying fallback installation steps")
                if fallbackPreinstallList is not None:
                    self.InstallList(fallbackPreinstallList, verbose)
                self.UseInstaller(software, installer["fallback"], verbose,
                 None)
            else:
                raise installError
        self.installedSoftware.append(software)

    def Install(self, software, verbose = False, fallbackPreinstallList = None):
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

        if "prereqs" in project:
            prereqs = project["prereqs"]
        else:
            prereqs = []

        if "fallback_prereqs" in project:
            fallback_prereqs = project["fallback_prereqs"]
        else:
            fallback_prereqs = []

        for prereq in prereqs:
            prereq = prereq.format(
             triplet=GetGenericTriplet(self.platform["target"]),
             arch=self.platform["target"].GetArch())
            self.Install(prereq, verbose, None)
        for fallback_prereq in fallback_prereqs:
            prereq = fallback_prereq.format(
             triplet=GetGenericTriplet(self.platform["target"]),
             arch=self.platform["target"].GetArch())

        installer = project["installer"]

        self.UseInstaller(software, installer, verbose, fallback_prereqs)

    def InstallList(self, softwareList, verbose = False):
        for software in softwareList:
            self.Install(software, verbose, None)
