data = {
    "ketopt": {
        "platform": "target",
        "projects": [
            {
                "fallback": True,
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "license": ["mit"],
                "changelog": "https://github.com/attractivechaos/klib/commits/master/ketopt.h",
                "checker": {
                    "type": "git",
                    "url": "https://github.com/attractivechaos/klib",
                    "files": ["ketopt.h"],
                },
                "installer": {
                    "type": "custom",
                    "name": "ketopt"
                },
            },
        ],
    },
    "libclipboard": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["linux"],
                "osVersion": ["any"],
                "abi": ["any"],
                "license": ["mit"],
                "changelog": "https://github.com/jtanx/libclipboard/releases",
                "prereqs": [
                    "{triplet}-g++",
                    "{triplet}-pkg-config",
                    "cmake",
                    "make",
                    "xcb",
                ],
                "checker": {
                    "type": "git",
                    "url": "https://github.com/jtanx/libclipboard.git",
                },
                "installer": {
                    "type": "custom",
                    "name": "libclipboard",
                },
            },
            {
                "arch": ["any"],
                "os": ["windows"],
                "osVersion": ["any"],
                "abi": ["any"],
                "license": ["mit"],
                "changelog": "https://github.com/jtanx/libclipboard/releases",
                "prereqs": [
                    "{triplet}-g++",
                    "{triplet}-pkg-config",
                    "cmake",
                    "make",
                ],
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
                "fallback": True,
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "license": ["mit"],
                "changelog": "https://github.com/libffi/libffi/releases",
                "prereqs": [
                    "{triplet}-gcc",
                    "{triplet}-g++",
                    "autoconf",
                    "automake",
                    "libtool",
                    "make",
                ],
                "checker": {
                    "type": "git",
                    "url": "https://github.com/libffi/libffi.git",
                },
                "installer": {
                    "type": "custom",
                    "name": "libffi",
                },
            },
            {
                "arch": ["any"],
                "os": ["archlinux"],
                "osVersion": ["latest"],
                "abi": ["gnu"],
                "license": ["mit"],
                "changelog": "https://github.com/libffi/libffi/releases",
                "checker": {
                    "type": "pacman",
                    "package": "libffi",
                },
                "installer": {
                    "type": "pacman",
                    "package": "libffi",
                },
            },
            {
                "arch": ["any"],
                "os": ["steamrt"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "license": ["mit"],
                "changelog": "https://github.com/libffi/libffi/releases",
                "checker": {
                    "type": "apt-cache",
                    "package": "libffi-dev",
                },
                "installer": {
                    "type": "not-needed",
                },
            },
        ],
    },
    # libintl under GNU LGPL 2.1
    # libintl-lite under version 1 of the Boost Software License
    "libintl": {
        "platform": "target",
        # TODO
        "projects": [
            {
                "arch": ["any"],
                "os": ["windows"],
                "osVersion": ["any"],
                "abi": ["any"],
                "license": ["bsl-1.0"],
                "changelog": "https://github.com/j-jorge/libintl-lite/commits/master/",
                "checker": {
                    "type": "git",
                    "url": "https://github.com/j-jorge/libintl-lite.git",
                    "files": ["CMakeLists.txt"],
                    "hint": r'LibIntl VERSION \d\.\d',
                },
                "installer": {
                    "type": "custom",
                    "name": "libintl-lite",
                },
            },
            {
                "arch": ["any"],
                "os": ["steamrt"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "license": ["lgpl-2.1"],
                "changelog": "https://fossies.org/linux/gettext/ChangeLog",
                "checker": {
                    "type": "apt-cache",
                    "package": "libc6-dev",
                },
                "installer": {
                    "type": "not-needed",
                },
            },
        ],
    },
    "liblzma": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["linux"],
                "osVersion": ["any"],
                "abi": ["any"],
                "license": ["pd"],
                "changelog": "https://github.com/tukaani-project/xz/blob/master/NEWS",
                "prereqs": [
                    "{triplet}-gcc",
                    "autoconf",
                    "automake",
                    "autopoint",
                    "libtool",
                    "make",
                ],
                "checker": {
                    "type": "git",
                    "url": "https://github.com/tukaani-project/xz.git",
                    "hint": r'v\d\.\d.\d+$',
                },
                "installer": {
                    "type": "custom",
                    "name": "liblzma",
                },
            },
            {
                "arch": ["any"],
                "os": ["windows"],
                "osVersion": ["any"],
                "abi": ["any"],
                "license": ["pd"],
                "changelog": "https://github.com/tukaani-project/xz/blob/master/NEWS",
                "prereqs": [
                    "{triplet}-gcc",
                    "autoconf",
                    "automake",
                    "autopoint",
                    "libtool",
                    "make",
                    # "libintl",
                ],
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
                "os": ["archlinux"],
                "osVersion": ["latest"],
                "abi": ["gnu"],
                "license": ["pd"],
                "changelog": "https://github.com/tukaani-project/xz/blob/master/NEWS",
                "prereqs": [
                    "xz",
                ],
                "checker": {
                    "type": "pacman",
                    "package": "xz",
                },
                "installer": {
                    "type": "not-needed",
                },
            },
            {
                "arch": ["any"],
                "os": ["steamrt"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "license": ["pd"],
                "changelog": "https://github.com/tukaani-project/xz/blob/master/NEWS",
                "checker": {
                    "type": "apt-cache",
                    "package": "liblzma-dev",
                },
                "installer": {
                    "type": "not-needed",
                },
            },
        ],
    },
}
