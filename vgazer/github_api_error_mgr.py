class GithubApiErrorMgr:
    def __init__(self, responseJson, repo):
        self.responseJson = responseJson
        self.repo = repo
        self.errorOccured = False
        self.errorText = "No error"

    def ApiRateLimitExceeded(self):
        return ("message" in self.responseJson
         and self.responseJson["documentation_url"]
          == "https://developer.github.com/v3/#rate-limiting")

    def BadCredentials(self):
        return ("message" in self.responseJson
         and self.responseJson["message"] == "Bad credentials")

    def ProcessErrors(self):
        if self.ApiRateLimitExceeded():
            self.errorOccured = True
            self.errorText = ("Github API rate limit reached while searching "
             "last version of repo: {0}".format(self.repo))
        if self.BadCredentials():
            self.errorOccured = True
            self.errorText = ("Github API bad credentials passed while "
             "searching last version of repo: {0}".format(self.repo))

    def __enter__(self):
        self.ProcessErrors()
        return self

    def __exit__(self, etype, value, traceback):
        pass

    def IsErrorOccured(self):
        return self.errorOccured

    def GetErrorText(self):
        return self.errorText