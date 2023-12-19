import os
import requests
from bs4 import BeautifulSoup

from vgazer.command     import GetCommandOutputUtf8
from vgazer.command     import RunCommand
from vgazer.env_vars    import EnvVar
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
        tags = auth["base"].GetJson(
         "https://gitlab.freedesktop.org/api/v4/projects/2429/repository/tags")

        tarballUrl = (
         "https://gitlab.freedesktop.org/api/v4/projects/2429/repository/"
         "archive.tar.gz?sha={tag}".format(tag=tags[0]["name"])
        )
        tarballShortFilename = tarballUrl.split("/")[-1]
        with WorkingDir(tempPath):
            RunCommand(["wget", "-P", "./", tarballUrl], verbose)
            RunCommand(
             ["tar", "--verbose", "--extract", "--gzip", "--file",
              tarballShortFilename],
             verbose)
            output = GetCommandOutputUtf8(
             ["tar", "--list", "--file", tarballShortFilename]
            )
        extractedDir = os.path.join(tempPath,
         output.splitlines()[0].split("/")[0])
        with (WorkingDir(extractedDir),
         EnvVar("ACLOCAL", "aclocal -I {prefix}/share/aclocal".format(
          prefix=installPrefix))):
            RunCommand(
             [
              "./autogen.sh", "--host={triplet}".format(triplet=targetTriplet),
              "--prefix={prefix}".format(prefix=installPrefix),
              "PKG_CONFIG_PATH={prefix}/lib/pkgconfig".format(
               prefix=installPrefix)
             ],
             verbose)
            RunCommand(
             ["make", "-j{cores_count}".format(cores_count=os.cpu_count())],
             verbose)
            RunCommand(["make", "install"], verbose)

    except requests.exceptions.ConnectionError:
        print("VGAZER: Unable to get tarball url for", software)
        raise InstallError("{software} not installed".format(software=software))
    except CommandError:
        print("VGAZER: Unable to install", software)
        raise InstallError("{software} not installed".format(software=software))

    print("VGAZER:", software, "installed")
