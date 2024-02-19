import os

from libvgazer.command     import RunCommand
from libvgazer.exceptions  import CommandError
from libvgazer.exceptions  import InstallError
from libvgazer.platform    import GetInstallPrefix
from libvgazer.platform    import GetTriplet
from libvgazer.store.temp  import StoreTemp
from libvgazer.version.git import GetLastTag
from libvgazer.working_dir import WorkingDir
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
             ["git", "clone", "https://github.com/alsa-project/alsa-lib.git"],
             verbose)
        clonedDir = os.path.join(tempPath, "alsa-lib")
        with WorkingDir(clonedDir):
            RunCommand(
             [
              "git", "checkout",
              GetLastTag("https://github.com/alsa-project/alsa-lib.git",
               hint=r'v1\.2\.\d\d')
             ],
             verbose)
            RunCommand(["touch", "ltconfig"], verbose)
            RunCommand(
             ["libtoolize", "--force", "--copy", "--automake"], verbose)
            RunCommand(["aclocal"], verbose)
            RunCommand(["autoheader"], verbose)
            RunCommand(
             ["automake", "--foreign", "--copy", "--add-missing"], verbose)
            RunCommand(["touch", "depcomp"], verbose)
            RunCommand(["autoconf"], verbose)
            RunCommand(
             ["./configure", "--host=" + targetTriplet,
              "--prefix=" + installPrefix, "--enable-symbolic-functions",
              "--disable-python"],
             verbose)
            RunCommand(
             ["make", "-j{cores_count}".format(cores_count=os.cpu_count())],
             verbose)
            RunCommand(["make", "install"], verbose)
    except CommandError:
        print("VGAZER: Unable to install", software)
        raise InstallError(software + " not installed")

    print("VGAZER:", software, "installed")
