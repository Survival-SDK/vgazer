from vgazer.auth.base               import AuthBase
from vgazer.auth.github             import AuthGithub
from vgazer.checkers_manager        import CheckersManager
from vgazer.exceptions              import CompatibleProjectNotFound
from vgazer.exceptions              import InstallError
from vgazer.exceptions              import UnknownSoftware
from vgazer.exceptions              import VersionCheckError
from vgazer.install.custom          import InstallCustom
from vgazer.installers_manager      import InstallersManager
from vgazer.mirrors.gnu             import MirrorsGnu
from vgazer.mirrors.sourceforge     import MirrorsSourceforge
from vgazer.mirrors.xorg            import MirrorsXorg
from vgazer.platform                import GetGenericTriplet
from vgazer.platform                import Platform
from vgazer.software                import SoftwareData
from vgazer.version.custom          import VersionCustom

class Vgazer:
    def __init__(self, arch=None, os=None, osVersion=None, abi=None,
     customCheckers={}, customInstallers={}, customSoftwareData={},
     supportOnly=False):
        if not supportOnly:
            self.auth = {
                "base": AuthBase(),
                "github": AuthGithub(),
            }
            self.versionCustom = VersionCustom(self.auth["base"],
             customCheckers)
            self.checkersManager = CheckersManager()
            self.installersManager = InstallersManager()
            self.mirrors = {
                "gnu": MirrorsGnu(),
                "sourceforge": MirrorsSourceforge(),
                "xorg": MirrorsXorg(),
            }
            self.installCustom = InstallCustom(customInstallers)
            self.installedSoftware = []
        self.softwareData = SoftwareData(customSoftwareData)
        self.platform = {
            "host":   Platform(),
            "target": Platform(arch, os, osVersion, abi),
        }

    def GetHostPlatform(self):
        return self.platform["host"]

    def GetTargetPlatform(self):
        return self.platform["target"]

    def GetSoftwareData(self):
        return self.softwareData

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

    def SearchFallbackProject(self, projects):
        for project in projects:
            if "fallback" in project:
                return project;

        return None;

    def UseChecker(self, software, checker):
        softwareData = self.softwareData.GetData()
        softwarePlatform = softwareData[software]["platform"]

        try:
            if checker["type"] == "custom":
                return self.versionCustom.Check(checker["name"], self.mirrors)
            else:
                checkFunc = self.checkersManager.GetCheckFunc(checker["type"])
                return checkFunc(self.auth, self.platform[softwarePlatform],
                 checker)

        except VersionCheckError as versionCheckError:
            if "fallback" in checker:
                return self.UseChecker(software, checker["fallback"])
            else:
                raise versionCheckError

    def CheckVersion(self, software):
        softwareData = self.softwareData.GetData()
        if software not in softwareData:
            raise UnknownSoftware("Unknown software: {software}".format(
             software=software))

        softwarePlatform = softwareData[software]["platform"]
        softwareProjects = softwareData[software]["projects"]
        project = self.ChooseProject(softwareProjects,
         self.platform[softwarePlatform])
        if project is None:
            raise CompatibleProjectNotFound(
             "Unable to find compatible project for software: "
             "{software}".format(software=software))

        checker = project["checker"]

        return self.UseChecker(software, checker)

    def UseInstaller(self, software, installer, verbose,
     fallbackPreinstallList):
        softwareData = self.softwareData.GetData()
        softwarePlatform = softwareData[software]["platform"]

        if software in self.installedSoftware:
            return

        try:
            if installer["type"] == "custom":
                self.installCustom.Install(self.auth, software,
                 installer["name"], softwarePlatform, self.platform,
                 self.mirrors, verbose)
            else:
                installFunc = self.installersManager.GetInstallFunc(
                 installer["type"])
                installFunc(software, self.auth, self.platform,
                 installer, self.mirrors, verbose)
            self.installedSoftware.append(software)
        except InstallError as installError:
            if "fallback" in installer:
                print(
                 "VGAZER: Something went wrong. Starting fallback "
                 "installation steps"
                )
                if fallbackPreinstallList is not None:
                    self.InstallList(fallbackPreinstallList, verbose)
                self.UseInstaller(software, installer["fallback"], verbose,
                 None)
            else:
                raise installError

    def Install(self, software, verbose=False, fallbackPreinstallList=None):
        if software in self.installedSoftware:
            return

        softwareData = self.softwareData.GetData()
        if software not in softwareData:
            raise UnknownSoftware("Unknown software: " + software)

        softwarePlatform = softwareData[software]["platform"]
        softwareProjects = softwareData[software]["projects"]
        project = self.ChooseProject(softwareProjects,
         self.platform[softwarePlatform])
        if project is None:
            raise CompatibleProjectNotFound(
             "Unable to find compatible project for software: " + software)

        prereqs = project["prereqs"] if "prereqs" in project else []
        fallback_prereqs = (project["fallback_prereqs"] if "fallback_prereqs"
         in project else [])
        postreqs = project["postreqs"] if "postreqs" in project else []
        postreqsOnce = (project["postreqsOnce"] if "postreqsOnce" in project
         else [])

        for prereq in prereqs:
            prereq = prereq.format(
             hostTriplet=GetGenericTriplet(self.platform["host"]),
             triplet=GetGenericTriplet(self.platform["target"]),
             arch=self.platform["target"].GetArch())
            if prereq not in self.installedSoftware:
                self.Install(prereq, verbose, None)

        installer = project["installer"]

        try:
            self.UseInstaller(software, installer, verbose, fallback_prereqs)
        except InstallError as installError:
            fallbackProject = self.SearchFallbackProject(softwareProjects);
            if (fallbackProject is not None and fallbackProject is not project):
                print(
                 "VGAZER: Something went wrong. Starting fallback installation "
                 "steps"
                )
                self.UseInstaller(software, fallbackProject["installer"], 
                 verbose, fallback_prereqs)
            else:
                raise installError

        # Resolving circullar dependencies
        # for example:
        # Mesa requires libva, libva requires Mesa.
        # Firstly install libva without mesa support as prereq of Mesa,
        # then install Mesa, then reinstall libva with Mesa support
        # Another example - Freetype-Harfbuzz-Freetype
        if len(postreqs) != 0:
            for postreq in postreqs:
                postreq = postreq.format(
                 triplet=GetGenericTriplet(self.platform["target"]),
                 arch=self.platform["target"].GetArch())
                self.installedSoftware.remove(postreq)
                self.Install(postreq, verbose, None)
        if len(postreqsOnce) != 0:
            for postreqOnce in postreqsOnce:
                postreqOnce = postreqOnce.format(
                 triplet=GetGenericTriplet(self.platform["target"]),
                 arch=self.platform["target"].GetArch())
                self.Install(postreqOnce, verbose, None)

    def InstallList(self, softwareList, verbose=False):
        for software in softwareList:
            self.Install(software, verbose, None)
