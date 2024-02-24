import os

from libvgazer.command      import GetCommandOutputUtf8
from libvgazer.command      import RunCommand
from libvgazer.exceptions   import CommandError
from libvgazer.exceptions   import InstallError
from libvgazer.store.temp   import StoreTemp
from libvgazer.version.git  import GetLastTag
from libvgazer.working_dir  import WorkingDir

def Install(software, platform, platformData, verbose):
    storeTemp = StoreTemp()
    storeTemp.ResolveEmptySubdirectory(software)
    tempPath = storeTemp.GetSubdirectoryPath(software)

    try:
        output = GetCommandOutputUtf8(["clang", "--version"])
        version = output.splitlines()[0].split(" ")[-1].split(".")[0]

        with WorkingDir(tempPath):
            RunCommand(
             [
              "git", "clone",
              "https://github.com/include-what-you-use/include-what-you-use.git",
              "."
             ],
             verbose)
            RunCommand(
             ["git", "checkout", "clang_{version}".format(version=version)],
             verbose)
            RunCommand(["mkdir", "build"], verbose)
        buildDir = os.path.join(tempPath, "build")
        with WorkingDir(buildDir):
            RunCommand(
             [
              "cmake", "..", "-DCMAKE_INSTALL_PREFIX=/usr/local",
              "-DCMAKE_PREFIX_PATH=/usr", "-DCMAKE_VERBOSE_MAKEFILE:BOOL=ON",
             ],
             verbose)
            RunCommand(
             ["make", "-j{cores_count}".format(cores_count=os.cpu_count())],
             verbose)
            RunCommand(["make", "install"], verbose)
    except CommandError:
        print("VGAZER: Unable to install", software)
        raise InstallError(
         "{software} not installed".format(software=software))

    print("VGAZER:", software, "installed")
