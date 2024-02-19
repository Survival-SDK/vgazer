import os

from libvgazer.command     import RunCommand
from libvgazer.exceptions  import CommandError
from libvgazer.exceptions  import InstallError
from libvgazer.platform    import GetInstallPrefix
from libvgazer.store.temp  import StoreTemp
from libvgazer.working_dir import WorkingDir

def Install(software, platform, platformData, verbose):
    installPrefix = GetInstallPrefix(platformData)

    storeTemp = StoreTemp()
    storeTemp.ResolveEmptySubdirectory(software)
    tempPath = storeTemp.GetSubdirectoryPath(software)

    try:
        with WorkingDir(tempPath):
            RunCommand(
             ["git", "clone", "https://github.com/attractivechaos/klib.git"],
             verbose)
        clonedDir = os.path.join(tempPath, "klib")
        with WorkingDir(clonedDir):
            if not os.path.exists(
             "{prefix}/include/klib".format(prefix=installPrefix)):
                RunCommand(
                 [
                  "mkdir", "-p",
                  "{prefix}/include/klib".format(prefix=installPrefix)
                 ],
                 verbose)
            RunCommand(
             [
              "cp", "./ketopt.h",
              "{prefix}/include/klib".format(prefix=installPrefix)
             ],
             verbose)
    except CommandError:
        print("VGAZER: Unable to install", software)
        raise InstallError(
         "{software} not installed".format(software=software))

    print("VGAZER:", software, "installed")
