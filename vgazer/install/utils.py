from vgazer.command     import RunCommand
from vgazer.exceptions  import CommandError

def SourceforgeDownloadTarballWhileErrorcodeFour(mirrorsManager, sfProject,
 filename, verbose):
    while True:
        try:
            RunCommand(
             [
              "wget",
              "--tries=1",
              "--timeout=10",
              "--continue",
              "-P",
              "./",
              "{url}/project/{sfProject}{filename}".format(
               url=mirrorsManager.GetMirrorUrl(),
               sfProject=sfProject,
               filename=filename
              )
             ],
             verbose)
        except CommandError as e:
            if e.errorcode == 4:
                mirrorsManager.ChangeMirror()
            else:
                raise e
        else:
            break

def GetVersionNumbers(versionText):
    version = {}
    version["major"] = int(versionText[0])
    version["minor"] = int(versionText[1])
    if len(versionText) == 3:
        version["patch"] = int(versionText[2])
        version["subpatch"] = 0
    elif len(versionText) == 2:
        version["patch"] = 0
        version["subpatch"] = 0
    else:
        version["patch"] = int(versionText[2])
        version["subpatch"] = int(versionText[3])

    return version
