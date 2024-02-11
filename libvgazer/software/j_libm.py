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
                "prereqs": [
                    "wget",
                ],
                "checker": {
                    "type": "git",
                    "url": "https://github.com/attractivechaos/klib",
                    "files": ["ketopt.h"],
                },
                "installer": {
                    "type": "custom",
                    "name": "ketopt",
                    "fallback": {
                        "type": "custom",
                        "name": "ketopt-master",
                    }
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
                    "wget",
                    "{triplet}-g++",
                    "make",
                    "{triplet}-pkg-config",
                    "cmake",
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
                    "wget",
                    "{triplet}-g++",
                    "make",
                    "{triplet}-pkg-config",
                    "cmake",
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
    "libdrm": {
        "platform": "target",
        "projects": [
            {
                "fallback": True,
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "license": ["mit"],
                "changelog": "https://gitlab.freedesktop.org/mesa/drm/-/tags",
                "prereqs": [
                    "wget",
                    "{triplet}-gcc",
                    "{triplet}-pkg-config",
                    "meson",
                    "xlib",
                    "libpciaccess",
                ],
                "checker": {
                    "type": "git",
                    "url": "https://gitlab.freedesktop.org/mesa/drm.git",
                    "hint": r'libdrm-\d\.\d\.\d+$',
                },
                "installer": {
                    "type": "custom",
                    "name": "libdrm",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "license": ["mit"],
                "changelog": "https://gitlab.freedesktop.org/mesa/drm/-/tags",
                "checker": {
                    "type": "apt-cache",
                    "package": "libdrm-dev",
                },
                "installer": {
                    "type": "apt",
                    "package": "libdrm-dev",
                },
            },
            {
                "arch": ["any"],
                "os": ["steamrt"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "license": ["mit"],
                "changelog": "https://gitlab.freedesktop.org/mesa/drm/-/tags",
                "checker": {
                    "type": "apt-cache",
                    "package": "libdrm-dev",
                },
                "installer": {
                    "type": "not_needed",
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
                    "wget",
                    "{triplet}-gcc",
                    "{triplet}-g++",
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
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "license": ["mit"],
                "changelog": "https://github.com/libffi/libffi/releases",
                "checker": {
                    "type": "apt-cache",
                    "package": "libffi-dev",
                },
                "installer": {
                    "type": "apt",
                    "package": "libffi-dev",
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
                    "type": "not_needed",
                },
            },
        ],
    },
    "libiconv": {
        "platform": "target",
        # TODO
        "projects": [
            {
                "fallback": True,
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "license": ["lgpl-2"],
                "changelog": "https://savannah.gnu.org/news/?group=libiconv",
                "checker": {
                    "type": "git",
                    "url": "https://git.savannah.gnu.org/git/libiconv.git",
                },
                "installer": {
                    "type": "custom",
                    "name": "libiconv",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "license": ["lgpl-2"],
                "changelog": "https://savannah.gnu.org/news/?group=libiconv",
                "checker": {
                    "type": "apt-cache",
                    "package": "libc6-dev",
                },
                "installer": {
                    "type": "not_needed",
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
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "license": ["lgpl-2.1"],
                "changelog": "https://fossies.org/linux/gettext/ChangeLog",
                "checker": {
                    "type": "apt-cache",
                    "package": "libc6-dev",
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
                "os": ["linux"],
                "osVersion": ["any"],
                "abi": ["any"],
                "license": ["pd"],
                "changelog": "https://github.com/tukaani-project/xz/blob/master/NEWS",
                "prereqs": [
                    "wget",
                    "{triplet}-gcc",
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
                    "wget",
                    "{triplet}-gcc",
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
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "license": ["pd"],
                "changelog": "https://github.com/tukaani-project/xz/blob/master/NEWS",
                "checker": {
                    "type": "apt-cache",
                    "package": "liblzma-dev",
                },
                "installer": {
                    "type": "apt",
                    "package": "liblzma-dev",
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
                    "type": "not_needed",
                },
            },
        ],
    },
}
