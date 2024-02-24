import os
import requests
from bs4 import BeautifulSoup

from libvgazer.command      import RunCommand
from libvgazer.config.cmake import ConfigCmake
from libvgazer.exceptions   import CommandError
from libvgazer.exceptions   import InstallError
from libvgazer.platform     import GetArFullPath
from libvgazer.platform     import GetInstallPrefix
from libvgazer.store.temp   import StoreTemp
from libvgazer.version.git  import GetLastTag
from libvgazer.working_dir  import WorkingDir

def Install(software, platform, platformData, verbose):
    installPrefix = GetInstallPrefix(platformData)
    ar = GetArFullPath(platformData["target"])

    storeTemp = StoreTemp()
    storeTemp.ResolveEmptySubdirectory(software)
    tempPath = storeTemp.GetSubdirectoryPath(software)

    try:
        with WorkingDir(tempPath):
            RunCommand(
             [
              "git", "clone", "https://git.cryptomilk.org/projects/cmocka.git",
              "."
             ],
             verbose)
            RunCommand(
             [
              "git", "checkout",
              GetLastTag("https://git.cryptomilk.org/projects/cmocka.git")
             ],
             verbose)
            RunCommand(["mkdir", "build"], verbose)
        buildDir = os.path.join(tempPath, "build")
        with WorkingDir(buildDir), ConfigCmake(platformData) as conf:
            RunCommand(
             [
              "cmake", "..",
              "-DCMAKE_TOOLCHAIN_FILE={conf}".format(conf=conf),
              "-DCMAKE_BUILD_TYPE=Debug",
              "-DCMAKE_INSTALL_PREFIX={prefix}".format(prefix=installPrefix),
              "-DCMAKE_VERBOSE_MAKEFILE:BOOL=ON",
              "-DCMAKE_AR={ar}".format(ar=ar), "-DWITH_STATIC_LIB=ON"
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
