#!/usr/bin/env python3

import os
import stat

from vgazer             import Vgazer
from vgazer.platform    import Platform

anyPlatform = Platform(arch="any", os="any", osVersion="any", abi="any")

def CreateHostPlatformsList(gazer):
    return [
        Platform(arch=gazer.GetHostPlatform().GetArch(), os="debian",
         osVersion="stretch", abi="gnu", suppressGenericFallback=True),
        Platform(arch=gazer.GetHostPlatform().GetArch(), os="debian",
         osVersion="buster", abi="gnu", suppressGenericFallback=True),
        Platform(arch=gazer.GetHostPlatform().GetArch(), os="debian",
         osVersion="bullseye", abi="gnu", suppressGenericFallback=True),
        Platform(arch=gazer.GetHostPlatform().GetArch(), os="debian",
         osVersion="bookworm", abi="gnu", suppressGenericFallback=True),
        Platform(arch=gazer.GetHostPlatform().GetArch(), os="steamrt",
         osVersion="latest", abi="gnu", suppressGenericFallback=True),
    ]

def CreateTargetPlatformsList(gazer):
    return [
        Platform(arch="x86_64", os="linux", osVersion="any", abi="gnu"),
        Platform(arch="x86_64", os="linux", osVersion="any", abi="musl"),
        Platform(arch="x86_64", os="windows", osVersion="any", abi="mingw32"),
    ]

def AddHostInstallEntries(gazer, installList, hostPlatformsList, software,
 projects):
    for hostPlatform in hostPlatformsList:
        if gazer.ChooseProject(projects, hostPlatform) is not None:
            installList.append([software, hostPlatform, anyPlatform])

def AddTargetInstallEntries(gazer, installList, hostPlatformsList,
 targetPlatformsList, software, projects):
    for hostPlatform in hostPlatformsList:
        for targetPlatform in targetPlatformsList:
            if gazer.ChooseProject(projects, targetPlatform) is not None:
                installList.append([software, hostPlatform, targetPlatform])
        targetPlatform = hostPlatform
        if gazer.ChooseProject(projects, targetPlatform) is not None:
            installList.append([software, hostPlatform, targetPlatform])

def CreateInstallList(gazer, hostPlatformsList, targetPlatformsList):
    installList = []
    softwareData = gazer.GetSoftwareData().GetData().items()
    for software, data in sorted(softwareData):
        if data["platform"] == "host":
            AddHostInstallEntries(gazer, installList, hostPlatformsList,
             software, data["projects"])
        else:
            AddTargetInstallEntries(gazer, installList, hostPlatformsList,
             targetPlatformsList, software, data["projects"])
    return installList

def GetShell(hostPlatform):
    return "/bin/bash"

def GenerateImageLaunchTarget(hostPlatform):
    shell = GetShell(hostPlatform)

    return ("image_{1}_{2}_{3}_launch:\n"
     "\tdocker run --net=host --entrypoint {0} -i -t \\\n"
     "     -v ~/.vgazer:/root/.vgazer -v `pwd`:/mnt/vgazer \\\n"
     "     --entrypoint sh vgazer_min_env_{1}_{2}_{3} \\\n"
     "\n".format(shell, hostPlatform.GetArch(), hostPlatform.GetOs(),
      hostPlatform.GetOsVersion()))

def GenerateCheckPlatformTarget(hostPlatform):
    return ("sample_{0}_{1}_{2}_check_platform:\n"
     "\tdocker run -i -t \\\n"
     "     -v ~/.vgazer:/root/.vgazer \\\n"
     "     -v `pwd`:/mnt/vgazer --entrypoint sh vgazer_min_env_{0}_{1}_{2} \\\n"
     "     -E -c ./samples/check_platform.py\n"
     "\n".format(hostPlatform.GetArch(), hostPlatform.GetOs(),
      hostPlatform.GetOsVersion()))

def GenerateSoftwareVersionsTarget(hostPlatform, targetPlatform):
    if targetPlatform.PlatformsEqual(hostPlatform):
        targetPlatformString = "host"
    else:
        targetPlatformString = "{0}_{1}_{2}".format(targetPlatform.GetArch(),
         targetPlatform.GetOs(), targetPlatform.GetAbi())
    return ("sample_{0}_{1}_{2}_software_versions_{3}:\n"
     "\tdocker run --net=host -i -t \\\n"
     "     -v ~/.vgazer:/root/.vgazer \\\n"
     "     -v `pwd`:/mnt/vgazer --entrypoint sh vgazer_min_env_{0}_{1}_{2} \\\n"
     "     -E -c ./samples/software_versions_{3}.py | tee versions.log\n"
     "\n".format(hostPlatform.GetArch(), hostPlatform.GetOs(),
      hostPlatform.GetOsVersion(), targetPlatformString))

def CreateSoftwareVersionsSample(targetPlatform):
    if targetPlatform is None:
        filename = "samples/software_versions_host.py"
        vgazerArgs = ""
    else:
        filename = "samples/software_versions_{0}_{1}_{2}.py".format(
         targetPlatform.GetArch(), targetPlatform.GetOs(),
         targetPlatform.GetAbi())
        vgazerArgs = 'arch="{0}", os="{1}", osVersion="any", abi="{2}"'.format(
         targetPlatform.GetArch(), targetPlatform.GetOs(),
         targetPlatform.GetAbi())

    with open(filename, "w") as sampleFile:
        sampleFile.write(
         "#!/usr/bin/env python3\n"
         "\n"
         "import os\n"
         "import sys\n"
         "import inspect\n"
         "\n"
         "currentFrame = inspect.currentframe()\n"
         "currentFile = os.path.abspath(inspect.getfile(currentFrame))\n"
         "currentDir = os.path.dirname(currentFile)\n"
         "parentDir = os.path.dirname(currentDir)\n"
         "\n"
         "sys.path.insert(0, parentDir)\n"
         "\n"
         "from vgazer            import Vgazer\n"
         "from vgazer.exceptions import CompatibleProjectNotFound\n"
         "\n"
         "def main():\n"
         "    gazer = Vgazer({0})\n"
         "\n"
         "    print('host:', gazer.GetHostPlatform().GetArch(),\n"
         "     gazer.GetHostPlatform().GetOs(),\n"
         "     gazer.GetHostPlatform().GetOsVersion(),\n"
         "     gazer.GetHostPlatform().GetAbi())\n"
         "    print('target:', gazer.GetTargetPlatform().GetArch(),\n"
         "     gazer.GetTargetPlatform().GetOs(),\n"
         "     gazer.GetTargetPlatform().GetOsVersion(),\n"
         "     gazer.GetTargetPlatform().GetAbi())\n"
         "\n"
         "    softwareData = gazer.GetSoftwareData().GetData().items()\n"
         "    for software, data in sorted(softwareData):\n"
         "        try:\n"
         "            print(software + ':', gazer.CheckVersion(software))\n"
         "        except CompatibleProjectNotFound:\n"
         "            print(software + ':', 'N/A')\n"
         "\n"
         "if __name__ == '__main__':\n"
         "    main()".format(vgazerArgs)
        )
    os.chmod(filename, stat.S_IRUSR | stat.S_IWUSR | stat.S_IXOTH)

def GenerateInstallTarget(installEntry):
    software = installEntry[0]
    hostPlatform = installEntry[1]
    targetPlatform = installEntry[2]
    targetPlatformString = "{0}_{1}_{2}".format(targetPlatform.GetArch(),
     targetPlatform.GetOs(), targetPlatform.GetAbi())
    if targetPlatform.PlatformsEqual(hostPlatform):
        targetInstallString = software + "_host"
    elif targetPlatform == anyPlatform:
        targetInstallString = software
    else:
        targetInstallString = "{0}_{1}".format(software,
         targetPlatformString)
    return ("sample_{0}_{1}_{2}_install_{3}:\n"
     "\tdocker run --net=host -i -t \\\n"
     "     -v ~/.vgazer:/root/.vgazer \\\n"
     "     -v `pwd`:/mnt/vgazer -v `pwd`/.vgazer_{4}:/mnt/vgazer_output \\\n"
     "     --entrypoint sh vgazer_min_env_{0}_{1}_{2} \\\n"
     "     -E -c ./samples/install_{3}.py | tee install.log\n"
     "\n".format(hostPlatform.GetArch(), hostPlatform.GetOs(),
      hostPlatform.GetOsVersion(), targetInstallString, targetPlatformString))

def CreateInstallSample(installEntry):
    software = installEntry[0]
    hostPlatform = installEntry[1]
    targetPlatform = installEntry[2]
    if targetPlatform.PlatformsEqual(hostPlatform):
        filename = "samples/install_" + software + "_host.py"
        vgazerArgs = ""
    elif targetPlatform == anyPlatform:
        filename = "samples/install_" + software + ".py"
        vgazerArgs = ""
    else:
        filename = "samples/install_{3}_{0}_{1}_{2}.py".format(
         targetPlatform.GetArch(), targetPlatform.GetOs(),
         targetPlatform.GetAbi(), software)
        vgazerArgs = 'arch="{0}", os="{1}", osVersion="any", abi="{2}"'.format(
         targetPlatform.GetArch(), targetPlatform.GetOs(),
         targetPlatform.GetAbi())

    with open(filename, "w") as sampleFile:
        sampleFile.write(
         "#!/usr/bin/env python3\n"
         "\n"
         "import os\n"
         "import sys\n"
         "import inspect\n"
         "\n"
         "currentFrame = inspect.currentframe()\n"
         "currentFile = os.path.abspath(inspect.getfile(currentFrame))\n"
         "currentDir = os.path.dirname(currentFile)\n"
         "parentDir = os.path.dirname(currentDir)\n"
         "\n"
         "sys.path.insert(0, parentDir)\n"
         "\n"
         "from vgazer import Vgazer\n"
         "\n"
         "def main():\n"
         "    gazer = Vgazer({0})\n"
         "\n"
         "    print('host:', gazer.GetHostPlatform().GetArch(),\n"
         "     gazer.GetHostPlatform().GetOs(),\n"
         "     gazer.GetHostPlatform().GetOsVersion(),\n"
         "     gazer.GetHostPlatform().GetAbi())\n"
         "    print('target:', gazer.GetTargetPlatform().GetArch(),\n"
         "     gazer.GetTargetPlatform().GetOs(),\n"
         "     gazer.GetTargetPlatform().GetOsVersion(),\n"
         "     gazer.GetTargetPlatform().GetAbi())\n"
         "\n"
         "    gazer.Install('{1}', verbose=True)\n"
         "\n"
         "if __name__ == '__main__':\n"
         "    main()".format(vgazerArgs, software)
        )
    os.chmod(filename, stat.S_IRUSR | stat.S_IWUSR | stat.S_IXOTH)

def GenerateSampleTargets(gazer, hostPlatformsList, targetPlatformsList,
 installList):
    with open("./sample_targets.mk", "w") as sampleTargetsFile:
        for hostPlatform in hostPlatformsList:
            imageLaunchTarget = GenerateImageLaunchTarget(hostPlatform)
            sampleTargetsFile.write(imageLaunchTarget)
            checkPlatformTarget = GenerateCheckPlatformTarget(hostPlatform)
            sampleTargetsFile.write(checkPlatformTarget)
            for targetPlatform in targetPlatformsList:
                softwareVersionsTarget = GenerateSoftwareVersionsTarget(
                 hostPlatform, targetPlatform)
                sampleTargetsFile.write(softwareVersionsTarget)
            targetPlatform = hostPlatform
            softwareVersionsTarget = GenerateSoftwareVersionsTarget(
             hostPlatform, targetPlatform)
            sampleTargetsFile.write(softwareVersionsTarget)
        for targetPlatform in targetPlatformsList:
            CreateSoftwareVersionsSample(targetPlatform)
        CreateSoftwareVersionsSample(None)
        for installEntry in installList:
            installTarget = GenerateInstallTarget(installEntry)
            sampleTargetsFile.write(installTarget)
            CreateInstallSample(installEntry)

def main():
    gazer = Vgazer(supportOnly=True)
    hostPlatformsList = CreateHostPlatformsList(gazer)
    targetPlatformsList = CreateTargetPlatformsList(gazer)
    installList = CreateInstallList(gazer, hostPlatformsList,
     targetPlatformsList)
    GenerateSampleTargets(gazer, hostPlatformsList, targetPlatformsList,
     installList)

if __name__ == "__main__":
    main()
