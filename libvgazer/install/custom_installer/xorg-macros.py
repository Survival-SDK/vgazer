import os

from libvgazer.command     import RunCommand
from libvgazer.exceptions  import CommandError
from libvgazer.exceptions  import InstallError
from libvgazer.platform    import GetInstallPrefix
from libvgazer.store.temp  import StoreTemp
from libvgazer.version.git import GetLastTag
from libvgazer.working_dir import WorkingDir

def Install(software, platform, platformData, verbose):
    installPrefix = GetInstallPrefix(platformData)
    storeTemp = StoreTemp()
    storeTemp.ResolveEmptySubdirectory(software)
    tempPath = storeTemp.GetSubdirectoryPath(software)

    try:
        with WorkingDir(tempPath):
            RunCommand(
             [
              "git", "clone",
              "https://gitlab.freedesktop.org/xorg/util/macros.git", "."
             ],
             verbose)
            RunCommand(
             [
              "git", "checkout",
              GetLastTag("https://gitlab.freedesktop.org/xorg/util/macros.git",
               hint=r'util-macros-1\.\d\d\.\d')
             ],
             verbose)
            RunCommand(["./autogen.sh",
             "--prefix={prefix}".format(prefix=installPrefix),
             "PKG_CONFIG_PATH={prefix}/lib/pkgconfig:"
             "{prefix}/share/pkgconfig".format(prefix=installPrefix)], verbose)
            RunCommand(["make", "install"], verbose)
    except CommandError:
        print("VGAZER: Unable to install", software)
        raise InstallError(software + " not installed")

    print("VGAZER:", software, "installed")
