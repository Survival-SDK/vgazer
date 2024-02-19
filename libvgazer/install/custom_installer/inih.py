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
             ["git", "clone", "https://github.com/benhoyt/inih.git", "."],
             verbose)
            RunCommand(
             [
              "git", "checkout",
              GetLastTag("https://github.com/benhoyt/inih.git")
             ],
             verbose)
            RunCommand(
             [
              "sed", "-i",
              "-e", "/#include <stdio.h>/a #define INI_HANDLER_LINENO 1",
              "-e",
              "/#include <stdio.h>"
              "/a #define INI_CALL_HANDLER_ON_NEW_SECTION 1",
              "-e", "/#include <stdio.h>/a #define INI_MAX_LINE 8192",
              "./ini.h",
             ],
             verbose)
            RunCommand([cc, "-c", "ini.c", "-o", "ini.o", "-O2", "-fPIC"],
             verbose)
            RunCommand([ar, "rcs", "libinih.a", "ini.o"], verbose)
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
             ["cp", "./ini.h",
              "{prefix}/include".format(prefix=installPrefix)],
             verbose)
            RunCommand(
             ["cp", "./libinih.a",
              "{prefix}/lib".format(prefix=installPrefix)],
             verbose)
    except CommandError:
        print("VGAZER: Unable to install", software)
        raise InstallError(
         "{software} not installed".format(software=software))

    print("VGAZER:", software, "installed")
