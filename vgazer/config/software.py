data = {
    "cjson": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "compiler": ["any"],
                "checker": {
                    "type": "github",
                    "user": "DaveGamble",
                    "repo": "cJSON",
                },
                "installer": {
                    "type": "custom",
                    "name": "cjson",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["buster"],
                "compiler": ["gcc"],
                "checker": {
                    "type": "debian",
                    "source": "cjson",
                    "package": "libcjson-dev",
                },
                "installer": {
                    "type": "debian",
                    "package": "libcjson-dev",
                },
            },
        ],
    },
    "cmake": {
        "platform": "host",
        "projects": [
            #{
                #"arch": ["any"],
                #"os": ["any"],
                #"osVersion": ["any"],
                #"compiler": ["any"],
                #"checker": {
                    #"type": "custom",
                    #"name": "cmake",
                #},
                #"installer": {
                    #"type": "custom",
                    #"name": "cmake",
                #},
            #},
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "compiler": ["any"],
                "checker": {
                    "type": "debian",
                    "source": "cmake",
                    "package": "cmake",
                },
                "installer": {
                    "type": "debian",
                    "package": "cmake",
                },
            },
        ],
    },
    "cmocka": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "compiler": ["any"],
                "checker": {
                    "type": "custom",
                    "name": "cmocka",
                },
                "installer": {
                    "type": "custom",
                    "name": "cmocka",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "compiler": ["gcc"],
                "checker": {
                    "type": "debian",
                    "source": "cmocka",
                    "package": "libcmocka-dev",
                },
                "installer": {
                    "type": "debian",
                    "package": "libcmocka-dev",
                },
            },
        ],
    },
    "dr_wav": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "compiler": ["any"],
                "checker": {
                    "type": "custom",
                    "name": "dr_wav",
                },
                "installer": {
                    "type": "custom",
                    "name": "dr_wav",
                },
            },
        ],
    },
    "duktape": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "compiler": ["any"],
                "checker": {
                    "type": "github",
                    "user": "svaarala",
                    "repo": "duktape",
                },
                "installer": {
                    "type": "custom",
                    "name": "duktape",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "compiler": ["gcc"],
                "checker": {
                    "type": "debian",
                    "source": "duktape",
                    "package": "duktape-dev",
                },
                "installer": {
                    "type": "debian",
                    "package": "duktape-dev",
                },
            },
        ],
    },
    "freetype": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "compiler": ["any"],
                "checker": {
                    "type": "custom",
                    "name": "freetype",
                },
                "installer": {
                    "type": "custom",
                    "name": "freetype",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "compiler": ["gcc"],
                "checker": {
                    "type": "debian",
                    "source": "freetype",
                    "package": "libfreetype6-dev",
                },
                "installer": {
                    "type": "debian",
                    "package": "libfreetype6-dev",
                },
            },
        ],
    },
    "giflib": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "compiler": ["any"],
                "checker": {
                    "type": "sourceforge",
                    "project": "giflib",
                },
                "installer": {
                    "type": "custom",
                    "name": "giflib",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "compiler": ["gcc"],
                "checker": {
                    "type": "debian",
                    "source": "giflib",
                    "package": "libgif-dev",
                },
                "installer": {
                    "type": "debian",
                    "package": "libgif-dev",
                },
            },
        ],
    },
    "git": {
        "platform": "host",
        "projects": [
            #{
                #"arch": ["any"],
                #"os": ["any"],
                #"osVersion": ["any"],
                #"compiler": ["any"],
                #"checker": {
                    #"type": "github",
                    #"user": "git",
                    #"repo": "git",
                #},
                #"installer": {
                    #"type": "custom",
                    #"name": "git",
                #},
            #},
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "compiler": ["any"],
                "checker": {
                    "type": "debian",
                    "source": "git",
                    "package": "git",
                },
                "installer": {
                    "type": "debian",
                    "package": "git",
                },
            },
        ],
    },
    "glew": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "compiler": ["any"],
                "checker": {
                    "type": "sourceforge",
                    "project": "glew",
                },
                "installer": {
                    "type": "custom",
                    "name": "glew",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "compiler": ["gcc"],
                "checker": {
                    "type": "debian",
                    "source": "glew",
                    "package": "libglew-dev",
                },
                "installer": {
                    "type": "debian",
                    "package": "libglew-dev",
                },
            },
        ],
    },
    "glib": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "compiler": ["any"],
                "checker": {
                    "type": "custom",
                    "name": "glib",
                },
                "installer": {
                    "type": "custom",
                    "name": "glib",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "compiler": ["gcc"],
                "checker": {
                    "type": "debian",
                    "source": "glib2.0",
                    "package": "libglib2.0-dev",
                },
                "installer": {
                    "type": "debian",
                    "package": "libglib2.0-dev",
                },
            },
        ],
    },
    "harfbuzz": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "compiler": ["any"],
                "checker": {
                    "type": "github",
                    "user": "harfbuzz",
                    "repo": "harfbuzz",
                },
                "installer": {
                    "type": "custom",
                    "name": "harfbuzz",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "compiler": ["gcc"],
                "checker": {
                    "type": "debian",
                    "source": "harfbuzz",
                    "package": "libharfbuzz-dev",
                },
                "installer": {
                    "type": "debian",
                    "package": "libharfbuzz-dev",
                },
            },
        ],
    },
    "i686-w64-mingw32-gcc": {
        "platform": "host",
        "projects": [
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "compiler": ["any"],
                "checker": {
                    "type": "debian",
                    "source": "gcc-mingw-w64",
                    "package": "gcc-mingw-w64-i686",
                },
                "installer": {
                    "type": "debian",
                    "package": "gcc-mingw-w64-i686",
                },
            },
        ],
    },
    "icu": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "compiler": ["any"],
                "checker": {
                    "type": "custom",
                    "name": "icu",
                },
                "installer": {
                    "type": "custom",
                    "name": "icu",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "compiler": ["gcc"],
                "checker": {
                    "type": "debian",
                    "source": "icu",
                    "package": "libicu-dev",
                },
                "installer": {
                    "type": "debian",
                    "package": "libicu-dev",
                },
            },
        ],
    },
    "inih": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "compiler": ["any"],
                "checker": {
                    "type": "github",
                    "user": "benhoyt",
                    "repo": "inih",
                },
                "installer": {
                    "type": "custom",
                    "name": "inih",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "compiler": ["gcc"],
                "checker": {
                    "type": "debian",
                    "source": "libinih",
                    "package": "libinih-dev",
                },
                "installer": {
                    "type": "debian",
                    "package": "libinih-dev",
                },
            },
        ],
    },
    "jpeg": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "compiler": ["any"],
                "checker": {
                    "type": "custom",
                    "name": "jpeg",
                },
                "installer": {
                    "type": "custom",
                    "name": "jpeg",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "compiler": ["gcc"],
                "checker": {
                    "type": "debian",
                    "source": "libjpeg-turbo",
                    "package": "libjpeg-dev",
                },
                "installer": {
                    "type": "debian",
                    "package": "libjpeg-dev",
                },
            },
        ],
    },
    "lazy-winapi.c": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["windows"],
                "osVersion": ["any"],
                "compiler": ["any"],
                "checker": {
                    "type": "github",
                    "user": "DoumanAsh",
                    "repo": "lazy-winapi.c",
                },
                "installer": {
                    "type": "custom",
                    "name": "lazy-winapi.c",
                },
            },
        ],
    },
    "libbzip2": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "compiler": ["any"],
                "checker": {
                    "type": "sourceforge",
                    "project": "bzip2",
                },
                "installer": {
                    "type": "custom",
                    "project": "bzip2",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "compiler": ["gcc"],
                "checker": {
                    "type": "debian",
                    "source": "bzip2",
                    "package": "libbz2-dev",
                },
                "installer": {
                    "type": "debian",
                    "package": "libbz2-dev",
                },
            },
        ],
    },
    "libffi": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "compiler": ["any"],
                "checker": {
                    "type": "custom",
                    "name": "libffi",
                },
                "installer": {
                    "type": "custom",
                    "name": "libffi",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "compiler": ["gcc"],
                "checker": {
                    "type": "debian",
                    "source": "libffi",
                    "package": "libffi-dev",
                },
                "installer": {
                    "type": "debian",
                    "package": "libffi-dev",
                },
            },
        ],
    },
    "libflac": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "compiler": ["any"],
                "checker": {
                    "type": "xiph",
                    "project": "libflac",
                },
                "installer": {
                    "type": "custom",
                    "name": "libflac",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "compiler": ["gcc"],
                "checker": {
                    "type": "debian",
                    "source": "flac",
                    "package": "libflac-dev",
                },
                "installer": {
                    "type": "debian",
                    "package": "libflac-dev",
                },
            },
        ],
    },
    "libiconv": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "compiler": ["any"],
                "checker": {
                    "type": "custom",
                    "name": "libiconv",
                },
                "installer": {
                    "type": "custom",
                    "name": "libiconv",
                },
            },
        ],
    },
    "libintl-lite": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "compiler": ["any"],
                "checker": {
                    "type": "github",
                    "user": "j-jorge",
                    "repo": "libintl-lite",
                },
                "installer": {
                    "type": "custom",
                    "name": "libintl-lite",
                },
            },
        ],
    },
    "liblzma": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "compiler": ["any"],
                "checker": {
                    "type": "sourceforge",
                    "project": "lzmautils",
                },
                "installer": {
                    "type": "custom",
                    "name": "liblzma",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "compiler": ["gcc"],
                "checker": {
                    "type": "debian",
                    "source": "xz-utils",
                    "package": "liblzma-dev",
                },
                "installer": {
                    "type": "debian",
                    "package": "liblzma-dev",
                },
            },
        ],
    },
    "libmodplug": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "compiler": ["any"],
                "checker": {
                    "type": "sourceforge",
                    "project": "modplug-xmms",
                },
                "installer": {
                    "type": "custom",
                    "name": "libmodplug",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "compiler": ["gcc"],
                "checker": {
                    "type": "debian",
                    "source": "libmodplug",
                    "package": "libmodplug-dev",
                },
                "installer": {
                    "type": "debian",
                    "package": "libmodplug-dev",
                },
            },
        ],
    },
    "libogg": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "compiler": ["any"],
                "checker": {
                    "type": "xiph",
                    "project": "libogg",
                },
                "installer": {
                    "type": "custom",
                    "name": "libogg",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "compiler": ["gcc"],
                "checker": {
                    "type": "debian",
                    "source": "libogg",
                    "package": "libogg-dev",
                },
                "installer": {
                    "type": "debian",
                    "package": "libogg-dev",
                },
            },
        ],
    },
    "libpng": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "compiler": ["any"],
                "checker": {
                    "type": "sourceforge",
                    "project": "libpng",
                },
                "installer": {
                    "type": "custom",
                    "name": "libpng",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "compiler": ["gcc"],
                "checker": {
                    "type": "debian",
                    "source": "libpng1.6",
                    "package": "libpng-dev",
                },
                "installer": {
                    "type": "debian",
                    "package": "libpng-dev",
                },
            },
        ],
    },
    "libtiff": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "compiler": ["any"],
                "checker": {
                    "type": "custom",
                    "name": "libtiff",
                },
                "installer": {
                    "type": "custom",
                    "name": "libtiff",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "compiler": ["gcc"],
                "checker": {
                    "type": "debian",
                    "source": "tiff",
                    "package": "libtiff-dev",
                },
                "installer": {
                    "type": "debian",
                    "package": "libtiff-dev",
                },
            },
        ],
    },
    "libvorbis": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "compiler": ["any"],
                "checker": {
                    "type": "xiph",
                    "project": "libvorbis",
                },
                "installer": {
                    "type": "custom",
                    "project": "libvorbis",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "compiler": ["gcc"],
                "checker": {
                    "type": "debian",
                    "source": "libvorbis",
                    "package": "libvorbis-dev",
                },
                "installer": {
                    "type": "debian",
                    "package": "libvorbis-dev",
                },
            },
        ],
    },
    "libwebp": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "compiler": ["any"],
                "checker": {
                    "type": "custom",
                    "name": "lebwebp",
                },
                "installer": {
                    "type": "custom",
                    "name": "libwebp",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "compiler": ["gcc"],
                "checker": {
                    "type": "debian",
                    "source": "libwebp",
                    "package": "libwebp-dev",
                },
                "installer": {
                    "type": "debian",
                    "package": "libwebp-dev",
                },
            },
        ],
    },
    "lua": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "compiler": ["any"],
                "checker": {
                    "type": "custom",
                    "name": "lua",
                },
                "installer": {
                    "type": "custom",
                    "name": "lua",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "compiler": ["gcc"],
                "checker": {
                    "type": "debian",
                    "source": "lua5.3",
                    "package": "liblua5.3-dev",
                },
                "installer": {
                    "type": "debian",
                    "package": "liblua5.3-dev",
                },
            },
        ],
    },
    "minini": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "compiler": ["any"],
                "checker": {
                    "type": "github",
                    "user": "compuphase",
                    "repo": "minIni",
                },
                "installer": {
                    "type": "custom",
                    "name": "minini",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "compiler": ["gcc"],
                "checker": {
                    "type": "debian",
                    "source": "libminini",
                    "package": "libminini-dev",
                },
                "installer": {
                    "type": "debian",
                    "source": "libminini",
                    "package": "libminini-dev",
                },
            },
        ],
    },
    "mpg123": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "compiler": ["any"],
                "checker": {
                    "type": "sourceforge",
                    "project": "mpg123",
                },
                "installer": {
                    "type": "custom",
                    "name": "mpg123",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "compiler": ["gcc"],
                "checker": {
                    "type": "debian",
                    "source": "libmpg123",
                    "package": "libmpg123-dev",
                },
                "installer": {
                    "type": "debian",
                    "package": "libmpg123-dev",
                },
            },
        ],
    },
    "nuklear": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "compiler": ["any"],
                "checker": {
                    "type": "github",
                    "user": "vurtun",
                    "repo": "nuklear",
                },
                "installer": {
                    "type": "custom",
                    "name": "nuklear",
                },
            },
        ],
    },
    "p7": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "compiler": ["any"],
                "checker": {
                    "type": "custom",
                    "name": "p7",
                },
                "installer": {
                    "type": "custom",
                    "name": "p7",
                },
            },
        ],
    },
    "physfs": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "compiler": ["any"],
                "checker": {
                    "type": "github",
                    "user": "criptych",
                    "repo": "physfs",
                    "ignoreReleases": True,
                },
                "installer": {
                    "type": "custom",
                    "name": "physfs",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "compiler": ["gcc"],
                "checker": {
                    "type": "debian",
                    "source": "libphysfs",
                    "package": "libphysfs-dev",
                },
                "installer": {
                    "type": "debian",
                    "package": "libphysfs-dev",
                },
            },
        ],
    },
    "portaudio": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "compiler": ["any"],
                "checker": {
                    "type": "custom",
                    "name": "portaudio",
                },
                "installer": {
                    "type": "custom",
                    "name": "portaudio",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "compiler": ["gcc"],
                "checker": {
                    "type": "debian",
                    "source": "portaudio19",
                    "package": "portaudio19-dev",
                },
                "installer": {
                    "type": "debian",
                    "package": "portaudio19-dev",
                },
            },
        ],
    },
    "saneopt": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "compiler": ["any"],
                "checker": {
                    "type": "github",
                    "user": "mmalecki",
                    "repo": "saneopt",
                },
                "installer": {
                    "type": "custom",
                    "name": "saneopt",
                },
            },
        ],
    },
    "sdl2": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "compiler": ["any"],
                "checker": {
                    "type": "custom",
                    "name": "sdl2",
                },
                "installer": {
                    "type": "custom",
                    "name": "sdl2",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "compiler": ["gcc"],
                "checker": {
                    "type": "debian",
                    "source": "libsdl2",
                    "package": "libsdl2-dev",
                },
                "installer": {
                    "type": "debian",
                    "package": "libsdl2-dev",
                },
            },
        ],
    },
    "sdl2_gfx": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "compiler": ["any"],
                "checker": {
                    "type": "sourceforge",
                    "project": "sdl2gfx",
                },
                "installer": {
                    "type": "custom",
                    "name": "sdl2_gfx",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "compiler": ["gcc"],
                "checker": {
                    "type": "debian",
                    "source": "libsdl2-gfx",
                    "package": "libsdl2-gfx-dev",
                },
                "installer": {
                    "type": "debian",
                    "package": "libsdl2-gfx-dev",
                },
            },
        ],
    },
    "sdl2_gpu": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "compiler": ["any"],
                "checker": {
                    "type": "github",
                    "user": "grimfang4",
                    "repo": "sdl-gpu",
                    "ignoreReleases": True,
                },
                "installer": {
                    "type": "custom",
                    "name": "sdl2_gpu",
                },
            },
        ],
    },
    "sdl2_image": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "compiler": ["any"],
                "checker": {
                    "type": "custom",
                    "name": "sdl2_image",
                },
                "installer": {
                    "type": "custom",
                    "name": "sdl2_image",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "compiler": ["gcc"],
                "checker": {
                    "type": "debian",
                    "source": "libsdl2-image",
                    "package": "libsdl2-image-dev",
                },
                "installer": {
                    "type": "debian",
                    "package": "libsdl2-image-dev",
                },
            },
        ],
    },
    "sdl2_mixer": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "compiler": ["any"],
                "checker": {
                    "type": "custom",
                    "name": "sdl2_mixer",
                },
                "installer": {
                    "type": "custom",
                    "name": "sdl2_mixer",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "compiler": ["gcc"],
                "checker": {
                    "type": "debian",
                    "source": "libsdl2-mixer",
                    "package": "libsdl2-mixer-dev",
                },
                "installer": {
                    "type": "debian",
                    "package": "libsdl2-mixer-dev",
                },
            },
        ],
    },
    "sdl2_ttf": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "compiler": ["any"],
                "checker": {
                    "type": "custom",
                    "name": "sdl2_ttf",
                },
                "installer": {
                    "type": "custom",
                    "name": "sdl2_ttf",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "compiler": ["gcc"],
                "checker": {
                    "type": "debian",
                    "source": "libsdl2-ttf",
                    "package": "libsdl2-ttf-dev",
                },
                "installer": {
                    "type": "debian",
                    "package": "libsdl2-ttf-dev",
                },
            },
        ],
    },
    "squirrel": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "compiler": ["any"],
                "checker": {
                    "type": "github",
                    "user": "albertodemichelis",
                    "repo": "squirrel",
                },
                "installer": {
                    "type": "custom",
                    "name": "squirrel",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "compiler": ["gcc"],
                "checker": {
                    "type": "debian",
                    "source": "squirrel3",
                    "package": "libsquirrel-dev",
                },
                "installer": {
                    "type": "debian",
                    "package": "libsquirrel-dev",
                },
            },
        ],
    },
    "std_rect_pack": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "compiler": ["any"],
                "checker": {
                    "type": "custom",
                    "name": "stb_rect_pack",
                },
                "installer": {
                    "type": "custom",
                    "name": "stb_rect_pack",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "compiler": ["any"],
                "checker": {
                    "type": "debian",
                    "source": "libstb",
                    "package": "libstb-dev",
                },
                "installer": {
                    "type": "debian",
                    "package": "libstb-dev",
                },
            },
        ],
    },
    "tinyfiledialogs": {
        "type": "library",
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "compiler": ["any"],
                "checker": {
                    "type": "custom",
                    "name": "tinyfiledialogs",
                },
                "installer": {
                    "type": "custom",
                    "name": "tinyfiledialogs",
                },
            },
        ],
    },
    "utf": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "compiler": ["any"],
                "checker": {
                    "type": "github",
                    "user": "andlabs",
                    "repo": "utf",
                },
                "installer": {
                    "type": "custom",
                    "name": "utf",
                },
            },
        ],
    },
    "utf8": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "compiler": ["any"],
                "checker": {
                    "type": "github",
                    "user": "haipome",
                    "repo": "utf8",
                },
                "installer": {
                    "type": "custom",
                    "name": "utf8",
                },
            },
        ],
    },
    "wget": {
        "platform": "host",
        "projects": [
            #{
                #"arch": ["any"],
                #"os": ["any"],
                #"osVersion": ["any"],
                #"compiler": ["any"],
                #"checker": {
                    #"type": "custom",
                    #"name": "wget",
                #},
                #"installer": {
                    #"type": "custom",
                    #"name": "wget",
                #},
            #},
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "compiler": ["gcc"],
                "checker": {
                    "type": "debian",
                    "source": "wget",
                    "package": "wget",
                },
                "installer": {
                    "type": "debian",
                    "package": "wget",
                },
            },
        ],
    },
    "x86_64-w64-mingw32-gcc": {
        "platform": "host",
        "projects": [
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "compiler": ["any"],
                "checker": {
                    "type": "debian",
                    "source": "gcc-mingw-w64",
                    "package": "gcc-mingw-w64-x86-64",
                },
                "installer": {
                    "type": "debian",
                    "package": "gcc-mingw-w64-x86-64",
                },
            },
        ],
    },
    "zlib": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "compiler": ["any"],
                "checker": {
                    "type": "custom",
                    "name": "zlib",
                },
                "installer": {
                    "type": "custom",
                    "name": "zlib",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "compiler": ["gcc"],
                "checker": {
                    "type": "debian",
                    "source": "zlib",
                    "package": "zlib1g-dev",
                },
                "installer": {
                    "type": "debian",
                    "package": "zlib1g-dev",
                },
            },
        ],
    },
}

class ConfigSoftware:
    def __init__(self, customData = {}):
        self.data = {**data, **customData}

    def AddData(self, customData):
        self.data = {**self.data, **customData}

    def GetData(self):
        return self.data
