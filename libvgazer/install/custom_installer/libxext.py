import os

from libvgazer.command     import RunCommand
from libvgazer.env_vars    import EnvVar
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

    aclocal = "aclocal -I {prefix}/share/aclocal".format(prefix=installPrefix)

    try:
        with WorkingDir(tempPath), EnvVar("ACLOCAL", aclocal):
            RunCommand(
             [
              "git", "clone",
              "https://gitlab.freedesktop.org/xorg/lib/libxext.git", "."
             ],
             verbose)
            RunCommand(
             [
              "git", "checkout",
              GetLastTag(
               "https://gitlab.freedesktop.org/xorg/lib/libxext.git",
               hint=r'libXext-\d\.\d(\.\d+(\.\d)?)?$')
             ],
             verbose)
            RunCommand(
             ["./autogen.sh", "--host=" + targetTriplet,
              "--prefix=" + installPrefix,
              "PKG_CONFIG_PATH=" + installPrefix + "/lib/pkgconfig"],
             verbose)
            RunCommand(
             ["make", "-j{cores_count}".format(cores_count=os.cpu_count())],
             verbose)
            RunCommand(["make", "install"], verbose)
    except CommandError:
        print("VGAZER: Unable to install", software)
        raise InstallError(software + " not installed")

    print("VGAZER:", software, "installed")
