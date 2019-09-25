import subprocess
from vgazer.exceptions import CommandError

def RunCommand(command, verbose):
    try:
        if verbose:
            print(" ".join(command))
            subprocess.check_call(command)
        else:
            output = subprocess.check_output(command, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        if not verbose:
            print ("Output:")
            print (output)
        print ("Error occured while running utility:", command[0])
        raise CommandError("Error occured while running utility:" + command[0], e.returncode)

def GetCommandOutputUtf8(command):
    try:
        return subprocess.check_output(
         command, stderr=subprocess.STDOUT
        ).decode("utf-8")
    except subprocess.CalledProcessError:
        raise CommandError("Error occured while running utility:" + command[0])
