data = {
    "patch": {
        "platform": "host",
        "projects": [
            {
                "arch": ["any"],
                "os": ["oraclelinux"],
                "osVersion": ["7"],
                "abi": ["any"],
                "changelog": "https://savannah.gnu.org/news/?group=patch",
                "checker": {
                    "type": "yum",
                    "package": "patch",
                },
                "installer": {
                    "type": "yum",
                    "package": "patch",
                },
            },
        ],
    },
    "perl-data-dumper": {
        "platform": "host",
        "projects": [
            {
                "arch": ["any"],
                "os": ["oraclelinux"],
                "osVersion": ["7"],
                "abi": ["any"],
                "changelog": "https://perldoc.perl.org/perldelta",
                "checker": {
                    "type": "yum",
                    "package": "perl-Data-Dumper",
                },
                "installer": {
                    "type": "yum",
                    "package": "perl-Data-Dumper",
                },
            },
        ],
    },
    "perl-thread-queue": {
        "platform": "host",
        "projects": [
            {
                "arch": ["any"],
                "os": ["oraclelinux"],
                "osVersion": ["7"],
                "abi": ["any"],
                "changelog": "https://metacpan.org/dist/Thread-Queue",
                "checker": {
                    "type": "yum",
                    "package": "perl-Thread-Queue",
                },
                "installer": {
                    "type": "yum",
                    "package": "perl-Thread-Queue",
                },
            },
        ],
    },
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
                "os": ["oraclelinux"],
                "osVersion": ["7"],
                "abi": ["any"],
                "changelog": "https://gitlab.freedesktop.org/pkg-config/pkg-config/-/blob/master/NEWS?ref_type=heads",
                "checker": {
                    "type": "yum",
                    "package": "pkgconfig",
                },
                "installer": {
                    "type": "cmd",
                    "cmds": [
                        ["mkdir", "-p", "/usr/local/share/aclocal"],
                        [
                            "ln", "-s", "/usr/share/aclocal/pkg.m4",
                            "/usr/local/share/aclocal/pkg.m4"
                        ],
                    ],
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
        ],
    },
}
