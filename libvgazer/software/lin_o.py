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
                    "{triplet}-binutils",
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
                "os": ["fedora"],
                "osVersion": ["43"],
                "abi": ["gnu"],
                "license": ["mit"],
                "changelog": "http://luajit.org/status.html",
                "checker": {
                    "type": "dnf",
                    "package": "luajit-devel",
                },
                "installer": {
                    "type": "dnf",
                    "package": "luajit-devel",
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
                    "hint": r'v\d\.\d\.\d$',
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
                "os": ["amazonlinux"],
                "osVersion": ["2"],
                "abi": ["any"],
                "changelog": "http://savannah.gnu.org/news/?group=m4",
                "checker": {
                    "type": "yum",
                    "package": "m4",
                },
                "installer": {
                    "type": "yum",
                    "package": "m4",
                },
            },
        ],
    },
    "make": {
        "platform": "host",
        "projects": [
            {
                "arch": ["any"],
                "os": ["amazonlinux"],
                "osVersion": ["2"],
                "abi": ["any"],
                "changelog": "https://savannah.gnu.org/news/?group=make",
                "checker": {
                    "type": "yum",
                    "package": "make",
                },
                "installer": {
                    "type": "yum",
                    "package": "make",
                },
            },
            {
                "arch": ["any"],
                "os": ["fedora"],
                "osVersion": ["43"],
                "abi": ["any"],
                "changelog": "https://savannah.gnu.org/news/?group=make",
                "checker": {
                    "type": "dnf",
                    "package": "make",
                },
                "installer": {
                    "type": "dnf",
                    "package": "make",
                },
            },
        ],
    },
    "makeinfo": {
        "platform": "host",
        "projects": [
            {
                "arch": ["any"],
                "os": ["amazonlinux"],
                "osVersion": ["2"],
                "abi": ["any"],
                "changelog": "https://git.savannah.gnu.org/cgit/texinfo.git/plain/NEWS",
                "checker": {
                    "type": "yum",
                    "package": "texinfo",
                },
                "installer": {
                    "type": "yum",
                    "package": "texinfo",
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
        ],
    },
    "ninja": {
        "platform": "host",
        "projects": [
            # xorgproto requires ninja >= 1.8.2
            # Amazon Linux 2 has ninja 1.7.2
            {
                "fallback": True,
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "changelog": "https://ninja-build.org/",
                "prereqs": [
                    "g++",
                ],
                "checker": {
                    "type": "git",
                    "url": "https://github.com/ninja-build/ninja.git",
                    "hint": r'v1\.\d\d\.\d+',
                },
                "installer": {
                    "type": "custom",
                    "name": "ninja",
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
                    "hint": r'4\.\d\d\.\d',
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
                "os": ["fedora"],
                "osVersion": ["43"],
                "abi": ["gnu"],
                "license": ["mit", "bsd-1", "bsd-3"],
                "changelog": "https://gitlab.freedesktop.org/glvnd/libglvnd/-/tags",
                "checker": {
                    "type": "dnf",
                    "package": "libglvnd-devel",
                },
                "installer": {
                    "type": "dnf",
                    "package": "libglvnd-devel",
                },
            },
        ],
    },
}
