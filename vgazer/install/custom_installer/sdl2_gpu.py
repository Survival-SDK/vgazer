import os

from vgazer.command         import RunCommand
from vgazer.config.cmake    import ConfigCmake
from vgazer.exceptions      import CommandError
from vgazer.exceptions      import InstallError
from vgazer.platform        import GetArFullPath
from vgazer.platform        import GetCc
from vgazer.platform        import GetInstallPrefix
from vgazer.store.temp      import StoreTemp
from vgazer.working_dir     import WorkingDir

def GetVersionFromSource(filename):
    with open(filename) as f:
        data = f.read()
    lines = data.splitlines()
    for line in lines:
        if "#define SDL_GPU_VERSION_MAJOR" in line:
            versionMajor = line.split(" ")[2]
        if "#define SDL_GPU_VERSION_MINOR" in line:
            versionMinor = line.split(" ")[2]
        if "#define SDL_GPU_VERSION_PATCH" in line:
            versionPatch = line.split(" ")[2]

    return "{major}.{minor}.{patch}".format(major=versionMajor,
     minor=versionMinor, patch=versionPatch)

def Install(auth, software, platform, platformData, mirrors, verbose):
    configCmake = ConfigCmake(platformData)
    configCmake.GenerateCrossFile()
    installPrefix = GetInstallPrefix(platformData)
    ar = GetArFullPath(platformData["target"])
    cc = GetCc(platformData["target"])

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
        sdlGpuHeader = os.path.join(clonedDir, "include/SDL_gpu.h")
        version = GetVersionFromSource(sdlGpuHeader)
        buildDir = os.path.join(clonedDir, "build")
        with WorkingDir(buildDir):
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
              "-o", "../src/externals/stb_image_write/stb_image_write.o",
              "-O2", "-Wall", "-mmmx", "-msse", "-msse2", "-mfpmath=sse",
              "-fPIC", "-I" + installPrefix + "/include"],
             verbose)
            RunCommand(
             [ar, "rcs", "../src/externals/stb_image_write/libstbi_write.a",
              "../src/externals/stb_image_write/stb_image_write.o"],
             verbose)
            RunCommand(
             [
              "cmake", "..", "-G", "Unix Makefiles",
              "-DCMAKE_TOOLCHAIN_FILE=" + configCmake.GetCrossFileName(),
              "-DCMAKE_INSTALL_PREFIX=" + installPrefix,
              "-DSDL_gpu_BUILD_DEMOS=OFF", "-DSDL_gpu_USE_SYSTEM_GLEW=ON",
              "-DSTBI_INCLUDE_DIR=" + installPrefix + "/include",
              "-DSTBI_LIBRARY=" + buildDir
              + "/../src/externals/stb_image/libstbi.a",
              "-DSTBI_FOUND=TRUE",
              "-DSTBI_WRITE_INCLUDE_DIR=" + installPrefix + "/include",
              "-DSTBI_WRITE_LIBRARY=" + buildDir
              + "/../src/externals/stb_image_write/libstbi_write.a",
              "-DSTBI_WRITE_FOUND=TRUE",
              "-DCMAKE_VERBOSE_MAKEFILE:BOOL=ON", "-DCMAKE_AR=" + ar
             ],
             verbose)
            RunCommand(["make"], verbose)
            RunCommand(["make", "install"], verbose)
            RunCommand(
             ["mv",
              installPrefix + "/SDL_gpu-" + version + "/lib/libSDL2_gpu.so",
              installPrefix + "/lib/libSDL2_gpu.so"],
             verbose)
            RunCommand(
             ["mv",
              installPrefix + "/SDL_gpu-" + version + "/lib/libSDL2_gpu.a",
              installPrefix + "/lib/libSDL2_gpu.a"],
             verbose)
            RunCommand(
             ["rm", "-rf", installPrefix + "/SDL_gpu-" + version],
             verbose)
    except CommandError:
        print("VGAZER: Unable to install", software)
        raise InstallError(software + " not installed")

    print("VGAZER:", software, "installed")
