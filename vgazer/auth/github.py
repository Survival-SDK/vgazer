from vgazer.auth.base import AuthBase
from vgazer.store.home import StoreHome

class AuthGithub(AuthBase):
    @staticmethod
    def ResolveHomeDirsAndFiles(storeHome):
        if not storeHome.ResolveSubdirectory("github"):
            return False

        filesResolved = (storeHome.ResolveSubdirectoryFile("github", "username")
         and storeHome.ResolveSubdirectoryFile("github", "token"))

        if not filesResolved:
            return False
        return True

    def __init__(self):
        super().__init__()

        if not self.useAuth:
            return None

        if not self.ResolveHomeDirsAndFiles(self.storeHome):
            print("ResolveHomeDirsAndFiles(storeHome) fail")
            return None

        username = AuthBase.GetAuthData(self.storeHome, "github", "username",
         "github username")
        token = AuthBase.GetAuthData(self.storeHome, "github", "token",
         "github access token")
        self.session.auth = (username, token)

        #print(username)
        #print(token)

        #import json

        #rate_limit_url = "https://api.github.com/rate_limit?q=github+api"
        #rate_limit = json.loads(self.session.get(rate_limit_url).text)

        #print(rate_limit)
