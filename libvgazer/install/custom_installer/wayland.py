import os

from libvgazer.command      import RunCommand
from libvgazer.env_vars     import EnvVar
from libvgazer.config.meson import ConfigMeson
from libvgazer.exceptions   import CommandError
from libvgazer.exceptions   import InstallError
from libvgazer.platform     import GetInstallPrefix
from libvgazer.store.temp   import StoreTemp
from libvgazer.version.git  import GetLastTag
from libvgazer.working_dir  import WorkingDir

def Install(software, platform, platformData, mirrors, verbose):
    configMeson = ConfigMeson(platformData)
    configMeson.GenerateCrossFile()

    installPrefix = GetInstallPrefix(platformData)

    storeTemp = StoreTemp()
    storeTemp.ResolveEmptySubdirectory(software)
    tempPath = storeTemp.GetSubdirectoryPath(software)

    if "PKG_CONFIG_LIBDIR" in os.environ:
        pkgConfigLibdir =
         "/usr/local/lib/pkgconfig:/usr/local/lib64/pkgconfig:{old}".format(
          old=os.environ["PKG_CONFIG_LIBDIR"])
    else:
        pkgConfigLibdir = "/usr/local/lib/pkgconfig:/usr/local/lib64/pkgconfig"

    try:
        with WorkingDir(tempPath), EnvVar("PKG_CONFIG_LIBDIR", pkgConfigLibdir):
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
              "meson", "setup", "build/",
              "--prefix={prefix}".format(prefix=installPrefix), "--cross-file",
              configMeson.GetCrossFileName(), "-Dscanner=false",
              "-Dtests=false", "-Ddocumentation=false",
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
