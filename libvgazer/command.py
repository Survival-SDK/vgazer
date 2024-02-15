import subprocess

from libvgazer.exceptions import CommandError

def RunCommand(command, verbose, allowedReturncodes=None):
    if verbose:
        print(" ".join(command))
    try:
        if verbose:
            subprocess.check_call(command)
        else:
            subprocess.check_output(command, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        if (allowedReturncodes is None
         or e.returncode not in allowedReturncodes):
            if not verbose:
                print("Output:", e.output)
            print("VGAZER: Error occured while running utility:", command[0])
            raise CommandError(
             "Error occured while running utility:" + command[0], e.cmd,
             e.returncode)

def GetCommandOutputUtf8(command, verbose=False):
    try:
        if verbose:
            print(" ".join(command))
        output = subprocess.check_output(
         command, stderr=subprocess.STDOUT
        ).decode("utf-8")
        if verbose:
            print(output)
        return output
    except subprocess.CalledProcessError as e:
        if verbose:
            print(e.output.decode("utf-8"))
        raise CommandError("Error occured while running utility:" + command[0],
         e.cmd, e.returncode)
