from libvgazer.software.a_f       import data as a_f
from libvgazer.software.g_i       import data as g_i
from libvgazer.software.j_libm    import data as j_libm
from libvgazer.software.libo_libz import data as libo_libz
from libvgazer.software.lin_o     import data as lin_o
from libvgazer.software.p_s       import data as p_s
from libvgazer.software.t_xc      import data as t_xc
from libvgazer.software.xd_z      import data as xd_z

class SoftwareData:
    def __init__(self, customData={}):
        self.data = {
            **a_f,
            **g_i,
            **j_libm,
            **libo_libz,
            **lin_o,
            **p_s,
            **t_xc,
            **xd_z,
            **customData,
        }

    def AddData(self, customData):
        self.data = {**self.data, **customData}

    def GetData(self):
        return self.data
