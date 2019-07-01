data = {
    "cjson": {
        "platform": "target",
        "projects": {
            "github": {
                "user": "DaveGamble",
                "repo": "cJSON"
            },
            "debian": {
                "generic": {
                    "source": "cjson",
                    "package": "libcjson-dev",
                },
            },
        },
    },
    "cmake": {
        "platform": "host",
        "projects": {
            "custom": "cmake",
            "debian": {
                "generic": {
                    "source": "cmake",
                    "package": "cmake",
                },
            },
        },
    },
    "cmocka": {
        "platform": "target",
        "projects": {
            "custom": "cmocka",
            "debian": {
                "generic": {
                    "source": "cmocka",
                    "package": "libcmocka-dev",
                },
            },
        },
    },
    "dr_wav": {
        "platform": "target",
        "projects": {
            "custom": "dr_wav",
        },
    },
    "duktape": {
        "platform": "target",
        "projects": {
            "github": {
                "user": "svaarala",
                "repo": "duktape",
            },
            "debian": {
                "generic": {
                    "source": "duktape",
                    "package": "duktape-dev",
                },
            },
        },
    },
    "freetype": {
        "platform": "target",
        "projects": {
            "custom": "freetype",
            "debian": {
                "generic": {
                    "source": "freetype",
                    "package": "libfreetype6-dev",
                },
            },
        },
    },
    "giflib": {
        "platform": "target",
        "projects": {
            "sourceforge": "giflib",
            "debian": {
                "generic": {
                    "source": "giflib",
                    "package": "libgif-dev",
                },
            },
        },
    },
    "glew": {
        "platform": "target",
        "projects": {
            "sourceforge": "glew",
            "debian": {
                "generic": {
                    "source": "glew",
                    "package": "libglew-dev",
                },
            },
        },
    },
    "glib": {
        "platform": "target",
        "projects": {
            "custom": "glib",
            "debian": {
                "generic": {
                    "source": "glib2.0",
                    "package": "libglib2.0-dev",
                },
            },
        },
    },
    "harfbuzz": {
        "platform": "target",
        "projects": {
            "github": {
                "user": "harfbuzz",
                "repo": "harfbuzz",
            },
            "debian": {
                "generic": {
                    "source": "harfbuzz",
                    "package": "libharfbuzz-dev",
                },
            },
        },
    },
    "icu": {
        "platform": "target",
        "projects": {
            "custom": "icu",
            "debian": {
                "generic": {
                    "source": "icu",
                    "package": "libicu-dev",
                },
            },
        },
    },
    "inih": {
        "platform": "target",
        "projects": {
            "github": {
                "user": "benhoyt",
                "repo": "inih",
            },
            "debian": {
                "generic": {
                    "source": "libinih",
                    "package": "libinih-dev",
                },
            },
        },
    },
    "jpeg": {
        "platform": "target",
        "projects": {
            "custom": "jpeg",
            "debian": {
                "generic": {
                    "source": "libjpeg-turbo",
                    "package": "libjpeg-dev",
                },
            },
        },
    },
    "lazy-winapi.c": {
        "platform": "target",
        "projects": {
            "github": {
                "user": "DoumanAsh",
                "repo": "lazy-winapi.c",
            },
        },
    },
    "libbzip2": {
        "platform": "target",
        "projects": {
            "sourceforge": "bzip2",
            "debian": {
                "generic": {
                    "source": "bzip2",
                    "package": "libbz2-dev",
                },
            },
        },
    },
    "libffi": {
        "platform": "target",
        "projects": {
            "custom": "libffi",
            "debian": {
                "generic": {
                    "source": "libffi",
                    "package": "libffi-dev",
                },
            },
        },
    },
    "libflac": {
        "platform": "target",
        "projects": {
            "xiph": "libflac",
            "debian": {
                "generic": {
                    "source": "flac",
                    "package": "libflac-dev",
                },
            },
        },
    },
    "libiconv": {
        "platform": "target",
        "projects": {
            "custom": "libiconv",
        },
    },
    "libintl-lite": {
        "platform": "target",
        "projects": {
            "github": {
                "user": "j-jorge",
                "repo": "libintl-lite",
            },
        },
    },
    "liblzma": {
        "platform": "target",
        "projects": {
            "sourceforge": "lzmautils",
            "debian": {
                "generic": {
                    "source": "xz-utils",
                    "package": "liblzma-dev",
                },
            },
        },
    },
    "libmodplug": {
        "platform": "target",
        "projects": {
            "sourceforge": "modplug-xmms",
            "debian": {
                "generic": {
                    "source": "libmodplug",
                    "package": "libmodplug-dev",
                },
            },
        },
    },
    "libogg": {
        "platform": "target",
        "projects": {
            "xiph": "libogg",
            "debian": {
                "generic": {
                    "source": "libogg",
                    "package": "libogg-dev",
                },
            },
        },
    },
    "libpng": {
        "platform": "target",
        "projects": {
            "sourceforge": "libpng",
            "debian": {
                "generic": {
                    "source": "libpng1.6",
                    "package": "libpng-dev",
                },
            },
        },
    },
    "libtiff": {
        "platform": "target",
        "projects": {
            "custom": "libtiff",
            "debian": {
                "generic": {
                    "source": "tiff",
                    "package": "libtiff-dev",
                },
            },
        },
    },
    "libvorbis": {
        "platform": "target",
            "xiph": "libvorbis",
            "debian": {
                "generic": {
                    "source": "libvorbis",
                    "package": "libvorbis-dev",
                },
            },
    },
    "libwebp": {
        "platform": "target",
        "projects": {
            "custom": "libwebp",
            "debian": {
                "generic": {
                    "source": "libwebp",
                    "package": "libwebp-dev",
                },
            },
        },
    },
    "lua": {
        "platform": "target",
        "projects": {
            "custom": "lua",
            "debian": {
                "generic": {
                    "source": "lua5.3",
                    "package": "liblua5.3-dev",
                },
            },
        },
    },
    "minini": {
        "platform": "target",
        "projects": {
            "github": {
                "user": "compuphase",
                "repo": "minIni",
            },
            "debian": {
                "generic": {
                    "source": "libminini",
                    "package": "libminini-dev",
                },
            },
        },
    },
    "mpg123": {
        "platform": "target",
        "projects": {
            "sourceforge": "mpg123",
            "debian": {
                "generic": {
                    "source": "libmpg123",
                    "package": "libmpg123-dev",
                },
            },
        },
    },
    "nuklear": {
        "platform": "target",
        "projects": {
            "github": {
                "user": "vurtun",
                "repo": "nuklear",
            },
        },
    },
    "p7": {
        "platform": "target",
        "projects": {
            "custom": "p7",
        },
    },
    "physfs": {
        "platform": "target",
        "projects": {
            "github": {
                "user": "criptych",
                "repo": "physfs",
                "ignore_releases": True,
            },
            "debian": {
                "generic": {
                    "source": "libphysfs",
                    "package": "libphysfs-dev",
                },
            },
        },
    },
    "portaudio": {
        "platform": "target",
        "projects": {
            "custom": "portaudio",
            "debian": {
                "generic": {
                    "source": "portaudio19",
                    "package": "portaudio19-dev",
                },
            },
        },
    },
    "saneopt": {
        "platform": "target",
        "projects": {
            "github": {
                "user": "mmalecki",
                "repo": "saneopt",
            },
        },
    },
    "sdl2": {
        "platform": "target",
        "projects": {
            "custom": "sdl2",
            "debian":  {
                "generic": {
                    "source": "libsdl2",
                    "package": "libsdl2-dev",
                },
            },
        },
    },
    "sdl2_gfx": {
        "platform": "target",
        "projects": {
            "sourceforge": "sdl2gfx",
            "debian": {
                "generic": {
                    "source": "libsdl2-gfx",
                    "package": "libsdl2-gfx-dev",
                },
            },
        },
    },
    "sdl2_gpu": {
        "platform": "target",
        "projects": {
            "github": {
                "user": "grimfang4",
                "repo": "sdl-gpu",
                "ignore_releases": True,
            },
        },
    },
    "sdl2_image": {
        "platform": "target",
        "projects": {
            "custom": "sdl2_image",
            "debian": {
                "generic": {
                    "source": "libsdl2-image",
                    "package": "libsdl2-image-dev",
                },
            },
        },
    },
    "sdl2_mixer": {
        "platform": "target",
        "projects": {
            "custom": "sdl2_mixer",
            "debian": {
                "generic": {
                    "source": "libsdl2-mixer",
                    "package": "libsdl2-mixer-dev",
                },
            },
        },
    },
    "sdl2_ttf": {
        "platform": "target",
        "projects": {
            "custom": "sdl2_ttf",
            "debian": {
                "generic": {
                    "source": "libsdl2-ttf",
                    "package": "libsdl2-ttf-dev",
                },
            },
        },
    },
    "squirrel": {
        "platform": "target",
        "projects": {
            "github": {
                "user": "albertodemichelis",
                "repo": "squirrel",
            },
            "debian": {
                "generic": {
                    "source": "squirrel3",
                    "package": "libsquirrel-dev",
                },
            },
        },
    },
    "std_rect_pack": {
        "platform": "target",
        "projects": {
            "custom": "stb_rect_pack",
            "debian": {
                "generic": {
                    "source": "libstb",
                    "package": "libstb-dev",
                },
            },
        },
    },
    "tinyfiledialogs": {
        "type": "library",
        "platform": "target",
        "projects": {
            "custom": "tinyfiledialogs",
        },
    },
    "utf": {
        "platform": "target",
        "projects": {
            "github": {
                "user": "andlabs",
                "repo": "utf",
            },
        },
    },
    "utf8": {
        "platform": "target",
        "projects": {
            "github": {
                "user": "haipome",
                "repo": "utf8",
            },
        },
    },
    "zlib": {
        "platform": "target",
        "projects": {
            "custom": "zlib",
            "debian": {
                "generic": {
                    "source": "zlib",
                    "package": "zlib1g-dev",
                },
            },
        },
    },
}

class ConfigSoftware:
    def __init__(self, customData = {}):
        self.data = {**data, **customData}

    def AddData(self, customData):
        self.data = {**self.data, **customData}

    def GetData(self):
        return self.data
