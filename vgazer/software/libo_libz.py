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
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["musl"],
                "license": ["bsd-3"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "libogg-dev",
                },
                "installer": {
                    "type": "apk",
                    "package": "libogg-dev",
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
    "libopus": {
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
                    "type": "opus-codec",
                    "project": "libopus",
                },
                "installer": {
                    "type": "custom",
                    "name": "libopus",
                },
            },
            {
                "arch": ["any"],
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["musl"],
                "license": ["bsd-3"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "opus-dev",
                },
                "installer": {
                    "type": "apk",
                    "package": "opus-dev",
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
                    "source": "opus",
                },
                "installer": {
                    "type": "apt",
                    "package": "libopus-dev",
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
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["musl"],
                "license": ["mit", "isc", "x11"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "libpciaccess-dev",
                },
                "installer": {
                    "type": "apk",
                    "package": "libpciaccess-dev",
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
    "libpcre": {
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
                    "{triplet}-g++",
                    "make",
                ],
                "checker": {
                    "type": "custom",
                    "name": "libpcre",
                },
                "installer": {
                    "type": "custom",
                    "name": "libpcre",
                },
            },
            {
                "arch": ["any"],
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["musl"],
                "license": ["bsd-3"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "pcre-dev",
                },
                "installer": {
                    "type": "apk",
                    "package": "pcre-dev",
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
                    "source": "pcre3",
                },
                "installer": {
                    "type": "apt",
                    "package": "libpcre3-dev",
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
                    "source": "pcre3",
                },
                "installer": {
                    "type": "not_needed",
                },
            },
        ],
    },
    "libpcre2": {
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
                    "unzip",
                    "{triplet}-gcc",
                    "make",
                ],
                "checker": {
                    "type": "sourceforge",
                    "project": "pcre",
                },
                "installer": {
                    "type": "custom",
                    "name": "libpcre2",
                },
            },
            {
                "arch": ["any"],
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["musl"],
                "license": ["bsd-3"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "pcre2-dev",
                },
                "installer": {
                    "type": "apk",
                    "package": "pcre2-dev",
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
                    "source": "pcre2",
                },
                "installer": {
                    "type": "apt",
                    "package": "libpcre2-dev",
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
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["musl"],
                "license": ["libpng-2.0"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "libpng-dev",
                },
                "installer": {
                    "type": "apk",
                    "package": "libpng-dev",
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
    "libsensors": {
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
                    "make",
                    "{triplet}-gcc",
                    "flex",
                    "bison",
                ],
                "checker": {
                    "type": "github",
                    "user": "lm-sensors",
                    "repo": "lm-sensors",
                    "ignoredTags": [
                        "i2c-2-8-km2",
                    ],
                },
                "installer": {
                    "type": "custom",
                    "name": "libsensors",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["stretch"],
                "abi": ["gnu"],
                "license": ["lgpl-2.1"],
                "checker": {
                    "type": "debian",
                    "source": "lm-sensors",
                },
                "installer": {
                    "type": "apt",
                    "package": "libsensors4-dev",
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
                    "source": "lm-sensors",
                },
                "installer": {
                    "type": "apt",
                    "package": "libsensors-dev",
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
                    "source": "lm-sensors",
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
    "libtiff": {
        "platform": "target",
        "projects": [
            {
                "fallback": True,
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "license": ["libtiff"],
                "prereqs": [
                    "wget",
                    "make",
                    "{triplet}-gcc",
                    "zlib",
                    "jpeg",
                    "liblzma",
                    "libzstd",
                    "libwebp",
                ],
                "checker": {
                    "type": "custom",
                    "name": "libtiff",
                },
                "installer": {
                    "type": "custom",
                    "name": "libtiff",
                },
            },
            {
                "arch": ["any"],
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["musl"],
                "license": ["libtiff"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "tiff-dev",
                },
                "installer": {
                    "type": "apk",
                    "package": "tiff-dev",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "license": ["libtiff"],
                "checker": {
                    "type": "debian",
                    "source": "tiff",
                },
                "installer": {
                    "type": "apt",
                    "package": "libtiff-dev",
                },
            },
            {
                "arch": ["any"],
                "os": ["steamrt"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "license": ["libtiff"],
                "checker": {
                    "type": "launchpad",
                    "distribution": "precise",
                    "source": "tiff",
                },
                "installer": {
                    "type": "not_needed",
                },
            },
        ],
    },
    "libtool": {
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
                    "package": "libtool",
                },
                "installer": {
                    "type": "apk",
                    "package": "libtool",
                },
            },
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
    "libudev": {
        "platform": "target",
        "projects": [
            {
                "fallback": True,
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "license": ["lgpl-2"],
                "prereqs": [
                    "{triplet}-gcc",
                    "{triplet}-pkg-config",
                    "autoconf",
                    "gperf",
                    "libtool",
                    "make",
                    "wget",
                ],
                "checker": {
                    "type": "github",
                    "user": "eudev-project",
                    "repo": "eudev",
                },
                "installer": {
                    "type": "custom",
                    "name": "libudev",
                },
            },
        ],
    },
    "libuc": {
        "platform": "target",
        "projects": [
            {
                "fallback": True,
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "license": ["cc0"],
                "prereqs": [
                    "wget",
                    "{triplet}-gcc",
                    "make",
                    "cmake",
                    "cmake_barebones",
                ],
                "checker": {
                    "type": "github",
                    "user": "edomin",
                    "repo": "libuc",
                },
                "installer": {
                    "type": "custom",
                    "name": "libuc",
                },
            },
        ],
    },
    "libva": {
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
                    "autoconf",
                    "libtool",
                    "make",
                    "{triplet}-gcc",
                    "{triplet}-pkg-config",
                    "xlib",
                    "libxext",
                    "libxfixes",
                    "libdrm",
                ],
                "postreqsOnce": [
                    "opengl",
                ],
                "checker": {
                    "type": "github",
                    "user": "intel",
                    "repo": "libva",
                },
                "installer": {
                    "type": "custom",
                    "name": "libva",
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
                    "package": "libva-dev",
                },
                "installer": {
                    "type": "apk",
                    "package": "libva-dev",
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
                    "source": "libva",
                },
                "installer": {
                    "type": "apt",
                    "package": "libva-dev",
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
                    "source": "libva",
                },
                "installer": {
                    "type": "not_needed",
                },
            },
        ],
    },
    "libvdpau": {
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
                    "libxext",
                    "meson",
                    "wget",
                    "xlib",
                    "xorgproto",
                ],
                "checker": {
                    "type": "gitlab",
                    "host": "gitlab.freedesktop.org",
                    "id": "887",
                },
                "installer": {
                    "type": "custom",
                    "name": "libvdpau",
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
                    "package": "libvdpau-dev",
                },
                "installer": {
                    "type": "apk",
                    "package": "libvdpau-dev",
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
                    "source": " libvdpau",
                },
                "installer": {
                    "type": "apt",
                    "package": " libvdpau-dev",
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
                    "source": "libdvpau",
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
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["musl"],
                "license": ["bsd-3"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "libvorbis-dev",
                },
                "installer": {
                    "type": "apk",
                    "package": "libvorbis-dev",
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
    "libwebp": {
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
                    "type": "custom",
                    "name": "libwebp",
                },
                "installer": {
                    "type": "custom",
                    "name": "libwebp",
                },
            },
            {
                "arch": ["any"],
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["musl"],
                "license": ["bsd-3"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "libwebp-dev",
                },
                "installer": {
                    "type": "apk",
                    "package": "libwebp-dev",
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
                    "source": "libwebp",
                },
                "installer": {
                    "type": "apt",
                    "package": "libwebp-dev",
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
                    "source": "libwebp",
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
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["musl"],
                "license": ["mit", "x11", "hpnd", "hpnd-sv", "smlnj"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "libxext-dev",
                },
                "installer": {
                    "type": "apk",
                    "package": "libxext-dev",
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
    "libxfixes": {
        "platform": "target",
        "projects": [
            {
                "fallback": True,
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "license": ["hpnd-sv", "mit"],
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
                    "id": "715",
                },
                "installer": {
                    "type": "custom",
                    "name": "libxfixes",
                },
            },
            {
                "arch": ["any"],
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["musl"],
                "license": ["hpnd-sv", "mit"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "libxfixes-dev",
                },
                "installer": {
                    "type": "apk",
                    "package": "libxfixes-dev",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "license": ["hpnd-sv", "mit"],
                "checker": {
                    "type": "debian",
                    "source": " libxfixes",
                },
                "installer": {
                    "type": "apt",
                    "package": " libxfixes-dev",
                },
            },
            {
                "arch": ["any"],
                "os": ["steamrt"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "license": ["hpnd-sv", "mit"],
                "checker": {
                    "type": "launchpad",
                    "distribution": "precise",
                    "source": "libxfixes",
                },
                "installer": {
                    "type": "not_needed",
                },
            },
        ],
    },
    "libxml2": {
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
                    "zlib",
                    "liblzma",
                ],
                "checker": {
                    "type": "custom",
                    "name": "libxml2",
                },
                "installer": {
                    "type": "custom",
                    "name": "libxml2",
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
                    "package": "libxml2",
                },
                "installer": {
                    "type": "apk",
                    "package": "libxml2",
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
                    "source": "libxml2",
                },
                "installer": {
                    "type": "apt",
                    "package": "libxml2-dev",
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
                    "source": "libxml2",
                },
                "installer": {
                    "type": "not_needed",
                },
            },
        ],
    },
    "libxrandr": {
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
                    "{triplet}-gcc",
                    "{triplet}-pkg-config",
                    "autoconf",
                    "libtool",
                    "libxext",
                    "make",
                    "wget",
                    "xlib",
                    "xorg-macros",
                    "xorgproto",
                    "xrender",
                ],
                "checker": {
                    "type": "gitlab",
                    "host": "gitlab.freedesktop.org",
                    "id": "728",
                },
                "installer": {
                    "type": "custom",
                    "name": "libxrandr",
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
                    "package": "libxrandr-dev",
                },
                "installer": {
                    "type": "apk",
                    "package": "libxrandr-dev",
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
                    "source": "libxrandr",
                },
                "installer": {
                    "type": "apt",
                    "package": "libxrandr-dev",
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
                    "source": "libxrandr",
                },
                "installer": {
                    "type": "not_needed",
                },
            },
        ],
    },
    "libxxf86vm": {
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
                    "libtool",
                    "libxext",
                    "make",
                    "wget",
                    "xlib",
                    "xorg-macros",
                    "xorgproto",
                ],
                "checker": {
                    "type": "gitlab",
                    "host": "gitlab.freedesktop.org",
                    "id": "738",
                },
                "installer": {
                    "type": "custom",
                    "name": "libxxf86vm",
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
                    "package": "libxxf86vm-dev",
                },
                "installer": {
                    "type": "apk",
                    "package": "libxxf86vm-dev",
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
                    "source": "libxxf86vm",
                },
                "installer": {
                    "type": "apt",
                    "package": "libxxf86vm-dev",
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
                    "source": "libxxf86vm",
                },
                "installer": {
                    "type": "not_needed",
                },
            },
        ],
    },
    "libzstd": {
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
                    "make",
                    "cmake",
                    "{triplet}-gcc",
                    "{triplet}-g++",
                ],
                "checker": {
                    "type": "github",
                    "user": "facebook",
                    "repo": "zstd",
                },
                "installer": {
                    "type": "custom",
                    "name": "libzstd",
                },
            },
            {
                "arch": ["any"],
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["musl"],
                "license": ["bsd-3"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "zstd-dev",
                },
                "installer": {
                    "type": "apk",
                    "package": "zstd-dev",
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
                    "source": "libzstd",
                },
                "installer": {
                    "type": "apt",
                    "package": "libzstd-dev",
                },
            },
        ],
    },
}
