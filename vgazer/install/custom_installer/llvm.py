import os

from vgazer.command              import GetCommandOutputUtf8
from vgazer.command              import RunCommand
from vgazer.exceptions           import CommandError
from vgazer.exceptions           import GithubApiError
from vgazer.exceptions           import InstallError
from vgazer.github_api_error_mgr import GithubApiErrorMgr
from vgazer.platform             import GetInstallPrefix
from vgazer.store.temp           import StoreTemp
from vgazer.working_dir          import WorkingDir

def Install(auth, software, platform, platformData, mirrors, verbose):
    installPrefix = GetInstallPrefix(platformData)

    storeTemp = StoreTemp()
    storeTemp.ResolveEmptySubdirectory(software)
    tempPath = storeTemp.GetSubdirectoryPath(software)
    llvmArch = {
        "x86_64": "X86",
    }[platformData["host"].GetArch()]

    try:
        releases = auth["github"].GetJson(
         "https://api.github.com/repos/llvm/llvm-project/releases")
    except ConnectionError:
        print("VGAZER: Unable to know last version of", software)
        raise InstallError("{software} not installed".format(software=software))

    with GithubApiErrorMgr(releases, "llvm/llvm-project") as errMgr:
        if errMgr.IsErrorOccured():
            raise GithubApiError(errMgr.GetErrorText())

    tarballUrl = releases[0]["tarball_url"]
    tarballShortFilename = "llvm.tar.gz"

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
        llvmDir = os.path.join(extractedDir, "llvm")
        with WorkingDir(llvmDir):
            RunCommand(["mkdir", "build"], verbose)
        buildDir = os.path.join(llvmDir, "build")
        with WorkingDir(buildDir):
            RunCommand(
             ["cmake", "..", "-DCMAKE_INSTALL_PREFIX=/usr/local",
              "-DCMAKE_VERBOSE_MAKEFILE:BOOL=ON",
              "-DCMAKE_BUILD_TYPE:STRING=Release",
              "-DLLVM_PARALLEL_COMPILE_JOBS:STRING={cores_count}".format(
               cores_count=os.cpu_count()),
              "-DLLVM_PARALLEL_LINK_JOBS:STRING={cores_count}".format(
               cores_count=os.cpu_count()),
              "-DLLVM_TARGETS_TO_BUILD:STRING={target}".format(target=llvmArch),
              "-DLLVM_BUILD_INSTRUMENTED_COVERAGE:BOOL=OFF",
              "-DLLVM_ENABLE_BINDINGS:BOOL=OFF", "-DLLVM_ENABLE_IDE:BOOL=OFF",
              "-DLLVM_ENABLE_MODULES:BOOL=OFF",
              "-DLLVM_ENABLE_Z3_SOLVER:BOOL=OFF", "-DLLVM_ENABLE_ZLIB:BOOL=OFF",
              "-DLLVM_INCLUDE_BENCHMARKS:BOOL=OFF",
              "-DLLVM_INCLUDE_EXAMPLES:BOOL=OFF",
              "-DLLVM_INCLUDE_TESTS:BOOL=OFF",
              "-DLLVM_INSTALL_BINUTILS_SYMLINKS:BOOL=OFF",
              "-DLLVM_INSTALL_CCTOOLS_SYMLINKS:BOOL=OFF",
             ],
             verbose)
            RunCommand(["cmake", "--build", "."], verbose)
            RunCommand(["cmake", "--build", ".", "--target", "install"],
             verbose)
    except CommandError:
        print("VGAZER: Unable to install", software)
        raise InstallError("{software} not installed".format(software=software))

    print("VGAZER:", software, "installed")
