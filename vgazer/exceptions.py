class CommandError(Exception):
    def __init__(self, message):
        super().__init__(message)

class CompatibleProjectNotFound(Exception):
    def __init__(self, message):
        super().__init__(message)

class DebianPackageUnavailable(Exception):
    def __init__(self, message):
        super().__init__(message)

class DebianReleaseDataNotFound(Exception):
    def __init__(self, message):
        super().__init__(message)

class DirNameEngaged(Exception):
        def __init__(self, message):
            super().__init__(message)

class FilenameEngaged(Exception):
    def __init__(self, message):
        super().__init__(message)

class GithubApiRateLimitExceeded(Exception):
    def __init__(self, message):
        super().__init__(message)

class InstallError(Exception):
    def __init__(self, message):
        super().__init__(message)

class MissingArgument(Exception):
    def __init__(self, message):
        super().__init__(message)

class MissingChecker(Exception):
    def __init__(self, message):
        super().__init__(message)

class MissingInstaller(Exception):
    def __init__(self, message):
        super().__init__(message)

class OsDataNotFound(Exception):
    def __init__(self, message):
        super().__init__(message)

class SourceforgeReleaseArchiveLost(Exception):
    def __init__(self, message):
        super().__init__(message)

class TarballLost(Exception):
    def __init__(self, message):
        super().__init__(message)

class UnexpectedOsType(Exception):
    def __init__(self, message):
        super().__init__(message)

class UnknownOs(Exception):
    def __init__(self, message):
        super().__init__(message)

class UnknownPlatform(Exception):
    def __init__(self, message):
        super().__init__(message)

class UnknownSoftware(Exception):
    def __init__(self, message):
        super().__init__(message)
