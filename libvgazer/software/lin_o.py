data = {
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
                    "{triplet}-gcc",
                    "make",
                ],
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
                    "type": "not-needed",
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
                    "type": "not-needed",
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
                    "type": "not-needed",
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
                    "type": "not-needed",
                },
            },
        ],
    },
    "makeinfo": {
        "platform": "host",
        "projects": [
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["any"],
                "changelog": "https://git.savannah.gnu.org/cgit/texinfo.git/plain/NEWS",
                "checker": {
                    "type": "apt-cache",
                    "package": "texinfo",
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
                "changelog": "https://git.savannah.gnu.org/cgit/texinfo.git/plain/NEWS",
                "checker": {
                    "type": "apt-cache",
                    "package": "texinfo",
                },
                "installer": {
                    "type": "not-needed",
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
            {
                "arch": ["any"],
                "os": ["steamrt"],
                "osVersion": ["any"],
                "abi": ["any"],
                "changelog": "https://mesonbuild.com/Release-notes.html",
                "checker": {
                    "type": "apt-cache",
                    "package": "meson",
                },
                "installer": {
                    "type": "not-needed",
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
                    "type": "not-needed",
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
                    "type": "not-needed",
                },
            },
        ],
    },
}
