data = {
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
                    "{triplet}-gcc",
                    "{triplet}-pkg-config",
                    "autoconf",
                    "make",
                    "wget",
                    "xcb",
                    "xtrans",
                    "xorgproto",
                ],
                "checker": {
                    "type": "gitlab",
                    "host": "gitlab.freedesktop.org",
                    "id": "701",
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
                    "autoconf",
                    "automake",
                    "make",
                    "wget",
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
    "xorgproto": {
        "platform": "target",
        "projects": [
            {
                "fallback": True,
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "license": [
                    "bsd-2", "hpnd", "hpnd-sv", "icu", "mit", "sgi-b-2",
                    "smlnj", "x11"
                ],
                "prereqs": [
                    "{triplet}-gcc",
                    "meson",
                    "ninja",
                    "wget",
                ],
                "checker": {
                    "type": "gitlab",
                    "host": "gitlab.freedesktop.org",
                    "id": "788",
                },
                "installer": {
                    "type": "custom",
                    "name": "xorgproto",
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
                    "type": "gitlab",
                    "host": "gitlab.freedesktop.org",
                    "id": "749",
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
