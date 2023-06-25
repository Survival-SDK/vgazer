import os
import requests
from bs4 import BeautifulSoup

from vgazer.command         import RunCommand
from vgazer.exceptions      import CommandError
from vgazer.exceptions      import InstallError
from vgazer.platform        import GetInstallPrefix
from vgazer.platform        import GetTriplet
from vgazer.store.temp      import StoreTemp
from vgazer.working_dir     import WorkingDir

def GetPubSubdir():
    response = requests.get(
     "https://mirrors.edge.kernel.org/pub/linux/utils/util-linux/")
    html = response.content.decode("utf-8")
    parsedHtml = BeautifulSoup(html, "html.parser")

    links = parsedHtml.find_all("a")

    return ("https://mirrors.edge.kernel.org/pub/linux/utils/util-linux/"
     + links[-1]["href"] + "/")

def GetTarballUrl():
    pubSubdir = GetPubSubdir()

    response = requests.get(pubSubdir)
    html = response.content.decode("utf-8")
    parsedHtml = BeautifulSoup(html, "html.parser")

    links = parsedHtml.find_all("a")

    maxVersionRc = -1
    for link in links:
        if ("util-linux-" in link.text and ".tar.gz" in link.text):
            if len(link.text.split("-")) == 3:
                return pubSubdir + link["href"]

            versionRc = int(
             link.text.split("-")[3].split(".")[0].split("rc")[1])

            if versionRc > maxVersionRc:
                maxVersionRc = versionRc
                maxVersionUrl = pubSubdir + link["href"]

    return maxVersionUrl

def Install(auth, software, platform, platformData, mirrors, verbose):
    installPrefix = GetInstallPrefix(platformData)
    targetTriplet = GetTriplet(platformData["target"])

    storeTemp = StoreTemp()
    storeTemp.ResolveEmptySubdirectory(software)
    tempPath = storeTemp.GetSubdirectoryPath(software)

    tarballUrl = GetTarballUrl()
    tarballShortFilename = tarballUrl.split("/")[-1]

    try:
        with WorkingDir(tempPath):
            RunCommand(["wget", "-P", "./", tarballUrl], verbose)
            RunCommand(
             ["tar", "--verbose", "--extract", "--gzip", "--file",
              tarballShortFilename],
             verbose)
        extractedDir = os.path.join(tempPath,
         tarballShortFilename.split(".tar.gz")[0])
        with WorkingDir(extractedDir):
            RunCommand(["./autogen.sh"], verbose)
            RunCommand(
             [
              "./configure", "--prefix=" + installPrefix,
              "--host=" + targetTriplet, "--disable-static",
              "--disable-all-programs", "--enable-libblkid",
              "--enable-libmount"
             ],
             verbose)
            RunCommand(
             ["make", "-j{cores_count}".format(cores_count=os.cpu_count())],
             verbose)
            RunCommand(["make", "install"], verbose)
    except CommandError:
        print("VGAZER: Unable to install", software)
        raise InstallError(software + " not installed")

    print("VGAZER:", software, "installed")
