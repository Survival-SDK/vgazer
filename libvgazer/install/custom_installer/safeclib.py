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
             ["git", "clone", "https://github.com/rurban/safeclib.git", "."],
             verbose)
            RunCommand(
             [
              "git", "checkout",
              GetLastTag("https://github.com/rurban/safeclib.git",
              hint=r'v\d\.\d(\.\d)?$')
             ],
             verbose)
            RunCommand(["autoreconf", "--install"], verbose)
            RunCommand(
             [
              "./configure", "--host={triplet}".format(triplet=targetTriplet),
              "--prefix={prefix}".format(prefix=installPrefix),
              "--disable-shared", "--enable-unsafe", "--disable-doc",
              "--enable-compile-warnings=no", "--disable-Werror",
              "--enable-strmax=268435456"
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
