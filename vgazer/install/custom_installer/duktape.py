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

    cc = GetCc(platformData["target"])
    ar = GetAr(platformData["target"])

    storeTemp = StoreTemp()
    storeTemp.ResolveEmptySubdirectory(software)
    tempPath = storeTemp.GetSubdirectoryPath(software)

    releases = auth["github"].GetJson(
     "https://api.github.com/repos/svaarala/duktape/releases")

    if GithubCheckApiRateLimitExceeded(releases):
        raise GithubApiRateLimitExceeded(
         "Github API rate limit reached while searching last version of "
         "repo: svaarala/duktape"
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
            RunCommand(
             ["python", "tools/configure.py", "--output-directory", "./build",
              "--rom-support", "--dll", "-DDUK_USE_FATAL_HANDLER"],
             verbose)
            RunCommand(
             [cc, "-Wall", "-mmmx", "-msse", "-msse2", "-mfpmath=sse", "-O2",
              "-fPIC", "-o", "./build/duktape.o", "-c", "./build/duktape.c"],
             verbose)
            RunCommand(
             [cc, "-o", "./build/libduktape.so", "-s", "-shared",
              "./build/duktape.o"],
             verbose)
            RunCommand(
             [ar, "rcs", "./build/libduktape.a", "./build/duktape.o"],
             verbose)
            RunCommand(
             [cc, "-Wall", "-mmmx", "-msse", "-msse2", "-mfpmath=sse", "-O2",
              "-o", "./build/duk_module_node.o",
              "-c", "./extras/module-node/duk_module_node.c", "-I./build"],
             verbose)
            RunCommand(
             [ar, "rcs", "./build/libduk_module_node.a",
              "./build/duk_module_node.o"],
             verbose)
            if not os.path.exists(installPrefix + "/include"):
                RunCommand(["mkdir", "-p", installPrefix + "/include"],
                 verbose)
            if not os.path.exists(installPrefix + "/lib"):
                RunCommand(["mkdir", "-p", installPrefix + "/lib"], verbose)
            RunCommand(["sh", "-c",
             "cp ./build/*.h " + installPrefix + "/include"],
             verbose)
            RunCommand(
             ["cp", "./extras/module-node/duk_module_node.h",
              installPrefix + "/include"],
             verbose)
            RunCommand(["sh", "-c",
             "cp ./build/*.a " + installPrefix + "/lib"],
             verbose)
            RunCommand(["cp", "./build/libduktape.so", installPrefix + "/lib"],
             verbose)
    except CommandError:
        print("VGAZER: Unable to install", software)
        raise InstallError(software + " not installed")

    print("VGAZER:", software, "installed")
