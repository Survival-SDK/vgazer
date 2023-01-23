import os

from vgazer.command     import RunCommand
from vgazer.exceptions  import CommandError
from vgazer.exceptions  import InstallError
from vgazer.platform    import GetInstallPrefix
from vgazer.platform    import GetTriplet
from vgazer.store.temp  import StoreTemp
from vgazer.working_dir import WorkingDir

def Install(auth, software, platform, platformData, mirrors, verbose):
    installPrefix = GetInstallPrefix(platformData)
    targetTriplet = GetTriplet(platformData["target"])

    storeTemp = StoreTemp()
    storeTemp.ResolveEmptySubdirectory(software)
    tempPath = storeTemp.GetSubdirectoryPath(software)

    try:
        with WorkingDir(tempPath):
            RunCommand(
             ["git", "clone", "https://github.com/AltSysrq/libbsd-minimal.git"],
             verbose)
        clonedDir = os.path.join(tempPath, "libbsd-minimal")
        with WorkingDir(clonedDir):
            RunCommand(["libtoolize"], verbose)
            RunCommand(["aclocal"], verbose)
            RunCommand(["autoheader"], verbose)
            RunCommand(["automake", "--add-missing"], verbose)
            RunCommand(["autoreconf"], verbose)
            RunCommand(
             ["./configure", "--host=" + targetTriplet,
              "--prefix=" + installPrefix, "--disable-shared",
              "CFLAGS=-D__THROW= -include features.h"],
             verbose)
            RunCommand(
             ["sed", "-i",
              "s"
              "/#define __nonnull(x)\t__attribute__((__nonnull__(x)))"
              "/#define __nonnull(x)    __attribute__((__nonnull__ x))"
              "/g",
              "include/bsd/sys/freebsd-cdefs.h"],
             verbose)
            RunCommand(["make", "V=1"], verbose)
            RunCommand(["make", "install"], verbose)
    except CommandError:
        print("VGAZER: Unable to install", software)
        raise InstallError(software + " not installed")

    print("VGAZER:", software, "installed")
