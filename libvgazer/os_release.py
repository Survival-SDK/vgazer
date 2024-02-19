class OsRelease:
    def __init__(self):
        self.entries = {}

        with open("/etc/os-release", "r") as osReleaseFile:
            data = osReleaseFile.read()
        lines = data.splitlines()
        for line in lines:
            if "=" in line:
                kv = line.split("=")
                self.entries[kv[0]] = kv[1]

    def __enter__(self):
        return self

    def __exit__(self, etype, value, traceback):
        pass

    def GetEntry(self, key):
        if key in self.entries:
            return self.entries[key].strip("\"")
