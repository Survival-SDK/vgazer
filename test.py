#!/usr/bin/env python3

from vgazer.version.github      import CheckGithub
from vgazer.version.sourceforge import CheckSourceforge
from vgazer.version.xiph        import CheckXiph
from vgazer.version.custom      import CheckCustom
from vgazer.auth.base           import AuthBase
from vgazer.auth.github         import AuthGithub

def main():
    authGithub = AuthGithub()
    authBase = AuthBase()

    #print("cJSON:", CheckGithub(authGithub, "cJSON"))
    #print("duktape", CheckGithub(authGithub, "duktape"))
    #print("harfbuzz:", CheckGithub(authGithub, "harfbuzz"))
    #print("inih:", CheckGithub(authGithub, "inih"))
    #print("lazy-winapi.c:", CheckGithub(authGithub, "lazy-winapi.c"))
    #print("libintl-lite:", CheckGithub(authGithub, "libintl-lite"))
    #print("nuklear:", CheckGithub(authGithub, "nuklear"))
    #print("saneopt:", CheckGithub(authGithub, "saneopt"))
    #print("sdl-gpu:", CheckGithub(authGithub, "sdl-gpu"))
    #print("utf:", CheckGithub(authGithub, "utf"))

    print("bzip2:", CheckSourceforge(AuthBase, "bzip2"))
    #print("giflib:", CheckSourceforge(AuthBase, "giflib"))
    #print("glew:", CheckSourceforge(AuthBase, "glew"))
    #print("lzmautils:", CheckSourceforge(AuthBase, "lzmautils"))
    #print("modplug-xmms:", CheckSourceforge(AuthBase, "modplug-xmms"))
    #print("mpg123:", CheckSourceforge(AuthBase, "mpg123"))
    #print("libpng:", CheckSourceforge(AuthBase, "libpng"))

    #print("libflac:", CheckXiph(AuthBase, "libflac"))
    #print("libogg:", CheckXiph(AuthBase, "libogg"))
    #print("libvorbis:", CheckXiph(AuthBase, "libvorbis"))

    #print("dr_wav:", CheckCustom(AuthBase, "dr_wav"))
    #print("freetype:", CheckCustom(AuthBase, "freetype"))
    #print("glib:", CheckCustom(AuthBase, "glib"))
    #print("icu:", CheckCustom(AuthBase, "icu"))
    #print("jpeg:", CheckCustom(AuthBase, "jpeg"))
    #print("libffi:", CheckCustom(AuthBase, "libffi"))
    #print("libiconv:", CheckCustom(AuthBase, "libiconv"))
    #print("libtiff:", CheckCustom(AuthBase, "libtiff"))
    #print("libwebp:", CheckCustom(AuthBase, "libwebp"))
    #print("stb_rect_pack:", CheckCustom(AuthBase, "stb_rect_pack"))
    #print("tinyfiledialogs:", CheckCustom(AuthBase, "tinyfiledialogs"))
    pass

if __name__ == "__main__":
    main()
