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
    "unzip": {
        "platform": "host",
        "projects": [
            {
                "arch": ["any"],
                "os": ["archlinux"],
                "osVersion": ["latest"],
                "abi": ["any"],
                "changelog": "https://infozip.sourceforge.net/UnZip.html#Release",
                "checker": {
                    "type": "pacman",
                    "package": "unzip",
                },
                "installer": {
                    "type": "pacman",
                    "package": "unzip",
                },
            },
            {
                "arch": ["any"],
                "os": ["steamrt"],
                "osVersion": ["any"],
                "abi": ["any"],
                "changelog": "https://infozip.sourceforge.net/UnZip.html#Release",
                "checker": {
                    "type": "apt-cache",
                    "package": "unzip",
                },
                "installer": {
                    "type": "apt",
                    "package": "unzip",
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
                    "package": "valgrind",
                },
            },
        ],
    },
    "wayland-libs": {
        "platform": "target",
        "projects": [
            {
                "fallback": True,
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "license": ["mit"],
                "changelog": "https://wayland.freedesktop.org/releases.html",
                "prereqs": [
                    "{triplet}-g++",
                    "{triplet}-gcc",
                    "{triplet}-pkg-config",
                    "libffi",
                    "meson",
                    "ninja",
                    "wayland-scanner",
                ],
                "checker": {
                    "type": "git",
                    "url": "https://gitlab.freedesktop.org/wayland/wayland.git",
                    "hint": r'1\.\d\d.\d+',
                },
                "installer": {
                    "type": "custom",
                    "name": "wayland",
                },
            },
            {
                "arch": ["any"],
                "os": ["archlinux"],
                "osVersion": ["latest"],
                "abi": ["any"],
                "license": ["mit"],
                "changelog": "https://wayland.freedesktop.org/releases.html",
                "checker": {
                    "type": "pacman",
                    "package": "wayland",
                },
                "installer": {
                    "type": "pacman",
                    "package": "wayland",
                },
            },
            {
                "arch": ["any"],
                "os": ["steamrt"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "license": ["mit"],
                "changelog": "https://wayland.freedesktop.org/releases.html",
                "checker": {
                    "type": "apt-cache",
                    "package": "libwayland-egl-backend-dev",
                },
                "installer": {
                    "type": "not-needed",
                },
            },
        ],
    },
    "wayland-scanner": {
        "platform": "host",
        "projects": [
            {
                "fallback": True,
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "license": ["mit"],
                "changelog": "https://wayland.freedesktop.org/releases.html",
                "prereqs": [
                    "expat",
                    "gcc",
                    "meson",
                    "ninja",
                    "pkg-config",
                ],
                "checker": {
                    "type": "git",
                    "url": "https://gitlab.freedesktop.org/wayland/wayland.git",
                    "hint": r'1\.\d\d.\d+',
                },
                "installer": {
                    "type": "custom",
                    "name": "wayland-scanner",
                },
            },
            {
                "arch": ["any"],
                "os": ["archlinux"],
                "osVersion": ["latest"],
                "abi": ["any"],
                "license": ["mit"],
                "changelog": "https://wayland.freedesktop.org/releases.html",
                "checker": {
                    "type": "pacman",
                    "package": "wayland",
                },
                "installer": {
                    "type": "pacman",
                    "package": "wayland",
                },
            },
            {
                "arch": ["any"],
                "os": ["steamrt"],
                "osVersion": ["any"],
                "abi": ["any"],
                "changelog": "https://wayland.freedesktop.org/releases.html",
                "checker": {
                    "type": "apt-cache",
                    "package": "libwayland-bin",
                },
                "installer": {
                    "type": "not-needed",
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
            {
                "arch": ["any"],
                "os": ["steamrt"],
                "osVersion": ["any"],
                "abi": ["any"],
                "changelog": "https://savannah.gnu.org/news/?group=wget",
                "checker": {
                    "type": "apt-cache",
                    "package": "wget",
                },
                "installer": {
                    "type": "not-needed",
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
            {
                "arch": ["x86_64"],
                "os": ["steamrt"],
                "osVersion": ["any"],
                "abi": ["any"],
                "changelog": "https://fossies.org/linux/binutils/binutils/NEWS",
                "checker": {
                    "type": "apt-cache",
                    "package": "binutils-x86-64-linux-gnu",
                },
                "installer": {
                    "type": "not-needed",
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
            {
                "arch": ["x86_64"],
                "os": ["steamrt"],
                "osVersion": ["any"],
                "abi": ["any"],
                "changelog": "https://gcc.gnu.org/",
                "prereqs": [
                    "gcc",
                ],
                "checker": {
                    "type": "apt-cache",
                    "package": "gcc-12-monolithic",
                },
                "installer": {
                    "type": "cmd",
                    "cmds": [
                        [
                            "update-alternatives", "--set",
                            "x86_64-linux-gnu-g++", "/usr/bin/g++-12", "1"
                        ],
                    ],
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
            {
                "arch": ["x86_64"],
                "os": ["steamrt"],
                "osVersion": ["any"],
                "abi": ["any"],
                "changelog": "https://gcc.gnu.org/",
                "checker": {
                    "type": "apt-cache",
                    "package": "gcc-12-monolithic",
                },
                "installer": {
                    "type": "cmd",
                    "cmds": [
                        [
                            "update-alternatives", "--set",
                            "x86_64-linux-gnu-cpp", "/usr/bin/cpp-12", "1"
                        ],
                        [
                            "update-alternatives", "--set",
                            "x86_64-linux-gnu-gcc", "/usr/bin/gcc-12", "1"
                        ],
                        [
                            "update-alternatives", "--set",
                            "x86_64-linux-gnu-gcc-ar", "/usr/bin/gcc-ar-12",
                            "1"
                        ],
                        [
                            "update-alternatives", "--set",
                            "x86_64-linux-gnu-gcc-nm", "/usr/bin/gcc-nm-12",
                            "1"
                        ],
                        [
                            "update-alternatives", "--set",
                            "x86_64-linux-gnu-gcc-ranlib",
                            "/usr/bin/gcc-ranlib-12", "1"
                        ],
                        [
                            "update-alternatives", "--set",
                            "x86_64-linux-gnu-gcov", "/usr/bin/gcov-12", "1"
                        ]
                    ],
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
            {
                "arch": ["any"],
                "os": ["steamrt"],
                "osVersion": ["any"],
                "abi": ["any"],
                "prereqs": [
                    "pkg-config",
                ],
                "checker": {
                    "type": "apt-cache",
                    "package": "pkg-config",
                },
                "installer": {
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
            {
                "arch": ["any"],
                "os": ["steamrt"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "license": ["mit"],
                "changelog": "https://gitlab.freedesktop.org/xorg/lib/libxau/-/tags",
                "checker": {
                    "type": "apt-cache",
                    "package": "libxau-dev",
                },
                "installer": {
                    "type": "not-needed",
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
            {
                "arch": ["any"],
                "os": ["steamrt"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "license": ["x11"],
                "changelog": "https://xcb.freedesktop.org/",
                "checker": {
                    "type": "apt-cache",
                    "package": "libx11-xcb-dev",
                },
                "installer": {
                    "type": "not-needed",
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
            {
                "arch": ["any"],
                "os": ["steamrt"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "license": ["x11"],
                "changelog": "https://xcb.freedesktop.org/",
                "checker": {
                    "type": "apt-cache",
                    "package": "xcb-proto",
                },
                "installer": {
                    "type": "not-needed",
                },
            },
        ],
    },
}
