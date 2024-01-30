data = {
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
                    "git",
                    "make",
                    "{triplet}-gcc",
                ],
                # TODO(edomin): check version like in installer
                "checker": {
                    "type": "custom",
                    "name": "luajit",
                    "fallback": {
                        "type": "github",
                        "user": "LuaJIT",
                        "repo": "LuaJIT",
                    },
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
    "lwrb": {
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
                ],
                "checker": {
                    "type": "github",
                    "user": "MaJerle",
                    "repo": "lwrb",
                },
                "installer": {
                    "type": "custom",
                    "name": "lwrb",
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
                "license": ["mit", "bsd-1", "bsd-3"],
                "prereqs": [
                    "{triplet}-gcc",
                    "{triplet}-pkg-config",
                    "autoconf",
                    "libxext",
                    "wget",
                    "xlib",
                    "xorgproto",
                ],
                "checker": {
                    "type": "gitlab",
                    "host": "gitlab.freedesktop.org",
                    "id": "4399",
                },
                "installer": {
                    "type": "custom",
                    "name": "libglvnd",
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
}
