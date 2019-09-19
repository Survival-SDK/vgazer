#!/usr/bin/env python3

from vgazer.vgazer      import Vgazer
from vgazer.platform    import Platform

anyPlatform = Platform(arch = "any", os = "any", osVersion = "any", abi = "any")

def CreateHostPlatformsList(gazer):
    return [
        Platform(arch = gazer.GetHostPlatform().GetArch(), os = "alpine",
         osVersion = "3.9", abi = "musl", suppressGenericFallback = True),
        Platform(arch = gazer.GetHostPlatform().GetArch(), os = "debian",
         osVersion = "stretch", abi = "gnu", suppressGenericFallback = True),
    ]

def CreateTargetPlatformsList(gazer):
    return [
        Platform(arch = "x86_64", os = "linux", osVersion = "any", abi = "gnu"),
        Platform(arch = "x86_64", os = "linux", osVersion = "any",
         abi = "musl"),
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
    if hostPlatform.GetOs() == "alpine":
        return "/bin/sh"
    else:
        return "/bin/bash"

def GenerateImageLaunchTarget(hostPlatform):
    shell = GetShell(hostPlatform)

    return "image_{1}_{2}_{3}_launch:\n\tdocker run --entrypoint {0} -i -t \\\n\
     -v ~/.vgazer/github:/home/vgazer_user/.vgazer/github \\\n\
     vgazer_min_env_{1}_{2}_{3}\n\n".format(shell, hostPlatform.GetArch(),
     hostPlatform.GetOs(), hostPlatform.GetOsVersion())

def GenerateCheckPlatformTarget(hostPlatform):
    return "sample_{0}_{1}_{2}_check_platform:\n\tdocker run -i -t \\\n\
     -v ~/.vgazer/github:/home/vgazer_user/.vgazer/github \\\n\
     -v `pwd`:/vgazer --entrypoint sudo vgazer_min_env_{0}_{1}_{2} \\\n\
     -E sh -c ./samples/check_platform.py\n\n".format(hostPlatform.GetArch(),
     hostPlatform.GetOs(), hostPlatform.GetOsVersion())

def GenerateSoftwareVersionsTarget(hostPlatform, targetPlatform):
    if targetPlatform.PlatformsEqual(hostPlatform):
        targetPlatformString = "native"
    else:
        targetPlatformString = "{0}_{1}_{2}".format(targetPlatform.GetArch(),
         targetPlatform.GetOs(), targetPlatform.GetAbi())
    return "sample_{0}_{1}_{2}_software_versions_{3}:\n\tdocker run -i -t \\\n\
     -v ~/.vgazer/github:/home/vgazer_user/.vgazer/github \\\n\
     -v `pwd`:/vgazer --entrypoint sudo vgazer_min_env_{0}_{1}_{2} \\\n\
     -E sh -c ./samples/software_versions_{3}.py\n\n".format(
     hostPlatform.GetArch(), hostPlatform.GetOs(), hostPlatform.GetOsVersion(),
     targetPlatformString)

def GenerateInstallTarget(installEntry):
    software = installEntry[0]
    hostPlatform = installEntry[1]
    targetPlatform = installEntry[2]
    if targetPlatform.PlatformsEqual(hostPlatform):
        targetInstallString = software + "_native"
    elif targetPlatform == anyPlatform:
        targetInstallString = software
    else:
        targetInstallString = "{3}_{0}_{1}_{2}".format(targetPlatform.GetArch(),
         targetPlatform.GetOs(), targetPlatform.GetAbi(), software)
    return "sample_{0}_{1}_{2}_install_{3}:\n\tdocker run -i -t \\\n\
     -v ~/.vgazer/github:/home/vgazer_user/.vgazer/github \\\n\
     -v `pwd`:/vgazer --entrypoint sudo vgazer_min_env_{0}_{1}_{2} \\\n\
     -E sh -c ./samples/install_{3}.py\n\n".format(hostPlatform.GetArch(),
     hostPlatform.GetOs(), hostPlatform.GetOsVersion(), targetInstallString)

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
        for installEntry in installList:
            installTarget = GenerateInstallTarget(installEntry)
            sampleTargetsFile.write(installTarget)

def main():
    gazer = Vgazer()
    hostPlatformsList = CreateHostPlatformsList(gazer)
    targetPlatformsList = CreateTargetPlatformsList(gazer)
    installList = CreateInstallList(gazer, hostPlatformsList,
     targetPlatformsList)
    GenerateSampleTargets(gazer, hostPlatformsList, targetPlatformsList,
     installList)

if __name__ == "__main__":
    main()
