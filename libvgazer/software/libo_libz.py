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
                    "wget",
                    "{triplet}-gcc",
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
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "license": ["bsd-3"],
                "changelog": "https://xiph.org/press/",
                "checker": {
                    "type": "apt-cache",
                    "package": "libogg-dev",
                },
                "installer": {
                    "type": "apt",
                    "package": "libogg-dev",
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
    # MinGW version here: https://github.com/smurfy/libpciaccess
    "libpciaccess": {
        "platform": "target",
        "projects": [
            {
                "fallback": True,
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "license": ["mit", "isc", "x11"],
                "changelog": "https://gitlab.freedesktop.org/xorg/lib/libpciaccess/-/tags",
                "prereqs": [
                    "wget",
                    "autoconf",
                    "libtool",
                    "{triplet}-pkg-config",
                    "{triplet}-gcc",
                    "make",
                    "xorg-macros",
                ],
                "checker": {
                    "type": "git",
                    "url": "https://gitlab.freedesktop.org/xorg/lib/libpciaccess.git",
                    "hint": r'libpciaccess-\d\.\d+$',
                },
                "installer": {
                    "type": "custom",
                    "name": "libpciaccess",
                    "fallback": {
                        "type": "custom",
                        "name": "libpciaccess-github",
                    },
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "license": ["mit", "isc", "x11"],
                "changelog": "https://gitlab.freedesktop.org/xorg/lib/libpciaccess/-/tags",
                "checker": {
                    "type": "apt-cache",
                    "package": "libpciaccess-dev",
                },
                "installer": {
                    "type": "apt",
                    "package": "libpciaccess-dev",
                },
            },
            {
                "arch": ["any"],
                "os": ["steamrt"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "license": ["mit", "isc", "x11"],
                "changelog": "https://gitlab.freedesktop.org/xorg/lib/libpciaccess/-/tags",
                "checker": {
                    "type": "apt-cache",
                    "package": "libpciaccess-dev",
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
                    "wget",
                    "{triplet}-gcc",
                    "{triplet}-pkg-config",
                    "make",
                    "zlib",
                ],
                "checker": {
                    "type": "git",
                    "url": "git://git.code.sf.net/p/libpng/code",
                    "hint": r'v\d\.\d\.\d+$',
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
                "abi": ["gnu"],
                "license": ["libpng-2.0"],
                "changelog": "http://www.libpng.org/pub/png/pngnews.html",
                "checker": {
                    "type": "apt-cache",
                    "package": "libpng-dev",
                },
                "installer": {
                    "type": "apt",
                    "package": "libpng-dev",
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
                    "wget",
                    "make",
                    "{triplet}-gcc",
                ],
                "checker": {
                    "type": "git",
                    "url": "https://github.com/aremmell/libsir.git",
                },
                "installer": {
                    "type": "custom",
                    "name": "libsir",
                    "fallback": {
                        "type": "custom",
                        "name": "libsir-master",
                    }
                },
            },
        ],
    },
    "libtool": {
        "platform": "host",
        "projects": [
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["buster", "bullseye"],
                "abi": ["any"],
                "changelog": "https://savannah.gnu.org/news/?group=libtool",
                "checker": {
                    "type": "apt-cache",
                    "package": "libtool",
                },
                "installer": {
                    "type": "apt",
                    "package": "libtool",
                    "postInstallCommands": [
                        ["mkdir", "-p", "/usr/local/share/aclocal"],
                        ["ln", "-s", "/usr/share/aclocal/libtool.m4",
                         "/usr/local/share/aclocal/libtool.m4"],
                        ["ln", "-s", "/usr/share/aclocal/ltoptions.m4",
                         "/usr/local/share/aclocal/ltoptions.m4"],
                        ["ln", "-s", "/usr/share/aclocal/ltsugar.m4",
                         "/usr/local/share/aclocal/ltsugar.m4"],
                        ["ln", "-s", "/usr/share/aclocal/ltversion.m4",
                         "/usr/local/share/aclocal/ltversion.m4"],
                        ["ln", "-s", "/usr/share/aclocal/lt~obsolete.m4",
                         "/usr/local/share/aclocal/lt~obsolete.m4"],
                    ],
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["bookworm", "trixie", "sid"],
                "abi": ["any"],
                "changelog": "https://savannah.gnu.org/news/?group=libtool",
                "checker": {
                    "type": "apt-cache",
                    "package": "libtool",
                },
                "installer": {
                    "type": "apt",
                    "package": "libtool",
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
                    "wget",
                    "{triplet}-pkg-config",
                    "{triplet}-gcc",
                    "make",
                    "libogg",
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
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "license": ["bsd-3"],
                "changelog": "https://xiph.org/press/",
                "checker": {
                    "type": "apt-cache",
                    "package": "libvorbis-dev",
                },
                "installer": {
                    "type": "apt",
                    "package": "libvorbis-dev",
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
                    "wget",
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
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "license": ["mit", "x11", "hpnd", "hpnd-sv", "smlnj"],
                "changelog": "https://gitlab.freedesktop.org/xorg/lib/libxext/-/tags",
                "checker": {
                    "type": "apt-cache",
                    "package": "libxext-dev",
                },
                "installer": {
                    "type": "apt",
                    "package": "libxext-dev",
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
