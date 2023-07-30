import os

from vgazer.command     import GetCommandOutputUtf8
from vgazer.command     import RunCommand
from vgazer.exceptions  import CommandError
from vgazer.exceptions  import InstallError
from vgazer.platform    import GetInstallPrefix
from vgazer.platform    import GetTriplet
from vgazer.store.temp  import StoreTemp
from vgazer.working_dir import WorkingDir

def Install(auth, software, platform, platformData, mirrors, verbose):
    installPrefix = GetInstallPrefix(platformData)
    targetTriplet = GetTriplet(platformData["target"])

    storeTemp = StoreTemp()
    storeTemp.ResolveEmptySubdirectory(software)
    tempPath = storeTemp.GetSubdirectoryPath(software)

    try:
        with WorkingDir(tempPath):
            RunCommand(
             [
              "wget", "-P", "./",
              "https://sourceware.org/elfutils/ftp/elfutils-latest.tar.bz2"
             ],
             verbose
            )
            RunCommand(
             ["tar", "--verbose", "--extract", "--bzip2", "--file",
              "elfutils-latest.tar.bz2"],
             verbose)
            output = GetCommandOutputUtf8(
             ["tar", "--list", "--file", "elfutils-latest.tar.bz2"]
            )
        extractedDir = os.path.join(tempPath,
         output.splitlines()[0].split("/")[0])
        with WorkingDir(extractedDir):
            RunCommand(
             [
              "./configure", "--host={triplet}".format(triplet=targetTriplet),
              "--prefix={prefix}".format(prefix=installPrefix),
              "--enable-install-elfh", "--disable-symbol-versioning",
              "--disable-rpath", "--disable-libdebuginfod",
              "--disable-debuginfod"
             ],
             verbose)
        with WorkingDir(os.path.join(extractedDir, "lib")):
            RunCommand(
             ["make", "-j{cores_count}".format(cores_count=os.cpu_count())],
             verbose)
        with WorkingDir(os.path.join(extractedDir, "libelf")):
            RunCommand(
             ["make", "-j{cores_count}".format(cores_count=os.cpu_count())],
             verbose)
            RunCommand(["make", "install"], verbose)
        with WorkingDir(os.path.join(extractedDir, "config")):
            RunCommand(["make", "install"], verbose)
    except CommandError:
        print("VGAZER: Unable to install", software)
        raise InstallError("{software} not installed".format(software=software))

    print("VGAZER:", software, "installed")
