import os

from libvgazer.command     import RunCommand
from libvgazer.exceptions  import CommandError
from libvgazer.exceptions  import InstallError
from libvgazer.platform    import GetInstallPrefix
from libvgazer.platform    import GetTriplet
from libvgazer.store.temp  import StoreTemp
from libvgazer.version.git import GetLastTag
from libvgazer.working_dir import WorkingDir

def Install(software, platform, platformData, mirrors, verbose):
    installPrefix = GetInstallPrefix(platformData)
    targetTriplet = GetTriplet(platformData["target"])

    storeTemp = StoreTemp()
    storeTemp.ResolveEmptySubdirectory(software)
    tempPath = storeTemp.GetSubdirectoryPath(software)

    libs = {
        "linux": "LIBS=-lasound",
        "windows": "",
    }[platformData["target"].GetOs()]

    try:
        with WorkingDir(tempPath):
            RunCommand(
             [
              "git", "clone", "https://github.com/PortAudio/portaudio.git", "."
             ],
             verbose)
            RunCommand(
             [
              "git", "checkout",
              GetLastTag("https://github.com/PortAudio/portaudio.git",
              hint=r'v\d+\.\d\.\d$')
             ],
             verbose)
            RunCommand(
             ["./configure", "--host=" + targetTriplet,
              "--prefix=" + installPrefix, "--disable-shared",
              "--with-alsa=yes", "--with-oss=yes",
              "--with-winapi=wmme,directx,wdmks",
              "LDFLAGS=-L" + installPrefix + "/lib", libs,
              "CPPFLAGS=-I" + installPrefix + "/include"],
             verbose)
            RunCommand(
             ["sed", "-i", "-e",
              "s#CFLAGS = #CFLAGS = -I" + installPrefix + "/include #g",
              "./Makefile"],
             verbose)
            RunCommand(
             ["make", "-j{cores_count}".format(cores_count=os.cpu_count())],
             verbose)
            RunCommand(["make", "install"], verbose)
    except CommandError:
        print("VGAZER: Unable to install", software)
        raise InstallError(software + " not installed")

    print("VGAZER:", software, "installed")
