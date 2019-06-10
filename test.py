#!/usr/bin/env python3

from vgazer.version.github      import CheckGithub
from vgazer.version.sourceforge import CheckSourceforge
from vgazer.version.custom      import CheckCustom
from vgazer.auth.base           import AuthBase
from vgazer.auth.github         import AuthGithub

def main():
    authGithub = AuthGithub()
    authBase = AuthBase()
    authSourceforge = authBase
    authCustom = authBase

    print("cJSON:", CheckGithub(authGithub, "cJSON"))
    #print("inih:", CheckGithub(authGithub, "inih"))
    #print("libintl-lite:", CheckGithub(authGithub, "libintl-lite"))
    #print("nuklear:", CheckGithub(authGithub, "nuklear"))
    #print("saneopt:", CheckGithub(authGithub, "saneopt"))
    #print("sdl-gpu:", CheckGithub(authGithub, "sdl-gpu"))
    #print("utf:", CheckGithub(authGithub, "utf"))

    print("bzip2:", CheckSourceforge(authSourceforge, "bzip2"))
    #print("giflib:", CheckSourceforge(authSourceforge, "giflib"))
    #print("glew:", CheckSourceforge(authSourceforge, "glew"))
    #print("modplug-xmms:", CheckSourceforge(authSourceforge, "modplug-xmms"))

    #print("tinyfiledialogs:", CheckCustom(authCustom, "tinyfiledialogs"))
    #print("dr_wav:", CheckCustom(authCustom, "dr_wav"))
    print("stb_rect_pack:", CheckCustom(authGithub, "stb_rect_pack"))

if __name__ == "__main__":
    main()
