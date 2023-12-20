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
    "perl": {
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
                    "package": "perl",
                },
                "installer": {
                    "type": "apk",
                    "package": "perl",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "debian",
                    "source": "perl",
                },
                "installer": {
                    "type": "apt",
                    "package": "perl",
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
                    "source": "perl",
                },
                "installer": {
                    "type": "not_needed",
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
                "os": ["alpine"],
                "osVersion": ["edge"],
                "abi": ["musl"],
                "license": ["zlib"],
                "checker": {
                    "type": "alpine",
                    "repo": "testing",
                    "package": "physfs-dev",
                },
                "installer": {
                    "type": "apk",
                    "package": "physfs-dev",
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
    "pip2": {
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
                    "package": "py2-pip",
                },
                "installer": {
                    "type": "apk",
                    "package": "py2-pip",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "debian",
                    "source": "python-pip",
                },
                "installer": {
                    "type": "apt",
                    "package": "python-pip",
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
                    "source": "python-pip",
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
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "pkgconf",
                },
                "installer": {
                    "type": "apk",
                    "package": "pkgconf",
                },
            },
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
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["musl"],
                "license": ["mit"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "portaudio-dev",
                },
                "installer": {
                    "type": "apk",
                    "package": "portaudio-dev",
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
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["musl"],
                "license": ["x11"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "libpthread-stubs",
                },
                "installer": {
                    "type": "apk",
                    "package": "libpthread-stubs",
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
    "python2": {
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
                    "package": "python2",
                },
                "installer": {
                    "type": "apk",
                    "package": "python2",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["stretch"],
                "abi": ["any"],
                "checker": {
                    "type": "debian",
                    "source": "python2.7",
                },
                "installer": {
                    "type": "apt",
                    "package": "python2.7",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["buster", "bullseye", "bookworm", "sid"],
                "abi": ["any"],
                "checker": {
                    "type": "debian",
                    "source": "python-defaults",
                },
                "installer": {
                    "type": "apt",
                    "package": "python2",
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
                    "source": "python2.7",
                },
                "installer": {
                    "type": "not_needed",
                },
            },
        ],
    },
    "python2-pyyaml": {
        "platform": "host",
        "projects": [
            {
                "fallback": True,
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "prereqs": [
                    "pip2",
                ],
                "checker": {
                    "type": "pypi",
                    "package": "PyYAML",
                },
                "installer": {
                    "type": "pip",
                    "package": "PyYAML",
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
                    "package": "py2-yaml",
                },
                "installer": {
                    "type": "apk",
                    "package": "py2-yaml",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["stretch", "buster"],
                "abi": ["any"],
                "checker": {
                    "type": "debian",
                    "source": "pyyaml",
                },
                "installer": {
                    "type": "apt",
                    "package": "python-pyyaml",
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
                    "source": "pyyaml",
                },
                "installer": {
                    "type": "apt",
                    "package": "python-yaml",
                },
            },
        ],
    },
    "python3-mako": {
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
                    "package": "Mako",
                },
                "installer": {
                    "type": "pip3",
                    "package": "Mako",
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
                    "package": "py3-mako",
                },
                "installer": {
                    "type": "apk",
                    "package": "py3-mako",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "debian",
                    "source": "mako",
                },
                "installer": {
                    "type": "apt",
                    "package": "python3-mako",
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
                    "source": "mako",
                },
                "installer": {
                    "type": "not_needed",
                },
            },
        ],
    },
    "rsync": {
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
                    "package": "rsync",
                },
                "installer": {
                    "type": "apk",
                    "package": "rsync",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "debian",
                    "source": "rsync",
                },
                "installer": {
                    "type": "apt",
                    "package": "rsync",
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
                    "source": "rsync",
                },
                "installer": {
                    "type": "not_needed",
                },
            },
        ],
    },
    "safe_memcpy": {
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
                ],
                "checker": {
                    "type": "github",
                    "user": "wangzhicheng2013",
                    "repo": "safe_memcpy",
                },
                "installer": {
                    "type": "custom",
                    "name": "safe_memcpy",
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
    "saneopt": {
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
                    "{triplet}-gcc",
                    "make",
                ],
                "checker": {
                    "type": "github",
                    "user": "mmalecki",
                    "repo": "saneopt",
                },
                "installer": {
                    "type": "custom",
                    "name": "saneopt",
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
    "sdl2": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["linux"],
                "osVersion": ["any"],
                "abi": ["any"],
                "license": ["zlib"],
                "prereqs": [
                    "wget",
                    "{triplet}-gcc",
                    "{triplet}-g++",
                    "{triplet}-pkg-config",
                    "make",
                    "alsa-lib",
                    "xlib",
                    "opengl",
                    "tslib",
                ],
                "checker": {
                    "type": "custom",
                    "name": "sdl2",
                },
                "installer": {
                    "type": "custom",
                    "name": "sdl2",
                },
            },
            {
                "arch": ["any"],
                "os": ["windows"],
                "osVersion": ["any"],
                "abi": ["any"],
                "license": ["zlib"],
                "prereqs": [
                    "wget",
                    "{triplet}-gcc",
                    "{triplet}-g++",
                    "{triplet}-pkg-config",
                    "make",
                    "tslib",
                ],
                "checker": {
                    "type": "custom",
                    "name": "sdl2",
                },
                "installer": {
                    "type": "custom",
                    "name": "sdl2",
                },
            },
            {
                "arch": ["any"],
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["musl"],
                "license": ["zlib"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "sdl2-dev",
                },
                "installer": {
                    "type": "apk",
                    "package": "sdl2-dev",
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
                    "source": "libsdl2",
                },
                "installer": {
                    "type": "apt",
                    "package": "libsdl2-dev",
                },
            },
            {
                "arch": ["any"],
                "os": ["steamrt"],
                "osVersion": ["any"],
                "abi": ["any"],
                "license": ["zlib"],
                "checker": {
                    "type": "dont_check", # Use preinstall version only
                },
                "installer": {
                    "type": "not_needed",
                },
            },
        ],
    },
    "sdl2_gfx": {
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
                    "libtool",
                    "make",
                    "sdl2",
                ],
                "checker": {
                    "type": "sourceforge",
                    "project": "sdl2gfx",
                },
                "installer": {
                    "type": "custom",
                    "name": "sdl2_gfx",
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
                    "source": "libsdl2-gfx",
                },
                "installer": {
                    "type": "apt",
                    "package": "libsdl2-gfx-dev",
                },
            },
        ],
    },
    "sdl2_gpu": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["linux"],
                "osVersion": ["any"],
                "abi": ["any"],
                "license": ["mit"],
                "prereqs": [
                    "git",
                    "{triplet}-g++",
                    "make",
                    "cmake",
                    "sdl2",
                    "glew",
                    "stb_image",
                    "stb_image_write",
                    "glu",
                ],
                "checker": {
                    "type": "custom",
                    "name": "sdl2_gpu",
                },
                "installer": {
                    "type": "custom",
                    "name": "sdl2_gpu",
                },
            },
            {
                "arch": ["any"],
                "os": ["windows"],
                "osVersion": ["any"],
                "abi": ["any"],
                "license": ["mit"],
                "prereqs": [
                    "git",
                    "{triplet}-g++",
                    "make",
                    "cmake",
                    "sdl2",
                    "glew",
                    "stb_image",
                    "stb_image_write",
                ],
                "checker": {
                    "type": "custom",
                    "name": "sdl2_gpu",
                },
                "installer": {
                    "type": "custom",
                    "name": "sdl2_gpu",
                },
            },
        ],
    },
    "sdl2_image": {
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
                    "{triplet}-pkg-config",
                    "autoconf",
                    "libtool",
                    "make",
                    "sdl2",
                    "jpeg",
                    "libtiff",
                    "libpng",
                    "zlib",
                    "libwebp",
                ],
                "checker": {
                    "type": "sdl2-addon",
                    "project": "SDL2_image",
                },
                "installer": {
                    "type": "custom",
                    "name": "sdl2_image",
                },
            },
            {
                "arch": ["any"],
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["musl"],
                "license": ["zlib"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "sdl2_image-dev",
                },
                "installer": {
                    "type": "apk",
                    "package": "sdl2_image-dev",
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
                    "source": "libsdl2-image",
                },
                "installer": {
                    "type": "apt",
                    "package": "libsdl2-image-dev",
                },
            },
        ],
    },
    "sdl2_mixer": {
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
                    "make",
                    "sdl2",
                    #"libmodplug",
                    "libogg",
                    "libvorbis",
                    "libflac",
                    "mpg123",
                    "opusfile",
                ],
                "checker": {
                    "type": "sdl2-addon",
                    "project": "SDL2_mixer",
                },
                "installer": {
                    "type": "custom",
                    "name": "sdl2_mixer",
                },
            },
            {
                "arch": ["any"],
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["musl"],
                "license": ["zlib"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "sdl2_mixer-dev",
                },
                "installer": {
                    "type": "apk",
                    "package": "sdl2_mixer-dev",
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
                    "source": "libsdl2-mixer",
                },
                "installer": {
                    "type": "apt",
                    "package": "libsdl2-mixer-dev",
                },
            },
        ],
    },
    "sdl2_ttf": {
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
                    "{triplet}-pkg-config",
                    "make",
                    "sdl2",
                    "freetype",
                ],
                "checker": {
                    "type": "sdl2-addon",
                    "project": "SDL2_ttf",
                },
                "installer": {
                    "type": "custom",
                    "name": "sdl2_ttf",
                },
            },
            {
                "arch": ["any"],
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["musl"],
                "license": ["zlib"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "sdl2_ttf-dev",
                },
                "installer": {
                    "type": "apk",
                    "package": "sdl2_ttf-dev",
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
                    "source": "libsdl2-ttf",
                },
                "installer": {
                    "type": "apt",
                    "package": "libsdl2-ttf-dev",
                },
            },
        ],
    },
    "squirrel": {
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
                    "{triplet}-g++",
                    "make",
                    "cmake",
                ],
                "checker": {
                    "type": "github",
                    "user": "albertodemichelis",
                    "repo": "squirrel",
                },
                "installer": {
                    "type": "custom",
                    "name": "squirrel",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["stretch", "buster", "bullseye", "sid"],
                "abi": ["gnu"],
                "license": ["mit"],
                "checker": {
                    "type": "debian",
                    "source": "squirrel3",
                },
                "installer": {
                    "type": "apt",
                    "package": "libsquirrel-dev",
                },
            },
        ],
    },
    "stb_image": {
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
                    "library": "stb_image",
                },
                "installer": {
                    "type": "stb",
                    "library": "stb_image",
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
    "stb_image_write": {
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
                    "library": "stb_image_write",
                },
                "installer": {
                    "type": "stb",
                    "library": "stb_image_write",
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
