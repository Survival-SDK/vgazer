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
                    "type": "custom",
                    "name": "tinyfiledialogs",
                },
                "installer": {
                    "type": "custom",
                    "name": "tinyfiledialogs",
                },
            },
        ],
    },
    "tslib": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["linux"],
                "osVersion": ["any"],
                "abi": ["any"],
                "license": ["lgpl-2.1"],
                "prereqs": [
                    "wget",
                    "{triplet}-gcc",
                    "make",
                    "cmake",
                ],
                "checker": {
                    "type": "github",
                    "user": "libts",
                    "repo": "tslib",
                },
                "installer": {
                    "type": "custom",
                    "name": "tslib",
                },
            },
            {
                "arch": ["any"],
                "os": ["windows"],
                "osVersion": ["any"],
                "abi": ["any"],
                "license": ["lgpl-2.1"],
                "prereqs": [
                    "wget",
                    "{triplet}-gcc",
                    "{triplet}-pkg-config",
                    "make",
                    "autoconf",
                    "libtool",
                ],
                "checker": {
                    "type": "github",
                    "user": "libts",
                    "repo": "tslib",
                },
                "installer": {
                    "type": "custom",
                    "name": "tslib",
                },
            },
            {
                "arch": ["any"],
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["musl"],
                "license": ["lgpl-2.1"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "tslib-dev",
                },
                "installer": {
                    "type": "apk",
                    "package": "tslib-dev",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["buster", "bullseye", "bookworm", "sid"],
                "abi": ["gnu"],
                "license": ["lgpl-2.1"],
                "checker": {
                    "type": "debian",
                    "source": "tslib",
                },
                "installer": {
                    "type": "apt",
                    "package": "libts-dev",
                },
            },
            {
                "arch": ["any"],
                "os": ["steamrt"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "license": ["lgpl-2.1"],
                "checker": {
                    "type": "launchpad",
                    "distribution": "precise",
                    "source": "tslib",
                },
                "installer": {
                    "type": "not_needed",
                },
            },
        ],
    },
    "unzip": {
        "platform": "host",
        "projects": [
            {
                "arch": ["any"],
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "unzip",
                },
                "installer": {
                    "type": "apk",
                    "package": "unzip",
                },
            },
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
    "utf": {
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
                    "git",
                    "{triplet}-gcc",
                ],
                "checker": {
                    "type": "github",
                    "user": "andlabs",
                    "repo": "utf",
                },
                "installer": {
                    "type": "custom",
                    "name": "utf",
                },
            },
        ],
    },
    "utf8": {
        "platform": "target",
        "projects": [
            {
                "fallback": True,
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "license": ["pd"],
                "prereqs": [
                    "git",
                    "{triplet}-gcc",
                ],
                "checker": {
                    "type": "github",
                    "user": "haipome",
                    "repo": "utf8",
                },
                "installer": {
                    "type": "custom",
                    "name": "utf8",
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
                    "type": "custom",
                    "name": "wayland",
                },
                "installer": {
                    "type": "custom",
                    "name": "wayland",
                },
            },
            {
                "arch": ["any"],
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["any"],
                "license": ["mit"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "wayland-dev",
                },
                "installer": {
                    "type": "apk",
                    "package": "wayland-dev",
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
                    "package": ["libwayland-dev", "libwayland-egl-backend-dev"],
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
    "wayland-protocols": {
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
                    "{triplet}-pkg-config",
                    "meson",
                    "ninja",
                    "wayland-scanner",
                    "wget",
                ],
                "checker": {
                    "type": "gitlab",
                    "host": "gitlab.freedesktop.org",
                    "id": "2891",
                },
                "installer": {
                    "type": "custom",
                    "name": "wayland-protocols",
                },
            },
            {
                "arch": ["any"],
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["any"],
                "license": ["mit"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "wayland-protocols",
                },
                "installer": {
                    "type": "apk",
                    "package": "wayland-protocols",
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
                    "source": "wayland-protocols",
                },
                "installer": {
                    "type": "apt",
                    "package": "wayland-protocols",
                },
            },
        ],
    },
    "wayland-scanner": {
        "platform": "host",
        "projects": [
            {
                "arch": ["any"],
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "wayland-dev",
                },
                "installer": {
                    "type": "apk",
                    "package": "wayland-dev",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "debian",
                    "source": "wayland",
                },
                "installer": {
                    "type": "apt",
                    "package": ["libwayland-bin", "libwayland-dev"],
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
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "wget",
                },
                "installer": {
                    "type": "pkg-config",
                    "triplet": "x86_64-linux-gnu",
                },
            },
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
                "fallback": True,
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "prereqs": [
                    "x86_64-linux-gnu-gcc",
                ],
                "checker": {
                    "type": "gcc-src",
                },
                "installer": {
                    "type": "dummy",
                },
            },
            {
                "arch": ["i686"],
                "os": ["debian"],
                "osVersion": ["buster", "bullseye", "bookworm", "sid"],
                "abi": ["any"],
                "checker": {
                    "type": "debian",
                    "source": "gcc-defaults",
                },
                "installer": {
                    "type": "apt",
                    "package": "g++-x86-64-linux-gnu",
                },
            },
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
                "fallback": True,
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "prereqs": [
                    "bash",
                    "bison",
                    "bsdtar",
                    "g++",
                    "gawk",
                    "gpg",
                    "make",
                    "makeinfo",
                    "wget",
                    "linux-headers-x86_64",
                ],
                "checker": {
                    "type": "gcc-src",
                },
                "installer": {
                    "type": "gcc-src",
                    "languages": "c",
                    "triplet": "x86_64-linux-gnu",
                },
            },
            {
                "arch": ["i686"],
                "os": ["debian"],
                "osVersion": ["buster", "bullseye", "bookworm", "sid"],
                "abi": ["any"],
                "checker": {
                    "type": "debian",
                    "source": "gcc-defaults",
                },
                "installer": {
                    "type": "apt",
                    "package": "gcc-x86-64-linux-gnu",
                },
            },
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
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "prereqs": [
                    "pkg-config",
                ],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "pkgconf",
                },
                "installer": {
                    "type": "pkg-config",
                    "triplet": "x86_64-linux-gnu",
                },
            },
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
    "x86_64-linux-musl-g++": {
        "platform": "host",
        "projects": [
            {
                "fallback": True,
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "prereqs": [
                    "x86_64-linux-musl-gcc",
                ],
                "checker": {
                    "type": "musl-cross-make",
                },
                "installer": {
                    "type": "dummy",
                },
            },
            {
                "arch": ["x86_64"],
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "g++",
                },
                "installer": {
                    "type": "apk",
                    "package": "g++",
                },
            },
        ],
    },
    "x86_64-linux-musl-gcc": {
        "platform": "host",
        "projects": [
            {
                "fallback": True,
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "prereqs": [
                    "wget",
                    "bsdtar",
                    "g++",
                    "make",
                ],
                "checker": {
                    "type": "musl-cross-make",
                },
                "installer": {
                    "type": "musl-cross-make",
                    "languages": "c,c++",
                    "triplet": "x86_64-linux-musl",
                },
            },
            {
                "arch": ["x86_64"],
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["any"],
                "prereqs": [
                    "musl",
                ],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "gcc",
                },
                "installer": {
                    "type": "apk",
                    "package": "gcc",
                },
            },
        ],
    },
    "x86_64-linux-musl-pkg-config": {
        "platform": "host",
        "projects": [
            {
                "arch": ["any"],
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["musl"],
                "prereqs": [
                    "pkg-config",
                ],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "pkgconf",
                },
                "installer": {
                    "type": "pkg-config",
                    "triplet": "x86_64-linux-musl",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["musl"],
                "prereqs": [
                    "pkg-config",
                ],
                "checker": {
                    "type": "debian",
                    "source": "pkg-config",
                },
                "installer": {
                    "type": "pkg-config",
                    "triplet": "x86_64-linux-musl",
                },
            },
        ],
    },
    "x86_64-w64-mingw32-g++": {
        "platform": "host",
        "projects": [
            {
                "arch": ["x86_64"],
                "os": ["alpine"],
                "osVersion": ["edge"],
                "abi": ["any"],
                "checker": {
                    "type": "alpine",
                    "repo": "testing",
                    "package": "mingw-w64-gcc",
                },
                "installer": {
                    "type": "apk",
                    "package": "mingw-w64-gcc",
                },
            },
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
                "arch": ["x86_64"],
                "os": ["alpine"],
                "osVersion": ["edge"],
                "abi": ["any"],
                "checker": {
                    "type": "alpine",
                    "repo": "testing",
                    "package": "mingw-w64-gcc",
                },
                "installer": {
                    "type": "apk",
                    "package": "mingw-w64-gcc",
                },
            },
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
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "prereqs": [
                    "pkg-config",
                ],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "pkgconf",
                },
                "installer": {
                    "type": "pkg-config",
                    "triplet": "x86_64-w64-mingw32",
                },
            },
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
                    "wget",
                    "{triplet}-gcc",
                    "make",
                    "{triplet}-pkg-config",
                    "xproto"
                ],
                "checker": {
                    "type": "custom",
                    "name": "xau",
                },
                "installer": {
                    "type": "custom",
                    "name": "xau",
                    "fallback": {
                        "type": "custom",
                        "name": "xau-gitlab",
                        "fallback": {
                            "type": "custom",
                            "name": "xau-github",
                        },
                    },
                },
            },
            {
                "arch": ["any"],
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["musl"],
                "license": ["mit"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "libxau-dev",
                },
                "installer": {
                    "type": "apk",
                    "package": "libxau-dev",
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
                    "wget",
                    "{triplet}-gcc",
                    "make",
                    "{triplet}-pkg-config",
                    "xcb-proto",
                    "pthread-stubs",
                    "xau",
                ],
                "checker": {
                    "type": "custom",
                    "name": "xcb",
                },
                "installer": {
                    "type": "custom",
                    "name": "xcb",
                },
            },
            {
                "arch": ["any"],
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["musl"],
                "license": ["x11"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "libxcb-dev",
                },
                "installer": {
                    "type": "apk",
                    "package": "libxcb-dev",
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
                    "wget",
                    "make",
                ],
                "fallback_prereqs": [
                    "autoconf"
                ],
                "checker": {
                    "type": "custom",
                    "name": "xcb-proto",
                },
                "installer": {
                    "type": "custom",
                    "name": "xcb-proto",
                    "fallback": {
                        "type": "custom",
                        "name": "xcb-proto-gitlab",
                    },
                },
            },
            {
                "arch": ["any"],
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["musl"],
                "license": ["x11"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "xcb-proto",
                },
                "installer": {
                    "type": "apk",
                    "package": "xcb-proto",
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
