from libvgazer.command     import RunCommand
from libvgazer.exceptions  import CommandError
from libvgazer.exceptions  import InstallError
from libvgazer.store.temp  import StoreTemp
from libvgazer.working_dir import WorkingDir

def InstallPkgConfig(software, triplet, platformData, verbose):
    storeTemp = StoreTemp()
    storeTemp.ResolveEmptySubdirectory(software)
    tempPath = storeTemp.GetSubdirectoryPath(software)

    try:
        with WorkingDir(tempPath):
            RunCommand(
             ["sh", "-c",
              "echo '#!/bin/sh' > /usr/local/bin/" + triplet + "-pkg-config"],
             verbose)
            RunCommand(
             [
              "sh",
              "-c",
              "echo 'export PKG_CONFIG_DIR=' >> /usr/local/bin/" + triplet
               + "-pkg-config"
             ],
             verbose)
            RunCommand(
             [
              "sh",
              "-c",
              "echo 'export PKG_CONFIG_PATH=/usr/local/" + triplet
               + "/lib/pkgconfig:/usr/local/" + triplet
               + "/share/pkgconfig' >> /usr/local/bin/" + triplet
               + "-pkg-config"
             ],
             verbose)
            RunCommand(
             [
              "sh",
              "-c",
              "echo 'export PKG_CONFIG_LIBDIR=/usr/local/" + triplet
               + "/lib/pkgconfig:/usr/local/" + triplet
               + "/share/pkgconfig' >> /usr/local/bin/" + triplet
               + "-pkg-config"
             ],
             verbose)
            RunCommand(
             [
              "sh",
              "-c",
              "echo 'export PKG_CONFIG_SYSROOT_DIR=/' >> /usr/local/bin/"
               + triplet + "-pkg-config"
             ],
             verbose)
            RunCommand(
             [
              "sh",
              "-c",
              "echo 'exec pkg-config \"$@\"' >> /usr/local/bin/" + triplet
               + "-pkg-config"
             ],
             verbose)
            RunCommand(
             [
              "chmod", "+x", "/usr/local/bin/" + triplet + "-pkg-config"
             ],
             verbose)

    except CommandError:
        print("VGAZER: Unable to install", software)
        raise InstallError(software + " not installed")

    print("VGAZER:", software, "installed")
