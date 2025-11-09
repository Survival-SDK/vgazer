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
                "os": ["fedora"],
                "osVersion": ["43"],
                "abi": ["gnu"],
                "license": ["mit", "x11", "hpnd-sv", "smlnj", "hpnd", "bsd-1"],
                "changelog": "https://gitlab.freedesktop.org/xorg/lib/libx11#release-187",
                "checker": {
                    "type": "dnf",
                    "package": "libX11-devel",
                },
                "installer": {
                    "type": "dnf",
                    "package": "libX11-devel",
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
        ],
    },
    "xz": {
        "platform": "host",
        "projects": [
            {
                "arch": ["any"],
                "os": ["amazonlinux"],
                "osVersion": ["2"],
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
                "os": ["fedora"],
                "osVersion": ["43"],
                "abi": ["gnu"],
                "license": ["zlib"],
                "changelog": "https://github.com/zlib-ng/zlib-ng/releases",
                "checker": {
                    "type": "dnf",
                    "package": "zlib-ng-compat-devel",
                },
                "installer": {
                    "type": "pacman",
                    "package": "zlib-ng-compat-devel",
                },
            },
        ],
    },
}
