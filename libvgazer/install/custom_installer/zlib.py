import os

from libvgazer.command     import RunCommand
from libvgazer.exceptions  import CommandError
from libvgazer.exceptions  import InstallError
from libvgazer.platform    import GetInstallPrefix
from libvgazer.platform    import GetTriplet
from libvgazer.store.temp  import StoreTemp
from libvgazer.version.git import GetLastTag
from libvgazer.working_dir import WorkingDir

def Install(software, platform, platformData, verbose):
    installPrefix = GetInstallPrefix(platformData)
    targetTriplet = GetTriplet(platformData["target"])
    targetOs = platformData["target"].GetOs()

    storeTemp = StoreTemp()
    storeTemp.ResolveEmptySubdirectory(software)
    tempPath = storeTemp.GetSubdirectoryPath(software)

    try:
        with WorkingDir(tempPath):
            RunCommand(
             ["git", "clone", "https://github.com/madler/zlib.git", "."],
             verbose)
            RunCommand(
             [
              "git", "checkout",
              GetLastTag("https://github.com/madler/zlib.git")
             ],
             verbose)
            if targetOs == "windows":
                RunCommand(
                 [
                  "make", "-j{cores_count}".format(cores_count=os.cpu_count()),
                  "-f", "./win32/Makefile.gcc", "PREFIX=" + targetTriplet + "-"
                 ],
                 verbose
                )
                if not os.path.exists(installPrefix + "/include"):
                    RunCommand(["mkdir", "-p", installPrefix + "/include"],
                     verbose)
                if not os.path.exists(installPrefix + "/lib"):
                    RunCommand(["mkdir", "-p", installPrefix + "/lib"],
                     verbose)
                RunCommand(
                 ["make", "install", "-f", "./win32/Makefile.gcc",
                  "prefix=" + installPrefix,
                  "BINARY_PATH=" + installPrefix + "/bin",
                  "INCLUDE_PATH=" + installPrefix + "/include",
                  "LIBRARY_PATH=" + installPrefix + "/lib"],
                 verbose)
            else:
                RunCommand(
                 ["./configure", "--prefix=" + installPrefix], verbose)
                RunCommand(
                 [
                  "make",
                  "-j{cores_count}".format(cores_count=os.cpu_count())
                 ],
                 verbose)
                RunCommand(["make", "install"], verbose)
    except CommandError:
        print("VGAZER: Unable to install", software)
        raise InstallError(software + " not installed")

    print("VGAZER:", software, "installed")
