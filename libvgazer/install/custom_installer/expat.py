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
             ["git", "clone", "https://github.com/libexpat/libexpat.git", "."],
             verbose)
            RunCommand(
             [
              "git", "checkout",
              GetLastTag("https://github.com/libexpat/libexpat.git",
               hint=r'R\_\d\_\d\_\d')
             ],
             verbose)
        expatDir = os.path.join(tempPath, "expat")
        with WorkingDir(expatDir):
            RunCommand(["./buildconf.sh"], verbose)
            RunCommand(
             [
              "./configure", "--host={triplet}".format(triplet=targetTriplet),
              "--prefix={prefix}".format(prefix=installPrefix),
              "--disable-shared", "--without-examples", "--without-docbook"
             ],
             verbose)
            RunCommand(["make", "-j{jobs}".format(jobs=os.cpu_count())],
             verbose, allowedReturncodes=[2])
            RunCommand(["make", "install"], verbose)
    except CommandError:
        print("VGAZER: Unable to install", software)
        raise InstallError(
         "{software} not installed".format(software=software))

    print("VGAZER:", software, "installed")
