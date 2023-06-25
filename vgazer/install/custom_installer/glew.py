import os
import requests

from vgazer.command         import RunCommand
from vgazer.exceptions      import CommandError
from vgazer.exceptions      import InstallError
from vgazer.install.utils   import SourceforgeDownloadTarballWhileErrorcodeFour
from vgazer.platform        import GetAr
from vgazer.platform        import GetCc
from vgazer.platform        import GetStrip
from vgazer.platform        import GetInstallPrefix
from vgazer.platform        import GetTriplet
from vgazer.store.temp      import StoreTemp
from vgazer.working_dir     import WorkingDir

def Install(auth, software, platform, platformData, mirrors, verbose):
    installPrefix = GetInstallPrefix(platformData)
    targetTriplet = GetTriplet(platformData["target"])
    targetOs = platformData["target"].GetOs()

    cc = GetCc(platformData["target"])
    ar = GetAr(platformData["target"])
    strip = GetStrip(platformData["target"])

    storeTemp = StoreTemp()
    storeTemp.ResolveEmptySubdirectory(software)
    tempPath = storeTemp.GetSubdirectoryPath(software)

    sourceforgeMirrorsManager = mirrors["sourceforge"].CreateMirrorsManager(
     ["https", "http"])

    filename = requests.get(
     "https://sourceforge.net/projects/glew/best_release.json"
    ).json()["release"]["filename"]
    tarballShortFilename = filename.split("/")[-1]

    try:
        with WorkingDir(tempPath):
            SourceforgeDownloadTarballWhileErrorcodeFour(
             sourceforgeMirrorsManager, "glew", filename, verbose)
            RunCommand(
             ["tar", "--verbose", "--extract", "--gzip", "--file",
              tarballShortFilename],
             verbose)
        extractedDir = os.path.join(tempPath, tarballShortFilename[0:-4])
        with WorkingDir(extractedDir):
            if targetOs == "windows":
                RunCommand(
                 ["make", "-j{cores_count}".format(cores_count=os.cpu_count()),
                  "glew.lib.static", "SYSTEM=linux-mingw64",
                  "HOST=" + targetTriplet, "AR=" + ar, "STRIP=" + strip,
                  "CFLAGS.EXTRA=-I" + installPrefix + "/include -fPIC",
                  "LDFLAGS.EXTRA=-L" + installPrefix + "/lib"],
                 verbose)
                RunCommand(
                 ["make", "install.include", "SYSTEM=linux-mingw64",
                  "GLEW_PREFIX=" + installPrefix,
                  "GLEW_DEST=" + installPrefix],
                 verbose)
                if not os.path.exists(installPrefix + "/lib"):
                    RunCommand(["mkdir", "-p", installPrefix + "/lib"],
                     verbose)
                RunCommand(["cp", "lib/libglew32.a", installPrefix + "/lib"],
                 verbose)
                RunCommand(
                 ["make", "install.pkgconfig", "SYSTEM=linux-mingw64",
                  "GLEW_PREFIX=" + installPrefix,
                  "GLEW_DEST=" + installPrefix],
                 verbose)
            else:
                RunCommand(
                 ["make", "-j{cores_count}".format(cores_count=os.cpu_count()),
                  "glew.lib", "CC=" + cc, "LD=" + cc, "AR=" + ar,
                  "STRIP=" + strip,
                  "CFLAGS.EXTRA=-I" + installPrefix + "/include -fPIC",
                  "LDFLAGS.EXTRA=-L" + installPrefix + "/lib"],
                 verbose)
                RunCommand(
                 ["make", "install", "GLEW_PREFIX=" + installPrefix,
                  "GLEW_DEST=" + installPrefix],
                 verbose)
    except CommandError:
        print("VGAZER: Unable to install", software)
        raise InstallError(software + " not installed")

    print("VGAZER:", software, "installed")
