import os

from libvgazer.command     import RunCommand
from libvgazer.exceptions  import CommandError
from libvgazer.exceptions  import InstallError
from libvgazer.store.temp  import StoreTemp
from libvgazer.version.git import GetLastTag
from libvgazer.working_dir import WorkingDir

def Install(software, platform, platformData, mirrors, verbose):
    storeTemp = StoreTemp()
    storeTemp.ResolveEmptySubdirectory(software)
    tempPath = storeTemp.GetSubdirectoryPath(software)

    try:
        with WorkingDir(tempPath):
            RunCommand(
             [
              "git", "clone",
              "https://gitlab.freedesktop.org/wayland/wayland.git", "."
             ],
             verbose)
            RunCommand(
             [
              "git", "checkout",
              GetLastTag("https://gitlab.freedesktop.org/wayland/wayland.git")
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
