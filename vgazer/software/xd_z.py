data = {
    "xdamage": {
        "platform": "target",
        "projects": [
            {
                "fallback": True,
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "license": ["hpnd-sv"],
                "prereqs": [
                    "wget",
                    "make",
                    "{triplet}-gcc",
                    "{triplet}-pkg-config",
                    "xorg-macros",
                    "damageproto",
                    "libxfixes",
                    "fixesproto",
                    "xextproto",
                    "xlib",
                ],
                "checker": {
                    "type": "custom",
                    "name": "xdamage",
                },
                "installer": {
                    "type": "custom",
                    "name": "xdamage",
                },
            },
            {
                "arch": ["any"],
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["musl"],
                "license": ["hpnd-sv"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "libxdamage-dev",
                },
                "installer": {
                    "type": "apk",
                    "package": "libxdamage-dev",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "license": ["hpnd-sv"],
                "checker": {
                    "type": "debian",
                    "source": "libxdamage",
                },
                "installer": {
                    "type": "apt",
                    "package": "libxdamage-dev",
                },
            },
            {
                "arch": ["any"],
                "os": ["steamrt"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "license": ["hpnd-sv"],
                "checker": {
                    "type": "launchpad",
                    "distribution": "precise",
                    "source": "libxdamage",
                },
                "installer": {
                    "type": "not_needed",
                },
            },
        ],
    },
    "xextproto": {
        "platform": "target",
        "projects": [
            {
                "fallback": True,
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "license": ["mit", "hpnd", "hpnd-sv", "x11", "smlnj"],
                "prereqs": [
                    "wget",
                    "{triplet}-gcc",
                    "make",
                ],
                "checker": {
                    "type": "custom",
                    "name": "xextproto",
                },
                "installer": {
                    "type": "custom",
                    "name": "xextproto",
                },
            },
            {
                "arch": ["any"],
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["musl"],
                "license": ["mit", "hpnd", "hpnd-sv", "x11", "smlnj"],
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
                "license": ["mit", "hpnd", "hpnd-sv", "x11", "smlnj"],
                "checker": {
                    "type": "debian",
                    "source": "x11proto-xext",
                },
                "installer": {
                    "type": "apt",
                    "package": "x11proto-xext-dev",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["buster"],
                "abi": ["gnu"],
                "license": ["mit", "hpnd", "hpnd-sv", "x11", "smlnj"],
                "checker": {
                    "type": "debian",
                    "source": "xorgproto",
                },
                "installer": {
                    "type": "apt",
                    "package": "x11proto-xext-dev",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["bullseye", "bookworm", "sid"],
                "abi": ["gnu"],
                "license": ["mit", "hpnd", "hpnd-sv", "x11", "smlnj"],
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
                "license": ["mit", "hpnd", "hpnd-sv", "x11", "smlnj"],
                "checker": {
                    "type": "launchpad",
                    "distribution": "precise",
                    "source": "x11proto-xext",
                },
                "installer": {
                    "type": "not_needed",
                },
            },
        ],
    },
    "xf86vidmodeproto": {
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
                ],
                "checker": {
                    "type": "custom",
                    "name": "xf86vidmodeproto",
                },
                "installer": {
                    "type": "custom",
                    "name": "xf86vidmodeproto",
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
                "license": ["x11"],
                "checker": {
                    "type": "debian",
                    "source": "x11proto-xf86vidmode",
                },
                "installer": {
                    "type": "apt",
                    "package": "x11proto-xf86vidmode-dev",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["buster"],
                "abi": ["gnu"],
                "license": ["x11"],
                "checker": {
                    "type": "debian",
                    "source": "xorgproto",
                },
                "installer": {
                    "type": "apt",
                    "package": "x11proto-xf86vidmode-dev",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["bullseye", "bookworm", "sid"],
                "abi": ["gnu"],
                "license": ["x11"],
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
                "license": ["x11"],
                "checker": {
                    "type": "launchpad",
                    "distribution": "precise",
                    "source": "x11proto-xf86vidmode",
                },
                "installer": {
                    "type": "not_needed",
                },
            },
        ],
    },
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
                "prereqs": [
                    "wget",
                    "{triplet}-gcc",
                    "make",
                    "{triplet}-pkg-config",
                    "xproto",
                    "xextproto",
                    "xtrans",
                    "xcb",
                    "kbproto",
                    "inputproto",
                ],
                "checker": {
                    "type": "custom",
                    "name": "xlib",
                },
                "installer": {
                    "type": "custom",
                    "name": "xlib",
                },
            },
            {
                "arch": ["any"],
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["musl"],
                "license": ["mit", "x11", "hpnd-sv", "smlnj", "hpnd", "bsd-1"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "libx11-dev",
                },
                "installer": {
                    "type": "apk",
                    "package": "libx11-dev",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "license": ["mit", "x11", "hpnd-sv", "smlnj", "hpnd", "bsd-1"],
                "checker": {
                    "type": "debian",
                    "source": "libx11",
                },
                "installer": {
                    "type": "apt",
                    "package": "libx11-dev",
                },
            },
            {
                "arch": ["any"],
                "os": ["steamrt"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "license": ["mit", "x11", "hpnd-sv", "smlnj", "hpnd", "bsd-1"],
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
                "prereqs": [
                    "wget",
                    "{triplet}-gcc",
                    "make",
                ],
                "checker": {
                    "type": "github",
                    "user": "XadillaX",
                    "repo": "xmempool",
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
                "prereqs": [
                    "wget",
                    "autoconf",
                    "make",
                ],
                "checker": {
                    "type": "gitlab",
                    "host": "gitlab.freedesktop.org",
                    "id": "798",
                },
                "installer": {
                    "type": "custom",
                    "name": "xorg-macros",
                },
            },
            {
                "arch": ["any"],
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "util-macros",
                },
                "installer": {
                    "type": "apk",
                    "package": "util-macros",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "debian",
                    "source": "xutils-dev",
                },
                "installer": {
                    "type": "apt",
                    "package": "xutils-dev",
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
                    "source": "xutils-dev",
                },
                "installer": {
                    "type": "not_needed",
                },
            },
        ],
    },
    "xproto": {
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
                    "name": "xproto",
                },
                "installer": {
                    "type": "custom",
                    "name": "xproto",
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
                    "source": "x11proto-core",
                },
                "installer": {
                    "type": "apt",
                    "package": "x11proto-core-dev",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["buster", "bullseye", "bookworm", "sid"],
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
                    "source": "x11proto-core",
                },
                "installer": {
                    "type": "not_needed",
                },
            },
        ],
    },
    "xrender": {
        "platform": "target",
        "projects": [
            {
                "fallback": True,
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "license": ["hpnd-sv"],
                "prereqs": [
                    "wget",
                    "autoconf",
                    "libtool",
                    "{triplet}-gcc",
                    "{triplet}-pkg-config",
                    "make",
                    "xorg-macros",
                    "xlib",
                    "renderproto",
                ],
                "checker": {
                    "type": "github",
                    "user": "freedesktop",
                    "repo": "xorg-libXrender",
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
                    ],
                },
                "installer": {
                    "type": "custom",
                    "name": "xrender",
                },
            },
            {
                "arch": ["any"],
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["musl"],
                "license": ["hpnd-sv"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "libxrender-dev",
                },
                "installer": {
                    "type": "apk",
                    "package": "libxrender-dev",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "license": ["hpnd-sv"],
                "checker": {
                    "type": "debian",
                    "source": "libxrender",
                },
                "installer": {
                    "type": "apt",
                    "package": "libxrender-dev",
                },
            },
            {
                "arch": ["any"],
                "os": ["steamrt"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "license": ["hpnd-sv"],
                "checker": {
                    "type": "launchpad",
                    "distribution": "precise",
                    "source": "libxrender",
                },
                "installer": {
                    "type": "not_needed",
                },
            },
        ],
    },
    "xshmfence": {
        "platform": "target",
        "projects": [
            {
                "fallback": True,
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "license": ["hpnd-sv"],
                "prereqs": [
                    "wget",
                    "{triplet}-gcc",
                    "{triplet}-pkg-config",
                    "make",
                    "xorg-macros",
                    "xproto",
                ],
                "checker": {
                    "type": "custom",
                    "name": "xshmfence",
                },
                "installer": {
                    "type": "custom",
                    "name": "xshmfence",
                },
            },
            {
                "arch": ["any"],
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["musl"],
                "license": ["hpnd-sv"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "libxshmfence-dev",
                },
                "installer": {
                    "type": "apk",
                    "package": "libxshmfence-dev",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "license": ["hpnd-sv"],
                "checker": {
                    "type": "debian",
                    "source": "libxshmfence",
                },
                "installer": {
                    "type": "apt",
                    "package": "libxshmfence-dev",
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
                "prereqs": [
                    "wget",
                    "{triplet}-gcc",
                    "{triplet}-pkg-config",
                    "make",
                    "xorg-macros",
                ],
                "checker": {
                    "type": "custom",
                    "name": "xtrans",
                },
                "installer": {
                    "type": "custom",
                    "name": "xtrans",
                },
            },
            {
                "arch": ["any"],
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["musl"],
                "license": ["mit", "hpnd", "x11", "hpnd-sv"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "xtrans",
                },
                "installer": {
                    "type": "apk",
                    "package": "xtrans",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "license": ["mit", "hpnd", "x11", "hpnd-sv"],
                "checker": {
                    "type": "debian",
                    "source": "xtrans",
                },
                "installer": {
                    "type": "apt",
                    "package": "xtrans-dev",
                },
            },
            {
                "arch": ["any"],
                "os": ["steamrt"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "license": ["mit", "hpnd", "x11", "hpnd-sv"],
                "checker": {
                    "type": "launchpad",
                    "distribution": "precise",
                    "source": "xtrans",
                },
                "installer": {
                    "type": "not_needed",
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
                "prereqs": [
                    "wget",
                    "{triplet}-g++",
                    "make",
                    "cmake",
                ],
                "checker": {
                    "type": "github",
                    "user": "kuba--",
                    "repo": "zip",
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
                "prereqs": [
                    "wget",
                    "{triplet}-gcc",
                    "make",
                ],
                "checker": {
                    "type": "custom",
                    "name": "zlib",
                },
                "installer": {
                    "type": "custom",
                    "name": "zlib",
                },
            },
            {
                "arch": ["any"],
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["musl"],
                "license": ["zlib"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "zlib-dev",
                },
                "installer": {
                    "type": "apk",
                    "package": "zlib-dev",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "license": ["zlib"],
                "checker": {
                    "type": "debian",
                    "source": "zlib",
                },
                "installer": {
                    "type": "apt",
                    "package": "zlib1g-dev",
                },
            },
            {
                "arch": ["any"],
                "os": ["steamrt"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "license": ["zlib"],
                "checker": {
                    "type": "launchpad",
                    "distribution": "precise",
                    "source": "zlib",
                },
                "installer": {
                    "type": "not_needed",
                },
            },
        ],
    },
}
