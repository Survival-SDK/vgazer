import os

from libvgazer.command      import GetCommandOutputUtf8
from libvgazer.command      import RunCommand
from libvgazer.config.meson import ConfigMeson
from libvgazer.exceptions   import CommandError
from libvgazer.exceptions   import InstallError
from libvgazer.platform     import GetInstallPrefix
from libvgazer.store.temp   import StoreTemp
from libvgazer.working_dir  import WorkingDir

def Install(auth, software, platform, platformData, mirrors, verbose):
    configMeson = ConfigMeson(platformData)
    configMeson.GenerateCrossFile()

    installPrefix = GetInstallPrefix(platformData)

    storeTemp = StoreTemp()
    storeTemp.ResolveEmptySubdirectory(software)
    tempPath = storeTemp.GetSubdirectoryPath(software)

    tags = auth["base"].GetJson(
     "https://gitlab.freedesktop.org/api/v4/projects/788/repository/tags")

    tarballUrl = (
     "https://gitlab.freedesktop.org/api/v4/projects/788/repository/"
     "archive.tar.gz?sha=" + tags[0]["name"]
    )
    tarballShortFilename = tarballUrl.split("/")[-1]

    try:
        with WorkingDir(tempPath):
            RunCommand(["wget", "-P", "./", tarballUrl], verbose)
            RunCommand(
             [
              "tar", "--verbose", "--extract", "--gzip", "--file",
              tarballShortFilename
             ],
             verbose)
            output = GetCommandOutputUtf8(
             ["tar", "--list", "--file", tarballShortFilename]
            )
        extractedDir = os.path.join(tempPath,
         output.splitlines()[0].split("/")[0])
        with (WorkingDir(extractedDir)):
            RunCommand(
             ["meson", "setup", "build/",
              "--prefix={prefix}".format(prefix=installPrefix), "--cross-file",
              configMeson.GetCrossFileName()
             ],
             verbose)
            RunCommand(["ninja", "-C", "build/", "install"], verbose)
    except CommandError:
        print("VGAZER: Unable to install", software)
        raise InstallError("{software} not installed".format(software=software))

    print("VGAZER:", software, "installed")