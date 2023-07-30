import os

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

    tags = auth["base"].GetJson(
     "https://gitlab.freedesktop.org/api/v4/projects/714/repository/tags")

    tarballUrl = (
     "https://gitlab.freedesktop.org/api/v4/projects/714/repository/"
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
        with (WorkingDir(extractedDir),
         EnvVar("ACLOCAL", "aclocal -I {prefix}/share/aclocal".format(
          prefix=installPrefix))):
            RunCommand(
             ["./autogen.sh", "--host=" + targetTriplet,
              "--prefix=" + installPrefix,
              "PKG_CONFIG_PATH=" + installPrefix + "/lib/pkgconfig"],
             verbose)
            RunCommand(
             ["make", "-j{cores_count}".format(cores_count=os.cpu_count())],
             verbose)
            RunCommand(["make", "install"], verbose)
    except CommandError:
        print("VGAZER: Unable to install", software)
        raise InstallError(software + " not installed")

    print("VGAZER:", software, "installed")
