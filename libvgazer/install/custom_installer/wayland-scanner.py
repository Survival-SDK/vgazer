import os

from libvgazer.command     import RunCommand
from libvgazer.env_vars    import EnvVar
from libvgazer.exceptions  import CommandError
from libvgazer.exceptions  import InstallError
from libvgazer.platform    import GetInstallPrefix
from libvgazer.store.temp  import StoreTemp
from libvgazer.version.git import GetLastTag
from libvgazer.working_dir import WorkingDir

def Install(software, platform, platformData, verbose):
    storeTemp = StoreTemp()
    storeTemp.ResolveEmptySubdirectory(software)
    tempPath = storeTemp.GetSubdirectoryPath(software)

    installPrefix = GetInstallPrefix(platformData)

    if "PKG_CONFIG_PATH" in os.environ:
        pkg_config_path = "{prefix}/lib/pkgconfig:{old}".format(
         prefix=installPrefix, old=os.environ["PKG_CONFIG_PATH"])
    else:
        pkg_config_path = "{prefix}/lib/pkgconfig".format(prefix=installPrefix)

    try:
        with WorkingDir(tempPath), EnvVar("PKG_CONFIG_PATH", pkg_config_path):
            RunCommand(
             [
              "git", "clone",
              "https://gitlab.freedesktop.org/wayland/wayland.git", "."
             ],
             verbose)
            RunCommand(
             [
              "git", "checkout",
              GetLastTag("https://gitlab.freedesktop.org/wayland/wayland.git",
               hint=r'1\.\d\d.\d+')
             ],
             verbose)
            RunCommand(
             [
              "meson", "setup", "build/", "--prefix=/usr/local",
              "-Dlibraries=false", "-Dtests=false", "-Ddocumentation=false",
              "-Ddtd_validation=false"
             ],
             verbose)
            RunCommand(["ninja", "-C", "build/"], verbose)
            RunCommand(["ninja", "-C", "build/", "install"], verbose)
    except CommandError:
        print("VGAZER: Unable to install", software)
        raise InstallError(
         "{software} not installed".format(software=software))

    print("VGAZER:", software, "installed")
