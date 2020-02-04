from vgazer.auth.base               import AuthBase
from vgazer.auth.github             import AuthGithub
from vgazer.checkers_manager        import CheckersManager
from vgazer.exceptions              import CompatibleProjectNotFound
from vgazer.exceptions              import InstallError
from vgazer.exceptions              import UnknownSoftware
from vgazer.exceptions              import VersionCheckError
from vgazer.install.custom          import InstallCustom
from vgazer.install.apk             import InstallApk
from vgazer.install.apt             import InstallApt
from vgazer.install.gcc_src         import InstallGccSrc
from vgazer.install.linux_headers   import InstallLinuxHeaders
from vgazer.install.musl_cross_make import InstallMuslCrossMake
from vgazer.install.pip             import InstallPip
from vgazer.install.pip3            import InstallPip3
from vgazer.install.pkg_config      import InstallPkgConfig
from vgazer.install.stb             import InstallStb
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
            self.checkersManager = CheckersManager(self.auth["base"])
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
        softwareData = self.softwareData.GetData()
        softwarePlatform = softwareData[software]["platform"]

        if software in self.installedSoftware:
            return

        try:
            if installer["type"] == "apk":
                InstallApk(software, installer["package"], verbose)
            elif installer["type"] == "apt":
                if isinstance(installer["package"], list):
                    for package in installer["package"]:
                        InstallApt(software, package, self.platform["host"],
                         package is installer["package"][-1], verbose)
                else:
                    InstallApt(software, installer["package"],
                     self.platform["host"], True, verbose)
            elif installer["type"] == "custom":
                self.installCustom.Install(self.auth, software,
                 installer["name"], softwarePlatform, self.platform,
                 self.mirrors, verbose)
            elif installer["type"] == "gcc-src":
                InstallGccSrc(self.auth["base"], software,
                 installer["languages"], installer["triplet"], self.platform,
                 self.mirrors["gnu"], verbose)
            elif installer["type"] == "linux-headers":
                InstallLinuxHeaders(self.auth["base"], self.platform, verbose)
            elif installer["type"] == "musl-cross-make":
                InstallMuslCrossMake(self.auth["github"], software,
                 installer["languages"], installer["triplet"], self.platform,
                 verbose)
            elif installer["type"] == "pip":
                InstallPip(software, installer["package"], verbose)
            elif installer["type"] == "pip3":
                InstallPip3(software, installer["package"], verbose)
            elif installer["type"] == "pkg-config":
                InstallPkgConfig(software, installer["triplet"], self.platform,
                 verbose)
            elif installer["type"] == "stb":
                InstallStb(installer["library"], self.platform, verbose)
        except InstallError as installError:
            if "fallback" in installer:
                print(
                 "VGAZER: Something goes wrong. Starting fallback installation "
                 "steps"
                )
                if fallbackPreinstallList is not None:
                    self.InstallList(fallbackPreinstallList, verbose)
                self.UseInstaller(software, installer["fallback"], verbose,
                 None)
            else:
                raise installError
        self.installedSoftware.append(software)

    def Install(self, software, verbose = False, fallbackPreinstallList = None):
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
             "Unable to find compatible project for sowtware: " + software)

        if "prereqs" in project:
            prereqs = project["prereqs"]
        else:
            prereqs = []

        if "fallback_prereqs" in project:
            fallback_prereqs = project["fallback_prereqs"]
        else:
            fallback_prereqs = []

        if "postreqs" in project:
            postreqs = project["postreqs"]
        else:
            postreqs = []

        if "postreqsOnce" in project:
            postreqsOnce = project["postreqsOnce"]
        else:
            postreqsOnce = []

        for prereq in prereqs:
            prereq = prereq.format(
             triplet=GetGenericTriplet(self.platform["target"]),
             arch=self.platform["target"].GetArch())
            if prereq not in self.installedSoftware:
                self.Install(prereq, verbose, None)

        installer = project["installer"]

        self.UseInstaller(software, installer, verbose, fallback_prereqs)

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

    def InstallList(self, softwareList, verbose = False):
        for software in softwareList:
            self.Install(software, verbose, None)
