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
                "changelog": "https://github.com/icculus/physfs/releases",
                "prereqs": [
                    "wget",
                    "{triplet}-gcc",
                    "{triplet}-g++",
                    "make",
                    "cmake",
                ],
                "checker": {
                    "type": "git",
                    "url": "https://github.com/icculus/physfs.git",
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
                "changelog": "https://github.com/icculus/physfs/releases",
                "checker": {
                    "type": "apt-cache",
                    "package": "libphysfs-dev",
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
                "changelog": "https://github.com/icculus/physfs/releases",
                "checker": {
                    "type": "apt-cache",
                    "package": "libphysfs-dev",
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
                "changelog": "https://github.com/PortAudio/portaudio/wiki/ReleaseNotes",
                "prereqs": [
                    "wget",
                    "{triplet}-gcc",
                    "make",
                    "alsa-lib",
                ],
                "checker": {
                    "type": "git",
                    "url": "https://github.com/PortAudio/portaudio.git",
                    "hint": r'v\d+\.\d\.\d$',
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
                "changelog": "https://github.com/PortAudio/portaudio/wiki/ReleaseNotes",
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
                "changelog": "https://github.com/PortAudio/portaudio/wiki/ReleaseNotes",
                "checker": {
                    "type": "apt-cache",
                    "package": "portaudio19-dev",
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
                "changelog": "https://github.com/PortAudio/portaudio/wiki/ReleaseNotes",
                "checker": {
                    "type": "apt-cache",
                    "package": "portaudio19-dev",
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
                "changelog": "https://gitlab.freedesktop.org/xorg/lib/pthread-stubs/-/tags",
                "prereqs": [
                    "{triplet}-gcc",
                    "autoconf",
                    "automake",
                    "make",
                    "wget",
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
                "changelog": "https://github.com/rurban/safeclib/blob/master/ChangeLog",
                "prereqs": [
                    "autoconf",
                    "automake",
                    "libtool",
                    "make",
                    "{triplet}-gcc",
                    "wget",
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
                "prereqs": [
                    "wget",
                ],
                "checker": {
                    "type": "git",
                    "url": "https://github.com/nothings/stb.git",
                    "files": ["stb_rect_pack.h"],
                    "hint": r'\d\.\d{2}',
                },
                "installer": {
                    "type": "stb",
                    "library": "stb_rect_pack",
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
        ],
    },
}
