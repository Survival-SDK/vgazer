import os

from vgazer.command              import RunCommand
from vgazer.exceptions           import CommandError
from vgazer.exceptions           import GithubApiError
from vgazer.exceptions           import InstallError
from vgazer.exceptions           import VersionCheckError
from vgazer.github_api_error_mgr import GithubApiErrorMgr
from vgazer.platform             import GetInstallPrefix
from vgazer.platform             import GetTriplet
from vgazer.store.temp           import StoreTemp
from vgazer.working_dir          import WorkingDir

def getLatestVersion(branches, software):
    maxMajor = -1
    maxMinor = -1

    for branch in branches:
        if not branch["name"].startswith("v"):
            continue

        tokens = branch["name"][1:].split(".")
        major = int(tokens[0])
        minor = int(tokens[1])

        if major > maxMajor:
            maxMajor = major
            maxMinor = 0
            continue

        if major == maxMajor and minor > maxMinor:
            maxMinor = minor
            continue

    if maxMajor == -1 or maxMinor == -1:
        raise VersionCheckError(
         "Unable to get last version of {software}".format(software=software))

    return "v{major}.{minor}".format(major=maxMajor, minor=maxMinor)

def Install(auth, software, platform, platformData, mirrors, verbose):
    installPrefix = GetInstallPrefix(platformData)
    triplet = GetTriplet(platformData["target"])

    storeTemp = StoreTemp()
    storeTemp.ResolveEmptySubdirectory(software)
    tempPath = storeTemp.GetSubdirectoryPath(software)

    try:
        branches = auth["github"].GetJson(
         "https://api.github.com/repos/LuaJIT/LuaJIT/branches")
    except ConnectionError:
        print("VGAZER: Unable to know last version of", software)
        raise InstallError("{software} not installed".format(software=software))

    with GithubApiErrorMgr(branches, "LuaJIT/LuaJIT") as errMgr:
        if errMgr.IsErrorOccured():
            raise GithubApiError(errMgr.GetErrorText())

    try:
        latest = getLatestVersion(branches, software)
    except VersionCheckError:
        print("VGAZER: Unable to know last version branch of", software)
        print("VGAZER: Building master branch")
        latest = "master"

    try:
        with WorkingDir(tempPath):
            RunCommand(["git", "clone", "https://github.com/LuaJIT/LuaJIT.git"],
             verbose)
        clonedDir = os.path.join(tempPath, "LuaJIT")
        with WorkingDir(clonedDir):
            RunCommand(["git", "checkout", latest], verbose)
            RunCommand(
             [
              "make", "-j{cores_count}".format(cores_count=os.cpu_count()),
              "CFLAGS=-fPIC", "BUILDMODE=static",
              "CROSS={triplet}-".format(triplet=triplet),
              "TARGET_SYS={os}".format(
               os=platformData["target"].GetOs().capitalize())
             ],
             verbose)
            RunCommand(
             ["make", "install",
              "PREFIX={prefix}".format(prefix=installPrefix)],
             verbose)
    except CommandError:
        print("VGAZER: Unable to install", software)
        raise InstallError("{software} not installed".format(software=software))

    print("VGAZER:", software, "installed")
