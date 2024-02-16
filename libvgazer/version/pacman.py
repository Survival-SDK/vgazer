from libvgazer.command import GetCommandOutputUtf8

def CheckPacman(package):
    output = GetCommandOutputUtf8(["pacman", "-Q", "--info", package])

    print(output)

    return output.splitlines()[1].split(":", 1)[1].strip()
