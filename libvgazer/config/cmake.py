from libvgazer.platform   import GetAr
from libvgazer.platform   import GetCc
from libvgazer.platform   import GetCxx
from libvgazer.platform   import GetInstallPrefix
from libvgazer.platform   import GetTriplet
from libvgazer.platform   import Platform
from libvgazer.store.temp import StoreTemp

class ConfigCmake():
    def __init__(self, platformData, cflags=None):
        print("VGAZER: Generating CMake toolchain file...")
        
        storeTemp = StoreTemp(".vgazer/cmake")
        self.crossFileName = storeTemp.GetDirectoryFilePath("toolchain.cmake")
        storeTemp.ResolveDirectory()

        cmakeOs = Platform.GetGenericOs(
         platformData["target"].GetOs()).capitalize()
        prefix = GetInstallPrefix(platformData)
        targetTriplet = GetTriplet(platformData["target"])

        cc = GetCc(platformData["target"])
        cxx = GetCxx(platformData["target"])
        ar = GetAr(platformData["target"])

        pkgConfigLibdirs = ("/usr/{triplet}/lib/pkgconfig"
         ":{prefix}/lib/pkgconfig:{prefix}/share/pkgconfig"
         ":/usr/lib/{triplet}/pkgconfig").format(
          prefix=prefix,
          triplet=targetTriplet
         )

        if platformData["target"].IsHost():
            findMode = "BOTH"
            pkgConfigLibdirs += ":/usr/share/pkgconfig:/usr/lib/pkgconfig"
        else:
            findMode = "ONLY"

        storeTemp.DirectoryWriteTextFile("toolchain.cmake",
         "set(CMAKE_SYSTEM_NAME {cmakeOs})\n"
         "set(CMAKE_SYSTEM_PROCESSOR {cpu})\n"
         "set(CMAKE_C_COMPILER {cc})\n"
         "set(CMAKE_C_FLAGS {cflags})\n"
         "set(CMAKE_CXX_COMPILER {cxx})\n"
         "set(CMAKE_AR {ar})\n"
         "set(CMAKE_FIND_ROOT_PATH {prefix})\n"
         "SET("
          "ENV{{PKG_CONFIG_LIBDIR}} "
          "{pkgConfigLibdirs}"
         ")\n"
         "SET(CMAKE_FIND_ROOT_PATH_MODE_PROGRAM NEVER)\n"
         "SET(CMAKE_FIND_ROOT_PATH_MODE_LIBRARY {findMode})\n"
         "SET(CMAKE_FIND_ROOT_PATH_MODE_INCLUDE {findMode})".format(
          cmakeOs=cmakeOs,
          cpu=platformData["target"].GetArch(),
          cc=cc,
          cflags=cflags if cflags is not None else "",
          cxx=cxx,
          ar=ar,
          prefix=prefix,
          pkgConfigLibdirs=pkgConfigLibdirs,
          findMode=findMode
         )
        )

    def __enter__(self):
        return self.crossFileName

    def __exit__(self, etype, value, traceback):
        pass
