#!/usr/bin/env python3

from libvgazer          import Vgazer
from libvgazer.platform import GetTriplet
from libvgazer.platform import Platform

anyPlatform = Platform(arch="any", os="any", osVersion="any", abi="any")

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

def GenerateImageLaunchTarget(hostPlatform):
    return ("image-{1}-{2}-{3}-launch:\n"
     "\tdocker run --net=host -i -t \\\n"
     "     -v ~/.vgazer:/root/.vgazer -v `pwd`:/mnt/vgazer \\\n"
     "     --entrypoint {0} vgazer-deps:{1}-{2}-{3} \\\n"
     "\n".format("/bin/bash", hostPlatform.GetArch(), hostPlatform.GetOs(),
      hostPlatform.GetOsVersion()))

def GenerateInstallAndVersionTarget(installEntry):
    software = installEntry[0]
    hostPlatform = installEntry[1]
    targetPlatform = installEntry[2]

    if targetPlatform.PlatformsEqual(hostPlatform):
        targetTriplet = GetTriplet(targetPlatform)
        targetInstallString = software
        targetArg = ""
    elif targetPlatform == anyPlatform:
        targetTriplet = "any-any-any"
        targetInstallString = software
        targetArg = ""
    else:
        targetTriplet = GetTriplet(targetPlatform)
        targetInstallString = "{0}-{1}".format(software, targetTriplet)
        targetArg = "--target={triplet}".format(triplet=targetTriplet)
    return (
     "sample-{harch}-{hos}-{hver}-version-{platform}:\n"
     "\tdocker run --net=host -i -t \\\n"
     "     -v ~/.vgazer:/root/.vgazer \\\n"
     "     -v `pwd`:/mnt/vgazer \\\n"
     "     -v `pwd`/.vgazer-{triplet}:/mnt/vgazer_output \\\n"
     "     --entrypoint ./vgazer vgazer-deps:{harch}-{hos}-{hver} \\\n"
     "     version {targetArg} {software} | tee version.log\n"
     "\n"
     "sample-{harch}-{hos}-{hver}-install-{platform}:\n"
     "\tdocker run --net=host -i -t \\\n"
     "     -v ~/.vgazer:/root/.vgazer \\\n"
     "     -v `pwd`:/mnt/vgazer \\\n"
     "     -v `pwd`/.vgazer-{triplet}:/mnt/vgazer_output \\\n"
     "     --entrypoint ./vgazer vgazer-deps:{harch}-{hos}-{hver} \\\n"
     "     install {targetArg} {software} | tee install.log\n"
     "\n".format(
        harch=hostPlatform.GetArch(),
        hos=hostPlatform.GetOs(),
        hver=hostPlatform.GetOsVersion(),
        platform=targetInstallString,
        software=software,
        triplet=targetTriplet,
        targetArg=targetArg
     )
    )

def GenerateSampleTargets(gazer, hostPlatformsList, targetPlatformsList,
 installList):
    with open("./sample_targets.mk", "w") as sampleTargetsFile:
        for hostPlatform in hostPlatformsList:
            imageLaunchTarget = GenerateImageLaunchTarget(hostPlatform)
            sampleTargetsFile.write(imageLaunchTarget)
        for installEntry in installList:
            installTarget = GenerateInstallAndVersionTarget(installEntry)
            sampleTargetsFile.write(installTarget)

def main():
    gazer = Vgazer(supportOnly=True)
    hostPlatformsList = [
        Platform(arch=gazer.GetHostPlatform().GetArch(), os="archlinux",
         osVersion="latest", abi="gnu", suppressGenericFallback=True),
        Platform(arch=gazer.GetHostPlatform().GetArch(), os="fedora",
         osVersion="40", abi="gnu", suppressGenericFallback=True),
        Platform(arch=gazer.GetHostPlatform().GetArch(), os="oraclelinux",
         osVersion="7", abi="gnu", suppressGenericFallback=True),
    ]
    targetPlatformsList = [
        Platform(arch="x86_64", os="linux", osVersion="any", abi="gnu"),
        Platform(arch="x86_64", os="windows", osVersion="any", abi="mingw32"),
    ]
    installList = CreateInstallList(gazer, hostPlatformsList,
     targetPlatformsList)
    GenerateSampleTargets(gazer, hostPlatformsList, targetPlatformsList,
     installList)

if __name__ == "__main__":
    main()
