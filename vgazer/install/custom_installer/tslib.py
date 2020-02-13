import os

from vgazer.command         import GetCommandOutputUtf8
from vgazer.command         import RunCommand
from vgazer.config.cmake    import ConfigCmake
from vgazer.exceptions      import CommandError
from vgazer.exceptions      import GithubApiRateLimitExceeded
from vgazer.exceptions      import InstallError
from vgazer.exceptions      import UnknownOs
from vgazer.github_common   import GithubCheckApiRateLimitExceeded
from vgazer.platform        import GetInstallPrefix
from vgazer.platform        import GetPkgConfig
from vgazer.platform        import GetTriplet
from vgazer.store.temp      import StoreTemp
from vgazer.working_dir     import WorkingDir

def Install(auth, software, platform, platformData, mirrors, verbose):
    targetOs = platformData["target"].GetOs()
    if targetOs == "linux":
        configCmake = ConfigCmake(platformData)
        configCmake.GenerateCrossFile()
    elif targetOs == "windows":
        targetTriplet = GetTriplet(platformData["target"])
        pkgConfig = GetPkgConfig(platformData["target"])
    else:
        raise UnknownOs("Unknown OS: " + targetOs)

    installPrefix = GetInstallPrefix(platformData)

    storeTemp = StoreTemp()
    storeTemp.ResolveEmptySubdirectory(software)
    tempPath = storeTemp.GetSubdirectoryPath(software)

    releases = auth["github"].GetJson(
     "https://api.github.com/repos/libts/tslib/releases")

    if GithubCheckApiRateLimitExceeded(releases):
        raise GithubApiRateLimitExceeded(
         "Github API rate limit reached while searching last version of "
         "repo: libts/tslib"
        )

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
            RunCommand(["mkdir", "build"], verbose)
            if targetOs == "windows":
                RunCommand(["./autogen.sh"], verbose)
        buildDir = os.path.join(extractedDir, "build")
        with WorkingDir(buildDir):
            if targetOs == "linux":
                RunCommand(
                 ["cmake", "..",
                  "-DCMAKE_TOOLCHAIN_FILE=" + configCmake.GetCrossFileName(),
                  "-DCMAKE_INSTALL_PREFIX=" + installPrefix,
                  "-DCMAKE_VERBOSE_MAKEFILE:BOOL=ON", "-DENABLE_TOOLS=OFF"],
                 verbose)
                RunCommand(["cmake", "--build", "."], verbose)
                RunCommand(["cmake", "-P", "cmake_install.cmake"], verbose)
            elif targetOs == "windows":
                RunCommand(
                 ["../configure", "--host=" + targetTriplet,
                  "--prefix=" + installPrefix, "--disable-input",
                  "--disable-touchkit", "--disable-waveshare",
                  "PKG_CONFIG=" + pkgConfig],
                 verbose)
                RunCommand(["make"], verbose)
                RunCommand(["make", "install"], verbose)
    except CommandError:
        print("VGAZER: Unable to install", software)
        raise InstallError(software + " not installed")

    print("VGAZER:", software, "installed")
