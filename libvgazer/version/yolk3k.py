from libvgazer.command import GetCommandOutputUtf8

def CheckYolk3k(package):
    return GetCommandOutputUtf8(["yolk", "-V", package]).split(" ")[1]
