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
                "changelog": "https://www.lua.org/versions.html",
                "prereqs": [
                    "wget",
                    "make",
                    "{triplet}-gcc",
                ],
                "checker": {
                    "type": "git",
                    "url": "https://github.com/lua/lua.git",
                },
                "installer": {
                    "type": "custom",
                    "name": "lua",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["buster"],
                "abi": ["gnu"],
                "license": ["mit"],
                "changelog": "https://www.lua.org/manual/5.3/readme.html#changes",
                "checker": {
                    "type": "apt-cache",
                    "package": "liblua5.3-dev",
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
                "changelog": "https://www.lua.org/manual/5.4/readme.html#changes",
                "checker": {
                    "type": "apt-cache",
                    "package": "liblua5.4-dev",
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
                "changelog": "https://www.lua.org/manual/5.2/readme.html#changes",
                "checker": {
                    "type": "apt-cache",
                    "package": "liblua5.2-dev",
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
                "changelog": "http://luajit.org/status.html",
                "prereqs": [
                    "make",
                    "{triplet}-gcc",
                ],
                # TODO(edomin): check version like in installer
                "checker": {
                    "type": "git",
                    "url": "https://luajit.org/git/luajit.git",
                },
                "installer": {
                    "type": "custom",
                    "name": "luajit",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "license": ["mit"],
                "changelog": "http://luajit.org/status.html",
                "checker": {
                    "type": "apt-cache",
                    "package": "libluajit-5.1-dev",
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
                "changelog": "http://luajit.org/status.html",
                "checker": {
                    "type": "apt-cache",
                    "package": "libluajit-5.1-dev",
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
                "changelog": "https://github.com/MaJerle/lwrb/blob/develop/CHANGELOG.md",
                "prereqs": [
                    "wget",
                    "{triplet}-gcc",
                ],
                "checker": {
                    "type": "git",
                    "url": "https://github.com/MaJerle/lwrb.git",
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
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["any"],
                "changelog": "http://savannah.gnu.org/news/?group=m4",
                "checker": {
                    "type": "apt-cache",
                    "package": "m4",
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
                "changelog": "http://savannah.gnu.org/news/?group=m4",
                "checker": {
                    "type": "apt-cache",
                    "package": "m4",
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
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["any"],
                "changelog": "https://savannah.gnu.org/news/?group=make",
                "checker": {
                    "type": "apt-cache",
                    "package": "make",
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
                "changelog": "https://savannah.gnu.org/news/?group=make",
                "checker": {
                    "type": "apt-cache",
                    "package": "make",
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
                "changelog": "https://mesonbuild.com/Release-notes.html",
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
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["any"],
                "changelog": "https://mesonbuild.com/Release-notes.html",
                "checker": {
                    "type": "apt-cache",
                    "package": "meson",
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
                "changelog": "https://www.compuphase.com/minini.htm",
                "prereqs": [
                    "wget",
                    "{triplet}-gcc",
                ],
                "checker": {
                    "type": "git",
                    "url": "https://github.com/compuphase/minIni.git",
                },
                "installer": {
                    "type": "custom",
                    "name": "minini",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "license": ["apache-2.0"],
                "changelog": "https://www.compuphase.com/minini.htm",
                "checker": {
                    "type": "apt-cache",
                    "package": "libminini-dev",
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
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["any"],
                "changelog": "https://ninja-build.org/",
                "checker": {
                    "type": "apt-cache",
                    "package": "ninja-build",
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
                "changelog": "https://ninja-build.org/",
                "checker": {
                    "type": "apt-cache",
                    "package": "ninja-build",
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
                "changelog": "https://immediate-mode-ui.github.io/Nuklear/doc/index.html#nuklear/changelog",
                "prereqs": [
                    "wget",
                ],
                "checker": {
                    "type": "git",
                    "url": "https://github.com/Immediate-Mode-UI/Nuklear.git",
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
                "changelog": "https://gitlab.freedesktop.org/glvnd/libglvnd/-/tags",
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
                    "type": "git",
                    "url": "https://gitlab.freedesktop.org/glvnd/libglvnd.git",
                },
                "installer": {
                    "type": "custom",
                    "name": "libglvnd",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "license": ["mit", "sgi-b-2.0", "bsl-1.0"],
                "changelog": "https://www.mesa3d.org/news/",
                "checker": {
                    "type": "apt-cache",
                    "package": "libgl1-mesa-dev",
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
                "changelog": "https://www.mesa3d.org/news/",
                "checker": {
                    "type": "apt-cache",
                    "package": "libgl1-mesa-dev",
                },
                "installer": {
                    "type": "not_needed",
                },
            },
        ],
    },
}
