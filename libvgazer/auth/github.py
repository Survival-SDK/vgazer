from libvgazer.auth.base import AuthBase

class AuthGithub(AuthBase):
    @staticmethod
    def ResolveHomeDirsAndFiles(storeHome):
        if not storeHome.ResolveSubdirectory("github"):
            return False

        filesResolved = (
         storeHome.ResolveSubdirectoryFile("github", "username")
         and storeHome.ResolveSubdirectoryFile("github", "token")
        )

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
