import os
import requests

from vgazer.command     import GetCommandOutputUtf8
from vgazer.command     import RunCommand
from vgazer.exceptions  import CommandError
from vgazer.exceptions  import InstallError
from vgazer.platform    import GetInstallPrefix
from vgazer.platform    import GetTriplet
from vgazer.store.temp  import StoreTemp
from vgazer.working_dir import WorkingDir

def Install(auth, software, platform, platformData, verbose):
    installPrefix = GetInstallPrefix(platformData)
    targetTriplet = GetTriplet(platformData["target"])

    storeTemp = StoreTemp()
    storeTemp.ResolveEmptySubdirectory(software)
    tempPath = storeTemp.GetSubdirectoryPath(software)

    tarballUrl = requests.get(
     "https://sourceforge.net/projects/sdl2gfx/best_release.json"
    ).json()["release"]["url"]
    tarballShortFilename = tarballUrl.split("/")[-2]

    try:
        with WorkingDir(tempPath):
            RunCommand(
             ["wget", "-P", "./", "-O", tarballShortFilename, tarballUrl],
             verbose)
            RunCommand(
             ["tar", "--verbose", "--extract", "--gzip", "--file",
              tarballShortFilename],
             verbose)
        extractedDir = os.path.join(tempPath, tarballShortFilename[0:-7])
        with WorkingDir(extractedDir):
            RunCommand(["mv", "./configure.in", "./configure.ac"], verbose)
            majorVersion = GetCommandOutputUtf8(
             ["sed", "-n", "14p", "./configure.ac"]
            ).split("=")[1].rstrip()
            minorVersion = GetCommandOutputUtf8(
             ["sed", "-n", "15p", "./configure.ac"]
            ).split("=")[1].rstrip()
            microVersion = GetCommandOutputUtf8(
             ["sed", "-n", "16p", "./configure.ac"]
            ).split("=")[1].rstrip()
            interfaceAge = GetCommandOutputUtf8(
             ["sed", "-n", "17p", "./configure.ac"]
            ).split("=")[1].rstrip()
            binaryAge = GetCommandOutputUtf8(
             ["sed", "-n", "18p", "./configure.ac"]
            ).split("=")[1].rstrip()
            version = majorVersion + "." + minorVersion + "." + microVersion
            ltRelease = majorVersion + "." + minorVersion
            ltCurrent = str(int(microVersion) - int(interfaceAge))
            ltRevision = interfaceAge
            ltAge = str(int(binaryAge) - int(interfaceAge))
            RunCommand(
             ["sed",  "-i",
              "-e", "s/AC_INIT(README)/AC_INIT([SDL2_gfx], [" + version + "])/g",
              "-e", "s/AM_INIT_AUTOMAKE(SDL2_gfx, $VERSION)/AM_INIT_AUTOMAKE/g",

              "-e", 's/MAJOR_VERSION=1/MAJOR_VERSION="' + majorVersion + '"/g',
              "-e", 's/MINOR_VERSION=0/MINOR_VERSION="' + minorVersion + '"/g',
              "-e", 's/MICRO_VERSION=2/MICRO_VERSION="' + microVersion + '"/g',
              "-e", 's/INTERFACE_AGE=2/INTERFACE_AGE="' + interfaceAge + '"/g',
              "-e", 's/BINARY_AGE=2/BINARY_AGE="' + binaryAge + '"/g',
              "-e", 's/VERSION=$MAJOR_VERSION.$MINOR_VERSION.$MICRO_VERSION/VERSION="' + version + '"/g',

              "-e", 's/AC_SUBST(MAJOR_VERSION)/AC_SUBST([MAJOR_VERSION])/g',
              "-e", 's/AC_SUBST(MINOR_VERSION)/AC_SUBST([MINOR_VERSION])/g',
              "-e", 's/AC_SUBST(MICRO_VERSION)/AC_SUBST([MICRO_VERSION])/g',
              "-e", 's/AC_SUBST(INTERFACE_AGE)/AC_SUBST([INTERFACE_AGE])/g',
              "-e", 's/AC_SUBST(BINARY_AGE)/AC_SUBST([BINARY_AGE])/g',
              "-e", 's/AC_SUBST(VERSION)/AC_SUBST([VERSION])/g',

              "-e", 's/LT_RELEASE=$MAJOR_VERSION.$MINOR_VERSION/LT_RELEASE="' + ltRelease + '"/g',
              "-e", 's/LT_CURRENT=`expr $MICRO_VERSION - $INTERFACE_AGE`/LT_CURRENT="' + ltCurrent + '"/g',
              "-e", 's/LT_REVISION=$INTERFACE_AGE/LT_REVISION="' + ltRevision + '"/g',
              "-e", 's/LT_AGE=`expr $BINARY_AGE - $INTERFACE_AGE`/LT_AGE="' + ltAge + '"/g',

              "-e", 's/AC_SUBST(LT_RELEASE)/AC_SUBST([LT_RELEASE])/g',
              "-e", 's/AC_SUBST(LT_CURRENT)/AC_SUBST([LT_CURRENT])/g',
              "-e", 's/AC_SUBST(LT_REVISION)/AC_SUBST([LT_REVISION])/g',
              "-e", 's/AC_SUBST(LT_AGE)/AC_SUBST([LT_AGE])/g',

              "./configure.ac"],
             verbose)
            RunCommand(
             ["sed",  "-i", "-e", "s/%.o : %.rc/rc.o:/g",
              "-e", "s/\\t-version-info $(LT_CURRENT):$(LT_REVISION):$(LT_AGE)/\\t-version-info @LT_CURRENT@:@LT_REVISION@:$@LT_AGE@/g",
              "./Makefile.am"],
             verbose)
            RunCommand(["rm", "-f", "./missing"], verbose)
            RunCommand(["autoreconf", "-i"], verbose)
            RunCommand(
             ["wget", "-O", "config.guess",
              "https://git.savannah.gnu.org/gitweb/?p=config.git;a=blob_plain;f=config.guess;hb=HEAD"],
             verbose)
            RunCommand(
             ["wget", "-O", "config.sub",
              "https://git.savannah.gnu.org/gitweb/?p=config.git;a=blob_plain;f=config.sub;hb=HEAD"],
             verbose)
            RunCommand(
             ["./configure", "--prefix=" + installPrefix,
              "--host=" + targetTriplet, "--disable-dependency-tracking",
              "--disable-sdltest"],
             verbose)
            RunCommand(["make"], verbose)
            RunCommand(["make", "install"], verbose)
    except CommandError:
        print("Unable to install", software)
        raise InstallError(software + " not installed")

    print(software, "installed")
