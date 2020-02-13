import os

from vgazer.command         import RunCommand
from vgazer.config.cmake    import ConfigCmake
from vgazer.exceptions      import CommandError
from vgazer.exceptions      import InstallError
from vgazer.platform        import GetInstallPrefix
from vgazer.store.temp      import StoreTemp
from vgazer.working_dir     import WorkingDir

def Install(auth, software, platform, platformData, mirrors, verbose):
    configCmake = ConfigCmake(platformData)
    configCmake.GenerateCrossFile()
    installPrefix = GetInstallPrefix(platformData)

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
            RunCommand(
             ["cmake", "..",
              "-DCMAKE_TOOLCHAIN_FILE=" + configCmake.GetCrossFileName(),
              "-DCMAKE_INSTALL_PREFIX=" + installPrefix,
              "-DPHYSFS_BUILD_SHARED=FALSE", "-DPHYSFS_BUILD_TEST=FALSE",
              "-DCMAKE_VERBOSE_MAKEFILE:BOOL=ON"],
             verbose)
            RunCommand(["make"], verbose)
            RunCommand(["make", "install"], verbose)
    except CommandError:
        print("VGAZER: Unable to install", software)
        raise InstallError(software + " not installed")

    print("VGAZER:", software, "installed")
