import os
import requests

from libvgazer.command       import RunCommand
from libvgazer.exceptions    import CommandError
from libvgazer.exceptions    import InstallError
from libvgazer.install.utils import SourceforgeDownloadTarballWhileErrorcodeFour
from libvgazer.platform      import GetInstallPrefix
from libvgazer.platform      import GetTriplet
from libvgazer.store.temp    import StoreTemp
from libvgazer.working_dir   import WorkingDir

def Install(auth, software, platform, platformData, mirrors, verbose):
    installPrefix = GetInstallPrefix(platformData)
    targetTriplet = GetTriplet(platformData["target"])

    storeTemp = StoreTemp()
    storeTemp.ResolveEmptySubdirectory(software)
    tempPath = storeTemp.GetSubdirectoryPath(software)

    sourceforgeMirrorsManager = mirrors["sourceforge"].CreateMirrorsManager(
     ["https", "http"])

    filename = requests.get(
     "https://sourceforge.net/projects/libpng/best_release.json"
    ).json()["release"]["filename"]
    tarballShortFilename = filename.split("/")[-1]

    try:
        with WorkingDir(tempPath):
            SourceforgeDownloadTarballWhileErrorcodeFour(
             sourceforgeMirrorsManager, "libpng", filename, verbose)
            RunCommand(
             ["tar", "--verbose", "--extract", "--xz", "--file",
              tarballShortFilename],
             verbose)
        extractedDir = os.path.join(tempPath, tarballShortFilename[0:-7])
        with WorkingDir(extractedDir):
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
        raise InstallError("{software} not installed".format(software=software))

    print("VGAZER:", software, "installed")
