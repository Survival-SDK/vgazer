import os

from vgazer.command              import GetCommandOutputUtf8
from vgazer.command              import RunCommand
from vgazer.exceptions           import CommandError
from vgazer.exceptions           import InstallError
from vgazer.platform             import GetInstallPrefix
from vgazer.store.temp           import StoreTemp
from vgazer.working_dir          import WorkingDir

def Install(auth, software, platform, platformData, mirrors, verbose):
    installPrefix = GetInstallPrefix(platformData)
    storeTemp = StoreTemp()
    storeTemp.ResolveEmptySubdirectory(software)
    tempPath = storeTemp.GetSubdirectoryPath(software)

    try:
        tags = auth["base"].GetJson(
         "https://gitlab.freedesktop.org/api/v4/projects/798/repository/tags")

        tarballUrl = (
         "https://gitlab.freedesktop.org/api/v4/projects/798/repository/"
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
        with WorkingDir(extractedDir):
            RunCommand(["./autogen.sh",
             "--prefix={prefix}".format(prefix=installPrefix),
             "PKG_CONFIG_PATH={prefix}/lib/pkgconfig:"
             "{prefix}/share/pkgconfig".format(prefix=installPrefix)], verbose)
            RunCommand(["make", "install"], verbose)
    except CommandError:
        print("VGAZER: Unable to install", software)
        raise InstallError(software + " not installed")

    print("VGAZER:", software, "installed")
