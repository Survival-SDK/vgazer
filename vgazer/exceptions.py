class CommandError(Exception):
    def __init__(self, message):
        super().__init__(message)

class DebianPackageUnavailable(Exception):
    def __init__(self, message):
        super().__init__(message)

class InstallError(Exception):
    def __init__(self, message):
        super().__init__(message)

class UnknownSoftware(Exception):
    def __init__(self, message):
        super().__init__(message)
