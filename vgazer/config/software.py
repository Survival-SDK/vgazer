data = {
    "autoconf": {
        "platform": "host",
        "projects": [
            {
                "arch": ["any"],
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "autoconf",
                },
                "installer": {
                    "type": "apk",
                    "package": "autoconf",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "debian",
                    "source": "autoconf",
                },
                "installer": {
                    "type": "apt",
                    "package": "autoconf",
                },
            },
        ],
    },
    "automake": {
        "platform": "host",
        "projects": [
            {
                "arch": ["any"],
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "automake",
                },
                "installer": {
                    "type": "apk",
                    "package": "automake",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["stretch"],
                "abi": ["any"],
                "checker": {
                    "type": "debian",
                    "source": "automake-1.15",
                },
                "installer": {
                    "type": "apt",
                    "package": "automake",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["buster", "bullseye", "sid"],
                "abi": ["any"],
                "checker": {
                    "type": "debian",
                    "source": "automake-1.16",
                },
                "installer": {
                    "type": "apt",
                    "package": "automake",
                },
            },
        ],
    },
    "automake1.11": {
        "platform": "host",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "custom",
                    "name": "automake1_11",
                },
                "installer": {
                    "type": "custom",
                    "name": "automake1_11",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "debian",
                    "source": "automake1.11",
                },
                "installer": {
                    "type": "apt",
                    "package": "automake1.11",
                },
            },
        ],
    },
    "autopoint": {
        "platform": "host",
        "projects": [
            {
                "arch": ["any"],
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "gettext",
                },
                "installer": {
                    "type": "apk",
                    "package": "gettext",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "debian",
                    "source": "gettext",
                },
                "installer": {
                    "type": "apt",
                    "package": "autopoint",
                },
            },
        ],
    },
    "bison": {
        "platform": "host",
        "projects": [
            {
                "arch": ["any"],
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "bison",
                },
                "installer": {
                    "type": "apk",
                    "package": "bison",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "debian",
                    "source": "bison",
                },
                "installer": {
                    "type": "apt",
                    "package": "bison",
                },
            },
        ],
    },
    "cjson": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
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
                "osVersion": ["buster", "bullseye", "sid"],
                "abi": ["gnu"],
                "checker": {
                    "type": "debian",
                    "source": "cjson",
                },
                "installer": {
                    "type": "apt",
                    "package": "libcjson-dev",
                },
            },
        ],
    },
    "cmake": {
        "platform": "host",
        "projects": [
            {
                "arch": ["any"],
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "cmake",
                },
                "installer": {
                    "type": "apk",
                    "package": "cmake",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "debian",
                    "source": "cmake",
                },
                "installer": {
                    "type": "apt",
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
                "abi": ["any"],
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
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["musl"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "cmocka-dev",
                },
                "installer": {
                    "type": "apk",
                    "package": "cmocka-dev",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "checker": {
                    "type": "debian",
                    "source": "cmocka",
                },
                "installer": {
                    "type": "apt",
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
                "abi": ["any"],
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
                "abi": ["any"],
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
                "abi": ["gnu"],
                "checker": {
                    "type": "debian",
                    "source": "duktape",
                },
                "installer": {
                    "type": "apt",
                    "package": "duktape-dev",
                },
            },
        ],
    },
    "file": {
        "platform": "host",
        "projects": [
            {
                "arch": ["any"],
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "file",
                },
                "installer": {
                    "type": "apk",
                    "package": "file",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "debian",
                    "source": "file",
                },
                "installer": {
                    "type": "apt",
                    "package": "file",
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
                "abi": ["any"],
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
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["musl"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "freetype-dev",
                },
                "installer": {
                    "type": "apk",
                    "package": "freetype-dev",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "checker": {
                    "type": "debian",
                    "source": "freetype",
                },
                "installer": {
                    "type": "apt",
                    "package": "libfreetype6-dev",
                },
            },
        ],
    },
    "gettext": {
        "platform": "host",
        "projects": [
            {
                "arch": ["any"],
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "gettext",
                },
                "installer": {
                    "type": "apk",
                    "package": "gettext",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "debian",
                    "source": "gettext",
                },
                "installer": {
                    "type": "apt",
                    "package": "gettext",
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
                "abi": ["any"],
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
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["musl"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "giflib-dev",
                },
                "installer": {
                    "type": "apk",
                    "package": "giflib-dev",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "checker": {
                    "type": "debian",
                    "source": "giflib",
                },
                "installer": {
                    "type": "apt",
                    "package": "libgif-dev",
                },
            },
        ],
    },
    "git": {
        "platform": "host",
        "projects": [
            {
                "arch": ["any"],
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "git",
                },
                "installer": {
                    "type": "apk",
                    "package": "git",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "debian",
                    "source": "git",
                },
                "installer": {
                    "type": "apt",
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
                "abi": ["any"],
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
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["musl"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "glew-dev",
                },
                "installer": {
                    "type": "apk",
                    "package": "glew-dev",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "checker": {
                    "type": "debian",
                    "source": "glew",
                },
                "installer": {
                    "type": "apt",
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
                "abi": ["any"],
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
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["musl"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "glib-dev",
                },
                "installer": {
                    "type": "apk",
                    "package": "glib-dev",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "checker": {
                    "type": "debian",
                    "source": "glib2.0",
                },
                "installer": {
                    "type": "apt",
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
                "abi": ["any"],
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
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["musl"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "harfbuzz-dev",
                },
                "installer": {
                    "type": "apk",
                    "package": "harfbuzz-dev",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "checker": {
                    "type": "debian",
                    "source": "harfbuzz",
                },
                "installer": {
                    "type": "apt",
                    "package": "libharfbuzz-dev",
                },
            },
        ],
    },
    "i586-linux-musl-g++": {
        "platform": "host",
        "projects": [
            {
                "arch": ["i686"],
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "g++",
                },
                "installer": {
                    "type": "apk",
                    "package": "g++",
                },
            },
        ],
    },
    "i586-linux-musl-gcc": {
        "platform": "host",
        "projects": [
            {
                "arch": ["i686"],
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "gcc",
                },
                "installer": {
                    "type": "apk",
                    "package": "gcc",
                },
            },
        ],
    },
    "i686-linux-gnu-g++": {
        "platform": "host",
        "projects": [
            {
                "arch": ["i686"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "debian",
                    "source": "gcc-defaults",
                },
                "installer": {
                    "type": "apt",
                    "package": "g++",
                },
            },
            {
                "arch": ["x86_64"],
                "os": ["debian"],
                "osVersion": ["buster", "bullseye", "sid"],
                "abi": ["any"],
                "checker": {
                    "type": "debian",
                    "source": "gcc-defaults",
                },
                "installer": {
                    "type": "apt",
                    "package": "g++-i686-linux-gnu",
                },
            },
        ],
    },
    "i686-linux-gnu-gcc": {
        "platform": "host",
        "projects": [
            {
                "arch": ["i686"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "debian",
                    "source": "gcc-defaults",
                },
                "installer": {
                    "type": "apt",
                    "package": "gcc",
                },
            },
            {
                "arch": ["x86_64"],
                "os": ["debian"],
                "osVersion": ["buster", "bullseye", "sid"],
                "abi": ["any"],
                "checker": {
                    "type": "debian",
                    "source": "gcc-defaults",
                },
                "installer": {
                    "type": "apt",
                    "package": "gcc-i686-linux-gnu",
                },
            },
        ],
    },
    "i686-linux-musl-g++": {
        "platform": "host",
        "projects": [
            {
                "arch": ["i686"],
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "g++",
                },
                "installer": {
                    "type": "apk",
                    "package": "g++",
                },
            },
        ],
    },
    "i686-linux-musl-gcc": {
        "platform": "host",
        "projects": [
            {
                "arch": ["i686"],
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "gcc",
                },
                "installer": {
                    "type": "apk",
                    "package": "gcc",
                },
            },
            {
                "arch": ["i686"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "debian",
                    "source": "musl",
                },
                "installer": {
                    "type": "apt",
                    "package": "musl-tools",
                },
            },
        ],
    },
    "i686-w64-mingw32-g++": {
        "platform": "host",
        "projects": [
            {
                "arch": ["i686"],
                "os": ["alpine"],
                "osVersion": ["edge"],
                "abi": ["any"],
                "checker": {
                    "type": "alpine",
                    "repo": "testing",
                    "package": "mingw-w64-gcc",
                },
                "installer": {
                    "type": "apk",
                    "package": "mingw-w64-gcc",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "debian",
                    "source": "g++-mingw-w64",
                },
                "installer": {
                    "type": "apt",
                    "package": "g++-mingw-w64-i686",
                },
            },
        ],
    },
    "i686-w64-mingw32-gcc": {
        "platform": "host",
        "projects": [
            {
                "arch": ["i686"],
                "os": ["alpine"],
                "osVersion": ["edge"],
                "abi": ["any"],
                "checker": {
                    "type": "alpine",
                    "repo": "testing",
                    "package": "mingw-w64-gcc",
                },
                "installer": {
                    "type": "apk",
                    "package": "mingw-w64-gcc",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "debian",
                    "source": "gcc-mingw-w64",
                },
                "installer": {
                    "type": "apt",
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
                "abi": ["any"],
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
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["musl"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "icu-dev",
                },
                "installer": {
                    "type": "apk",
                    "package": "icu-dev",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "checker": {
                    "type": "debian",
                    "source": "icu",
                },
                "installer": {
                    "type": "apt",
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
                "abi": ["any"],
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
                "osVersion": ["buster", "bullseye", "sid"],
                "abi": ["gnu"],
                "checker": {
                    "type": "debian",
                    "source": "libinih",
                },
                "installer": {
                    "type": "apt",
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
                "abi": ["any"],
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
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["musl"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "jpeg-dev",
                },
                "installer": {
                    "type": "apk",
                    "package": "jpeg-dev",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "checker": {
                    "type": "debian",
                    "source": "libjpeg-turbo",
                },
                "installer": {
                    "type": "apt",
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
                "abi": ["any"],
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
                "abi": ["any"],
                "checker": {
                    "type": "sourceforge",
                    "project": "bzip2",
                },
                "installer": {
                    "type": "custom",
                    "name": "bzip2",
                },
            },
            {
                "arch": ["any"],
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["musl"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "bzip2-dev",
                },
                "installer": {
                    "type": "apk",
                    "package": "bzip2-dev",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "checker": {
                    "type": "debian",
                    "source": "bzip2",
                },
                "installer": {
                    "type": "apt",
                    "package": "libbz2-dev",
                },
            },
        ],
    },
    "libclipboard": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "github",
                    "user": "jtanx",
                    "repo": "libclipboard",
                },
                "installer": {
                    "type": "custom",
                    "name": "libclipboard",
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
                "abi": ["any"],
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
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["musl"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "libffi-dev",
                },
                "installer": {
                    "type": "apk",
                    "package": "libffi-dev",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "checker": {
                    "type": "debian",
                    "source": "libffi",
                },
                "installer": {
                    "type": "apt",
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
                "abi": ["any"],
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
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["musl"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "flac-dev",
                },
                "installer": {
                    "type": "apk",
                    "package": "flac-dev",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "checker": {
                    "type": "debian",
                    "source": "flac",
                },
                "installer": {
                    "type": "apt",
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
                "abi": ["any"],
                "checker": {
                    "type": "custom",
                    "name": "libiconv",
                },
                "installer": {
                    "type": "custom",
                    "name": "libiconv",
                },
            },
            {
                "arch": ["any"],
                "os": ["alpine"],
                "osVersion": ["3.10", "edge"],
                "abi": ["gnu"],
                "checker": {
                    "type": "alpine",
                    "repo": "community",
                    "package": "gnu-libiconv-dev",
                },
                "installer": {
                    "type": "apk",
                    "package": "gnu-libiconv-dev",
                },
            },
            {
                "arch": ["any"],
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["musl"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "musl-dev",
                },
                "installer": {
                    "type": "apk",
                    "package": "musl-dev",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "checker": {
                    "type": "debian",
                    "source": "glibc",
                },
                "installer": {
                    "type": "apt",
                    "package": "libc6-dev",
                },
            },
        ],
    },
    "libintl": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["windows"],
                "osVersion": ["any"],
                "abi": ["any"],
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
            {
                "arch": ["any"],
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["musl"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "gettext-dev",
                },
                "installer": {
                    "type": "apk",
                    "package": "gettext-dev",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "checker": {
                    "type": "debian",
                    "source": "glibc",
                },
                "installer": {
                    "type": "apt",
                    "package": "libc6-dev",
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
                "abi": ["any"],
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
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["musl"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "xz-dev",
                },
                "installer": {
                    "type": "apk",
                    "package": "xz-dev",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "checker": {
                    "type": "debian",
                    "source": "xz-utils",
                },
                "installer": {
                    "type": "apt",
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
                "abi": ["any"],
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
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["musl"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "libmodplug-dev",
                },
                "installer": {
                    "type": "apk",
                    "package": "libmodplug-dev",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "checker": {
                    "type": "debian",
                    "source": "libmodplug",
                },
                "installer": {
                    "type": "apt",
                    "package": "libmodplug-dev",
                },
            },
        ],
    },
    "libmount": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "github",
                    "user": "karelzak",
                    "repo": "util-linux",
                },
                "installer": {
                    "type": "custom",
                    "name": "libmount",
                },
            },
            {
                "arch": ["any"],
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["musl"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "util-linux-dev",
                },
                "installer": {
                    "type": "apk",
                    "package": "util-linux-dev",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "debian",
                    "source": "util-linux",
                },
                "installer": {
                    "type": "apt",
                    "package": "libmount-dev",
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
                "abi": ["any"],
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
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["musl"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "libogg-dev",
                },
                "installer": {
                    "type": "apk",
                    "package": "libogg-dev",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "checker": {
                    "type": "debian",
                    "source": "libogg",
                },
                "installer": {
                    "type": "apt",
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
                "abi": ["any"],
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
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["musl"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "libpng-dev",
                },
                "installer": {
                    "type": "apk",
                    "package": "libpng-dev",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "checker": {
                    "type": "debian",
                    "source": "libpng1.6",
                },
                "installer": {
                    "type": "apt",
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
                "abi": ["any"],
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
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["musl"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "tiff-dev",
                },
                "installer": {
                    "type": "apk",
                    "package": "tiff-dev",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "checker": {
                    "type": "debian",
                    "source": "tiff",
                },
                "installer": {
                    "type": "apt",
                    "package": "libtiff-dev",
                },
            },
        ],
    },
    "libtool": {
        "platform": "host",
        "projects": [
            {
                "arch": ["any"],
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "libtool",
                },
                "installer": {
                    "type": "apk",
                    "package": "libtool",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "debian",
                    "source": "libtool",
                },
                "installer": {
                    "type": "apt",
                    "package": "libtool",
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
                "abi": ["any"],
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
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["musl"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "libvorbis-dev",
                },
                "installer": {
                    "type": "apk",
                    "package": "libvorbis-dev",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "checker": {
                    "type": "debian",
                    "source": "libvorbis",
                },
                "installer": {
                    "type": "apt",
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
                "abi": ["any"],
                "checker": {
                    "type": "custom",
                    "name": "libwebp",
                },
                "installer": {
                    "type": "custom",
                    "name": "libwebp",
                },
            },
            {
                "arch": ["any"],
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["musl"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "libwebp-dev",
                },
                "installer": {
                    "type": "apk",
                    "package": "libwebp-dev",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "checker": {
                    "type": "debian",
                    "source": "libwebp",
                },
                "installer": {
                    "type": "apt",
                    "package": "libwebp-dev",
                },
            },
        ],
    },
    "linux-headers-i686": {
        "platform": "target",
        "projects": [
            {
                "arch": ["i686"],
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "linux-headers",
                },
                "installer": {
                    "type": "apk",
                    "package": "linux-headers",
                },
            },
            {
                "arch": ["i686"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "debian",
                    "source": "linux-latest",
                },
                "installer": {
                    "type": "apt",
                    "package": "linux-headers-686",
                },
            },
        ],
    },
    "linux-headers-x86_64": {
        "platform": "target",
        "projects": [
            {
                "arch": ["x86_64"],
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "linux-headers",
                },
                "installer": {
                    "type": "apk",
                    "package": "linux-headers",
                },
            },
            {
                "arch": ["x86_64"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "debian",
                    "source": "linux-latest",
                },
                "installer": {
                    "type": "apt",
                    "package": "linux-headers-amd64",
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
                "abi": ["any"],
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
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["musl"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "lua5.3-dev",
                },
                "installer": {
                    "type": "apk",
                    "package": "lua5.3-dev",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "checker": {
                    "type": "debian",
                    "source": "lua5.3",
                },
                "installer": {
                    "type": "apt",
                    "package": "liblua5.3-dev",
                },
            },
        ],
    },
    "make": {
        "platform": "host",
        "projects": [
            {
                "arch": ["any"],
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "make",
                },
                "installer": {
                    "type": "apk",
                    "package": "make",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "debian",
                    "source": "make-dfsg",
                },
                "installer": {
                    "type": "apt",
                    "package": "make",
                },
            },
        ],
    },
    "meson": {
        "platform": "host",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "pypi",
                    "package": "meson",
                },
                "installer": {
                    "type": "pip3",
                    "package": "meson",
                },
            },
            {
                "arch": ["any"],
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "meson",
                },
                "installer": {
                    "type": "apk",
                    "package": "meson",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                # glib requires minimal version of Meson 0.49.2. Debian Stretch
                # repos have Meson with version smaller than 0.49.2
                "osVersion": ["buster", "bullseye", "sid"],
                "abi": ["any"],
                "checker": {
                    "type": "debian",
                    "source": "meson",
                },
                "installer": {
                    "type": "apt",
                    "package": "meson",
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
                "abi": ["any"],
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
                "osVersion": ["buster", "bullseye", "sid"],
                "abi": ["gnu"],
                "checker": {
                    "type": "debian",
                    "source": "libminini",
                },
                "installer": {
                    "type": "apt",
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
                "abi": ["any"],
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
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["musl"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "mpg123-dev",
                },
                "installer": {
                    "type": "apk",
                    "package": "mpg123-dev",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "checker": {
                    "type": "debian",
                    "source": "libmpg123",
                },
                "installer": {
                    "type": "apt",
                    "package": "libmpg123-dev",
                },
            },
        ],
    },
    "musl": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["musl"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "musl-dev",
                },
                "installer": {
                    "type": "apk",
                    "package": "musl-dev",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["musl"],
                "checker": {
                    "type": "debian",
                    "source": "musl",
                },
                "installer": {
                    "type": "apt",
                    "package": "musl-dev",
                },
            },
        ],
    },
    "ninja": {
        "platform": "host",
        "projects": [
            {
                "arch": ["any"],
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "ninja",
                },
                "installer": {
                    "type": "apk",
                    "package": "ninja",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "debian",
                    "source": "ninja-build",
                },
                "installer": {
                    "type": "apt",
                    "package": "ninja-build",
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
                "abi": ["any"],
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
                "abi": ["any"],
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
    "perl": {
        "platform": "host",
        "projects": [
            {
                "arch": ["any"],
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "perl",
                },
                "installer": {
                    "type": "apk",
                    "package": "perl",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "debian",
                    "source": "perl",
                },
                "installer": {
                    "type": "apt",
                    "package": "perl",
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
                "abi": ["any"],
                "checker": {
                    "type": "custom",
                    "name": "physfs",
                    "fallback": {
                        "type": "github",
                        "user": "criptych",
                        "repo": "physfs",
                        "ignoreReleases": True,
                    },
                },
                "installer": {
                    "type": "custom",
                    "name": "physfs",
                    "fallback": {
                        "type": "custom",
                        "name": "physfs-github",
                    }
                },
            },
            {
                "arch": ["any"],
                "os": ["alpine"],
                "osVersion": ["edge"],
                "abi": ["musl"],
                "checker": {
                    "type": "alpine",
                    "repo": "testing",
                    "package": "physfs-dev",
                },
                "installer": {
                    "type": "apk",
                    "package": "physfs-dev",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "checker": {
                    "type": "debian",
                    "source": "libphysfs",
                },
                "installer": {
                    "type": "apt",
                    "package": "libphysfs-dev",
                },
            },
        ],
    },
    "pip2": {
        "platform": "host",
        "projects": [
            {
                "arch": ["any"],
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "py2-pip",
                },
                "installer": {
                    "type": "apk",
                    "package": "py2-pip",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "debian",
                    "source": "python-pip",
                },
                "installer": {
                    "type": "apt",
                    "package": "python-pip",
                },
            },
        ],
    },
    "pkg-config": {
        "platform": "host",
        "projects": [
            {
                "arch": ["any"],
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "pkgconf",
                },
                "installer": {
                    "type": "apk",
                    "package": "pkgconf",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "debian",
                    "source": "pkg-config",
                },
                "installer": {
                    "type": "apt",
                    "package": "pkg-config",
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
                "abi": ["any"],
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
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["musl"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "portaudio-dev",
                },
                "installer": {
                    "type": "apk",
                    "package": "portaudio-dev",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "checker": {
                    "type": "debian",
                    "source": "portaudio19",
                },
                "installer": {
                    "type": "apt",
                    "package": "portaudio19-dev",
                },
            },
        ],
    },
    "python2": {
        "platform": "host",
        "projects": [
            {
                "arch": ["any"],
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "python2",
                },
                "installer": {
                    "type": "apk",
                    "package": "python2",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "debian",
                    "source": "python2.7",
                },
                "installer": {
                    "type": "apt",
                    "package": "python2.7",
                },
            },
        ],
    },
    "python2-pyyaml": {
        "platform": "host",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "pypi",
                    "package": "PyYAML",
                },
                "installer": {
                    "type": "pip",
                    "package": "PyYAML",
                },
            },
            {
                "arch": ["any"],
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "py2-yaml",
                },
                "installer": {
                    "type": "apk",
                    "package": "py2-yaml",
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
                "abi": ["any"],
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
                "abi": ["any"],
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
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["musl"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "sdl2-dev",
                },
                "installer": {
                    "type": "apk",
                    "package": "sdl2-dev",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "checker": {
                    "type": "debian",
                    "source": "libsdl2",
                },
                "installer": {
                    "type": "apt",
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
                "abi": ["any"],
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
                "abi": ["gnu"],
                "checker": {
                    "type": "debian",
                    "source": "libsdl2-gfx",
                },
                "installer": {
                    "type": "apt",
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
                "abi": ["any"],
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
                "abi": ["any"],
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
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["musl"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "sdl2_image-dev",
                },
                "installer": {
                    "type": "apk",
                    "package": "sdl2_image-dev",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "checker": {
                    "type": "debian",
                    "source": "libsdl2-image",
                },
                "installer": {
                    "type": "apt",
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
                "abi": ["any"],
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
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["musl"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "sdl2_mixer-dev",
                },
                "installer": {
                    "type": "apk",
                    "package": "sdl2_mixer-dev",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "checker": {
                    "type": "debian",
                    "source": "libsdl2-mixer",
                },
                "installer": {
                    "type": "apt",
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
                "abi": ["any"],
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
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["musl"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "sdl2_ttf-dev",
                },
                "installer": {
                    "type": "apk",
                    "package": "sdl2_ttf-dev",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "checker": {
                    "type": "debian",
                    "source": "libsdl2-ttf",
                },
                "installer": {
                    "type": "apt",
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
                "abi": ["any"],
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
                "abi": ["gnu"],
                "checker": {
                    "type": "debian",
                    "source": "squirrel3",
                },
                "installer": {
                    "type": "apt",
                    "package": "libsquirrel-dev",
                },
            },
        ],
    },
    "stb_rect_pack": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
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
                "abi": ["any"],
                "checker": {
                    "type": "debian",
                    "source": "libstb",
                },
                "installer": {
                    "type": "apt",
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
                "abi": ["any"],
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
    "unzip": {
        "platform": "host",
        "projects": [
            {
                "arch": ["any"],
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "unzip",
                },
                "installer": {
                    "type": "apk",
                    "package": "unzip",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "debian",
                    "source": "unzip",
                },
                "installer": {
                    "type": "apt",
                    "package": "unzip",
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
                "abi": ["any"],
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
                "abi": ["any"],
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
            {
                "arch": ["any"],
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "wget",
                },
                "installer": {
                    "type": "apk",
                    "package": "wget",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "debian",
                    "source": "wget",
                },
                "installer": {
                    "type": "apt",
                    "package": "wget",
                },
            },
        ],
    },
    "x86_64-linux-gnu-g++": {
        "platform": "host",
        "projects": [
            {
                "arch": ["i686"],
                "os": ["debian"],
                "osVersion": ["buster", "bullseye", "sid"],
                "abi": ["any"],
                "checker": {
                    "type": "debian",
                    "source": "gcc-defaults",
                },
                "installer": {
                    "type": "apt",
                    "package": "g++-x86-64-linux-gnu",
                },
            },
            {
                "arch": ["x86_64"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "debian",
                    "source": "gcc-defaults",
                },
                "installer": {
                    "type": "apt",
                    "package": "g++",
                },
            },
        ],
    },
    "x86_64-linux-gnu-gcc": {
        "platform": "host",
        "projects": [
            {
                "arch": ["i686"],
                "os": ["debian"],
                "osVersion": ["buster", "bullseye", "sid"],
                "abi": ["any"],
                "checker": {
                    "type": "debian",
                    "source": "gcc-defaults",
                },
                "installer": {
                    "type": "apt",
                    "package": "gcc-x86-64-linux-gnu",
                },
            },
            {
                "arch": ["x86_64"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "debian",
                    "source": "gcc-defaults",
                },
                "installer": {
                    "type": "apt",
                    "package": "gcc",
                },
            },
        ],
    },
    "x86_64-linux-musl-g++": {
        "platform": "host",
        "projects": [
            {
                "arch": ["x86_64"],
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "g++",
                },
                "installer": {
                    "type": "apk",
                    "package": "g++",
                },
            },
        ],
    },
    "x86_64-linux-musl-gcc": {
        "platform": "host",
        "projects": [
            {
                "arch": ["x86_64"],
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "gcc",
                },
                "installer": {
                    "type": "apk",
                    "package": "gcc",
                },
            },
            {
                "arch": ["x86_64"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "debian",
                    "source": "musl",
                },
                "installer": {
                    "type": "apt",
                    "package": "musl-tools",
                },
            },
        ],
    },
    "x86_64-w64-mingw32-g++": {
        "platform": "host",
        "projects": [
            {
                "arch": ["x86_64"],
                "os": ["alpine"],
                "osVersion": ["edge"],
                "abi": ["any"],
                "checker": {
                    "type": "alpine",
                    "repo": "testing",
                    "package": "mingw-w64-gcc",
                },
                "installer": {
                    "type": "apk",
                    "package": "mingw-w64-gcc",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "debian",
                    "source": "g++-mingw-w64",
                },
                "installer": {
                    "type": "apt",
                    "package": "g++-mingw-w64-x86-64",
                },
            },
        ],
    },
    "x86_64-w64-mingw32-gcc": {
        "platform": "host",
        "projects": [
            {
                "arch": ["x86_64"],
                "os": ["alpine"],
                "osVersion": ["edge"],
                "abi": ["any"],
                "checker": {
                    "type": "alpine",
                    "repo": "testing",
                    "package": "mingw-w64-gcc",
                },
                "installer": {
                    "type": "apk",
                    "package": "mingw-w64-gcc",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "debian",
                    "source": "gcc-mingw-w64",
                },
                "installer": {
                    "type": "apt",
                    "package": "gcc-mingw-w64-x86-64",
                },
            },
        ],
    },
    "xcb": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "custom",
                    "name": "xcb",
                },
                "installer": {
                    "type": "custom",
                    "name": "xcb",
                },
            },
            {
                "arch": ["any"],
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["musl"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "libxcb-dev",
                },
                "installer": {
                    "type": "apk",
                    "package": "libxcb-dev",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "checker": {
                    "type": "debian",
                    "source": "libx11",
                },
                "installer": {
                    "type": "apt",
                    "package": "libx11-xcb-dev",
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
                "abi": ["any"],
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
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["musl"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "zlib-dev",
                },
                "installer": {
                    "type": "apk",
                    "package": "zlib-dev",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "checker": {
                    "type": "debian",
                    "source": "zlib",
                },
                "installer": {
                    "type": "apt",
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
