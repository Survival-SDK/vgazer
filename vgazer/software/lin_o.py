data = {
    "linux-headers-i686": {
        "platform": "target",
        "projects": [
            {
                "arch": ["i686"],
                "os": ["linux"],
                "osVersion": ["any"],
                "abi": ["any"],
                "license": ["gpl-2-lsn"],
                "prereqs": [
                    "wget",
                    "make",
                    "bsdtar",
                    "rsync",
                ],
                "checker": {
                    "type": "linux-headers",
                },
                "installer": {
                    "type": "linux-headers",
                },
            },
            {
                "arch": ["i686"],
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["any"],
                "license": ["gpl-2-lsn"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "linux-headers",
                },
                "installer": {
                    "type": "apk",
                    "package": "linux-headers",
                },
            },
            {
                "arch": ["i686"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["any"],
                "license": ["gpl-2-lsn"],
                "checker": {
                    "type": "debian",
                    "source": "linux-latest",
                },
                "installer": {
                    "type": "not_needed",
                },
            },
        ],
    },
    "linux-headers-x86_64": {
        "platform": "target",
        "projects": [
            {
                "arch": ["x86_64"],
                "os": ["linux"],
                "osVersion": ["any"],
                "abi": ["any"],
                "license": ["gpl-2.0-lsn"],
                "prereqs": [
                    "wget",
                    "make",
                    "bsdtar",
                    "rsync",
                ],
                "checker": {
                    "type": "linux-headers",
                },
                "installer": {
                    "type": "linux-headers",
                },
            },
            {
                "arch": ["x86_64"],
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["any"],
                "license": ["gpl-2.0-lsn"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "linux-headers",
                },
                "installer": {
                    "type": "apk",
                    "package": "linux-headers",
                },
            },
            {
                "arch": ["x86_64"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["any"],
                "license": ["gpl-2.0-lsn"],
                "checker": {
                    "type": "debian",
                    "source": "linux-latest",
                },
                "installer": {
                    "type": "not_needed",
                },
            },
            {
                "arch": ["x86_64"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["any"],
                "license": ["gpl-2.0-lsn"],
                "checker": {
                    "type": "debian",
                    "source": "linux-lts-trusty",
                },
                "installer": {
                    "type": "not_needed",
                },
            },
        ],
    },
    "list": {
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
                "checker": {
                    "type": "github",
                    "user": "clibs",
                    "repo": "list",
                },
                "installer": {
                    "type": "custom",
                    "name": "list",
                },
            },
        ],
    },
    "llvm": {
        "platform": "host",
        "projects": [
            {
                "arch": ["any"],
                "os": ["alpine"],
                "osVersion": ["v3.9"],
                "abi": ["any"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "llvm5",
                },
                "installer": {
                    "type": "apk",
                    "package": "llvm5",
                },
            },
            {
                "arch": ["any"],
                "os": ["alpine"],
                "osVersion": ["v3.10"],
                "abi": ["any"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "llvm8",
                },
                "installer": {
                    "type": "apk",
                    "package": "llvm8",
                },
            },
            {
                "arch": ["any"],
                "os": ["alpine"],
                "osVersion": ["edge"],
                "abi": ["any"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "llvm9",
                },
                "installer": {
                    "type": "apk",
                    "package": "llvm9",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "debian",
                    "source": "llvm-defaults",
                },
                "installer": {
                    "type": "apt",
                    "package": "llvm",
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
                    "source": "llvm-3.0",
                },
                "installer": {
                    "type": "not_needed",
                },
            },
        ],
    },
    "llvm8": {
        "platform": "host",
        "projects": [
            {
                "arch": ["any"],
                "os": ["alpine"],
                "osVersion": ["v3.10", "edge"],
                "abi": ["any"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "llvm8",
                },
                "installer": {
                    "type": "apk",
                    "package": "llvm8",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["buster"],
                "abi": ["any"],
                "checker": {
                    "type": "debian",
                    "source": "llvm-toolchain-8",
                },
                "installer": {
                    "type": "apt",
                    "package": "llvm-8",
                },
            },
        ],
    },
    "lua": {
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
                "checker": {
                    "type": "custom",
                    "name": "lua",
                },
                "installer": {
                    "type": "custom",
                    "name": "lua",
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
                    "package": "lua5.3-dev",
                },
                "installer": {
                    "type": "apk",
                    "package": "lua5.3-dev",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["stretch", "buster"],
                "abi": ["gnu"],
                "license": ["mit"],
                "checker": {
                    "type": "debian",
                    "source": "lua5.3",
                },
                "installer": {
                    "type": "apt",
                    "package": "liblua5.3-dev",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["bullseye", "bookworm", "sid"],
                "abi": ["gnu"],
                "license": ["mit"],
                "checker": {
                    "type": "debian",
                    "source": "lua5.4",
                },
                "installer": {
                    "type": "apt",
                    "package": "liblua5.4-dev",
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
                    "source": "lua5.2",
                },
                "installer": {
                    "type": "not_needed",
                },
            },
        ],
    },
    "luajit": {
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
                "checker": {
                    "type": "custom",
                    "name": "luajit",
                },
                "installer": {
                    "type": "custom",
                    "name": "luajit",
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
                    "package": "luajit-dev",
                },
                "installer": {
                    "type": "apk",
                    "package": "luajit-dev",
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
                    "source": "luajit",
                },
                "installer": {
                    "type": "apt",
                    "package": "libluajit-5.1-dev",
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
                    "source": "luajit5.1",
                },
                "installer": {
                    "type": "not_needed",
                },
            },
        ],
    },
    "m4": {
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
                    "package": "m4",
                },
                "installer": {
                    "type": "apk",
                    "package": "m4",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "debian",
                    "source": "m4",
                },
                "installer": {
                    "type": "apt",
                    "package": "m4",
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
                    "source": "m4",
                },
                "installer": {
                    "type": "not_needed",
                },
            },
        ],
    },
    "make": {
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
                    "package": "make",
                },
                "installer": {
                    "type": "apk",
                    "package": "make",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "debian",
                    "source": "make-dfsg",
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
                    "source": "make-dfsg",
                },
                "installer": {
                    "type": "not_needed",
                },
            },
        ],
    },
    "makeinfo": {
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
                    "package": "texinfo",
                },
                "installer": {
                    "type": "apk",
                    "package": "texinfo",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "debian",
                    "source": "texinfo",
                },
                "installer": {
                    "type": "apt",
                    "package": "texinfo",
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
                    "source": "texinfo",
                },
                "installer": {
                    "type": "not_needed",
                },
            },
        ],
    },
    "meson": {
        "platform": "host",
        "projects": [
            {
                "fallback": True,
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "pypi",
                    "package": "meson",
                },
                "installer": {
                    "type": "pip3",
                    "package": "meson",
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
                    "package": "meson",
                },
                "installer": {
                    "type": "apk",
                    "package": "meson",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                # glib requires minimal version of Meson 0.49.2. Debian Stretch
                # repos have Meson with version smaller than 0.49.2
                "osVersion": ["buster", "bullseye", "sid"],
                "abi": ["any"],
                "checker": {
                    "type": "debian",
                    "source": "meson",
                },
                "installer": {
                    "type": "apt",
                    "package": "meson",
                },
            },
        ],
    },
    "minini": {
        "platform": "target",
        "projects": [
            {
                "fallback": True,
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "license": ["apache-2.0"],
                "prereqs": [
                    "wget",
                    "{triplet}-gcc",
                ],
                "checker": {
                    "type": "github",
                    "user": "compuphase",
                    "repo": "minIni",
                },
                "installer": {
                    "type": "custom",
                    "name": "minini",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["buster", "bullseye", "bookworm", "sid"],
                "abi": ["gnu"],
                "license": ["apache-2.0"],
                "checker": {
                    "type": "debian",
                    "source": "libminini",
                },
                "installer": {
                    "type": "apt",
                    "package": "libminini-dev",
                },
            },
        ],
    },
    "mpg123": {
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
                    "{triplet}-pkg-config",
                    "make",
                ],
                "checker": {
                    "type": "sourceforge",
                    "project": "mpg123",
                },
                "installer": {
                    "type": "custom",
                    "name": "mpg123",
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
                    "package": "mpg123-dev",
                },
                "installer": {
                    "type": "apk",
                    "package": "mpg123-dev",
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
                    "source": "libmpg123",
                },
                "installer": {
                    "type": "apt",
                    "package": "libmpg123-dev",
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
                    "source": "mpg123",
                },
                "installer": {
                    "type": "not_needed",
                },
            },
        ],
    },
    "musl": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["musl"],
                "license": ["mit"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "musl-dev",
                },
                "installer": {
                    "type": "apk",
                    "package": "musl-dev",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["musl"],
                "license": ["mit"],
                "checker": {
                    "type": "debian",
                    "source": "musl",
                },
                "installer": {
                    "type": "apt",
                    "package": "musl-dev",
                },
            },
        ],
    },
    "nasm": {
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
                    "package": "nasm",
                },
                "installer": {
                    "type": "apk",
                    "package": "nasm",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "debian",
                    "source": "nasm",
                },
                "installer": {
                    "type": "apt",
                    "package": "nasm",
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
                    "source": "nasm",
                },
                "installer": {
                    "type": "not_needed",
                },
            },
        ],
    },
    "ninja": {
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
                    "package": "ninja",
                },
                "installer": {
                    "type": "apk",
                    "package": "ninja",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "debian",
                    "source": "ninja-build",
                },
                "installer": {
                    "type": "apt",
                    "package": "ninja-build",
                },
            },
            {
                "arch": ["any"],
                "os": ["steamrt"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "launchpad",
                    "distribution": "ninja-build",
                    "source": "nasm",
                },
                "installer": {
                    "type": "not_needed",
                },
            },
        ],
    },
    "nuklear": {
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
                    "type": "github",
                    "user": "Immediate-Mode-UI",
                    "repo": "Nuklear",
                },
                "installer": {
                    "type": "custom",
                    "name": "nuklear",
                },
            },
        ],
    },
    "opengl": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["linux"],
                "osVersion": ["any"],
                "abi": ["any"],
                "license": ["mit", "sgi-b-2.0", "bsl-1.0"],
                "prereqs": [
                    "wget",
                    "{triplet}-gcc",
                    "{triplet}-pkg-config",
                    "meson",
                    "python3-mako",
                    "flex",
                    "bison",
                    "llvm8",
                    "gettext",
                    "zlib",
                    "libdrm",
                    "libva",
                    "libvdpau",
                    "wayland-protocols",
                    "libelf",
                    "wayland-egl-backend",
                    "xdamage",
                    "xshmfence",
                    "glproto",
                    "libxxf86vm",
                    "libxrandr",
                    "libsensors",
                ],
                "postreqs": [
                    "libva",
                ],
                "checker": {
                    "type": "custom",
                    "name": "mesa",
                },
                "installer": {
                    "type": "custom",
                    "name": "mesa",
                },
            },
            {
                "arch": ["any"],
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["musl"],
                "license": ["mit", "sgi-b-2.0", "bsl-1.0"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "mesa-dev",
                },
                "installer": {
                    "type": "apk",
                    "package": "mesa-dev",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "license": ["mit", "sgi-b-2.0", "bsl-1.0"],
                "checker": {
                    "type": "debian",
                    "source": "mesa",
                },
                "installer": {
                    "type": "apt",
                    "package": "libgl1-mesa-dev",
                },
            },
            {
                "arch": ["any"],
                "os": ["steamrt"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "license": ["mit", "sgi-b-2.0", "bsl-1.0"],
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
    "opusfile": {
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
                    "{triplet}-pkg-config",
                    "make",
                    "libopus",
                    "libogg",
                ],
                "checker": {
                    "type": "opus-codec",
                    "project": "opusfile",
                },
                "installer": {
                    "type": "custom",
                    "name": "opusfile",
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
                    "package": "opusfile-dev",
                },
                "installer": {
                    "type": "apk",
                    "package": "opusfile-dev",
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
                    "source": "opusfile",
                },
                "installer": {
                    "type": "apt",
                    "package": "libopusfile-dev",
                },
            },
        ],
    },
}
