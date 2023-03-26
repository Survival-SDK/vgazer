data = {
    "gawk": {
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
                    "package": "gawk",
                },
                "installer": {
                    "type": "apk",
                    "package": "gawk",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "debian",
                    "source": "gawk",
                },
                "installer": {
                    "type": "apt",
                    "package": "gawk",
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
                    "source": "gawk",
                },
                "installer": {
                    "type": "not_needed",
                },
            },
        ],
    },
    "g++": {
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
                    "package": "g++",
                },
                "installer": {
                    "type": "apk",
                    "package": "g++",
                },
            },
            {
                "arch": ["any"],
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
    "gettext": {
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
                    "package": "gettext",
                },
                "installer": {
                    "type": "apk",
                    "package": "gettext",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "debian",
                    "source": "gettext",
                },
                "installer": {
                    "type": "apt",
                    "package": "gettext",
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
                    "source": "gettext",
                },
                "installer": {
                    "type": "not_needed",
                },
            },
        ],
    },
    "giflib": {
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
                ],
                "checker": {
                    "type": "sourceforge",
                    "project": "giflib",
                },
                "installer": {
                    "type": "custom",
                    "name": "giflib",
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
                    "package": "giflib-dev",
                },
                "installer": {
                    "type": "apk",
                    "package": "giflib-dev",
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
                    "source": "giflib",
                },
                "installer": {
                    "type": "apt",
                    "package": "libgif-dev",
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
                    "source": "giflib",
                },
                "installer": {
                    "type": "not_needed",
                },
            },
        ],
    },
    "git": {
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
                    "package": "git",
                },
                "installer": {
                    "type": "apk",
                    "package": "git",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "debian",
                    "source": "git",
                },
                "installer": {
                    "type": "apt",
                    "package": "git",
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
                    "source": "git",
                },
                "installer": {
                    "type": "apt",
                    "package": "git",
                },
            },
        ],
    },
    "glew": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["linux"],
                "osVersion": ["any"],
                "abi": ["any"],
                "license": ["bsd-3", "mit"],
                "prereqs": [
                    "wget",
                    "{triplet}-gcc",
                    "make",
                    "xlib",
                    "opengl",
                ],
                "checker": {
                    "type": "sourceforge",
                    "project": "glew",
                },
                "installer": {
                    "type": "custom",
                    "name": "glew",
                },
            },
            {
                "arch": ["any"],
                "os": ["windows"],
                "osVersion": ["any"],
                "abi": ["any"],
                "license": ["bsd-3", "mit"],
                "prereqs": [
                    "wget",
                    "{triplet}-gcc",
                    "make",
                ],
                "checker": {
                    "type": "sourceforge",
                    "project": "glew",
                },
                "installer": {
                    "type": "custom",
                    "name": "glew",
                },
            },
            {
                "arch": ["any"],
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["musl"],
                "license": ["bsd-3", "mit"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "glew-dev",
                },
                "installer": {
                    "type": "apk",
                    "package": "glew-dev",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "license": ["bsd-3", "mit"],
                "checker": {
                    "type": "debian",
                    "source": "glew",
                },
                "installer": {
                    "type": "apt",
                    "package": "libglew-dev",
                },
            },
            {
                "arch": ["any"],
                "os": ["steamrt"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "license": ["bsd-3", "mit"],
                "checker": {
                    "type": "launchpad",
                    "distribution": "precise",
                    "source": "glew",
                },
                "installer": {
                    "type": "not_needed",
                },
            },
        ],
    },
    "glib": {
        "platform": "target",
        "projects": [
            {
                "fallback": True,
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "license": ["lgpl-2.1"],
                "prereqs": [
                    "wget",
                    "{triplet}-gcc",
                    "{triplet}-g++",
                    "{triplet}-pkg-config",
                    "meson",
                    "libpcre",
                    "libffi",
                    "zlib",
                    "libmount",
                    "libelf",
                ],
                "checker": {
                    "type": "custom",
                    "name": "glib",
                },
                "installer": {
                    "type": "custom",
                    "name": "glib",
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
                    "package": "glib-dev",
                },
                "installer": {
                    "type": "apk",
                    "package": "glib-dev",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "license": ["lgpl-2.1"],
                "checker": {
                    "type": "debian",
                    "source": "glib2.0",
                },
                "installer": {
                    "type": "apt",
                    "package": "libglib2.0-dev",
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
                    "source": "glib2.0",
                },
                "installer": {
                    "type": "not_needed",
                },
            },
        ],
    },
    "glproto": {
        "platform": "target",
        "projects": [
            {
                "fallback": True,
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "license": ["sgi-b-2.0"],
                "prereqs": [
                    "wget",
                    "{triplet}-gcc",
                    "autoconf",
                    "make",
                    "xorg-macros",
                ],
                "checker": {
                    "type": "github",
                    "user": "freedesktop",
                    "repo": "glproto",
                    "ignoredTags": [
                        "xo-6_7_0",
                        "xf86-012804-2330",
                        "xf86-4_4_99_1",
                        "xf86-4_4_0",
                        "xf86-4_3_99_903",
                        "xf86-4_3_99_903_special",
                        "xf86-4_3_99_902",
                        "xf86-4_3_99_901",
                        "xf86-4_3_99_16",
                        "xf86-4_3_0_1",
                        "sco_port_update-base",
                        "rel-0-6-1",
                        "lg3d-rel-0-7-0",
                        "lg3d-rel-0-6-2",
                        "lg3d-base",
                    ],
                },
                "installer": {
                    "type": "custom",
                    "name": "glproto",
                },
            },
            {
                "arch": ["any"],
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["musl"],
                "license": ["sgi-b-2.0"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "xorgproto",
                },
                "installer": {
                    "type": "apk",
                    "package": "xorgproto",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["stretch"],
                "abi": ["gnu"],
                "license": ["sgi-b-2.0"],
                "checker": {
                    "type": "debian",
                    "source": "x11proto-gl",
                },
                "installer": {
                    "type": "apt",
                    "package": "x11proto-gl-dev",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["buster"],
                "abi": ["gnu"],
                "license": ["sgi-b-2.0"],
                "checker": {
                    "type": "debian",
                    "source": "xorgproto",
                },
                "installer": {
                    "type": "apt",
                    "package": "x11proto-gl-dev",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["bullseye", "bookworm", "sid"],
                "abi": ["gnu"],
                "license": ["sgi-b-2.0"],
                "checker": {
                    "type": "debian",
                    "source": "xorgproto",
                },
                "installer": {
                    "type": "apt",
                    "package": "x11proto-dev",
                },
            },
            {
                "arch": ["any"],
                "os": ["steamrt"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "license": ["sgi-b-2.0"],
                "checker": {
                    "type": "launchpad",
                    "distribution": "precise",
                    "source": "x11proto-gl",
                },
                "installer": {
                    "type": "not_needed",
                },
            },
        ],
    },
    "glu": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["linux"],
                "osVersion": ["any"],
                "abi": ["any"],
                "license": ["sgi-b-1.1", "sgi-b-2.0"],
                "prereqs": [
                    "wget",
                    "{triplet}-gcc",
                    "{triplet}-g++",
                    "{triplet}-pkg-config",
                    "make",
                    "opengl",
                ],
                "checker": {
                    "type": "custom",
                    "name": "mesa-glu",
                },
                "installer": {
                    "type": "custom",
                    "name": "mesa-glu",
                },
            },
            {
                "arch": ["any"],
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["musl"],
                "license": ["sgi-b-1.1", "sgi-b-2.0"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "glu-dev",
                },
                "installer": {
                    "type": "apk",
                    "package": "glu-dev",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "license": ["sgi-b-1.1", "sgi-b-2.0"],
                "checker": {
                    "type": "debian",
                    "source": "libglu",
                },
                "installer": {
                    "type": "apt",
                    "package": "libglu1-mesa-dev",
                },
            },
            {
                "arch": ["any"],
                "os": ["steamrt"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "license": ["sgi-b-1.1", "sgi-b-2.0"],
                "checker": {
                    "type": "launchpad",
                    "distribution": "precise",
                    "source": "mesa",
                },
                "installer": {
                    "type": "not_needed",
                },
            },
        ],
    },
    "gpg": {
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
                    "package": "gnupg",
                },
                "installer": {
                    "type": "apk",
                    "package": "gnupg",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "debian",
                    "source": "gnupg2",
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
                    "source": "gnupg2",
                },
                "installer": {
                    "type": "not_needed",
                },
            },
        ],
    },
    "graphite2": {
        "platform": "target",
        "projects": [
            {
                "fallback": True,
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "license": ["lgpl-2.1"],
                "prereqs": [
                    "wget",
                    "{triplet}-gcc",
                    "{triplet}-g++",
                    "make",
                    "cmake",

                ],
                "checker": {
                    "type": "github",
                    "user": "silnrsi",
                    "repo": "graphite",
                },
                "installer": {
                    "type": "custom",
                    "name": "graphite2",
                },
            },
            {
                "arch": ["any"],
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["musl"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "graphite2-dev",
                },
                "installer": {
                    "type": "apk",
                    "package": "graphite2-dev",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "checker": {
                    "type": "debian",
                    "source": "graphite2",
                },
                "installer": {
                    "type": "apt",
                    "package": "libgraphite2-dev",
                },
            },
            {
                "arch": ["any"],
                "os": ["steamrt"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "checker": {
                    "type": "launchpad",
                    "distribution": "precise",
                    "source": "graphite2",
                },
                "installer": {
                    "type": "not_needed",
                },
            },
        ],
    },
    "harfbuzz": {
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
                    "{triplet}-g++",
                    "{triplet}-pkg-config",
                    "make",
                    "cmake",
                    "freetype",
                    "graphite2",
                    "glib",
                    "icu",

                ],
                "postreqs": [
                    "freetype",
                ],
                "checker": {
                    "type": "github",
                    "user": "harfbuzz",
                    "repo": "harfbuzz",
                },
                "installer": {
                    "type": "custom",
                    "name": "harfbuzz",
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
                    "package": "harfbuzz-dev",
                },
                "installer": {
                    "type": "apk",
                    "package": "harfbuzz-dev",
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
                    "source": "harfbuzz",
                },
                "installer": {
                    "type": "apt",
                    "package": "libharfbuzz-dev",
                },
            },
        ],
    },
    "i686-linux-gnu-g++": {
        "platform": "host",
        "projects": [
            {
                "fallback": True,
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "prereqs": [
                    "i686-linux-gnu-gcc",
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
                "arch": ["x86_64"],
                "os": ["debian"],
                "osVersion": ["buster", "bullseye", "bookworm", "sid"],
                "abi": ["any"],
                "checker": {
                    "type": "debian",
                    "source": "gcc-defaults",
                },
                "installer": {
                    "type": "apt",
                    "package": "g++-i686-linux-gnu",
                },
            },
        ],
    },
    "i686-linux-gnu-gcc": {
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
                    "linux-headers-i686",
                ],
                "checker": {
                    "type": "gcc-src",
                },
                "installer": {
                    "type": "gcc-src",
                    "languages": "c,c++",
                    "triplet": "i686-linux-gnu",
                },
            },
            {
                "arch": ["i686"],
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
                "arch": ["x86_64"],
                "os": ["debian"],
                "osVersion": ["buster", "bullseye", "bookworm", "sid"],
                "abi": ["any"],
                "checker": {
                    "type": "debian",
                    "source": "gcc-defaults",
                },
                "installer": {
                    "type": "apt",
                    "package": "gcc-i686-linux-gnu",
                },
            },
        ],
    },
    "i686-linux-gnu-pkg-config": {
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
                    "triplet": "i686-linux-gnu",
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
                    "triplet": "i686-linux-gnu",
                },
            },
        ],
    },
    "i686-linux-musl-g++": {
        "platform": "host",
        "projects": [
            {
                "fallback": True,
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "prereqs": [
                    "i686-linux-musl-gcc"
                ],
                "checker": {
                    "type": "musl-cross-make",
                },
                "installer": {
                    "type": "dummy",
                },
            },
            {
                "arch": ["i686"],
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
    "i686-linux-musl-gcc": {
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
                    "triplet": "i686-linux-musl",
                },
            },
            {
                "arch": ["i686"],
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["any"],
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
    "i686-linux-musl-pkg-config": {
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
                    "triplet": "i686-linux-musl",
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
                    "triplet": "i686-linux-musl",
                },
            },
        ],
    },
    "i686-w64-mingw32-g++": {
        "platform": "host",
        "projects": [
            {
                "arch": ["i686"],
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
                    "package": "g++-mingw-w64-i686",
                    "postInstallCommands": [
                        ["update-alternatives", "--set",
                         "i686-w64-mingw32-gcc",
                         "/usr/bin/i686-w64-mingw32-gcc-posix"],
                        ["update-alternatives", "--set",
                         "i686-w64-mingw32-g++",
                         "/usr/bin/i686-w64-mingw32-g++-posix"],
                    ],
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
                    "source": "gcc-mingw-w64",
                },
                "installer": {
                    "type": "not_needed",
                },
            },
        ],
    },
    "i686-w64-mingw32-gcc": {
        "platform": "host",
        "projects": [
            {
                "arch": ["i686"],
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
                    "package": "gcc-mingw-w64-i686",
                    "postInstallCommands": [
                        ["update-alternatives", "--set",
                         "i686-w64-mingw32-gcc",
                         "/usr/bin/i686-w64-mingw32-gcc-posix"],
                    ],
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
                    "source": "gcc-mingw-w64",
                },
                "installer": {
                    "type": "not_needed",
                },
            },
        ],
    },
    "i686-w64-mingw32-pkg-config": {
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
                    "triplet": "i686-w64-mingw32",
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
                    "triplet": "i686-w64-mingw32",
                },
            },
        ],
    },
    "icu": {
        "platform": "target",
        "projects": [
            {
                "fallback": True,
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "license": ["unicode", "icu", "bsd-3", "naist", "bsd-2"],
                "prereqs": [
                    "wget",
                    "{hostTriplet}-gcc",
                    "{hostTriplet}-g++",
                    "{triplet}-gcc",
                    "{triplet}-g++",
                    "make",
                ],
                "checker": {
                    "type": "custom",
                    "name": "icu",
                },
                "installer": {
                    "type": "custom",
                    "name": "icu",
                },
            },
            {
                "arch": ["any"],
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["musl"],
                "license": ["unicode", "icu", "bsd-3", "naist", "bsd-2"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "icu-dev",
                },
                "installer": {
                    "type": "apk",
                    "package": "icu-dev",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "license": ["unicode", "icu", "bsd-3", "naist", "bsd-2"],
                "checker": {
                    "type": "debian",
                    "source": "icu",
                },
                "installer": {
                    "type": "apt",
                    "package": "libicu-dev",
                },
            },
            {
                "arch": ["any"],
                "os": ["steamrt"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "license": ["unicode", "icu", "bsd-3", "naist", "bsd-2"],
                "checker": {
                    "type": "launchpad",
                    "distribution": "precise",
                    "source": "icu",
                },
                "installer": {
                    "type": "not_needed",
                },
            },
        ],
    },
    "inih": {
        "platform": "target",
        "projects": [
            {
                "fallback": True,
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "license": ["bsd-3"],
                "prereqs": [
                    "wget",
                    "{triplet}-gcc",
                ],
                "checker": {
                    "type": "github",
                    "user": "benhoyt",
                    "repo": "inih",
                },
                "installer": {
                    "type": "custom",
                    "name": "inih",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["buster", "bullseye", "bookworm", "sid"],
                "abi": ["gnu"],
                "license": ["bsd-3"],
                "checker": {
                    "type": "debian",
                    "source": "libinih",
                },
                "installer": {
                    "type": "apt",
                    "package": "libinih-dev",
                },
            },
        ],
    },
    "inputproto": {
        "platform": "target",
        "projects": [
            {
                "fallback": True,
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "license": ["mit", "smlnj"],
                "prereqs": [
                    "wget",
                    "{triplet}-gcc",
                    "make",
                ],
                "checker": {
                    "type": "custom",
                    "name": "inputproto",
                },
                "installer": {
                    "type": "custom",
                    "name": "inputproto",
                },
            },
            {
                "arch": ["any"],
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["musl"],
                "license": ["mit", "smlnj"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "xorgproto",
                },
                "installer": {
                    "type": "apk",
                    "package": "xorgproto",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["stretch"],
                "abi": ["gnu"],
                "license": ["mit", "smlnj"],
                "checker": {
                    "type": "debian",
                    "source": "x11proto-input",
                },
                "installer": {
                    "type": "apt",
                    "package": "x11proto-input-dev",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["buster"],
                "abi": ["gnu"],
                "license": ["mit", "smlnj"],
                "checker": {
                    "type": "debian",
                    "source": "xorgproto",
                },
                "installer": {
                    "type": "apt",
                    "package": "x11proto-input-dev",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["bullseye", "bookworm", "sid"],
                "abi": ["gnu"],
                "license": ["mit", "smlnj"],
                "checker": {
                    "type": "debian",
                    "source": "xorgproto",
                },
                "installer": {
                    "type": "apt",
                    "package": "x11proto-dev",
                },
            },
            {
                "arch": ["any"],
                "os": ["steamrt"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "license": ["mit", "smlnj"],
                "checker": {
                    "type": "launchpad",
                    "distribution": "precise",
                    "source": "x11proto-input",
                },
                "installer": {
                    "type": "not_needed",
                },
            },
        ],
    },
}
