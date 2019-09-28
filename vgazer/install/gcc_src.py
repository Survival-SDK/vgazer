import os
import requests
from bs4 import BeautifulSoup

from vgazer.command     import RunCommand
from vgazer.exceptions  import CommandError
from vgazer.exceptions  import InstallError
from vgazer.exceptions  import NoSuitableMirrors
from vgazer.exceptions  import UnknownTargetArch
from vgazer.platform    import GetFilesystemType
from vgazer.store.temp  import StoreTemp
from vgazer.working_dir import WorkingDir

def GetVersionStr(versionInfo):
    if versionInfo["versionPatch"] == 0:
        return (str(versionInfo["maxVersionMajor"]) + "."
         + str(versionInfo["maxVersionMinor"]))
    else:
        return (str(versionInfo["maxVersionMajor"]) + "."
         + str(versionInfo["maxVersionMinor"]) + "."
         + str(versionInfo["maxVersionPatch"]))

def InitVersionInfo():
    return {
        "maxVersionMajor": -1,
        "maxVersionMinor": -1,
        "maxVersionPatch": -1,
    }

def UpdateVersionInfo(versionInfo, splitedVersion, versionFilename):
    versionInfo["versionMajor"] = int(splitedVersion[0])
    versionInfo["versionMinor"] = int(splitedVersion[1])
    if len(splitedVersion) == 2:
        versionInfo["versionPatch"] = 0
    elif "a" in splitedVersion[2]:
        versionInfo["versionPatch"] = int(splitedVersion[2][:-1])
    else:
        versionInfo["versionPatch"] = int(splitedVersion[2])

    if versionInfo["versionMajor"] > versionInfo["maxVersionMajor"]:
        versionInfo["maxVersionMajor"] = versionInfo["versionMajor"]
        versionInfo["maxVersionMinor"] = versionInfo["versionMinor"]
        versionInfo["maxVersionPatch"] = versionInfo["versionPatch"]
        versionInfo["maxVersionFilename"] = versionFilename
    elif (versionInfo["versionMajor"] == versionInfo["maxVersionMajor"]
     and versionInfo["versionMinor"] > versionInfo["maxVersionMinor"]):
        versionInfo["maxVersionMinor"] = versionInfo["versionMinor"]
        versionInfo["maxVersionPatch"] = versionInfo["versionPatch"]
        versionInfo["maxVersionFilename"] = versionFilename
    elif (versionInfo["versionMajor"] == versionInfo["maxVersionMajor"]
     and versionInfo["versionMinor"] == versionInfo["maxVersionMinor"]
     and versionInfo["versionPatch"] > versionInfo["maxVersionPatch"]):
        versionInfo["maxVersionPatch"] = versionInfo["versionPatch"]
        versionInfo["maxVersionFilename"] = versionFilename

def GetMirrorUrlFunc(mirrorsManager, firstTry):
    if firstTry:
        return mirrorsManager.GetMirrorUrl
    else:
        return mirrorsManager.GetNewMirrorUrl

def GetLastBinutilsSuburl(auth, mirrorsManager, firstTry = True):
    getMirrorUrl = GetMirrorUrlFunc(mirrorsManager, firstTry)

    try:
        response = requests.get(getMirrorUrl() + "/binutils/")
    except requests.exceptions.ConnectionError:
        return GetLastBinutilsSuburl(auth, mirrorsManager, firstTry = False)
    html = response.content.decode("utf-8")
    parsedHtml = BeautifulSoup(html, "html.parser")

    links = parsedHtml.find_all("a")

    versionInfo = InitVersionInfo()

    for link in links:
        if ("binutils" in link.text and ".tar.gz" in link.text
         and ".sig" not in link.text):
            version = link.text.split("-")[1].split(".tar.gz")[0].split(".")
            UpdateVersionInfo(versionInfo, version, link.text)

    #versionStr = GetVersionStr(versionInfo)

    return "binutils/" + versionInfo["maxVersionFilename"]

def GetLastGccSuburl(auth, mirrorsManager, firstTry = True):
    getMirrorUrl = GetMirrorUrlFunc(mirrorsManager, firstTry)

    try:
        response = requests.get(getMirrorUrl() + "/gcc/")
    except requests.exceptions.ConnectionError:
        return GetLastGccSuburl(auth, mirrorsManager, firstTry = False)
    html = response.content.decode("utf-8")
    parsedHtml = BeautifulSoup(html, "html.parser")

    links = parsedHtml.find_all("a")

    versionInfo = InitVersionInfo()
    for link in links:
        if ("gcc" in link.text and "/" in link.text):
            version = link.text.split("-")[1].split("/")[0].split(".")
            UpdateVersionInfo(versionInfo, version, link.text)

    versionStr = GetVersionStr(versionInfo)

    return ("gcc/" + versionInfo["maxVersionFilename"]
     + versionInfo["maxVersionFilename"][:-1] + ".tar.gz")

def GetLastKernelUrlInSubdir(auth, majorVersion):
    VersionDirUrl = ("https://mirrors.edge.kernel.org/pub/linux/kernel/v"
     + str(majorVersion) + ".x/")

    response = requests.get(VersionDirUrl)
    html = response.content.decode("utf-8")
    parsedHtml = BeautifulSoup(html, "html.parser")

    links = parsedHtml.find_all("a")

    versionInfo = InitVersionInfo()
    for link in links:
        if ("linux" in link.text and ".tar.gz" in link.text):
            version = link.text.split("-")[1].split(".tar.gz")[0].split(".")
            UpdateVersionInfo(versionInfo, version, link.text)

    if versionInfo["maxVersionMajor"] == -1:
        return None

    #versionStr = GetVersionStr(versionInfo)

    return VersionDirUrl + versionInfo["maxVersionFilename"]

def GetLastKernelUrl(auth):
    response = requests.get("https://www.kernel.org/pub/linux/kernel/")
    html = response.content.decode("utf-8")
    parsedHtml = BeautifulSoup(html, "html.parser")

    links = parsedHtml.find_all("a")

    maxVersion = -1
    for link in links:
        if "v" in link.text and "." in link.text:
            version = int(link.text[1:-1].split(".")[0])
            if version > maxVersion:
                maxVersion = version

    url = GetLastKernelUrlInSubdir(auth, maxVersion)
    if url is None:
        return GetLastKernelUrlInSubdir(auth, maxVersion - 1)
    else:
        return url

def GetLastGlibcSuburl(auth, mirrorsManager, firstTry = True):
    getMirrorUrl = GetMirrorUrlFunc(mirrorsManager, firstTry)

    try:
        response = requests.get(getMirrorUrl() + "/glibc/")
    except requests.exceptions.ConnectionError:
        return GetLastGlibcSuburl(auth, mirrorsManager, firstTry = False)
    html = response.content.decode("utf-8")
    parsedHtml = BeautifulSoup(html, "html.parser")

    links = parsedHtml.find_all("a")

    versionInfo = InitVersionInfo()

    for link in links:
        if ("glibc" in link.text and ".tar.gz" in link.text
         and ".sig" not in link.text and "libidn" not in link.text
         and "linuxthreads" not in link.text and "ports" not in link.text
         and "crypt" not in link.text and "localedata" not in link.text):
            version = link.text.split("-")[1].split(".tar.gz")[0].split(".")
            UpdateVersionInfo(versionInfo, version, link.text)

    #versionStr = GetVersionStr(versionInfo)

    return "glibc/" + versionInfo["maxVersionFilename"]

def GetLastMpfrSuburl(auth, mirrorsManager, firstTry = True):
    getMirrorUrl = GetMirrorUrlFunc(mirrorsManager, firstTry)

    try:
        response = requests.get(getMirrorUrl() + "/mpfr/")
    except requests.exceptions.ConnectionError:
        return GetLastMpfrSuburl(auth, mirrorsManager, firstTry = False)
    html = response.content.decode("utf-8")
    parsedHtml = BeautifulSoup(html, "html.parser")

    links = parsedHtml.find_all("a")

    versionInfo = InitVersionInfo()

    for link in links:
        if ("mpfr" in link.text and ".tar.gz" in link.text
         and ".sig" not in link.text):
            version = link.text.split("-")[1].split(".tar.gz")[0].split(".")
            UpdateVersionInfo(versionInfo, version, link.text)

    #versionStr = GetVersionStr(versionInfo)

    return "mpfr/" + versionInfo["maxVersionFilename"]

def GetLastGmpSuburl(auth, mirrorsManager, firstTry = True):
    getMirrorUrl = GetMirrorUrlFunc(mirrorsManager, firstTry)

    try:
        response = requests.get(getMirrorUrl() + "/gmp/")
    except requests.exceptions.ConnectionError:
        return GetLastGmpSuburl(auth, mirrorsManager, firstTry = False)
    html = response.content.decode("utf-8")
    parsedHtml = BeautifulSoup(html, "html.parser")

    links = parsedHtml.find_all("a")

    versionInfo = InitVersionInfo()

    for link in links:
        if ("gmp" in link.text and ".tar.bz2" in link.text
         and ".sig" not in link.text):
            version = link.text.split("-")[1].split(".tar.bz2")[0].split(".")
            UpdateVersionInfo(versionInfo, version, link.text)

    #versionStr = GetVersionStr(versionInfo)

    return "gmp/" + versionInfo["maxVersionFilename"]

def GetLastMpcSuburl(auth, mirrorsManager, firstTry = True):
    getMirrorUrl = GetMirrorUrlFunc(mirrorsManager, firstTry)

    try:
        response = requests.get(getMirrorUrl() + "/mpc/")
    except requests.exceptions.ConnectionError:
        return GetLastMpcSuburl(auth, mirrorsManager, firstTry = False)
    html = response.content.decode("utf-8")
    parsedHtml = BeautifulSoup(html, "html.parser")

    links = parsedHtml.find_all("a")

    versionInfo = InitVersionInfo()

    for link in links:
        if ("mpc" in link.text and ".tar.gz" in link.text
         and ".sig" not in link.text):
            version = link.text.split("-")[1].split(".tar.gz")[0].split(".")
            UpdateVersionInfo(versionInfo, version, link.text)

    #versionStr = GetVersionStr(versionInfo)

    return "mpc/" + versionInfo["maxVersionFilename"]

def GetLastIslUrl(auth):
    response = requests.get("https://gcc.gnu.org/pub/gcc/infrastructure/")
    html = response.content.decode("utf-8")
    parsedHtml = BeautifulSoup(html, "html.parser")

    links = parsedHtml.find_all("a")

    versionInfo = InitVersionInfo()

    for link in links:
        if ("isl" in link.text and ".tar.bz2" in link.text):
            version = link.text.split("-")[1].split(".tar.bz2")[0].split(".")
            UpdateVersionInfo(versionInfo, version, link.text)

    #versionStr = GetVersionStr(versionInfo)

    return ("https://gcc.gnu.org/pub/gcc/infrastructure/"
     + versionInfo["maxVersionFilename"])

def GetLastCloogUrl(auth):
    response = requests.get("https://gcc.gnu.org/pub/gcc/infrastructure/")
    html = response.content.decode("utf-8")
    parsedHtml = BeautifulSoup(html, "html.parser")

    links = parsedHtml.find_all("a")

    versionInfo = InitVersionInfo()

    for link in links:
        if ("cloog" in link.text and ".tar.gz" in link.text
         and "parma" not in link.text and "ppl" not in link.text):
            version = link.text.split("-")[1].split(".tar.gz")[0].split(".")
            UpdateVersionInfo(versionInfo, version, link.text)

    #versionStr = GetVersionStr(versionInfo)

    return ("https://gcc.gnu.org/pub/gcc/infrastructure/"
     + versionInfo["maxVersionFilename"])

def DownloadKeyringWhileErrorcodeFour(gnuWgetMirrorsManager, verbose):
    while True:
        try:
            RunCommand(
             ["wget", "--tries=1", "--timeout=10", "--continue", "-P", "./",
              gnuWgetMirrorsManager.GetMirrorUrl() + "/gnu-keyring.gpg"],
             verbose)
        except CommandError as e:
            if e.errorcode == 4:
                gnuWgetMirrorsManager.ChangeMirror()
            else:
                raise e
        else:
            break

def RunWgetWhileErrorcodeFour(gnuWgetMirrorsManager, suburl, shortFilename,
 verbose):
    while True:
        try:
            RunCommand(
             ["wget", "--tries=1", "--timeout=10", "--continue", "-P", "./",
              gnuWgetMirrorsManager.GetMirrorUrl() + "/" + suburl],
             verbose)
            RunCommand(
             ["wget", "--tries=1", "--timeout=10", "--continue", "-P", "./",
              gnuWgetMirrorsManager.GetMirrorUrl() + "/" + suburl + ".sig"],
             verbose)
            RunCommand(
             ["gpg", "--verify", "--keyring", "./gnu-keyring.gpg",
              shortFilename + ".sig"],
             verbose = True)
        except CommandError as e:
            if (e.command[0] == "wget" and e.errorcode == 4
             or e.command[0] == "gpg" and e.errorcode == 1):
                gnuWgetMirrorsManager.ChangeMirror()
            else:
                raise e
        else:
            break

def InstallGccSrc(auth, software, languages, triplet, platformData, mirrorsGnu,
 verbose):
    compilerTargetArch = triplet.split("-")[0]
    if compilerTargetArch in ["i386", "i486", "i586", "i686", "x86_64"]:
        kernelArch = "x86"
    else:
        raise UnknownTargetArch("Unknown compiler's target arch:",
         compilerTargetArch)

    storeTemp = StoreTemp()
    storeTemp.ResolveEmptySubdirectory(software)
    tempPath = storeTemp.GetSubdirectoryPath(software)

    if (GetFilesystemType(tempPath) == "overlay"
     and platformData["host"].GetOs() == "debian"):
        kernelTar = "bsdtar"
    else:
        kernelTar = "tar"

    gnuWebMirrorsManager = mirrorsGnu.CreateMirrorsManager(["https", "http"])
    gnuWgetMirrorsManager = mirrorsGnu.CreateMirrorsManager(
     ["https", "http", "ftp"])

    try:
        binutilsTarballSuburl = GetLastBinutilsSuburl(auth,
         gnuWebMirrorsManager)
        binutilsTarballShortFilename = binutilsTarballSuburl.split("/")[-1]
        binutilsExtractedDir = binutilsTarballShortFilename[0:-7]
        gccTarballSuburl = GetLastGccSuburl(auth, gnuWebMirrorsManager)
        gccTarballShortFilename = gccTarballSuburl.split("/")[-1]
        gccExtractedDir = gccTarballShortFilename[0:-7]
        kernelTarballUrl = GetLastKernelUrl(auth)
        kernelTarballShortFilename = kernelTarballUrl.split("/")[-1]
        kernelExtractedDir = kernelTarballShortFilename[0:-7]
        glibcTarballSuburl = GetLastGlibcSuburl(auth, gnuWebMirrorsManager)
        glibcTarballShortFilename = glibcTarballSuburl.split("/")[-1]
        glibcExtractedDir = glibcTarballShortFilename[0:-7]
        mpfrTarballSuburl = GetLastMpfrSuburl(auth, gnuWebMirrorsManager)
        mpfrTarballShortFilename = mpfrTarballSuburl.split("/")[-1]
        mpfrExtractedDir = mpfrTarballShortFilename[0:-7]
        gmpTarballSuburl = GetLastGmpSuburl(auth, gnuWebMirrorsManager)
        gmpTarballShortFilename = gmpTarballSuburl.split("/")[-1]
        gmpExtractedDir = gmpTarballShortFilename[0:-8]
        mpcTarballSuburl = GetLastMpcSuburl(auth, gnuWebMirrorsManager)
        mpcTarballShortFilename = mpcTarballSuburl.split("/")[-1]
        mpcExtractedDir = mpcTarballShortFilename[0:-7]
        islTarballUrl = GetLastIslUrl(auth)
        islTarballShortFilename = islTarballUrl.split("/")[-1]
        islExtractedDir = islTarballShortFilename[0:-8]
        cloogTarballUrl = GetLastCloogUrl(auth)
        cloogTarballShortFilename = cloogTarballUrl.split("/")[-1]
        cloogExtractedDir = cloogTarballShortFilename[0:-7]
    except NoSuitableMirrors:
        print("Unable to install", software)
        raise InstallError(software + " not installed")

    try:
        with WorkingDir(tempPath):
            DownloadKeyringWhileErrorcodeFour(gnuWgetMirrorsManager, verbose)
            RunWgetWhileErrorcodeFour(gnuWgetMirrorsManager,
             binutilsTarballSuburl, binutilsTarballShortFilename, verbose)
            RunWgetWhileErrorcodeFour(gnuWgetMirrorsManager, gccTarballSuburl,
             gccTarballShortFilename, verbose)
            RunCommand(["wget", "-P", "./", kernelTarballUrl], verbose)
            RunWgetWhileErrorcodeFour(gnuWgetMirrorsManager, glibcTarballSuburl,
             glibcTarballShortFilename, verbose)
            RunWgetWhileErrorcodeFour(gnuWgetMirrorsManager, mpfrTarballSuburl,
             mpfrTarballShortFilename, verbose)
            RunWgetWhileErrorcodeFour(gnuWgetMirrorsManager, gmpTarballSuburl,
             gmpTarballShortFilename, verbose)
            RunWgetWhileErrorcodeFour(gnuWgetMirrorsManager, mpcTarballSuburl,
             mpcTarballShortFilename, verbose)
            RunCommand(["wget", "-P", "./", islTarballUrl], verbose)
            RunCommand(["wget", "-P", "./", cloogTarballUrl], verbose)
            RunCommand(
             ["tar", "--verbose", "--extract", "--file",
              binutilsTarballShortFilename],
             verbose)
            RunCommand(
             ["tar", "--verbose", "--extract", "--file",
              gccTarballShortFilename],
             verbose)
            RunCommand(
             [kernelTar, "--verbose", "--extract", "--file",
              kernelTarballShortFilename],
             verbose)
            RunCommand(
             ["tar", "--verbose", "--extract", "--file",
              glibcTarballShortFilename],
             verbose)
            RunCommand(
             ["tar", "--verbose", "--extract", "--file",
              mpfrTarballShortFilename],
             verbose)
            RunCommand(
             ["tar", "--verbose", "--extract", "--file",
              gmpTarballShortFilename],
             verbose)
            RunCommand(
             ["tar", "--verbose", "--extract", "--file",
              mpcTarballShortFilename],
             verbose)
            RunCommand(
             ["tar", "--verbose", "--extract", "--file",
              islTarballShortFilename],
             verbose)
            RunCommand(
             ["tar", "--verbose", "--extract", "--file",
              cloogTarballShortFilename],
             verbose)
        gccExtractedFullDir = os.path.join(tempPath, gccExtractedDir)
        with WorkingDir(gccExtractedFullDir):
            RunCommand(["ln", "-s", "../" + mpfrExtractedDir, "mpfr"], verbose)
            RunCommand(["ln", "-s", "../" + gmpExtractedDir, "gmp"], verbose)
            RunCommand(["ln", "-s", "../" + mpcExtractedDir, "mpc"], verbose)
            RunCommand(["ln", "-s", "../" + islExtractedDir, "isl"], verbose)
            RunCommand(["ln", "-s", "../" + cloogExtractedDir, "cloog"],
             verbose)
        with WorkingDir(tempPath):
            RunCommand(["mkdir", "build-binutils"], verbose)
        buildBinutilsDir = os.path.join(tempPath, "build-binutils")
        with WorkingDir(buildBinutilsDir):
            RunCommand(
             ["../" + binutilsExtractedDir + "/configure",
              "--prefix=/usr/local", "--target=" + triplet,
              "--disable-multilib"],
             verbose)
            RunCommand(["make", "-j" + str(os.cpu_count())], verbose)
            RunCommand(["make", "install"], verbose)
        linuxHeadersDir = os.path.join(tempPath, kernelExtractedDir)
        with WorkingDir(linuxHeadersDir):
            RunCommand(
             ["make", "ARCH=" + kernelArch,
              "INSTALL_HDR_PATH=/usr/local/" + triplet, "headers_install"],
             verbose)
        with WorkingDir(tempPath):
            RunCommand(["mkdir", "build-gcc"], verbose)
        buildGccDir = os.path.join(tempPath, "build-gcc")
        with WorkingDir(buildGccDir):
            RunCommand(
             ["../" + gccExtractedDir + "/configure", "--prefix=/usr/local",
              "--target=" + triplet, "--enable-languages=" + languages,
              "--disable-multilib"],
             verbose)
            RunCommand(["make", "-j" + str(os.cpu_count()), "all-gcc"], verbose)
            RunCommand(["make", "install-gcc"], verbose)
        with WorkingDir(tempPath):
            RunCommand(["mkdir", "build-glibc"], verbose)
        buildGlibcDir = os.path.join(tempPath, "build-glibc")
        with WorkingDir(buildGlibcDir):
            # $MACHTYPE is bash variable? It is unavailable in Alpine's sh
            RunCommand(
             [
              "bash",
              "-c",
              "../" + glibcExtractedDir + "/configure "
               "--prefix=/usr/local/" + triplet + " --build=$MACHTYPE "
               "--host=" + triplet + " --target=" + triplet + " "
               "--with-headers=/usr/local/" + triplet + "/include "
               "--disable-multilib libc_cv_forced_unwind=yes"
             ],
             verbose)
            RunCommand(
             ["make", "install-bootstrap-headers=yes", "install-headers"],
             verbose)
            RunCommand(["make", "-j" + str(os.cpu_count()), "csu/subdir_lib"],
             verbose)
            RunCommand(
             ["install", "csu/crt1.o", "csu/crti.o", "csu/crtn.o",
              "/usr/local/" + triplet + "/lib"],
             verbose)
            RunCommand(
             [triplet + "-gcc", "-nostdlib", "-nostartfiles", "-shared", "-x",
              "c", "/dev/null", "-o", "/usr/local/" + triplet + "/lib/libc.so"],
             verbose)
            RunCommand(
             ["touch", "/usr/local/" + triplet + "/include/gnu/stubs.h"],
             verbose)
        with WorkingDir(buildGccDir):
            RunCommand(
             ["make", "-j" + str(os.cpu_count()), "all-target-libgcc"],
             verbose)
            RunCommand(["make", "install-target-libgcc"],
             verbose)
        with WorkingDir(buildGlibcDir):
            RunCommand(["make", "-j" + str(os.cpu_count())], verbose)
            RunCommand(["make", "install"], verbose)
        with WorkingDir(buildGccDir):
            if "linux" in triplet:
                RunCommand(
                 ["sed",  "-i", "-e",
                  "s|#include <limits.h>|#include <linux/limits.h>|g",
                  os.path.join(gccExtractedFullDir,
                   "libsanitizer/asan/asan_linux.cc")
                 ],
                 verbose)
            RunCommand(["make", "-j" + str(os.cpu_count())], verbose)
            RunCommand(["make", "install"], verbose)

    except CommandError:
        print("Unable to install", software)
        raise InstallError(software + " not installed")

    print(software, "installed")
