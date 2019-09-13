from samples.versions_common import PrintVersion

def PrintLibrariesVersions(gazer):
    softwareData = gazer.GetSoftwareData().GetData().items()
    for software, data in sorted(softwareData):
        if data["platform"] == "target":
            PrintVersion(gazer, software)
