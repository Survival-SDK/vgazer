import os

from vgazer.command              import GetCommandOutputUtf8
from vgazer.command              import RunCommand
from vgazer.exceptions           import CommandError
from vgazer.exceptions           import GithubApiError
from vgazer.exceptions           import InstallError
from vgazer.exceptions           import UnknownOs
from vgazer.github_api_error_mgr import GithubApiErrorMgr
from vgazer.platform             import GetBitness
from vgazer.platform             import GetCc
from vgazer.platform             import GetCxx
from vgazer.platform             import GetInstallPrefix
from vgazer.platform             import GetTriplet
from vgazer.store.temp           import StoreTemp
from vgazer.working_dir          import WorkingDir

def GetIcuPlatformName(osName):
    if osName == "linux":
        return "Linux/gcc"
    elif osName == "windows":
        return "MinGW"
    else:
        raise UnknownOs("Unknown generic OS: " + osName)

def Install(auth, software, platform, platformData, mirrors, verbose):
    isCrossbuild = not (
     platformData["target"].PlatformsEqual(platformData["host"])
    )
    hostBitness = GetBitness(platformData["host"])
    hostTriplet = GetTriplet(platformData["host"])
    hostCc = GetCc(platformData["host"])
    hostCxx = GetCxx(platformData["host"])
    hostOs = platformData["host"].GetOs()
    hostIcuPlatformName = GetIcuPlatformName(
     platformData["host"].GetGenericOs(hostOs))
    if isCrossbuild:
        hostInstallPrefix = "/usr/local"
        targetInstallPrefix = GetInstallPrefix(platformData)
        targetTriplet = GetTriplet(platformData["target"])
        targetCc = GetCc(platformData["target"])
        targetCxx = GetCxx(platformData["target"])
        targetOs = platformData["host"].GetOs()
        targetIcuPlatformName = GetIcuPlatformName(
         platformData["target"].GetGenericOs(targetOs))
    else:
        hostInstallPrefix = GetInstallPrefix(platformData)

    storeTemp = StoreTemp()
    storeTemp.ResolveEmptySubdirectory(software)
    tempPath = storeTemp.GetSubdirectoryPath(software)

    try:
        releases = auth["github"].GetJson(
         "https://api.github.com/repos/unicode-org/icu/releases")
    except ConnectionError:
        print("VGAZER: Unable to know last version of", software)
        raise InstallError(software + " not installed")

    with GithubApiErrorMgr(releases, "unicode-org/icu") as errMgr:
        if errMgr.IsErrorOccured():
            raise GithubApiError(errMgr.GetErrorText())

    tarballUrl = releases[0]["tarball_url"]
    tarballShortFilename = tarballUrl.split("/")[-1]

    try:
        with WorkingDir(tempPath):
            RunCommand(["wget", "-P", "./", tarballUrl], verbose)
            RunCommand(
             ["tar", "--verbose", "--extract", "--gzip", "--file",
              tarballShortFilename],
             verbose)
            output = GetCommandOutputUtf8(
             ["tar", "--list", "--file", tarballShortFilename]
            )
        extractedDir = os.path.join(tempPath,
         output.splitlines()[0].split("/")[0])
        with WorkingDir(extractedDir):
            RunCommand(["mkdir", "icu4c/hostBuild"], verbose)
        hostBuildDir = os.path.join(extractedDir, "icu4c/hostBuild")
        with WorkingDir(hostBuildDir):
            RunCommand(
             ["../source/runConfigureICU", hostIcuPlatformName,
              "--host=" + hostTriplet, "--prefix=" + hostInstallPrefix,
              "--disable-shared", "--enable-static=yes", "--enable-extras=no",
              "--enable-icuio=no", "--enable-layoutex=no", "--enable-tools",
              "--enable-tests=no", "--enable-samples=no",
              "--with-library-bits=" + str(hostBitness), "CC=" + hostCc,
              "CXX=" + hostCxx],
             verbose)
            RunCommand(["make"], verbose)
            if not isCrossbuild:
                RunCommand(["make", "install"], verbose)
        if isCrossbuild:
            with WorkingDir(extractedDir):
                RunCommand(["mkdir", "icu4c/targetBuild"], verbose)
            targetBuildDir = os.path.join(extractedDir, "icu4c/targetBuild")
            with WorkingDir(targetBuildDir):
                RunCommand(
                 ["../source/runConfigureICU", targetIcuPlatformName,
                  "--host=" + targetTriplet, "--prefix=" + targetInstallPrefix,
                  "--with-cross-build=" + hostBuildDir, "--disable-shared",
                  "--enable-static=yes", "--enable-extras=no",
                  "--enable-icuio=no", "--enable-layoutex=no",
                  "--enable-tools", "--enable-tests=no", "--enable-samples=no",
                  "CC=" + targetCc, "CXX=" + targetCxx],
                 verbose)
                RunCommand(["make"], verbose)
                RunCommand(["make", "install"], verbose)
    except CommandError:
        print("VGAZER: Unable to install", software)
        raise InstallError(software + " not installed")

    print("VGAZER:", software, "installed")
