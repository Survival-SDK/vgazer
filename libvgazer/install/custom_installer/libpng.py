import os

from libvgazer.command     import RunCommand
from libvgazer.exceptions  import CommandError
from libvgazer.exceptions  import InstallError
from libvgazer.platform    import GetInstallPrefix
from libvgazer.platform    import GetTriplet
from libvgazer.store.temp  import StoreTemp
from libvgazer.version.git import GetLastTag
from libvgazer.working_dir import WorkingDir

def Install(software, platform, platformData, verbose):
    installPrefix = GetInstallPrefix(platformData)
    targetTriplet = GetTriplet(platformData["target"])

    storeTemp = StoreTemp()
    storeTemp.ResolveEmptySubdirectory(software)
    tempPath = storeTemp.GetSubdirectoryPath(software)

    try:
        with WorkingDir(tempPath):
            RunCommand(
             ["git", "clone", "git://git.code.sf.net/p/libpng/code", "."],
             verbose)
            RunCommand(
             [
              "git", "checkout",
              GetLastTag("git://git.code.sf.net/p/libpng/code",
               hint=r'(:?v1\.6\.\d\d$)|(:?v1\.7\.\d+$)')
             ],
             verbose)
            RunCommand(
             [
              "./configure", "--host={triplet}".format(triplet=targetTriplet),
              "--prefix={prefix}".format(prefix=installPrefix),
              "--disable-shared", "--enable-hardware-optimizations=yes",
              "CFLAGS=-fPIC",
              "CPPFLAGS=-I{prefix}/include".format(prefix=installPrefix),
              "LDFLAGS=-L{prefix}/lib".format(prefix=installPrefix)
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
