import os

from libvgazer.command       import RunCommand
from libvgazer.exceptions    import CommandError
from libvgazer.exceptions    import InstallError
from libvgazer.platform      import GetAr
from libvgazer.platform      import GetCc
from libvgazer.platform      import GetInstallPrefix
from libvgazer.store.temp    import StoreTemp
from libvgazer.working_dir   import WorkingDir

def Install(software, platform, platformData, verbose):
    installPrefix = GetInstallPrefix(platformData)

    cc = GetCc(platformData["target"])
    ar = GetAr(platformData["target"])

    storeTemp = StoreTemp()
    storeTemp.ResolveEmptySubdirectory(software)
    tempPath = storeTemp.GetSubdirectoryPath(software)

    try:
        with WorkingDir(tempPath):
            RunCommand(
             [
              "git", "clone", "https://git.code.sf.net/p/tinyfiledialogs/code",
              "."
             ],
             verbose)
            RunCommand(
             [cc, "-c", "tinyfiledialogs.c", "-o", "tinyfiledialogs.o", "-O2",
              "-Wall", "-fPIC"],
             verbose)
            RunCommand(
             [ar, "rcs", "libtinyfiledialogs.a", "tinyfiledialogs.o"],
             verbose)
            if not os.path.exists(
             "{prefix}/include".format(prefix=installPrefix)):
                RunCommand(
                 [
                  "mkdir", "-p",
                  "{prefix}/include".format(prefix=installPrefix)
                 ],
                 verbose)
            if not os.path.exists("{prefix}/lib".format(prefix=installPrefix)):
                RunCommand(["mkdir", "-p",
                 "{prefix}/lib".format(prefix=installPrefix)], verbose)
            RunCommand(
             [
              "cp", "./tinyfiledialogs.h",
              "{prefix}/include".format(prefix=installPrefix)
             ],
             verbose)
            RunCommand(
             [
              "cp", "./libtinyfiledialogs.a",
              "{prefix}/lib".format(prefix=installPrefix)
             ],
             verbose)
    except CommandError:
        print("VGAZER: Unable to install", software)
        raise InstallError(
         "{software} not installed".format(software=software))

    print("VGAZER:", software, "installed")
