data = {
    "p7": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["linux"],
                "osVersion": ["any"],
                "abi": ["any"],
                "license": ["lgpl-3"],
                "prereqs": [
                    "wget",
                    "unzip",
                    "{triplet}-g++",
                    "make",
                    "cmake",
                ],
                "checker": {
                    "type": "custom",
                    "name": "p7",
                },
                "installer": {
                    "type": "custom",
                    "name": "p7",
                },
            },
        ],
    },
    "physfs": {
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
                    "{triplet}-g++",
                    "make",
                    "cmake",
                ],
                "checker": {
                    "type": "custom",
                    "name": "physfs",
                    "fallback": {
                        "type": "custom",
                        "name": "physfs-github",
                    },
                },
                "installer": {
                    "type": "custom",
                    "name": "physfs",
                    "fallback": {
                        "type": "custom",
                        "name": "physfs-github",
                    }
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
                    "source": "libphysfs",
                },
                "installer": {
                    "type": "apt",
                    "package": "libphysfs-dev",
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
                    "source": "libphysfs",
                },
                "installer": {
                    "type": "not_needed",
                },
            },
        ],
    },
    "pkg-config": {
        "platform": "host",
        "projects": [
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["stretch", "buster", "bullseye"],
                "abi": ["any"],
                "checker": {
                    "type": "debian",
                    "source": "pkg-config",
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
                "checker": {
                    "type": "debian",
                    "source": "pkgconf",
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
                "checker": {
                    "type": "launchpad",
                    "distribution": "precise",
                    "source": "pkg-config",
                },
                "installer": {
                    "type": "not_needed",
                },
            },
        ],
    },
    "portaudio": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["linux"],
                "osVersion": ["any"],
                "abi": ["any"],
                "license": ["mit"],
                "prereqs": [
                    "wget",
                    "{triplet}-gcc",
                    "make",
                    "alsa-lib",
                ],
                "checker": {
                    "type": "custom",
                    "name": "portaudio",
                },
                "installer": {
                    "type": "custom",
                    "name": "portaudio",
                },
            },
            {
                "arch": ["any"],
                "os": ["windows"],
                "osVersion": ["any"],
                "abi": ["any"],
                "license": ["mit"],
                "prereqs": [
                    "wget",
                    "{triplet}-gcc",
                    "{triplet}-g++",
                    "make",
                ],
                "checker": {
                    "type": "custom",
                    "name": "portaudio",
                },
                "installer": {
                    "type": "custom",
                    "name": "portaudio",
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
                    "source": "portaudio19",
                },
                "installer": {
                    "type": "apt",
                    "package": "portaudio19-dev",
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
                    "source": "portaudio19",
                },
                "installer": {
                    "type": "not_needed",
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
                "prereqs": [
                    "{triplet}-gcc",
                    "autoconf",
                    "automake",
                    "make",
                    "wget",
                ],
                "checker": {
                    "type": "gitlab",
                    "host": "gitlab.freedesktop.org",
                    "id": "2428",
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
                "checker": {
                    "type": "debian",
                    "source": "pthread-stubs",
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
                "checker": {
                    "type": "launchpad",
                    "distribution": "precise",
                    "source": "pthread-stubs",
                },
                "installer": {
                    "type": "not_needed",
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
                "prereqs": [
                    "autoconf",
                    "automake",
                    "libtool",
                    "make",
                    "{triplet}-gcc",
                    "wget",
                ],
                "checker": {
                    "type": "github",
                    "user": "rurban",
                    "repo": "safeclib",
                },
                "installer": {
                    "type": "custom",
                    "name": "safeclib",
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
                "prereqs": [
                    "{triplet}-gcc",
                    "git",
                ],
                "checker": {
                    "type": "github",
                    "user": "jibsen",
                    "repo": "scv",
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
                "prereqs": [
                    "wget",
                ],
                "checker": {
                    "type": "stb",
                    "library": "stb_rect_pack",
                },
                "installer": {
                    "type": "stb",
                    "library": "stb_rect_pack",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["buster", "bullseye", "bookworm", "sid"],
                "abi": ["any"],
                "license": ["unlicense"],
                "checker": {
                    "type": "debian",
                    "source": "libstb",
                },
                "installer": {
                    "type": "apt",
                    "package": "libstb-dev",
                },
            },
        ],
    },
}
