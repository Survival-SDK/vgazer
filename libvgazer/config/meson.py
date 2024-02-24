from libvgazer.exceptions import UnknownTargetArch
from libvgazer.platform   import GetAr
from libvgazer.platform   import GetCc
from libvgazer.platform   import GetCmake
from libvgazer.platform   import GetCxx
from libvgazer.platform   import GetPkgConfig
from libvgazer.platform   import GetStrip
from libvgazer.platform   import Platform
from libvgazer.store.temp import StoreTemp

class ConfigMeson():
    def __init__(self, platformData):
        print("VGAZER: Generating Meson cross-build definition file...")

        storeTemp = StoreTemp(".vgazer/meson")
        self.crossFileName = storeTemp.GetDirectoryFilePath("cross-file")
        storeTemp.ResolveDirectory()
        platformData = platformData

        ar = GetAr(platformData["target"])
        cc = GetCc(platformData["target"])
        cxx = GetCxx(platformData["target"])
        pkgConfig = GetPkgConfig(platformData["target"])
        strip = GetStrip(platformData["target"])
        cmake = GetCmake(platformData["target"])
        genericOs = Platform.GetGenericOs(platformData["target"].GetOs())
        if platformData["target"].GetArch() == "x86_64":
            mesonCpuFamily = "x86_64"
            mesonCpu = "x86_64"
        else:
            raise UnknownTargetArch(
             "Unknown target architecture: {arch}".format(
              arch=platformData["target"].GetArch())
            )

        storeTemp.DirectoryWriteTextFile("cross-file",
         "[binaries]\n"
         "c = '{cc}'\n"
         "cpp = '{cxx}'\n"
         "ar = '{ar}'\n"
         "strip = '{strip}'\n"
         "pkgconfig = '{pkgConfig}'\n"
         "cmake = '{cmake}'\n"
         "\n"
         "[host_machine]\n"
         "system = '{genericOs}'\n"
         "cpu_family = '{mesonCpuFamily}'\n"
         "cpu = '{mesonCpu}'\n"
         "endian = 'little'".format(ar=ar, cc=cc, cmake=cmake, cxx=cxx,
          pkgConfig=pkgConfig, strip=strip, genericOs=genericOs,
          mesonCpuFamily=mesonCpuFamily, mesonCpu=mesonCpu)
        )

    def __enter__(self):
        return self.crossFileName

    def __exit__(self, etype, value, traceback):
        pass
