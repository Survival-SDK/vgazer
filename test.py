#!/usr/bin/env python3

from vgazer.version.custom      import CheckCustom
from vgazer.version.github      import CheckGithub
from vgazer.version.sourceforge import CheckSourceforge
from vgazer.version.xiph        import CheckXiph
from vgazer.auth.base           import AuthBase
from vgazer.auth.github         import AuthGithub

def testGeneric(authBase, authGithub):
    print("cJSON:", CheckGithub(authGithub, "cJSON"))
    print("duktape", CheckGithub(authGithub, "duktape"))
    print("harfbuzz:", CheckGithub(authGithub, "harfbuzz"))
    print("inih:", CheckGithub(authGithub, "inih"))
    print("lazy-winapi.c:", CheckGithub(authGithub, "lazy-winapi.c"))
    print("libintl-lite:", CheckGithub(authGithub, "libintl-lite"))
    print("minIni:", CheckGithub(authGithub, "minIni"))
    print("nuklear:", CheckGithub(authGithub, "nuklear"))
    ## Github mirror
    ## Official website broken: https://icculus.org/physfs/
    print("physfs:", CheckGithub(authGithub, "physfs"))
    print("saneopt:", CheckGithub(authGithub, "saneopt"))
    print("sdl-gpu:", CheckGithub(authGithub, "sdl-gpu"))
    print("squirrel:", CheckGithub(authGithub, "squirrel"))
    print("utf:", CheckGithub(authGithub, "utf"))
    print("utf8:", CheckGithub(authGithub, "utf8"))

    print("bzip2:", CheckSourceforge(AuthBase, "bzip2"))
    print("giflib:", CheckSourceforge(AuthBase, "giflib"))
    print("glew:", CheckSourceforge(AuthBase, "glew"))
    print("lzmautils:", CheckSourceforge(AuthBase, "lzmautils"))
    print("modplug-xmms:", CheckSourceforge(AuthBase, "modplug-xmms"))
    print("mpg123:", CheckSourceforge(AuthBase, "mpg123"))
    print("libpng:", CheckSourceforge(AuthBase, "libpng"))
    print("sdl2gfx:", CheckSourceforge(AuthBase, "sdl2gfx"))

    print("libflac:", CheckXiph(AuthBase, "libflac"))
    print("libogg:", CheckXiph(AuthBase, "libogg"))
    print("libvorbis:", CheckXiph(AuthBase, "libvorbis"))

    print("dr_wav:", CheckCustom(AuthBase, "dr_wav"))
    print("freetype:", CheckCustom(AuthBase, "freetype"))
    print("glib:", CheckCustom(AuthBase, "glib"))
    print("icu:", CheckCustom(AuthBase, "icu"))
    print("jpeg:", CheckCustom(AuthBase, "jpeg"))
    print("libffi:", CheckCustom(AuthBase, "libffi"))
    print("libiconv:", CheckCustom(AuthBase, "libiconv"))
    print("libtiff:", CheckCustom(AuthBase, "libtiff"))
    print("libwebp:", CheckCustom(AuthBase, "libwebp"))
    print("lua:", CheckCustom(AuthBase, "lua"))
    print("portaudio:", CheckCustom(AuthBase, "portaudio"))
    print("sdl2:", CheckCustom(AuthBase, "sdl2"))
    print("sdl2_image:", CheckCustom(AuthBase, "sdl2_image"))
    print("sdl2_mixer:", CheckCustom(AuthBase, "sdl2_mixer"))
    print("sdl2_ttf:", CheckCustom(AuthBase, "sdl2_ttf"))
    print("stb_rect_pack:", CheckCustom(AuthBase, "stb_rect_pack"))
    print("tinyfiledialogs:", CheckCustom(AuthBase, "tinyfiledialogs"))
    print("zlib:", CheckCustom(AuthBase, "zlib"))
    pass

def main():
    authGithub = AuthGithub()
    authBase = AuthBase()
    testGeneric(authBase, authGithub)


if __name__ == "__main__":
    main()
