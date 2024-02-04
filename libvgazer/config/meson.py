from vgazer.exceptions  import UnknownTargetArch
from vgazer.platform    import GetAr
from vgazer.platform    import GetCc
from vgazer.platform    import GetCmake
from vgazer.platform    import GetCxx
from vgazer.platform    import GetPkgConfig
from vgazer.platform    import GetStrip
from vgazer.platform    import Platform
from vgazer.store.temp  import StoreTemp

class ConfigMeson():
    def __init__(self, platformData):
        self.storeTemp = StoreTemp(".vgazer/meson")
        self.crossFileName = self.storeTemp.GetDirectoryFilePath("cross-file")
        self.storeTemp.ResolveDirectory()
        self.platformData = platformData

    def GetCrossFileName(self):
        return self.crossFileName

    def GenerateCrossFile(self):
        print("VGAZER: Generating Meson cross-build definition file...")
        ar = GetAr(self.platformData["target"])
        cc = GetCc(self.platformData["target"])
        cxx = GetCxx(self.platformData["target"])
        pkgConfig = GetPkgConfig(self.platformData["target"])
        strip = GetStrip(self.platformData["target"])
        cmake = GetCmake(self.platformData["target"])
        genericOs = Platform.GetGenericOs(self.platformData["target"].GetOs())
        if self.platformData["target"].GetArch() == "x86_64":
            mesonCpuFamily = "x86_64"
            mesonCpu = "x86_64"
        else:
            raise UnknownTargetArch(
             "Unknown target architecture: "
              + self.platformData["target"].GetArch()
            )

        self.storeTemp.DirectoryWriteTextFile("cross-file",
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
