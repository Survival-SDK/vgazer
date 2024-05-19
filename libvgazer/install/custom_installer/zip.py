import os

from libvgazer.command      import RunCommand
from libvgazer.config.cmake import ConfigCmake
from libvgazer.exceptions   import CommandError
from libvgazer.exceptions   import InstallError
from libvgazer.platform     import GetInstallPrefix
from libvgazer.store.temp   import StoreTemp
from libvgazer.version.git  import GetLastTag
from libvgazer.working_dir  import WorkingDir

def Install(software, platform, platformData, verbose):
    installPrefix = GetInstallPrefix(platformData)

    storeTemp = StoreTemp()
    storeTemp.ResolveEmptySubdirectory(software)
    tempPath = storeTemp.GetSubdirectoryPath(software)

    try:
        with WorkingDir(tempPath):
            RunCommand(
             ["git", "clone", "https://github.com/kuba--/zip.git", "."],
             verbose)
            RunCommand(
             [
              "git", "checkout",
              GetLastTag("https://github.com/kuba--/zip.git")
             ],
             verbose)
            RunCommand(
             ["sed", "-i",
              "s/  set(CMAKE_C_FLAGS \"${CMAKE_C_FLAGS} -Wall -Wextra -Werror -pedantic\")/  set(CMAKE_C_FLAGS \"${CMAKE_C_FLAGS} -Wall -Wextra -pedantic\")/",
              "./CMakeLists.txt"],
             verbose)
            RunCommand(["mkdir", "build"], verbose)
        buildDir = os.path.join(tempPath, "build")
        with WorkingDir(buildDir), ConfigCmake(platformData, cflags="-std=gnu99") as conf:
            RunCommand(
             ["cmake", "..",
              "-DCMAKE_TOOLCHAIN_FILE={crossfile}".format(crossfile=conf),
              "-DCMAKE_INSTALL_PREFIX={prefix}".format(prefix=installPrefix),
              "-DCMAKE_VERBOSE_MAKEFILE:BOOL=ON",
              "-DCMAKE_DISABLE_TESTING=ON"],
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
