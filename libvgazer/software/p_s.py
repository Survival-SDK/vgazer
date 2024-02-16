data = {
    "pkg-config": {
        "platform": "host",
        "projects": [
            {
                "arch": ["any"],
                "os": ["archlinux"],
                "osVersion": ["latest"],
                "abi": ["any"],
                "changelog": "https://gitlab.freedesktop.org/pkg-config/pkg-config/-/blob/master/NEWS?ref_type=heads",
                "checker": {
                    "type": "pacman",
                    "package": "pkgconf",
                },
                "installer": {
                    "type": "pacman",
                    "package": "pkgconf",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["buster", "bullseye"],
                "abi": ["any"],
                "changelog": "https://gitlab.freedesktop.org/pkg-config/pkg-config/-/blob/master/NEWS?ref_type=heads",
                "checker": {
                    "type": "apt-cache",
                    "package": "pkg-config",
                },
                "installer": {
                    "type": "apt",
                    "package": "pkg-config",
                    "postInstallCommands": [
                        ["mkdir", "-p", "/usr/local/share/aclocal"],
                        ["ln", "-s", "/usr/share/aclocal/pkg.m4",
                         "/usr/local/share/aclocal/pkg.m4"],
                    ],
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["bookworm", "trixie", "sid"],
                "abi": ["any"],
                "changelog": "https://gitlab.freedesktop.org/pkg-config/pkg-config/-/blob/master/NEWS?ref_type=heads",
                "checker": {
                    "type": "apt-cache",
                    "package": "pkg-config",
                },
                "installer": {
                    "type": "apt",
                    "package": "pkg-config",
                },
            },
            {
                "arch": ["any"],
                "os": ["steamrt"],
                "osVersion": ["any"],
                "abi": ["any"],
                "changelog": "https://gitlab.freedesktop.org/pkg-config/pkg-config/-/blob/master/NEWS?ref_type=heads",
                "checker": {
                    "type": "apt-cache",
                    "package": "pkg-config",
                },
                "installer": {
                    "type": "not-needed",
                },
            },
        ],
    },
    "pthread-stubs": {
        "platform": "target",
        "projects": [
            {
                "fallback": True,
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "license": ["x11"],
                "changelog": "https://gitlab.freedesktop.org/xorg/lib/pthread-stubs/-/tags",
                "prereqs": [
                    "{triplet}-gcc",
                    "autoconf",
                    "automake",
                    "make",
                ],
                "checker": {
                    "type": "git",
                    "url": "https://gitlab.freedesktop.org/xorg/lib/pthread-stubs.git",
                },
                "installer": {
                    "type": "custom",
                    "name": "pthread-stubs",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "license": ["x11"],
                "changelog": "https://gitlab.freedesktop.org/xorg/lib/pthread-stubs/-/tags",
                "checker": {
                    "type": "apt-cache",
                    "package": "libpthread-stubs0-dev",
                },
                "installer": {
                    "type": "apt",
                    "package": "libpthread-stubs0-dev",
                },
            },
            {
                "arch": ["any"],
                "os": ["steamrt"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "license": ["x11"],
                "changelog": "https://gitlab.freedesktop.org/xorg/lib/pthread-stubs/-/tags",
                "checker": {
                    "type": "apt-cache",
                    "package": "libpthread-stubs0-dev",
                },
                "installer": {
                    "type": "not-needed",
                },
            },
        ],
    },
    "safeclib": {
        "platform": "target",
        "projects": [
            {
                "fallback": True,
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "license": ["mit"],
                "changelog": "https://github.com/rurban/safeclib/blob/master/ChangeLog",
                "prereqs": [
                    "{triplet}-gcc",
                    "autoconf",
                    "automake",
                    "libtool",
                    "make",
                ],
                "checker": {
                    "type": "git",
                    "url": "https://github.com/rurban/safeclib.git",
                    "hint": r'v\d\.\d(\.\d)?$',
                },
                "installer": {
                    "type": "custom",
                    "name": "safeclib",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["buster", "bullseye", "bookworm", "sid"],
                "abi": ["gnu"],
                "license": ["mit"],
                "changelog": "https://gitlab.freedesktop.org/xorg/lib/pthread-stubs/-/tags",
                "checker": {
                    "type": "apt-cache",
                    "package": "libsafec-dev",
                },
                "installer": {
                    "type": "apt",
                    "package": "libsafec-dev",
                },
            },
            # Temporary stub
            {
                "arch": ["any"],
                "os": ["steamrt"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "license": ["mit"],
                "changelog": "https://gitlab.freedesktop.org/xorg/lib/pthread-stubs/-/tags",
                "checker": {
                    "type": "apt-cache",
                    "package": "libsafec-dev",
                },
                "installer": {
                    "type": "not-needed",
                },
            },
        ],
    },
    "scv": {
        "platform": "target",
        "projects": [
            {
                "fallback": True,
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "license": ["mit"],
                "changelog": "https://github.com/jibsen/scv/commits/master/",
                "prereqs": [
                    "{triplet}-gcc",
                ],
                "checker": {
                    "type": "git",
                    "url": "https://github.com/jibsen/scv.git",
                },
                "installer": {
                    "type": "custom",
                    "name": "scv",
                },
            },
        ],
    },
    "stb_rect_pack": {
        "platform": "target",
        "projects": [
            {
                "fallback": True,
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "license": ["unlicense"],
                "changelog": "https://github.com/nothings/stb/blob/master/stb_rect_pack.h#L42",
                "checker": {
                    "type": "git",
                    "url": "https://github.com/nothings/stb.git",
                    "files": ["stb_rect_pack.h"],
                    "hint": r'\d\.\d{2}',
                },
                "installer": {
                    "type": "custom",
                    "name": "stb_rect_pack",
                },
            },
            {
                "arch": ["any"],
                "os": ["archlinux"],
                "osVersion": ["latest"],
                "abi": ["any"],
                "license": ["unlicense"],
                "changelog": "https://github.com/nothings/stb/blob/master/stb_rect_pack.h#L42",
                "checker": {
                    "type": "pacman",
                    "package": "stb",
                },
                "installer": {
                    "type": "pacman",
                    "package": "stb",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["any"],
                "license": ["unlicense"],
                "changelog": "https://github.com/nothings/stb/blob/master/stb_rect_pack.h#L42",
                "checker": {
                    "type": "apt-cache",
                    "package": "libstb-dev",
                },
                "installer": {
                    "type": "apt",
                    "package": "libstb-dev",
                },
            },
            # Temporary stub
            {
                "arch": ["any"],
                "os": ["steamrt"],
                "osVersion": ["any"],
                "abi": ["any"],
                "license": ["unlicense"],
                "changelog": "https://github.com/nothings/stb/blob/master/stb_rect_pack.h#L42",
                "checker": {
                    "type": "apt-cache",
                    "package": "libstb-dev",
                },
                "installer": {
                    "type": "not-needed",
                },
            },
        ],
    },
}
