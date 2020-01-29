from vgazer.command     import RunCommand
from vgazer.exceptions  import CommandError
from vgazer.exceptions  import InstallError
from vgazer.store.temp  import StoreTemp
from vgazer.working_dir import WorkingDir

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
             ["sh",
              "-c",
              "echo 'export PKG_CONFIG_DIR=' >> /usr/local/bin/" + triplet
               + "-pkg-config"
             ],
            verbose)
            RunCommand(
             ["sh",
              "-c",
              "echo 'export PKG_CONFIG_LIBDIR=/usr/local/" + triplet
               + "/lib/pkgconfig:/usr/local/" + triplet
               + "/share/pkgconfig' >> /usr/local/bin/" + triplet
               + "-pkg-config"
             ],
            verbose)
            RunCommand(
             ["sh",
              "-c",
              "echo 'export PKG_CONFIG_SYSROOT_DIR=/' >> /usr/local/bin/"
               + triplet + "-pkg-config"
             ],
            verbose)
            RunCommand(
             ["sh",
              "-c",
              "echo 'exec pkg-config \"$@\"' >> /usr/local/bin/" + triplet
               + "-pkg-config"
             ],
            verbose)

    except CommandError:
        print("VGAZER: Unable to install", software)
        raise InstallError(software + " not installed")

    print("VGAZER:", software, "installed")
