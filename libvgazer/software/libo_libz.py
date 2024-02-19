data = {
    "libogg": {
        "platform": "target",
        "projects": [
            {
                "fallback": True,
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "license": ["bsd-3"],
                "changelog": "https://xiph.org/press/",
                "prereqs": [
                    "{triplet}-gcc",
                    "autoconf",
                    "automake",
                    "libtool",
                    "make",
                ],
                "checker": {
                    "type": "git",
                    "url": "https://gitlab.xiph.org/xiph/ogg.git",
                },
                "installer": {
                    "type": "custom",
                    "name": "libogg",
                },
            },
            {
                "arch": ["any"],
                "os": ["archlinux"],
                "osVersion": ["latest"],
                "abi": ["gnu"],
                "license": ["bsd-3"],
                "changelog": "https://xiph.org/press/",
                "checker": {
                    "type": "pacman",
                    "package": "libogg",
                },
                "installer": {
                    "type": "pacman",
                    "package": "libogg",
                },
            },
            {
                "arch": ["any"],
                "os": ["steamrt"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "license": ["bsd-3"],
                "changelog": "https://xiph.org/press/",
                "checker": {
                    "type": "apt-cache",
                    "package": "libogg-dev",
                },
                "installer": {
                    "type": "not-needed",
                },
            },
        ],
    },
    "libpng": {
        "platform": "target",
        "projects": [
            {
                "fallback": True,
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "license": ["libpng-2.0"],
                "changelog": "http://www.libpng.org/pub/png/pngnews.html",
                "prereqs": [
                    "{triplet}-gcc",
                    "{triplet}-pkg-config",
                    "make",
                    "zlib",
                ],
                "checker": {
                    "type": "git",
                    "url": "git://git.code.sf.net/p/libpng/code",
                    "hint": r'(:?v1\.6\.\d\d$)|(:?v1\.7\.\d+$)',
                },
                "installer": {
                    "type": "custom",
                    "name": "libpng",
                },
            },
            {
                "arch": ["any"],
                "os": ["archlinux"],
                "osVersion": ["latest"],
                "abi": ["gnu"],
                "license": ["bsd-3"],
                "changelog": "https://xiph.org/press/",
                "checker": {
                    "type": "pacman",
                    "package": "libpng",
                },
                "installer": {
                    "type": "pacman",
                    "package": "libpng",
                },
            },
            {
                "arch": ["any"],
                "os": ["steamrt"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "license": ["libpng-2.0"],
                "changelog": "http://www.libpng.org/pub/png/pngnews.html",
                "checker": {
                    "type": "apt-cache",
                    "package": "libpng-dev",
                },
                "installer": {
                    "type": "not-needed",
                },
            },
        ],
    },
    "libsir": {
        "platform": "target",
        "projects": [
            {
                "fallback": True,
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "license": ["mit"],
                "changelog": "https://github.com/aremmell/libsir/releases",
                "prereqs": [
                    "{triplet}-gcc",
                    "make",
                ],
                "checker": {
                    "type": "git",
                    "url": "https://github.com/aremmell/libsir.git",
                },
                "installer": {
                    "type": "custom",
                    "name": "libsir",
                },
            },
        ],
    },
    "libtool": {
        "platform": "host",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "changelog": "https://savannah.gnu.org/news/?group=libtool",
                "prereqs": [
                    "autoconf",
                    "automake",
                    "gcc",
                    "help2man",
                    "make",
                    "makeinfo",
                    "xz",
                ],
                "checker": {
                    "type": "git",
                    "url": "git://git.savannah.gnu.org/libtool.git",
                },
                "installer": {
                    "type": "custom",
                    "name": "libtool",
                },
            },
            {
                "arch": ["any"],
                "os": ["archlinux"],
                "osVersion": ["latest"],
                "abi": ["any"],
                "changelog": "https://savannah.gnu.org/news/?group=libtool",
                "checker": {
                    "type": "pacman",
                    "package": "libtool",
                },
                "installer": {
                    "type": "pacman",
                    "package": "libtool",
                },
            },
            {
                "arch": ["any"],
                "os": ["oraclelinux"],
                "osVersion": ["7"],
                "abi": ["any"],
                "changelog": "https://savannah.gnu.org/news/?group=libtool",
                "prereqs": [
                    "autoconf",
                    "automake",
                    "gcc",
                    "help2man",
                    "make",
                    "makeinfo",
                    "patch",
                    "xz",
                ],
                "checker": {
                    "type": "git",
                    "url": "git://git.savannah.gnu.org/libtool.git",
                },
                "installer": {
                    "type": "custom",
                    "name": "libtool",
                },
            },
            {
                "arch": ["any"],
                "os": ["steamrt"],
                "osVersion": ["any"],
                "abi": ["any"],
                "changelog": "https://savannah.gnu.org/news/?group=libtool",
                "checker": {
                    "type": "apt-cache",
                    "package": "libtool",
                },
                "installer": {
                    "type": "not-needed",
                },
            },
        ],
    },
    "libvorbis": {
        "platform": "target",
        "projects": [
            {
                "fallback": True,
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "license": ["bsd-3"],
                "changelog": "https://xiph.org/press/",
                "prereqs": [
                    "{triplet}-gcc",
                    "{triplet}-pkg-config",
                    "autoconf",
                    "automake",
                    "libogg",
                    "libtool",
                    "make",
                ],
                "checker": {
                    "type": "git",
                    "url": "https://gitlab.xiph.org/xiph/vorbis.git",
                },
                "installer": {
                    "type": "custom",
                    "name": "libvorbis",
                },
            },
            {
                "arch": ["any"],
                "os": ["archlinux"],
                "osVersion": ["latest"],
                "abi": ["gnu"],
                "license": ["bsd-3"],
                "changelog": "https://xiph.org/press/",
                "checker": {
                    "type": "pacman",
                    "package": "libvorbis",
                },
                "installer": {
                    "type": "pacman",
                    "package": "libvorbis",
                },
            },
            {
                "arch": ["any"],
                "os": ["steamrt"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "license": ["bsd-3"],
                "changelog": "https://xiph.org/press/",
                "checker": {
                    "type": "apt-cache",
                    "package": "libvorbis-dev",
                },
                "installer": {
                    "type": "not-needed",
                },
            },
        ],
    },
    "libxext": {
        "platform": "target",
        "projects": [
            {
                "fallback": True,
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "license": ["mit", "x11", "hpnd", "hpnd-sv", "smlnj"],
                "changelog": "https://gitlab.freedesktop.org/xorg/lib/libxext/-/tags",
                "prereqs": [
                    "{triplet}-gcc",
                    "{triplet}-pkg-config",
                    "autoconf",
                    "libtool",
                    "make",
                    "xlib",
                    "xorg-macros",
                    "xorgproto",
                ],
                "checker": {
                    "type": "git",
                    "url": "https://gitlab.freedesktop.org/xorg/lib/libxext.git",
                    "hint": r'libXext-\d\.\d(\.\d+(\.\d)?)?$',
                },
                "installer": {
                    "type": "custom",
                    "name": "libxext",
                },
            },
            {
                "arch": ["any"],
                "os": ["archlinux"],
                "osVersion": ["latest"],
                "abi": ["gnu"],
                "license": ["mit", "x11", "hpnd", "hpnd-sv", "smlnj"],
                "changelog": "https://gitlab.freedesktop.org/xorg/lib/libxext/-/tags",
                "checker": {
                    "type": "pacman",
                    "package": "libxext",
                },
                "installer": {
                    "type": "pacman",
                    "package": "libxext",
                },
            },
            {
                "arch": ["any"],
                "os": ["steamrt"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "license": ["mit", "x11", "hpnd", "hpnd-sv", "smlnj"],
                "changelog": "https://gitlab.freedesktop.org/xorg/lib/libxext/-/tags",
                "checker": {
                    "type": "apt-cache",
                    "package": "libxext-dev",
                },
                "installer": {
                    "type": "not-needed",
                },
            },
        ],
    },
}
