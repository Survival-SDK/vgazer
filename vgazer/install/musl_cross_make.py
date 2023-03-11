import os

from vgazer.command              import GetCommandOutputUtf8
from vgazer.command              import RunCommand
from vgazer.exceptions           import CommandError
from vgazer.exceptions           import GithubApiError
from vgazer.exceptions           import InstallError
from vgazer.github_api_error_mgr import GithubApiErrorMgr
from vgazer.platform             import GetFilesystemType
from vgazer.store.temp           import StoreTemp
from vgazer.working_dir          import WorkingDir

def InstallMuslCrossMake(auth, software, languages, triplet, platformData,
 verbose):
    storeTemp = StoreTemp()
    storeTemp.ResolveEmptySubdirectory(software)
    tempPath = storeTemp.GetSubdirectoryPath(software)

    if (GetFilesystemType(tempPath) == "overlay"
     and platformData["host"].GetOs() == "debian"):
        useBsdTar = True
    else:
        useBsdTar = False

    tags = auth.GetJson(
     "https://api.github.com/repos/richfelker/musl-cross-make/tags")

    with GithubApiErrorMgr(tags, "richfelker/musl-cross-make") as errMgr:
        if errMgr.IsErrorOccured():
            raise GithubApiError(errMgr.GetErrorText())

    tarballUrl = tags[0]["tarball_url"]
    tarballShortFilename = "musl-cross-make.tar.gz"

    try:
        with WorkingDir(tempPath):
            RunCommand(
             ["wget", "-P", "./", "-O", tarballShortFilename, tarballUrl],
             verbose)
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
            RunCommand(
             ["sh", "-c", "echo 'TARGET = " + triplet + "' > config.mak"],
             verbose)
            RunCommand(
             ["sh", "-c", "echo 'OUTPUT = /usr/local' >> config.mak"],
             verbose)
            RunCommand(
             [
              "sh",
              "-c",
              "echo 'COMMON_CONFIG += CFLAGS=\"-g0 -Os\" "
              "CXXFLAGS=\"-g0 -Os\" LDFLAGS=\"-s\"' >> config.mak"
             ],
             verbose)
            RunCommand(
             [
              "sh",
              "-c",
              "echo 'GCC_CONFIG += --enable-languages=" + languages
              + "' >> config.mak"
             ],
             verbose)
            RunCommand(
             ["sh", "-c",
              "echo 'GCC_CONFIG += --disable-multilib' >> config.mak"],
             verbose)
            if useBsdTar:
                RunCommand(
                 ["sed",  "-i", "-e", r"s/\(tar z\|tar j\|tar J\)/bsdtar /g",
                  "./Makefile"],
                 verbose)
            RunCommand(["make"], verbose)
            RunCommand(["make", "install"], verbose)
    except CommandError:
        print("VGAZER: Unable to install", software)
        raise InstallError(software + " not installed")

    print("VGAZER:", software, "installed")
