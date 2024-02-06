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
                "prereqs": [
                    "wget",
                    "{triplet}-gcc",
                    "unzip",
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
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "debian",
                    "source": "unzip",
                },
                "installer": {
                    "type": "apt",
                    "package": "unzip",
                },
            },
            {
                "arch": ["any"],
                "os": ["steamrt"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "launchpad",
                    "distribution": "precise",
                    "source": "unzip",
                },
                "installer": {
                    "type": "apt",
                    "package": "unzip",
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
                "prereqs": [
                    "{triplet}-g++",
                    "{triplet}-gcc",
                    "{triplet}-pkg-config",
                    "libffi",
                    "meson",
                    "wayland-scanner",
                    "wget",
                ],
                "checker": {
                    "type": "git",
                    "url": "https://gitlab.freedesktop.org/wayland/wayland.git",
                },
                "installer": {
                    "type": "custom",
                    "name": "wayland",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["any"],
                "license": ["mit"],
                "checker": {
                    "type": "debian",
                    "source": "wayland",
                },
                "installer": {
                    "type": "apt",
                    "package": [
                        "libwayland-dev",
                        "libwayland-egl-backend-dev"
                    ],
                },
            },
            {
                "arch": ["any"],
                "os": ["steamrt"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "license": ["mit"],
                "checker": {
                    "type": "launchpad",
                    "distribution": "precise",
                    "source": "wayland",
                },
                "installer": {
                    "type": "not_needed",
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
                "prereqs": [
                    "gcc",
                    "meson",
                    "pkg-config",
                    "wget",
                ],
                "checker": {
                    "type": "git",
                    "url": "https://gitlab.freedesktop.org/wayland/wayland.git",
                },
                "installer": {
                    "type": "custom",
                    "name": "wayland-scanner",
                },
            },
            {
                "arch": ["any"],
                "os": ["steamrt"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "launchpad",
                    "distribution": "precise",
                    "source": "wayland",
                },
                "installer": {
                    "type": "not_needed",
                },
            },
        ],
    },
    "wget": {
        "platform": "host",
        "projects": [
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["buster", "bullseye"],
                "abi": ["any"],
                "checker": {
                    "type": "debian",
                    "source": "wget",
                },
                "installer": {
                    "type": "not_needed",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["bookworm", "trixie", "sid"],
                "abi": ["any"],
                "checker": {
                    "type": "debian",
                    "source": "wget",
                },
                "installer": {
                    "type": "apt",
                    "package": "wget",
                },
            },
            {
                "arch": ["any"],
                "os": ["steamrt"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "launchpad",
                    "distribution": "precise",
                    "source": "wget",
                },
                "installer": {
                    "type": "not_needed",
                },
            },
        ],
    },
    "x86_64-linux-gnu-g++": {
        "platform": "host",
        "projects": [
            {
                "arch": ["x86_64"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "debian",
                    "source": "gcc-defaults",
                },
                "installer": {
                    "type": "not_needed",
                },
            },
            {
                "arch": ["any"],
                "os": ["steamrt"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "launchpad",
                    "distribution": "precise",
                    "source": "gcc-4.6",
                },
                "installer": {
                    "type": "not_needed",
                },
            },
        ],
    },
    "x86_64-linux-gnu-gcc": {
        "platform": "host",
        "projects": [
            {
                "arch": ["x86_64"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "debian",
                    "source": "gcc-defaults",
                },
                "installer": {
                    "type": "not_needed",
                },
            },
            {
                "arch": ["any"],
                "os": ["steamrt"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "launchpad",
                    "distribution": "precise",
                    "source": "gcc-4.6",
                },
                "installer": {
                    "type": "not_needed",
                },
            },
        ],
    },
    "x86_64-linux-gnu-pkg-config": {
        "platform": "host",
        "projects": [
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "prereqs": [
                    "pkg-config",
                ],
                "checker": {
                    "type": "debian",
                    "source": "pkg-config",
                },
                "installer": {
                    "type": "pkg-config",
                    "triplet": "x86_64-linux-gnu",
                },
            },
            {
                "arch": ["any"],
                "os": ["steamrt"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "launchpad",
                    "distribution": "precise",
                    "source": "pkg-config",
                },
                "installer": {
                    "type": "pkg-config",
                    "triplet": "x86_64-linux-gnu",
                },
            },
        ],
    },
    "x86_64-w64-mingw32-g++": {
        "platform": "host",
        "projects": [
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "debian",
                    "source": "gcc-mingw-w64",
                },
                "installer": {
                    "type": "apt",
                    "package": "g++-mingw-w64-x86-64",
                    "postInstallCommands": [
                        ["update-alternatives", "--set",
                         "x86_64-w64-mingw32-gcc",
                         "/usr/bin/x86_64-w64-mingw32-gcc-posix"],
                        ["update-alternatives", "--set",
                         "x86_64-w64-mingw32-g++",
                         "/usr/bin/x86_64-w64-mingw32-g++-posix"],
                    ],
                },
            },
        ],
    },
    "x86_64-w64-mingw32-gcc": {
        "platform": "host",
        "projects": [
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "debian",
                    "source": "gcc-mingw-w64",
                },
                "installer": {
                    "type": "apt",
                    "package": "gcc-mingw-w64-x86-64",
                    "postInstallCommands": [
                        ["update-alternatives", "--set",
                         "x86_64-w64-mingw32-gcc",
                         "/usr/bin/x86_64-w64-mingw32-gcc-posix"],
                    ],
                },
            },
        ],
    },
    "x86_64-w64-mingw32-pkg-config": {
        "platform": "host",
        "projects": [
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "prereqs": [
                    "pkg-config",
                ],
                "checker": {
                    "type": "debian",
                    "source": "pkg-config",
                },
                "installer": {
                    "type": "pkg-config",
                    "triplet": "x86_64-w64-mingw32",
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
                "prereqs": [
                    "{triplet}-gcc",
                    "{triplet}-pkg-config",
                    "autoconf",
                    "libtool",
                    "make",
                    "wget",
                    "xorg-macros",
                    "xorgproto",
                ],
                "checker": {
                    "type": "git",
                    "url": "https://gitlab.freedesktop.org/xorg/lib/libxau.git",
                    "hint": r'libXau-\d\.\d\.\d+',
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
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "license": ["mit"],
                "checker": {
                    "type": "debian",
                    "source": "libxau",
                },
                "installer": {
                    "type": "apt",
                    "package": "libxau-dev",
                },
            },
            {
                "arch": ["any"],
                "os": ["steamrt"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "license": ["mit"],
                "checker": {
                    "type": "launchpad",
                    "distribution": "precise",
                    "source": "libxau",
                },
                "installer": {
                    "type": "not_needed",
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
                },
                "installer": {
                    "type": "custom",
                    "name": "xcb",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "license": ["x11"],
                "checker": {
                    "type": "debian",
                    "source": "libx11",
                },
                "installer": {
                    "type": "apt",
                    "package": "libx11-xcb-dev",
                },
            },
            {
                "arch": ["any"],
                "os": ["steamrt"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "license": ["x11"],
                "checker": {
                    "type": "launchpad",
                    "distribution": "precise",
                    "source": "libx11",
                },
                "installer": {
                    "type": "not_needed",
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
                "prereqs": [
                    "autoconf",
                    "automake",
                    "make",
                    "wget",
                ],
                "checker": {
                    "type": "git",
                    "url": "https://gitlab.freedesktop.org/xorg/proto/xcbproto.git",
                },
                "installer": {
                    "type": "custom",
                    "name": "xcb-proto",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "license": ["x11"],
                "checker": {
                    "type": "debian",
                    "source": "xcb-proto",
                },
                "installer": {
                    "type": "apt",
                    "package": "xcb-proto",
                },
            },
            {
                "arch": ["any"],
                "os": ["steamrt"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "license": ["x11"],
                "checker": {
                    "type": "launchpad",
                    "distribution": "precise",
                    "source": "xcb-proto",
                },
                "installer": {
                    "type": "not_needed",
                },
            },
        ],
    },
}
