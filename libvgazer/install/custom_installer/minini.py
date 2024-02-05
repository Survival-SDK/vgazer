import os

from libvgazer.command              import GetCommandOutputUtf8
from libvgazer.command              import RunCommand
from libvgazer.exceptions           import CommandError
from libvgazer.exceptions           import GithubApiError
from libvgazer.exceptions           import InstallError
from libvgazer.github_api_error_mgr import GithubApiErrorMgr
from libvgazer.platform             import GetAr
from libvgazer.platform             import GetCc
from libvgazer.platform             import GetInstallPrefix
from libvgazer.store.temp           import StoreTemp
from libvgazer.working_dir          import WorkingDir

def Install(auth, software, platform, platformData, mirrors, verbose):
    installPrefix = GetInstallPrefix(platformData)

    cc = GetCc(platformData["target"])
    ar = GetAr(platformData["target"])

    storeTemp = StoreTemp()
    storeTemp.ResolveEmptySubdirectory(software)
    tempPath = storeTemp.GetSubdirectoryPath(software)

    try:
        releases = auth["github"].GetJson(
         "https://api.github.com/repos/compuphase/minIni/releases")
    except ConnectionError:
        print("VGAZER: Unable to know last version of", software)
        raise InstallError(
         "{software} not installed".format(software=software))

    with GithubApiErrorMgr(releases, "compuphase/minIni") as errMgr:
        if errMgr.IsErrorOccured():
            raise GithubApiError(errMgr.GetErrorText())

    tarballUrl = releases[0]["tarball_url"]
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
        with WorkingDir(os.path.join(extractedDir, "dev")):
            RunCommand(
             [cc, "-O2", "-Wall", "-fPIC", "-c", "minIni.c", "-o", "minIni.o"],
             verbose)
            RunCommand([ar, "rcs", "libminini.a", "minIni.o"], verbose)
            if not os.path.exists(
             "{prefix}/include".format(prefix=installPrefix)):
                RunCommand(
                 [
                  "mkdir", "-p",
                  "{prefix}/include".format(prefix=installPrefix)
                 ],
                 verbose)
            if not os.path.exists("{prefix}/lib".format(prefix=installPrefix)):
                RunCommand(
                 ["mkdir", "-p", "{prefix}/lib".format(prefix=installPrefix)],
                 verbose)
            RunCommand(
             [
              "mkdir", "-p",
              "{prefix}/include/minINI".format(prefix=installPrefix)
             ],
             verbose)
            RunCommand(
             [
              "sh", "-c",
              "cp ./*.h {prefix}/include/minINI".format(prefix=installPrefix)
             ],
             verbose)
            RunCommand(
             [
              "cp", "./libminini.a",
              "{prefix}/lib".format(prefix=installPrefix)
             ],
             verbose)
    except CommandError:
        print("VGAZER: Unable to install", software)
        raise InstallError(
         "{software} not installed".format(software=software))

    print("VGAZER:", software, "installed")
