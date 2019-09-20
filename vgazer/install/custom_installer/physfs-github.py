import os
import requests
from bs4 import BeautifulSoup

from vgazer.command         import RunCommand
from vgazer.env_vars        import SetEnvVar
from vgazer.exceptions      import CommandError
from vgazer.exceptions      import InstallError
from vgazer.platform        import GetCc
from vgazer.platform        import GetCxx
from vgazer.platform        import GetInstallPrefix
from vgazer.store.temp      import StoreTemp
from vgazer.working_dir     import WorkingDir

def Install(auth, software, platform, platformData, verbose):
    installPrefix = GetInstallPrefix(platformData)
    cc = GetCc(platformData["target"])
    cxx = GetCxx(platformData["target"])

    storeTemp = StoreTemp()
    storeTemp.ResolveEmptySubdirectory(software)
    tempPath = storeTemp.GetSubdirectoryPath(software)

    try:
        with WorkingDir(tempPath):
            RunCommand(
             ["git", "clone", "https://github.com/criptych/physfs.git"],
            verbose)
        clonedDir = os.path.join(tempPath, "physfs")
        with WorkingDir(clonedDir):
            RunCommand(["mkdir", "build"], verbose)
        buildDir = os.path.join(clonedDir, "build")
        with WorkingDir(buildDir):
            SetEnvVar("CC", cc)
            SetEnvVar("CXX", cxx)
            RunCommand(
             ["cmake", "..", "-DPHYSFS_BUILD_TEST=FALSE",
              "-DCMAKE_INSTALL_PREFIX=" + installPrefix],
             verbose)
            RunCommand(["make"], verbose)
            RunCommand(["make", "install"], verbose)
    except CommandError:
        print("Unable to install", software)
        raise InstallError(software + " not installed")

    print(software, "installed")
