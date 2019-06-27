#!/usr/bin/env python3

from vgazer.version.custom      import CheckCustom
from vgazer.version.github      import CheckGithub
from vgazer.version.sourceforge import CheckSourceforge
from vgazer.version.xiph        import CheckXiph
from vgazer.version.debian      import CheckDebian
from vgazer.auth.base           import AuthBase
from vgazer.auth.github         import AuthGithub

def testGeneric(authBase, authGithub):
    print("cjson:", CheckGithub(authGithub, "cjson"))
    print("duktape", CheckGithub(authGithub, "duktape"))
    print("harfbuzz:", CheckGithub(authGithub, "harfbuzz"))
    print("inih:", CheckGithub(authGithub, "inih"))
    print("lazy-winapi.c:", CheckGithub(authGithub, "lazy-winapi.c"))
    print("libintl-lite:", CheckGithub(authGithub, "libintl-lite"))
    print("minini:", CheckGithub(authGithub, "minIni"))
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

    print("cmocka:", CheckCustom(AuthBase, "cmocka"))
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
    print("p7:", CheckCustom(AuthBase, "p7"))
    print("portaudio:", CheckCustom(AuthBase, "portaudio"))
    print("sdl2:", CheckCustom(AuthBase, "sdl2"))
    print("sdl2_image:", CheckCustom(AuthBase, "sdl2_image"))
    print("sdl2_mixer:", CheckCustom(AuthBase, "sdl2_mixer"))
    print("sdl2_ttf:", CheckCustom(AuthBase, "sdl2_ttf"))
    print("stb_rect_pack:", CheckCustom(AuthBase, "stb_rect_pack"))
    print("tinyfiledialogs:", CheckCustom(AuthBase, "tinyfiledialogs"))
    print("zlib:", CheckCustom(AuthBase, "zlib"))
    pass

def testDebian(authBase):
    print("cjson:", CheckDebian(authBase, "buster", "cjson"))
    print("cmocka:", CheckDebian(authBase, "buster", "cmocka"))
    print("duktape:", CheckDebian(authBase, "buster", "duktape"))
    print("harfbuzz:", CheckDebian(authBase, "buster", "harfbuzz"))
    print("inih:", CheckDebian(authBase, "buster", "libinih"))
    print("minini:", CheckDebian(authBase, "buster", "libminini"))
    print("physfs:", CheckDebian(authBase, "buster", "libphysfs"))
    print("squirrel:", CheckDebian(authBase, "buster", "squirrel3"))
    print("bzip2:", CheckDebian(authBase, "buster", "bzip2"))
    print("giflib:", CheckDebian(authBase, "buster", "giflib"))
    print("glew:", CheckDebian(authBase, "buster", "glew"))
    print("liblzma:", CheckDebian(authBase, "buster", "xz-utils"))
    print("libmodplug:", CheckDebian(authBase, "buster", "libmodplug"))
    print("mpg123:", CheckDebian(authBase, "buster", "mpg123"))
    print("libpng:", CheckDebian(authBase, "buster", "libpng1.6"))
    print("sdl2_gfx:", CheckDebian(authBase, "buster", "libsdl2-gfx"))
    print("libflac:", CheckDebian(authBase, "buster", "flac"))
    print("libogg:", CheckDebian(authBase, "buster", "libogg"))
    print("libvorbis:", CheckDebian(authBase, "buster", "libvorbis"))
    print("freetype:", CheckDebian(authBase, "buster", "freetype"))
    print("glib:", CheckDebian(authBase, "buster", "glib2.0"))
    print("icu:", CheckDebian(authBase, "buster", "icu"))
    print("jpeg:", CheckDebian(authBase, "buster", "libjpeg-turbo"))
    print("libffi:", CheckDebian(authBase, "buster", "libffi"))
    print("libtiff:", CheckDebian(authBase, "buster", "tiff"))
    print("libwebp:", CheckDebian(authBase, "buster", "libwebp"))
    print("lua:", CheckDebian(authBase, "buster", "lua5.3"))
    print("portaudio:", CheckDebian(authBase, "buster", "portaudio19"))
    print("sdl2:", CheckDebian(authBase, "buster", "libsdl2"))
    print("sdl2_image:", CheckDebian(authBase, "buster", "libsdl2-image"))
    print("sdl2_mixer:", CheckDebian(authBase, "buster", "libsdl2-mixer"))
    print("sdl2_ttf:", CheckDebian(authBase, "buster", "libsdl2-ttf"))
    print("stb_rect_pack:", CheckDebian(authBase, "buster", "libstb"))
    print("zlib:", CheckDebian(authBase, "buster", "zlib"))
    pass

def main():
    authGithub = AuthGithub()
    authBase = AuthBase()
    testGeneric(authBase, authGithub)
    testDebian(authBase)


if __name__ == "__main__":
    main()
