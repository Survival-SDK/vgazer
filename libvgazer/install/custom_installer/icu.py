import os

from libvgazer.command     import RunCommand
from libvgazer.exceptions  import CommandError
from libvgazer.exceptions  import InstallError
from libvgazer.exceptions  import UnknownOs
from libvgazer.platform    import GetBitness
from libvgazer.platform    import GetCc
from libvgazer.platform    import GetCxx
from libvgazer.platform    import GetInstallPrefix
from libvgazer.platform    import GetTriplet
from libvgazer.store.temp  import StoreTemp
from libvgazer.version.git import GetLastTag
from libvgazer.working_dir import WorkingDir

def GetIcuPlatformName(osName):
    if osName == "linux":
        return "Linux/gcc"
    elif osName == "windows":
        return "MinGW"
    else:
        raise UnknownOs("Unknown generic OS: " + osName)

def Install(software, platform, platformData, verbose):
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
        with WorkingDir(tempPath):
            RunCommand(
             ["git", "clone", "https://github.com/unicode-org/icu.git", "."],
             verbose)
            RunCommand(
             [
              "git", "checkout",
              GetLastTag("https://github.com/unicode-org/icu.git",
               hint=r'release-\d+-\d$')
             ],
             verbose)
            RunCommand(["mkdir", "icu4c/hostBuild"], verbose)
        hostBuildDir = os.path.join(tempPath, "icu4c/hostBuild")
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
            RunCommand(
             ["make", "-j{cores_count}".format(cores_count=os.cpu_count())],
             verbose)
            if not isCrossbuild:
                RunCommand(["make", "install"], verbose)
        if isCrossbuild:
            with WorkingDir(tempPath):
                RunCommand(["mkdir", "icu4c/targetBuild"], verbose)
            targetBuildDir = os.path.join(tempPath, "icu4c/targetBuild")
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
                RunCommand(
                 ["make",
                  "-j{cores_count}".format(cores_count=os.cpu_count())],
                 verbose)
                RunCommand(["make", "install"], verbose)
    except CommandError:
        print("VGAZER: Unable to install", software)
        raise InstallError(software + " not installed")

    print("VGAZER:", software, "installed")
