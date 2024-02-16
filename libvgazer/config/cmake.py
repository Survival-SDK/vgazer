from libvgazer.platform   import GetAr
from libvgazer.platform   import GetCc
from libvgazer.platform   import GetCxx
from libvgazer.platform   import GetInstallPrefix
from libvgazer.platform   import GetTriplet
from libvgazer.platform   import Platform
from libvgazer.store.temp import StoreTemp

class ConfigCmake():
    def __init__(self, platformData):
        self.storeTemp = StoreTemp(".vgazer/cmake")
        self.crossFileName = self.storeTemp.GetDirectoryFilePath(
         "toolchain.cmake")
        self.storeTemp.ResolveDirectory()
        self.platformData = platformData

    def GetCrossFileName(self):
        return self.crossFileName

    def GenerateCrossFile(self):
        print("VGAZER: Generating CMake toolchain file...")
        cmakeOs = Platform.GetGenericOs(
          self.platformData["target"].GetOs()
         ).capitalize()
        prefix = GetInstallPrefix(self.platformData)
        targetTriplet = GetTriplet(self.platformData["target"])

        cc = GetCc(self.platformData["target"])
        cxx = GetCxx(self.platformData["target"])
        ar = GetAr(self.platformData["target"])

        pkgConfigLibdirs = ("/usr/{triplet}/lib/pkgconfig"
         ":{prefix}/lib/pkgconfig:{prefix}/share/pkgconfig"
         ":/usr/lib/{triplet}/pkgconfig").format(
          prefix=prefix,
          triplet=targetTriplet
         )

        if self.platformData["target"].IsHost():
            findMode = "BOTH"
            pkgConfigLibdirs += ":/usr/share/pkgconfig:/usr/lib/pkgconfig"
        else:
            findMode = "ONLY"

        self.storeTemp.DirectoryWriteTextFile("toolchain.cmake",
         "set(CMAKE_SYSTEM_NAME {cmakeOs})\n"
         "set(CMAKE_SYSTEM_PROCESSOR {cpu})\n"
         "set(CMAKE_C_COMPILER {cc})\n"
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
          cpu=self.platformData["target"].GetArch(),
          cc=cc,
          cxx=cxx,
          ar=ar,
          prefix=prefix,
          pkgConfigLibdirs=pkgConfigLibdirs,
          findMode=findMode
         )
        )
