import os

from vgazer.command              import RunCommand
from vgazer.exceptions           import CommandError
from vgazer.exceptions           import InstallError
from vgazer.platform             import GetInstallPrefix
from vgazer.store.temp           import StoreTemp
from vgazer.working_dir          import WorkingDir

def Install(auth, software, platform, platformData, mirrors, verbose):
    installPrefix = GetInstallPrefix(platformData)

    storeTemp = StoreTemp()
    storeTemp.ResolveEmptySubdirectory(software)
    tempPath = storeTemp.GetSubdirectoryPath(software)

    try:
        with WorkingDir(tempPath):
            RunCommand(
             ["git", "clone", "https://github.com/edomin/cmake_barebones.git"],
             verbose)
        srcDir = os.path.join(tempPath, "cmake_barebones")
        with WorkingDir(srcDir):
            RunCommand(
             ["./install.sh", "--prefix={prefix}".format(prefix=installPrefix)],
             verbose)
    except CommandError:
        print("VGAZER: Unable to install", software)
        raise InstallError(software + " not installed")

    print("VGAZER:", software, "installed")
