import os

from vgazer.command     import RunCommand
from vgazer.env_vars    import SetEnvVar
from vgazer.exceptions  import CommandError
from vgazer.exceptions  import InstallError
from vgazer.platform    import GetAr
from vgazer.platform    import GetCc
from vgazer.platform    import GetCxx
from vgazer.platform    import GetInstallPrefix
from vgazer.store.temp  import StoreTemp
from vgazer.working_dir import WorkingDir

def Install(auth, software, platform, platformData, verbose):
    installPrefix = GetInstallPrefix(platformData)
    ar = GetAr(platformData["target"])
    cc = GetCc(platformData["target"])
    cxx = GetCxx(platformData["target"])

    storeTemp = StoreTemp()
    storeTemp.ResolveEmptySubdirectory(software)
    tempPath = storeTemp.GetSubdirectoryPath(software)

    try:
        with WorkingDir(tempPath):
            RunCommand(
             ["git", "clone", "https://github.com/grimfang4/sdl-gpu.git",
              "sdl2-gpu"],
            verbose)
        clonedDir = os.path.join(tempPath, "sdl2-gpu")
        with WorkingDir(clonedDir):
            RunCommand(["mkdir", "build"], verbose)
        buildDir = os.path.join(clonedDir, "build")
        with WorkingDir(buildDir):
            SetEnvVar("CC", cc)
            SetEnvVar("CXX", cxx)
            RunCommand(
             [cc, "-c", "../src/externals/stb_image/stb_image.c",
              "-o", "../src/externals/stb_image/stb_image.o", "-O2", "-Wall",
              "-mmmx", "-msse", "-msse2", "-mfpmath=sse", "-fPIC",
              "-I" + installPrefix + "/include"],
             verbose)
            RunCommand(
             [ar, "rcs", "../src/externals/stb_image/libstbi.a",
              "../src/externals/stb_image/stb_image.o"],
             verbose)
            RunCommand(
             [cc, "-c", "../src/externals/stb_image_write/stb_image_write.c",
              "-o", "../src/externals/stb_image_write/stb_image_write.o", "-O2",
              "-Wall", "-mmmx", "-msse", "-msse2", "-mfpmath=sse", "-fPIC",
              "-I" + installPrefix + "/include"],
             verbose)
            RunCommand(
             [ar, "rcs", "../src/externals/stb_image_write/libstbi_write.a",
              "../src/externals/stb_image_write/stb_image_write.o"],
             verbose)
            RunCommand(
             ["cmake", "..", "-G", "Unix Makefiles",
              "-DCMAKE_INSTALL_PREFIX=" + installPrefix,
              "-DSDL_gpu_BUILD_DEMOS=OFF", "-DSDL_gpu_USE_SYSTEM_GLEW=ON",
              "-DSTBI_INCLUDE_DIR=" + installPrefix + "/include",
              "-DSTBI_LIBRARY=" + buildDir + "/../src/externals/stb_image/libstbi.a",
              "-DSTBI_FOUND=TRUE"
              "-DSTBI_WRITE_INCLUDE_DIR=" + installPrefix + "/include",
              "-DSTBI_WRITE_LIBRARY=" + buildDir + "/../src/externals/stb_image_write/libstbi_write.a",
              "-DSTBI_WRITE_FOUND=TRUE"
             ],
            verbose)
            RunCommand(["make"], verbose)
            RunCommand(["make", "install"], verbose)
    except CommandError:
        print("Unable to install", software)
        raise InstallError(software + " not installed")

    print(software, "installed")
