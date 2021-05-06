import os

from vgazer.command         import GetCommandOutputUtf8
from vgazer.command         import RunCommand
from vgazer.exceptions      import CommandError
from vgazer.exceptions      import GithubApiRateLimitExceeded
from vgazer.exceptions      import InstallError
from vgazer.github_common   import GithubCheckApiRateLimitExceeded
from vgazer.platform        import GetAr
from vgazer.platform        import GetCc
from vgazer.platform        import GetInstallPrefix
from vgazer.store.temp      import StoreTemp
from vgazer.working_dir     import WorkingDir

def Install(auth, software, platform, platformData, mirrors, verbose):
    installPrefix = GetInstallPrefix(platformData)
    ar = GetAr(platformData["target"])
    cc = GetCc(platformData["target"])

    storeTemp = StoreTemp()
    storeTemp.ResolveEmptySubdirectory(software)
    tempPath = storeTemp.GetSubdirectoryPath(software)

    tags = auth["github"].GetJson(
     "https://api.github.com/repos/robertvazan/crc32c-hw/tags")

    if GithubCheckApiRateLimitExceeded(tags):
        raise GithubApiRateLimitExceeded(
         "Github API rate limit reached while searching last version of "
         "repo: ryanlederman/libsir"
        )
    tarballUrl = tags[0]["tarball_url"]
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
            RunCommand(["sed", "-i", "s/ar rcs/$(AR) rcs/g", "Makefile"],
             verbose)
            RunCommand(["make", "build", "CC=" + cc, "AR=" + ar], verbose)
            if not os.path.exists(installPrefix + "/include"):
                RunCommand(["mkdir", "-p", installPrefix + "/include"],
                 verbose)
            if not os.path.exists(installPrefix + "/lib"):
                RunCommand(["mkdir", "-p", installPrefix + "/lib"], verbose)
            RunCommand(["cp", "libcrc32c.a", installPrefix + "/lib"], verbose)
            RunCommand(["cp", "crc32c/crc32c.h", installPrefix + "/include"],
             verbose)
    except CommandError:
        print("VGAZER: Unable to install", software)
        raise InstallError(software + " not installed")

    print("VGAZER:", software, "installed")
