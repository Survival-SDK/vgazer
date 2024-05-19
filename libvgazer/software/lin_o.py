data = {
    "llvm": {
        "platform": "host",
        "projects": [
            {
                "arch": ["any"],
                "os": ["archlinux"],
                "osVersion": ["any"],
                "abi": ["any"],
                "changelog": "https://llvm.org/docs/ReleaseNotes.html",
                "checker": {
                    "type": "pacman",
                    "package": "llvm",
                },
                "installer": {
                    "type": "pacman",
                    "package": "llvm",
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
                "os": ["archlinux"],
                "osVersion": ["latest"],
                "abi": ["gnu"],
                "license": ["mit"],
                "changelog": "http://luajit.org/status.html",
                "checker": {
                    "type": "pacman",
                    "package": "luajit",
                },
                "installer": {
                    "type": "pacman",
                    "package": "luajit",
                },
            },
            {
                "arch": ["any"],
                "os": ["fedora"],
                "osVersion": ["40"],
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
                "os": ["archlinux"],
                "osVersion": ["latest"],
                "abi": ["any"],
                "changelog": "http://savannah.gnu.org/news/?group=m4",
                "checker": {
                    "type": "pacman",
                    "package": "m4",
                },
                "installer": {
                    "type": "pacman",
                    "package": "m4",
                },
            },
            {
                "arch": ["any"],
                "os": ["oraclelinux"],
                "osVersion": ["7"],
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
                "os": ["archlinux"],
                "osVersion": ["latest"],
                "abi": ["any"],
                "changelog": "https://savannah.gnu.org/news/?group=make",
                "checker": {
                    "type": "pacman",
                    "package": "make",
                },
                "installer": {
                    "type": "pacman",
                    "package": "make",
                },
            },
            {
                "arch": ["any"],
                "os": ["fedora"],
                "osVersion": ["40"],
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
            {
                "arch": ["any"],
                "os": ["oraclelinux"],
                "osVersion": ["7"],
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
        ],
    },
    "makeinfo": {
        "platform": "host",
        "projects": [
            {
                "arch": ["any"],
                "os": ["archlinux"],
                "osVersion": ["latest"],
                "abi": ["any"],
                "changelog": "https://git.savannah.gnu.org/cgit/texinfo.git/plain/NEWS",
                "checker": {
                    "type": "pacman",
                    "package": "texinfo",
                },
                "installer": {
                    "type": "pacman",
                    "package": "texinfo",
                },
            },
            {
                "arch": ["any"],
                "os": ["oraclelinux"],
                "osVersion": ["7"],
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
                    "type": "yolk3k",
                    "package": "meson",
                },
                "installer": {
                    "type": "pip3",
                    "package": "meson",
                },
            },
            {
                "arch": ["any"],
                "os": ["archlinux"],
                "osVersion": ["latest"],
                "abi": ["any"],
                "changelog": "https://mesonbuild.com/Release-notes.html",
                "checker": {
                    "type": "pacman",
                    "package": "meson",
                },
                "installer": {
                    "type": "pacman",
                    "package": "meson",
                },
            },
        ],
    },
    "ninja": {
        "platform": "host",
        "projects": [
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
            {
                "arch": ["any"],
                "os": ["archlinux"],
                "osVersion": ["latest"],
                "abi": ["any"],
                "changelog": "https://ninja-build.org/",
                "checker": {
                    "type": "pacman",
                    "package": "ninja",
                },
                "installer": {
                    "type": "pacman",
                    "package": "ninja",
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
                "os": ["archlinux"],
                "osVersion": ["latest"],
                "abi": ["gnu"],
                "license": ["mit", "bsd-1", "bsd-3"],
                "changelog": "https://gitlab.freedesktop.org/glvnd/libglvnd/-/tags",
                "checker": {
                    "type": "pacman",
                    "package": "libglvnd",
                },
                "installer": {
                    "type": "pacman",
                    "package": "libglvnd",
                },
            },
            {
                "arch": ["any"],
                "os": ["fedora"],
                "osVersion": ["40"],
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
