from vgazer.command     import RunCommand
from vgazer.exceptions  import CommandError

def SourceforgeDownloadTarballWhileErrorcodeFour(mirrorsManager, sfProject,
 filename, verbose):
    while True:
        try:
            RunCommand(
             ["wget", "--tries=1", "--timeout=10", "--continue", "-P", "./",
              mirrorsManager.GetMirrorUrl() + "/project/" + sfProject + filename
             ],
             verbose)
        except CommandError as e:
            if e.errorcode == 4:
                mirrorsManager.ChangeMirror()
            else:
                raise e
        else:
            break