data = {
    "libogg": {
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
                    "make",
                ],
                "checker": {
                    "type": "xiph",
                    "project": "libogg",
                },
                "installer": {
                    "type": "custom",
                    "name": "libogg",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "license": ["bsd-3"],
                "checker": {
                    "type": "debian",
                    "source": "libogg",
                },
                "installer": {
                    "type": "apt",
                    "package": "libogg-dev",
                },
            },
            {
                "arch": ["any"],
                "os": ["steamrt"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "license": ["bsd-3"],
                "checker": {
                    "type": "launchpad",
                    "distribution": "precise",
                    "source": "libogg",
                },
                "installer": {
                    "type": "not_needed",
                },
            },
        ],
    },
    # MinGW version here: https://github.com/smurfy/libpciaccess
    "libpciaccess": {
        "platform": "target",
        "projects": [
            {
                "fallback": True,
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "license": ["mit", "isc", "x11"],
                "prereqs": [
                    "wget",
                    "autoconf",
                    "libtool",
                    "{triplet}-pkg-config",
                    "{triplet}-gcc",
                    "make",
                    "xorg-macros",
                ],
                "checker": {
                    "type": "gitlab",
                    "host": "gitlab.freedesktop.org",
                    "id": "743",
                },
                "installer": {
                    "type": "custom",
                    "name": "libpciaccess",
                    "fallback": {
                        "type": "custom",
                        "name": "libpciaccess-github",
                    },
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "license": ["mit", "isc", "x11"],
                "checker": {
                    "type": "debian",
                    "source": "libpciaccess",
                },
                "installer": {
                    "type": "apt",
                    "package": "libpciaccess-dev",
                },
            },
            {
                "arch": ["any"],
                "os": ["steamrt"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "license": ["mit", "isc", "x11"],
                "checker": {
                    "type": "launchpad",
                    "distribution": "precise",
                    "source": "libpciaccess",
                },
                "installer": {
                    "type": "not_needed",
                },
            },
        ],
    },
    "libpng": {
        "platform": "target",
        "projects": [
            {
                "fallback": True,
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "license": ["libpng-2.0"],
                "prereqs": [
                    "wget",
                    "{triplet}-gcc",
                    "{triplet}-pkg-config",
                    "make",
                    "zlib",
                ],
                "checker": {
                    "type": "sourceforge",
                    "project": "libpng",
                },
                "installer": {
                    "type": "custom",
                    "name": "libpng",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "license": ["libpng-2.0"],
                "checker": {
                    "type": "debian",
                    "source": "libpng1.6",
                },
                "installer": {
                    "type": "apt",
                    "package": "libpng-dev",
                },
            },
            {
                "arch": ["any"],
                "os": ["steamrt"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "license": ["libpng-2.0"],
                "checker": {
                    "type": "launchpad",
                    "distribution": "precise",
                    "source": "libpng",
                },
                "installer": {
                    "type": "not_needed",
                },
            },
        ],
    },
    "libsir": {
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
                    "make",
                    "{triplet}-gcc",
                ],
                "fallback_prereqs": [
                    "git",
                ],
                "checker": {
                    "type": "github",
                    "user": "ryanlederman",
                    "repo": "libsir",
                },
                "installer": {
                    "type": "custom",
                    "name": "libsir",
                    "fallback": {
                        "type": "custom",
                        "name": "libsir-master",
                    }
                },
            },
        ],
    },
    "libtool": {
        "platform": "host",
        "projects": [
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["stretch", "buster", "bullseye"],
                "abi": ["any"],
                "checker": {
                    "type": "debian",
                    "source": "libtool",
                },
                "installer": {
                    "type": "apt",
                    "package": "libtool",
                    "postInstallCommands": [
                        ["mkdir", "-p", "/usr/local/share/aclocal"],
                        ["ln", "-s", "/usr/share/aclocal/libtool.m4",
                         "/usr/local/share/aclocal/libtool.m4"],
                        ["ln", "-s", "/usr/share/aclocal/ltoptions.m4",
                         "/usr/local/share/aclocal/ltoptions.m4"],
                        ["ln", "-s", "/usr/share/aclocal/ltsugar.m4",
                         "/usr/local/share/aclocal/ltsugar.m4"],
                        ["ln", "-s", "/usr/share/aclocal/ltversion.m4",
                         "/usr/local/share/aclocal/ltversion.m4"],
                        ["ln", "-s", "/usr/share/aclocal/lt~obsolete.m4",
                         "/usr/local/share/aclocal/lt~obsolete.m4"],
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
                    "source": "libtool",
                },
                "installer": {
                    "type": "apt",
                    "package": "libtool",
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
                    "source": "libtool",
                },
                "installer": {
                    "type": "not_needed",
                },
            },
        ],
    },
    "libvorbis": {
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
                    "{triplet}-pkg-config",
                    "{triplet}-gcc",
                    "make",
                    "libogg",
                ],
                "checker": {
                    "type": "xiph",
                    "project": "libvorbis",
                },
                "installer": {
                    "type": "custom",
                    "name": "libvorbis",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "license": ["bsd-3"],
                "checker": {
                    "type": "debian",
                    "source": "libvorbis",
                },
                "installer": {
                    "type": "apt",
                    "package": "libvorbis-dev",
                },
            },
            {
                "arch": ["any"],
                "os": ["steamrt"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "license": ["bsd-3"],
                "checker": {
                    "type": "launchpad",
                    "distribution": "precise",
                    "source": "libvorbis",
                },
                "installer": {
                    "type": "not_needed",
                },
            },
        ],
    },
    "libxext": {
        "platform": "target",
        "projects": [
            {
                "fallback": True,
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "license": ["mit", "x11", "hpnd", "hpnd-sv", "smlnj"],
                "prereqs": [
                    "{triplet}-gcc",
                    "{triplet}-pkg-config",
                    "autoconf",
                    "libtool",
                    "make",
                    "wget",
                    "xlib",
                    "xorg-macros",
                    "xorgproto",
                ],
                "checker": {
                    "type": "gitlab",
                    "host": "gitlab.freedesktop.org",
                    "id": "714",
                },
                "installer": {
                    "type": "custom",
                    "name": "libxext",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "license": ["mit", "x11", "hpnd", "hpnd-sv", "smlnj"],
                "checker": {
                    "type": "debian",
                    "source": "libxext",
                },
                "installer": {
                    "type": "apt",
                    "package": "libxext-dev",
                },
            },
            {
                "arch": ["any"],
                "os": ["steamrt"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "license": ["mit", "x11", "hpnd", "hpnd-sv", "smlnj"],
                "checker": {
                    "type": "launchpad",
                    "distribution": "precise",
                    "source": "libxext",
                },
                "installer": {
                    "type": "not_needed",
                },
            },
        ],
    },
}
