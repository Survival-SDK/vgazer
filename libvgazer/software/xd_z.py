data = {
    "xlib": {
        "platform": "target",
        "projects": [
            {
                "fallback": True,
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "license": ["mit", "x11", "hpnd-sv", "smlnj", "hpnd", "bsd-1"],
                "changelog": "https://gitlab.freedesktop.org/xorg/lib/libx11#release-187",
                "prereqs": [
                    "{triplet}-gcc",
                    "{triplet}-pkg-config",
                    "autoconf",
                    "make",
                    "xcb",
                    "xorgproto",
                    "xtrans",
                ],
                "checker": {
                    "type": "git",
                    "url": "https://gitlab.freedesktop.org/xorg/lib/libx11.git",
                    "hint": r'libX11-\d\.\d+(?:\.\d+(?:\.\d+)?)?',
                },
                "installer": {
                    "type": "custom",
                    "name": "xlib",
                },
            },
            {
                "arch": ["any"],
                "os": ["archlinux"],
                "osVersion": ["latest"],
                "abi": ["gnu"],
                "license": ["mit", "x11", "hpnd-sv", "smlnj", "hpnd", "bsd-1"],
                "changelog": "https://gitlab.freedesktop.org/xorg/lib/libx11#release-187",
                "checker": {
                    "type": "pacman",
                    "package": "libx11",
                },
                "installer": {
                    "type": "pacman",
                    "package": "libx11",
                },
            },
            {
                "arch": ["any"],
                "os": ["steamrt"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "license": ["mit", "x11", "hpnd-sv", "smlnj", "hpnd", "bsd-1"],
                "changelog": "https://gitlab.freedesktop.org/xorg/lib/libx11#release-187",
                "checker": {
                    "type": "apt-cache",
                    "package": "libx11-dev",
                },
                "installer": {
                    "type": "not-needed",
                },
            },
        ],
    },
    "xmempool": {
        "platform": "target",
        "projects": [
            {
                "fallback": True,
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "license": ["mit"],
                "changelog": "https://github.com/XadillaX/xmempool/tags",
                "prereqs": [
                    "{triplet}-gcc",
                    "make",
                ],
                "checker": {
                    "type": "git",
                    "url": "https://github.com/XadillaX/xmempool.git",
                },
                "installer": {
                    "type": "custom",
                    "name": "xmempool",
                },
            },
        ],
    },
    "xorg-macros": {
        "platform": "target",
        "projects": [
            {
                "fallback": True,
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "changelog": "https://gitlab.freedesktop.org/xorg/util/macros/-/tags",
                "prereqs": [
                    "autoconf",
                    "automake",
                    "make",
                ],
                "checker": {
                    "type": "git",
                    "url": "https://gitlab.freedesktop.org/xorg/util/macros.git",
                    "hint": r'util-macros-1\.\d\d\.\d',
                },
                "installer": {
                    "type": "custom",
                    "name": "xorg-macros",
                },
            },
            {
                "arch": ["any"],
                "os": ["archlinux"],
                "osVersion": ["latest"],
                "abi": ["any"],
                "changelog": "https://gitlab.freedesktop.org/xorg/util/macros/-/tags",
                "checker": {
                    "type": "pacman",
                    "package": "xorg-util-macros",
                },
                "installer": {
                    "type": "pacman",
                    "package": "xorg-util-macros",
                },
            },
            {
                "arch": ["any"],
                "os": ["steamrt"],
                "osVersion": ["any"],
                "abi": ["any"],
                "changelog": "https://gitlab.freedesktop.org/xorg/util/macros/-/tags",
                "checker": {
                    "type": "apt-cache",
                    "package": "xutils-dev",
                },
                "installer": {
                    "type": "not-needed",
                },
            },
        ],
    },
    "xorgproto": {
        "platform": "target",
        "projects": [
            {
                "fallback": True,
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "license": [
                    "bsd-2", "hpnd", "hpnd-sv", "icu", "mit", "sgi-b-2",
                    "smlnj", "x11"
                ],
                "changelog": "https://gitlab.freedesktop.org/xorg/proto/xorgproto/-/tags",
                "prereqs": [
                    "{triplet}-gcc",
                    "meson",
                    "ninja",
                ],
                "checker": {
                    "type": "git",
                    "url": "https://gitlab.freedesktop.org/xorg/proto/xorgproto.git",
                },
                "installer": {
                    "type": "custom",
                    "name": "xorgproto",
                },
            },
            {
                "arch": ["any"],
                "os": ["archlinux"],
                "osVersion": ["latest"],
                "abi": ["gnu"],
                "license": ["mit", "smlnj"],
                "changelog": "https://gitlab.freedesktop.org/xorg/proto/xorgproto/-/tags",
                "checker": {
                    "type": "pacman",
                    "package": "xorgproto",
                },
                "installer": {
                    "type": "pacman",
                    "package": "xorgproto",
                },
            },
            {
                "arch": ["any"],
                "os": ["steamrt"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "license": ["mit", "smlnj"],
                "changelog": "https://gitlab.freedesktop.org/xorg/proto/xorgproto/-/tags",
                "checker": {
                    "type": "apt-cache",
                    "package": "x11proto-dev",
                },
                "installer": {
                    "type": "not-needed",
                },
            },
        ],
    },
    "xtrans": {
        "platform": "target",
        "projects": [
            {
                "fallback": True,
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "license": ["mit", "hpnd", "x11", "hpnd-sv"],
                "changelog": "https://gitlab.freedesktop.org/xorg/lib/libxtrans/-/tags",
                "prereqs": [
                    "{triplet}-gcc",
                    "{triplet}-pkg-config",
                    "make",
                    "xorg-macros",
                ],
                "checker": {
                    "type": "git",
                    "url": "https://gitlab.freedesktop.org/xorg/lib/libxtrans.git",
                    "hint": r'xtrans-\d\.\d\.\d',
                },
                "installer": {
                    "type": "custom",
                    "name": "xtrans",
                },
            },
            {
                "arch": ["any"],
                "os": ["archlinux"],
                "osVersion": ["latest"],
                "abi": ["gnu"],
                "license": ["mit", "hpnd", "x11", "hpnd-sv"],
                "changelog": "https://gitlab.freedesktop.org/xorg/lib/libxtrans/-/tags",
                "checker": {
                    "type": "pacman",
                    "package": "xtrans",
                },
                "installer": {
                    "type": "pacman",
                    "package": "xtrans",
                },
            },
            {
                "arch": ["any"],
                "os": ["steamrt"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "license": ["mit", "hpnd", "x11", "hpnd-sv"],
                "changelog": "https://gitlab.freedesktop.org/xorg/lib/libxtrans/-/tags",
                "checker": {
                    "type": "apt-cache",
                    "package": "xtrans-dev",
                },
                "installer": {
                    "type": "not-needed",
                },
            },
        ],
    },
    "xz": {
        "platform": "host",
        "projects": [
            {
                "arch": ["any"],
                "os": ["archlinux"],
                "osVersion": ["latest"],
                "abi": ["gnu"],
                "license": ["pd"],
                "changelog": "https://github.com/tukaani-project/xz/blob/master/NEWS",
                "checker": {
                    "type": "pacman",
                    "package": "xz",
                },
                "installer": {
                    "type": "pacman",
                    "package": "xz",
                },
            },
            {
                "arch": ["any"],
                "os": ["oraclelinux"],
                "osVersion": ["7"],
                "abi": ["any"],
                "changelog": "https://github.com/tukaani-project/xz/blob/master/NEWS",
                "checker": {
                    "type": "yum",
                    "package": "xz",
                },
                "installer": {
                    "type": "yum",
                    "package": "xz",
                },
            },
            # Temporary stub
            {
                "arch": ["any"],
                "os": ["steamrt"],
                "osVersion": ["any"],
                "abi": ["any"],
                "changelog": "https://savannah.gnu.org/news/?group=coreutils",
                "checker": {
                    "type": "apt-cache",
                    "package": "xz-utils",
                },
                "installer": {
                    "type": "not-needed",
                },
            },
        ],
    },
    "zip": {
        "platform": "target",
        "projects": [
            {
                "fallback": True,
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "license": ["unlicense"],
                "changelog": "https://github.com/kuba--/zip/releases",
                "prereqs": [
                    "{triplet}-g++",
                    "cmake",
                    "make",
                ],
                "checker": {
                    "type": "git",
                    "url": "https://github.com/kuba--/zip.git",
                },
                "installer": {
                    "type": "custom",
                    "name": "zip",
                },
            },
        ],
    },
    "zlib": {
        "platform": "target",
        "projects": [
            {
                "fallback": True,
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "license": ["zlib"],
                "changelog": "https://www.zlib.net/ChangeLog.txt",
                "prereqs": [
                    "{triplet}-gcc",
                    "make",
                ],
                "checker": {
                    "type": "git",
                    "url": "https://github.com/madler/zlib.git",
                },
                "installer": {
                    "type": "custom",
                    "name": "zlib",
                },
            },
            {
                "arch": ["any"],
                "os": ["archlinux"],
                "osVersion": ["latest"],
                "abi": ["gnu"],
                "license": ["zlib"],
                "changelog": "https://www.zlib.net/ChangeLog.txt",
                "checker": {
                    "type": "pacman",
                    "package": "zlib",
                },
                "installer": {
                    "type": "pacman",
                    "package": "zlib",
                },
            },
            {
                "arch": ["any"],
                "os": ["steamrt"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "license": ["zlib"],
                "changelog": "https://www.zlib.net/ChangeLog.txt",
                "checker": {
                    "type": "apt-cache",
                    "package": "zlib1g-dev",
                },
                "installer": {
                    "type": "not-needed",
                },
            },
        ],
    },
}
