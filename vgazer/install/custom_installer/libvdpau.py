import os
import requests

from vgazer.command         import GetCommandOutputUtf8
from vgazer.command         import RunCommand
from vgazer.config.meson    import ConfigMeson
from vgazer.env_vars        import SetEnvVar
from vgazer.exceptions      import CommandError
from vgazer.exceptions      import InstallError
from vgazer.platform        import GetInstallPrefix
from vgazer.platform        import GetTriplet
from vgazer.store.temp      import StoreTemp
from vgazer.working_dir     import WorkingDir

def Install(auth, software, platform, platformData, verbose):
    configMeson = ConfigMeson(platformData)
    configMeson.GenerateCrossFile()

    installPrefix = GetInstallPrefix(platformData)

    storeTemp = StoreTemp()
    storeTemp.ResolveEmptySubdirectory(software)
    tempPath = storeTemp.GetSubdirectoryPath(software)

    tags = auth["base"].GetJson(
     "https://gitlab.freedesktop.org/api/v4/projects/887/repository/tags")

    tarballUrl = (
     "https://gitlab.freedesktop.org/api/v4/projects/887/repository/"
     "archive.tar.gz?sha=" + tags[0]["name"]
    )
    tarballShortFilename = tarballUrl.split("/")[-1]

    try:
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
        with WorkingDir(extractedDir):
            RunCommand(["mkdir", "build"], verbose)
        SetEnvVar("PKG_CONFIG_PATH", installPrefix + "/lib/pkgconfig")
        buildDir = os.path.join(extractedDir, "build")
        with WorkingDir(buildDir):
            RunCommand(
             ["meson", "--prefix=" + installPrefix,
              "--cross-file",
              configMeson.GetCrossFileName(), "-Ddocumentation=false"],
             verbose)
            RunCommand(
             ["ln", "-s", installPrefix + "/include/X11", "../include/X11"],
             verbose)
            RunCommand(["ninja"], verbose)
            RunCommand(["ninja", "install"], verbose)
            # Meson does not install ".pc" files to properly dirs and it can not
            # be fixed
            RunCommand(["mkdir", "-p", installPrefix + "/lib/pkgconfig"],
             verbose)
            RunCommand(
             [
              "sh",
              "-c",
              "mv " + installPrefix + "/lib/"
               + GetTriplet(platformData["target"]) + "/pkgconfig/* "
               + installPrefix + "/lib/pkgconfig"
             ],
             verbose
            )
    except CommandError:
        print("VGAZER: Unable to install", software)
        raise InstallError(software + " not installed")

    print("VGAZER:", software, "installed")