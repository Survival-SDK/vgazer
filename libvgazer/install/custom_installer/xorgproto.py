import os

from libvgazer.command      import RunCommand
from libvgazer.config.meson import ConfigMeson
from libvgazer.exceptions   import CommandError
from libvgazer.exceptions   import InstallError
from libvgazer.platform     import GetInstallPrefix
from libvgazer.store.temp   import StoreTemp
from libvgazer.version.git  import GetLastTag
from libvgazer.working_dir  import WorkingDir

def Install(software, platform, platformData, verbose):
    installPrefix = GetInstallPrefix(platformData)

    storeTemp = StoreTemp()
    storeTemp.ResolveEmptySubdirectory(software)
    tempPath = storeTemp.GetSubdirectoryPath(software)

    try:
        with WorkingDir(tempPath), ConfigMeson(platformData) as conf:
            RunCommand(
             [
              "git", "clone",
              "https://gitlab.freedesktop.org/xorg/proto/xorgproto.git", "."
             ],
             verbose)
            RunCommand(
             [
              "git", "checkout",
              GetLastTag(
               "https://gitlab.freedesktop.org/xorg/proto/xorgproto.git")
             ],
             verbose)
            RunCommand(
             [
              "meson", "setup", "build/",
              "--prefix={prefix}".format(prefix=installPrefix), "--cross-file",
              conf
             ],
             verbose)
            RunCommand(["ninja", "-C", "build/", "install"], verbose)
    except CommandError:
        print("VGAZER: Unable to install", software)
        raise InstallError(
         "{software} not installed".format(software=software))

    print("VGAZER:", software, "installed")
