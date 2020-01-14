import os
import requests

from vgazer.command     import RunCommand
from vgazer.exceptions  import CommandError
from vgazer.exceptions  import InstallError
from vgazer.exceptions  import TarballLost
from vgazer.platform    import GetAr
from vgazer.platform    import GetCc
from vgazer.platform    import GetInstallPrefix
from vgazer.store.temp  import StoreTemp
from vgazer.working_dir import WorkingDir

def Install(auth, software, platform, platformData, mirrors, verbose):
    installPrefix = GetInstallPrefix(platformData)

    cc = GetCc(platformData["target"])
    ar = GetAr(platformData["target"])

    storeTemp = StoreTemp()
    storeTemp.ResolveEmptySubdirectory(software)
    tempPath = storeTemp.GetSubdirectoryPath(software)

    tarballUrl = requests.get(
     "https://sourceforge.net/projects/glew/best_release.json"
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
        extractedDir = os.path.join(tempPath, tarballShortFilename[0:-4])
        with WorkingDir(extractedDir):
            RunCommand(
             ["make", "glew.lib", "CC=" + cc, "LD=" + cc, "AR=" + ar,
              "CFLAGS.EXTRA=-I" + installPrefix + "/include -fPIC",
              "LDFLAGS.EXTRA=-L" + installPrefix + "/lib"],
             verbose)
            #RunCommand(
             #["make", "glew.lib.mx", "CC=" + cc, "LD=" + cc, "AR=" + ar,
              #"CFLAGS.EXTRA=-I" + installPrefix + "/include -fPIC",
              #"LDFLAGS.EXTRA=-L" + installPrefix + "/lib"],
             #verbose)
            RunCommand(
             ["make", "install", "GLEW_PREFIX=" + installPrefix,
              "GLEW_DEST=" + installPrefix],
             verbose)
            #RunCommand(
             #["make", "install.mx", "GLEW_PREFIX=" + installPrefix,
              #"GLEW_DEST=" + installPrefix],
             #verbose)
    except CommandError:
        print("VGAZER: Unable to install", software)
        raise InstallError(software + " not installed")

    print("VGAZER:", software, "installed")
