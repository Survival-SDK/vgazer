data = {
    "tinyfiledialogs": {
        "type": "library",
        "platform": "target",
        "projects": [
            {
                "fallback": True,
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "license": ["zlib"],
                "changelog": "https://sourceforge.net/p/tinyfiledialogs/activity/?page=0&limit=100#65c79b2c7e19948b1b33b56a",
                "prereqs": [
                    "{triplet}-gcc",
                ],
                "checker": {
                    "type": "git",
                    "url": "https://git.code.sf.net/p/tinyfiledialogs/code",
                    "files": ["README.txt"],
                    "hint": r'tiny file dialogs \( cross-platform C C\+\+ \) v\d\.\d+(?:\.\d)?',
                },
                "installer": {
                    "type": "custom",
                    "name": "tinyfiledialogs",
                },
            },
        ],
    },
    "valgrind": {
        "platform": "host",
        "projects": [
            {
                "arch": ["any"],
                "os": ["archlinux"],
                "osVersion": ["latest"],
                "abi": ["any"],
                "changelog": "https://valgrind.org/docs/manual/dist.news.html",
                "checker": {
                    "type": "pacman",
                    "package": "valgrind",
                },
                "installer": {
                    "type": "pacman",
                    "package": ["valgrind", "debuginfod"],
                },
            },
            {
                "arch": ["any"],
                "os": ["fedora"],
                "osVersion": ["40"],
                "abi": ["any"],
                "changelog": "https://valgrind.org/docs/manual/dist.news.html",
                "checker": {
                    "type": "dnf",
                    "package": "valgrind",
                },
                "installer": {
                    "type": "dnf",
                    "package": "valgrind",
                },
            },
        ],
    },
    "wget": {
        "platform": "host",
        "projects": [
            {
                "arch": ["any"],
                "os": ["archlinux"],
                "osVersion": ["latest"],
                "abi": ["any"],
                "changelog": "https://savannah.gnu.org/news/?group=wget",
                "checker": {
                    "type": "pacman",
                    "package": "wget",
                },
                "installer": {
                    "type": "pacman",
                    "package": "wget",
                },
            },
            {
                "arch": ["any"],
                "os": ["oraclelinux"],
                "osVersion": ["7"],
                "abi": ["any"],
                "changelog": "https://savannah.gnu.org/news/?group=wget",
                "checker": {
                    "type": "yum",
                    "package": "wget",
                },
                "installer": {
                    "type": "yum",
                    "package": "wget",
                },
            },
        ],
    },
    "x86_64-linux-gnu-binutils": {
        "platform": "host",
        "projects": [
            {
                "arch": ["x86_64"],
                "os": ["oraclelinux"],
                "osVersion": ["7"],
                "abi": ["any"],
                "changelog": "https://fossies.org/linux/binutils/binutils/NEWS",
                "checker": {
                    "type": "yum",
                    "package": "binutils",
                },
                "installer": {
                    "type": "cmd",
                    "cmds": [
                        ["mkdir", "-p", "/usr/local/bin"],
                        [
                            "ln", "-s", "/usr/bin/ar",
                            "/usr/local/bin/x86_64-linux-gnu-ar"
                        ],
                        [
                            "ln", "-s", "/usr/bin/strip",
                            "/usr/local/bin/x86_64-linux-gnu-strip"
                        ],
                    ]
                },
            },
        ],
    },
    "x86_64-linux-gnu-g++": {
        "platform": "host",
        "projects": [
            {
                "arch": ["x86_64"],
                "os": ["archlinux"],
                "osVersion": ["any"],
                "abi": ["any"],
                "changelog": "https://gcc.gnu.org/",
                "prereqs": ["g++"],
                "checker": {
                    "type": "pacman",
                    "package": "gcc",
                },
                "installer": {
                    "type": "not-needed",
                },
            },
            {
                "arch": ["x86_64"],
                "os": ["fedora"],
                "osVersion": ["40"],
                "abi": ["any"],
                "changelog": "https://gcc.gnu.org/",
                "prereqs": ["g++"],
                "checker": {
                    "type": "dnf",
                    "package": "gcc-c++",
                },
                "installer": {
                    "type": "cmd",
                    "cmds": [
                        ["mkdir", "-p", "/usr/local/bin"],
                        [
                            "ln", "-s", "/usr/bin/g++",
                            "/usr/local/bin/x86_64-linux-gnu-g++"
                        ],
                    ]
                },
            },
            {
                "arch": ["x86_64"],
                "os": ["oraclelinux"],
                "osVersion": ["7"],
                "abi": ["any"],
                "changelog": "https://gcc.gnu.org/",
                "prereqs": ["g++"],
                "checker": {
                    "type": "yum",
                    "package": "g++",
                },
                "installer": {
                    "type": "cmd",
                    "cmds": [
                        ["mkdir", "-p", "/usr/local/bin"],
                        [
                            "ln", "-s", "/usr/bin/g++",
                            "/usr/local/bin/x86_64-linux-gnu-g++"
                        ],
                    ]
                },
            },
        ],
    },
    "x86_64-linux-gnu-gcc": {
        "platform": "host",
        "projects": [
            {
                "arch": ["x86_64"],
                "os": ["archlinux"],
                "osVersion": ["any"],
                "abi": ["any"],
                "changelog": "https://gcc.gnu.org/",
                "prereqs": ["gcc"],
                "checker": {
                    "type": "pacman",
                    "package": "gcc",
                },
                "installer": {
                    "type": "not-needed",
                },
            },
            {
                "arch": ["x86_64"],
                "os": ["fedora"],
                "osVersion": ["40"],
                "abi": ["any"],
                "changelog": "https://gcc.gnu.org/",
                "prereqs": ["gcc"],
                "checker": {
                    "type": "dnf",
                    "package": "gcc",
                },
                "installer": {
                    "type": "cmd",
                    "cmds": [
                        ["mkdir", "-p", "/usr/local/bin"],
                        [
                            "ln", "-s", "/usr/bin/gcc",
                            "/usr/local/bin/x86_64-linux-gnu-gcc"
                        ],
                        [
                            "ln", "-s", "/usr/bin/gcc-ar",
                            "/usr/local/bin/x86_64-linux-gnu-gcc-ar"
                        ],
                        [
                            "ln", "-s", "/usr/bin/gcc-nm",
                            "/usr/local/bin/x86_64-linux-gnu-gcc-nm"
                        ],
                        [
                            "ln", "-s", "/usr/bin/gcc-ranlib",
                            "/usr/local/bin/x86_64-linux-gnu-gcc-ranlib"
                        ],
                        [
                            "ln", "-s", "/usr/bin/gcov",
                            "/usr/local/bin/x86_64-linux-gnu-gcov"
                        ],
                    ]
                },
            },
            {
                "arch": ["x86_64"],
                "os": ["oraclelinux"],
                "osVersion": ["7"],
                "abi": ["any"],
                "changelog": "https://gcc.gnu.org/",
                "prereqs": ["gcc"],
                "checker": {
                    "type": "yum",
                    "package": "gcc",
                },
                "installer": {
                    "type": "cmd",
                    "cmds": [
                        ["mkdir", "-p", "/usr/local/bin"],
                        [
                            "ln", "-s", "/usr/bin/gcc",
                            "/usr/local/bin/x86_64-linux-gnu-gcc"
                        ],
                        [
                            "ln", "-s", "/usr/bin/gcc-ar",
                            "/usr/local/bin/x86_64-linux-gnu-gcc-ar"
                        ],
                        [
                            "ln", "-s", "/usr/bin/gcc-nm",
                            "/usr/local/bin/x86_64-linux-gnu-gcc-nm"
                        ],
                        [
                            "ln", "-s", "/usr/bin/gcc-ranlib",
                            "/usr/local/bin/x86_64-linux-gnu-gcc-ranlib"
                        ],
                        [
                            "ln", "-s", "/usr/bin/gcov",
                            "/usr/local/bin/x86_64-linux-gnu-gcov"
                        ],
                    ]
                },
            },
        ],
    },
    "x86_64-linux-gnu-pkg-config": {
        "platform": "host",
        "projects": [
            {
                "arch": ["any"],
                "os": ["archlinux"],
                "osVersion": ["latest"],
                "abi": ["gnu"],
                "changelog": "https://gitlab.freedesktop.org/pkg-config/pkg-config/-/blob/master/NEWS?ref_type=heads",
                "prereqs": [
                    "pkg-config",
                ],
                "checker": {
                    "type": "pacman",
                    "package": "pkg-config",
                },
                "installer": {
                    "type": "cmd",
                    "cmds": [
                        ["mkdir", "-p", "/usr/local/bin/"],
                        ["sh", "-c", "echo "
                            "'#!/bin/sh\n"
                            "export PKG_CONFIG_DIR=\n"
                            "export PKG_CONFIG_PATH="
                                "/usr/local/x86_64-linux-gnu/lib/pkgconfig:"
                                "/usr/local/x86_64-linux-gnu/share/pkgconfig"
                                "\n"
                            "export PKG_CONFIG_LIBDIR="
                                "/usr/local/x86_64-linux-gnu/lib/pkgconfig:"
                                "/usr/local/x86_64-linux-gnu/share/pkgconfig"
                                "\n"
                            "export PKG_CONFIG_SYSROOT_DIR=/\n"
                            "exec pkg-config \"$@\"' "
                            "> /usr/local/bin/x86_64-linux-gnu-pkg-config",
                        ],
                        [
                            "chmod", "+x",
                            "/usr/local/bin/x86_64-linux-gnu-pkg-config",
                        ],
                    ],
                },
            },
            {
                "arch": ["any"],
                "os": ["fedora"],
                "osVersion": ["40"],
                "abi": ["gnu"],
                "changelog": "https://gitlab.freedesktop.org/pkg-config/pkg-config/-/blob/master/NEWS?ref_type=heads",
                "prereqs": [
                    "pkg-config",
                ],
                "checker": {
                    "type": "dnf",
                    "package": "pkgconf-pkg-config",
                },
                "installer": {
                    "type": "cmd",
                    "cmds": [
                        ["mkdir", "-p", "/usr/local/bin/"],
                        ["sh", "-c", "echo "
                            "'#!/bin/sh\n"
                            "export PKG_CONFIG_DIR=\n"
                            "export PKG_CONFIG_PATH="
                                "/usr/local/x86_64-linux-gnu/lib/pkgconfig:"
                                "/usr/local/x86_64-linux-gnu/share/pkgconfig"
                                "\n"
                            "export PKG_CONFIG_LIBDIR="
                                "/usr/local/x86_64-linux-gnu/lib/pkgconfig:"
                                "/usr/local/x86_64-linux-gnu/share/pkgconfig"
                                "\n"
                            "export PKG_CONFIG_SYSROOT_DIR=/\n"
                            "exec pkg-config \"$@\"' "
                            "> /usr/local/bin/x86_64-linux-gnu-pkg-config",
                        ],
                        [
                            "chmod", "+x",
                            "/usr/local/bin/x86_64-linux-gnu-pkg-config",
                        ],
                    ],
                },
            },
            {
                "arch": ["any"],
                "os": ["oraclelinux"],
                "osVersion": ["7"],
                "abi": ["gnu"],
                "changelog": "https://gitlab.freedesktop.org/pkg-config/pkg-config/-/blob/master/NEWS?ref_type=heads",
                "prereqs": [
                    "pkg-config",
                ],
                "checker": {
                    "type": "yum",
                    "package": "pkgconfig",
                },
                "installer": {
                    "type": "cmd",
                    "cmds": [
                        ["mkdir", "-p", "/usr/local/bin/"],
                        ["sh", "-c", "echo "
                            "'#!/bin/sh\n"
                            "export PKG_CONFIG_DIR=\n"
                            "export PKG_CONFIG_PATH="
                                "/usr/local/x86_64-linux-gnu/lib/pkgconfig:"
                                "/usr/local/x86_64-linux-gnu/share/pkgconfig"
                                "\n"
                            "export PKG_CONFIG_LIBDIR="
                                "/usr/local/x86_64-linux-gnu/lib/pkgconfig:"
                                "/usr/local/x86_64-linux-gnu/share/pkgconfig"
                                "\n"
                            "export PKG_CONFIG_SYSROOT_DIR=/\n"
                            "exec pkg-config \"$@\"' "
                            "> /usr/local/bin/x86_64-linux-gnu-pkg-config",
                        ],
                        [
                            "chmod", "+x",
                            "/usr/local/bin/x86_64-linux-gnu-pkg-config",
                        ],
                    ],
                },
            },
        ],
    },
    "x86_64-w64-mingw32-g++": {
        "platform": "host",
        "projects": [
            {
                "arch": ["any"],
                "os": ["archlinux"],
                "osVersion": ["latest"],
                "abi": ["any"],
                "changelog": "https://www.mingw-w64.org/changelog/",
                "prereqs": ["x86_64-w64-mingw32-gcc"],
                "checker": {
                    "type": "pacman",
                    "package": "mingw-w64-gcc",
                },
                "installer": {
                    "type": "not-needed",
                },
            },
        ],
    },
    "x86_64-w64-mingw32-gcc": {
        "platform": "host",
        "projects": [
            {
                "arch": ["any"],
                "os": ["archlinux"],
                "osVersion": ["latest"],
                "abi": ["any"],
                "changelog": "https://www.mingw-w64.org/changelog/",
                "checker": {
                    "type": "pacman",
                    "package": "mingw-w64-gcc",
                },
                "installer": {
                    "type": "pacman",
                    "package": "mingw-w64-gcc",
                },
            },
        ],
    },
    "x86_64-w64-mingw32-pkg-config": {
        "platform": "host",
        "projects": [
            {
                "arch": ["any"],
                "os": ["archlinux"],
                "osVersion": ["latest"],
                "abi": ["gnu"],
                "changelog": "https://gitlab.freedesktop.org/pkg-config/pkg-config/-/blob/master/NEWS?ref_type=heads",
                "prereqs": [
                    "pkg-config",
                ],
                "checker": {
                    "type": "pacman",
                    "package": "pkgconf",
                },
                "installer": {
                    "cmds": [
                        ["mkdir", "-p", "/usr/local/bin/"],
                        ["sh", "-c", "echo "
                            "'#!/bin/sh\n"
                            "export PKG_CONFIG_DIR=\n"
                            "export PKG_CONFIG_PATH="
                                "/usr/local/x86_64-w64-mingw32/lib/pkgconfig:"
                                "/usr/local/x86_64-w64-mingw32/share/pkgconfig"
                                "\n"
                            "export PKG_CONFIG_LIBDIR="
                                "/usr/local/x86_64-w64-mingw32/lib/pkgconfig:"
                                "/usr/local/x86_64-w64-mingw32/share/pkgconfig"
                                "\n"
                            "export PKG_CONFIG_SYSROOT_DIR=/\n"
                            "exec pkg-config \"$@\"' "
                            ">> /usr/local/bin/x86_64-w64-mingw32-pkg-config",
                        ],
                        [
                            "chmod", "+x",
                            "/usr/local/bin/x86_64-w64-mingw32-pkg-config",
                        ],
                    ],
                },
            },
        ],
    },
    "xau": {
        "platform": "target",
        "projects": [
            {
                "fallback": True,
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "license": ["mit"],
                "changelog": "https://gitlab.freedesktop.org/xorg/lib/libxau/-/tags",
                "prereqs": [
                    "{triplet}-gcc",
                    "{triplet}-pkg-config",
                    "autoconf",
                    "libtool",
                    "make",
                    "xorg-macros",
                    "xorgproto",
                ],
                "checker": {
                    "type": "git",
                    "url": "https://gitlab.freedesktop.org/xorg/lib/libxau.git",
                    "hint": r'libXau-1\.0\.\d\d',
                },
                "installer": {
                    "type": "custom",
                    "name": "xau",
                    "fallback": {
                        "type": "custom",
                        "name": "xau-github",
                    },
                },
            },
            {
                "arch": ["any"],
                "os": ["archlinux"],
                "osVersion": ["latest"],
                "abi": ["gnu"],
                "license": ["mit"],
                "changelog": "https://gitlab.freedesktop.org/xorg/lib/libxau/-/tags",
                "checker": {
                    "type": "pacman",
                    "package": "libxau",
                },
                "installer": {
                    "type": "pacman",
                    "package": "libxau",
                },
            },
        ],
    },
    "xcb": {
        "platform": "target",
        "projects": [
            {
                "fallback": True,
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "license": ["x11"],
                "changelog": "https://xcb.freedesktop.org/",
                "prereqs": [
                    "{triplet}-gcc",
                    "{triplet}-pkg-config",
                    "autoconf",
                    "make",
                    "pthread-stubs",
                    "wget",
                    "xcb-proto",
                    "xau",
                ],
                "checker": {
                    "type": "git",
                    "url": "https://gitlab.freedesktop.org/xorg/lib/libxcb.git",
                    "hint": r'libxcb-1\.\d\d',
                },
                "installer": {
                    "type": "custom",
                    "name": "xcb",
                },
            },
            {
                "arch": ["any"],
                "os": ["archlinux"],
                "osVersion": ["latest"],
                "abi": ["gnu"],
                "license": ["x11"],
                "changelog": "https://xcb.freedesktop.org/",
                "checker": {
                    "type": "pacman",
                    "package": "libxcb",
                },
                "installer": {
                    "type": "pacman",
                    "package": "libxcb",
                },
            },
        ],
    },
    "xcb-proto": {
        "platform": "target",
        "projects": [
            {
                "fallback": True,
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "license": ["x11"],
                "changelog": "https://xcb.freedesktop.org/",
                "prereqs": [
                    "autoconf",
                    "automake",
                    "make",
                ],
                "checker": {
                    "type": "git",
                    "url": "https://gitlab.freedesktop.org/xorg/proto/xcbproto.git",
                    "hint": r'xcb-proto-1\.\d\d\.\d',
                },
                "installer": {
                    "type": "custom",
                    "name": "xcb-proto",
                },
            },
            {
                "arch": ["any"],
                "os": ["archlinux"],
                "osVersion": ["latest"],
                "abi": ["gnu"],
                "license": ["x11"],
                "changelog": "https://xcb.freedesktop.org/",
                "checker": {
                    "type": "pacman",
                    "package": "xcb-proto",
                },
                "installer": {
                    "type": "pacman",
                    "package": "xcb-proto",
                },
            },
        ],
    },
}
