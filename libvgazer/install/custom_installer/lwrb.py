import os

from libvgazer.command     import RunCommand
from libvgazer.exceptions  import CommandError
from libvgazer.exceptions  import InstallError
from libvgazer.platform    import GetAr
from libvgazer.platform    import GetCc
from libvgazer.platform    import GetInstallPrefix
from libvgazer.store.temp  import StoreTemp
from libvgazer.version.git import GetLastTag
from libvgazer.working_dir import WorkingDir

def Install(software, platform, platformData, verbose):
    installPrefix = GetInstallPrefix(platformData)
    ar = GetAr(platformData["target"])
    cc = GetCc(platformData["target"])

    storeTemp = StoreTemp()
    storeTemp.ResolveEmptySubdirectory(software)
    tempPath = storeTemp.GetSubdirectoryPath(software)

    try:
        with WorkingDir(tempPath):
            RunCommand(
             ["git", "clone", "https://github.com/MaJerle/lwrb.git", "."],
             verbose)
            RunCommand(
             [
              "git", "checkout",
              GetLastTag("https://github.com/MaJerle/lwrb.git",
               hint=r'v\d\.\d\.\d$')
             ],
             verbose)
            # TODO Remove sed when we get rid gcc-4.8
            RunCommand(
             [
              "sed", "-i", "1i #define LWRB_DISABLE_ATOMIC",
              "lwrb/src/include/lwrb/lwrb.h"
             ],
             verbose
            )
            RunCommand(
             [
              cc, "-O2", "-fPIC", "-std=c11", "-I", "lwrb/src/include", "-c",
              "lwrb/src/lwrb/lwrb.c", "-o", "lwrb.o"
             ],
             verbose
            )
            RunCommand([ar, "rcs", "liblwrb.a", "lwrb.o"], verbose)
            if not os.path.exists(
             "{prefix}/include".format(prefix=installPrefix)):
                RunCommand(
                 [
                  "mkdir", "-p",
                  "{prefix}/include".format(prefix=installPrefix)
                 ],
                 verbose
                )
            if not os.path.exists("{prefix}/lib".format(prefix=installPrefix)):
                RunCommand(
                 ["mkdir", "-p", "{prefix}/lib".format(prefix=installPrefix)],
                 verbose)
            RunCommand(
             [
              "cp", "lwrb/src/include/lwrb/lwrb.h",
              "{prefix}/include".format(prefix=installPrefix)
             ],
             verbose
            )
            RunCommand(
             ["cp", "./liblwrb.a",
              "{prefix}/lib".format(prefix=installPrefix)],
             verbose)
    except CommandError:
        print("VGAZER: Unable to install", software)
        raise InstallError(
         "{software} not installed".format(software=software))

    print("VGAZER:", software, "installed")
