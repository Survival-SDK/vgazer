from samples.versions_common import PrintVersion

def PrintSoftwareVersions(gazer):
    softwareData = gazer.GetSoftwareData().GetData().items()
    for software, data in sorted(softwareData):
        PrintVersion(gazer, software)
