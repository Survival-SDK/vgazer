from vgazer.command         import RunCommand
from vgazer.exceptions      import CommandError
from vgazer.exceptions      import InstallError
from vgazer.platform        import GetInstallPrefix

def Install(auth, software, platform, platformData, verbose):
    installPrefix = GetInstallPrefix(platformData)

    url = "https://raw.githubusercontent.com/mackron/dr_libs/master/dr_wav.h"

    try:
        if not os.path.exists(installPrefix + "/include"):
            RunCommand(["mkdir", "-p", installPrefix + "/include"], verbose)
        RunCommand(["wget", "-P", installPrefix + "/include", url], verbose)
    except CommandError:
        print("Unable to install", software)
        raise InstallError(software + " not installed")

    print(software, "installed")
