data = {
    "autoconf": {
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
                    "package": "autoconf",
                },
                "installer": {
                    "type": "apk",
                    "package": "autoconf",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "debian",
                    "source": "autoconf",
                },
                "installer": {
                    "type": "apt",
                    "package": "autoconf",
                },
            },
        ],
    },
    "automake": {
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
                    "package": "automake",
                },
                "installer": {
                    "type": "apk",
                    "package": "automake",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["stretch"],
                "abi": ["any"],
                "checker": {
                    "type": "debian",
                    "source": "automake-1.15",
                },
                "installer": {
                    "type": "apt",
                    "package": "automake",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["buster", "bullseye", "sid"],
                "abi": ["any"],
                "checker": {
                    "type": "debian",
                    "source": "automake-1.16",
                },
                "installer": {
                    "type": "apt",
                    "package": "automake",
                },
            },
        ],
    },
    "automake1.11": {
        "platform": "host",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "prereqs": [
                    "autoconf",
                    "make",
                ],
                "checker": {
                    "type": "custom",
                    "name": "automake1_11",
                },
                "installer": {
                    "type": "custom",
                    "name": "automake1_11",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "debian",
                    "source": "automake1.11",
                },
                "installer": {
                    "type": "apt",
                    "package": "automake1.11",
                },
            },
        ],
    },
    "autopoint": {
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
                    "package": "gettext",
                },
                "installer": {
                    "type": "apk",
                    "package": "gettext",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "debian",
                    "source": "gettext",
                },
                "installer": {
                    "type": "apt",
                    "package": "autopoint",
                },
            },
        ],
    },
    "bash": {
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
                    "package": "bash",
                },
                "installer": {
                    "type": "apk",
                    "package": "bash",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "debian",
                    "source": "bash",
                },
                "installer": {
                    "type": "not_needed",
                },
            },
        ],
    },
    "bison": {
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
                    "package": "bison",
                },
                "installer": {
                    "type": "apk",
                    "package": "bison",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "debian",
                    "source": "bison",
                },
                "installer": {
                    "type": "apt",
                    "package": "bison",
                },
            },
        ],
    },
    "bsdtar": {
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
                    "package": "libarchive-tools",
                },
                "installer": {
                    "type": "apk",
                    "package": "libarchive-tools",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "debian",
                    "source": "libarchive",
                },
                "installer": {
                    "type": "apt",
                    "package": "bsdtar",
                },
            },
        ],
    },
    "cjson": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "prereqs": [
                    "wget",
                    "{triplet}-gcc",
                    "make",
                    "cmake",
                ],
                "checker": {
                    "type": "github",
                    "user": "DaveGamble",
                    "repo": "cJSON",
                },
                "installer": {
                    "type": "custom",
                    "name": "cjson",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["buster", "bullseye", "sid"],
                "abi": ["gnu"],
                "checker": {
                    "type": "debian",
                    "source": "cjson",
                },
                "installer": {
                    "type": "apt",
                    "package": "libcjson-dev",
                },
            },
        ],
    },
    "cmake": {
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
                    "package": "cmake",
                },
                "installer": {
                    "type": "apk",
                    "package": "cmake",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "debian",
                    "source": "cmake",
                },
                "installer": {
                    "type": "apt",
                    "package": "cmake",
                },
            },
        ],
    },
    "cmocka": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "prereqs": [
                    "wget",
                    "{triplet}-gcc",
                    "make",
                    "cmake",
                ],
                "checker": {
                    "type": "custom",
                    "name": "cmocka",
                },
                "installer": {
                    "type": "custom",
                    "name": "cmocka",
                },
            },
            {
                "arch": ["any"],
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["musl"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "cmocka-dev",
                },
                "installer": {
                    "type": "apk",
                    "package": "cmocka-dev",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "checker": {
                    "type": "debian",
                    "source": "cmocka",
                },
                "installer": {
                    "type": "apt",
                    "package": "libcmocka-dev",
                },
            },
        ],
    },
    "damageproto": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "prereqs": [
                    "wget",
                    "{triplet}-gcc",
                    "make",
                ],
                "checker": {
                    "type": "custom",
                    "name": "damageproto",
                },
                "installer": {
                    "type": "custom",
                    "name": "damageproto",
                },
            },
            {
                "arch": ["any"],
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["musl"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "xorgproto",
                },
                "installer": {
                    "type": "apk",
                    "package": "xorgproto",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "checker": {
                    "type": "debian",
                    "source": "x11proto-damage",
                },
                "installer": {
                    "type": "apt",
                    "package": "x11proto-damage-dev",
                },
            },
        ],
    },
    "dr_wav": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "prereqs": [
                    "wget",
                ],
                "checker": {
                    "type": "custom",
                    "name": "dr_wav",
                },
                "installer": {
                    "type": "custom",
                    "name": "dr_wav",
                },
            },
        ],
    },
    "dri2proto": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "prereqs": [
                    "wget",
                    "{triplet}-gcc",
                    "make",
                ],
                "checker": {
                    "type": "custom",
                    "name": "dri2proto",
                },
                "installer": {
                    "type": "custom",
                    "name": "dri2proto",
                },
            },
            {
                "arch": ["any"],
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["musl"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "xorgproto",
                },
                "installer": {
                    "type": "apk",
                    "package": "xorgproto",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "checker": {
                    "type": "debian",
                    "source": "x11proto-dri2",
                },
                "installer": {
                    "type": "apt",
                    "package": "x11proto-dri2-dev",
                },
            },
        ],
    },
    "duktape": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "prereqs": [
                    "wget",
                    "{triplet}-gcc",
                    "python2",
                    "python2-pyyaml",
                ],
                "checker": {
                    "type": "github",
                    "user": "svaarala",
                    "repo": "duktape",
                },
                "installer": {
                    "type": "custom",
                    "name": "duktape",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "checker": {
                    "type": "debian",
                    "source": "duktape",
                },
                "installer": {
                    "type": "apt",
                    "package": "duktape-dev",
                },
            },
        ],
    },
    "file": {
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
                    "package": "file",
                },
                "installer": {
                    "type": "apk",
                    "package": "file",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "debian",
                    "source": "file",
                },
                "installer": {
                    "type": "not_needed",
                },
            },
        ],
    },
    "fixesproto": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "prereqs": [
                    "wget",
                    "{triplet}-gcc",
                    "make",
                ],
                "checker": {
                    "type": "custom",
                    "name": "fixesproto",
                },
                "installer": {
                    "type": "custom",
                    "name": "fixesproto",
                },
            },
            {
                "arch": ["any"],
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["musl"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "xorgproto",
                },
                "installer": {
                    "type": "apk",
                    "package": "xorgproto",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "checker": {
                    "type": "debian",
                    "source": "x11proto-fixes",
                },
                "installer": {
                    "type": "apt",
                    "package": "x11proto-fixes-dev",
                },
            },
        ],
    },
    "flex": {
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
                    "package": "flex",
                },
                "installer": {
                    "type": "apk",
                    "package": "flex",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "debian",
                    "source": "flex",
                },
                "installer": {
                    "type": "apt",
                    "package": "flex",
                },
            },
        ],
    },
    "freetype": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "prereqs": [
                    "wget",
                    "{triplet}-gcc",
                    "{triplet}-pkg-config",
                    "make",
                    "zlib",
                    "libbzip2",
                    "libpng",
                ],
                "postreqsOnce": [
                    "harfbuzz",
                ],
                "checker": {
                    "type": "custom",
                    "name": "freetype",
                },
                "installer": {
                    "type": "custom",
                    "name": "freetype",
                },
            },
            {
                "arch": ["any"],
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["musl"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "freetype-dev",
                },
                "installer": {
                    "type": "apk",
                    "package": "freetype-dev",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "checker": {
                    "type": "debian",
                    "source": "freetype",
                },
                "installer": {
                    "type": "apt",
                    "package": "libfreetype6-dev",
                },
            },
        ],
    },
    "gawk": {
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
                    "package": "gawk",
                },
                "installer": {
                    "type": "apk",
                    "package": "gawk",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "debian",
                    "source": "gawk",
                },
                "installer": {
                    "type": "apt",
                    "package": "gawk",
                },
            },
        ],
    },
    "g++": {
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
                    "package": "g++",
                },
                "installer": {
                    "type": "apk",
                    "package": "g++",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "debian",
                    "source": "gcc-defaults",
                },
                "installer": {
                    "type": "not_needed",
                },
            },
        ],
    },
    "gettext": {
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
                    "package": "gettext",
                },
                "installer": {
                    "type": "apk",
                    "package": "gettext",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "debian",
                    "source": "gettext",
                },
                "installer": {
                    "type": "apt",
                    "package": "gettext",
                },
            },
        ],
    },
    "giflib": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "prereqs": [
                    "wget",
                    "{triplet}-gcc",
                    "make",
                ],
                "checker": {
                    "type": "sourceforge",
                    "project": "giflib",
                },
                "installer": {
                    "type": "custom",
                    "name": "giflib",
                },
            },
            {
                "arch": ["any"],
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["musl"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "giflib-dev",
                },
                "installer": {
                    "type": "apk",
                    "package": "giflib-dev",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "checker": {
                    "type": "debian",
                    "source": "giflib",
                },
                "installer": {
                    "type": "apt",
                    "package": "libgif-dev",
                },
            },
        ],
    },
    "git": {
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
                    "package": "git",
                },
                "installer": {
                    "type": "apk",
                    "package": "git",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "debian",
                    "source": "git",
                },
                "installer": {
                    "type": "apt",
                    "package": "git",
                },
            },
        ],
    },
    "glew": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["linux"],
                "osVersion": ["any"],
                "abi": ["any"],
                "prereqs": [
                    "wget",
                    "{triplet}-gcc",
                    "make",
                    "xlib",
                    "opengl",
                ],
                "checker": {
                    "type": "sourceforge",
                    "project": "glew",
                },
                "installer": {
                    "type": "custom",
                    "name": "glew",
                },
            },
            {
                "arch": ["any"],
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["musl"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "glew-dev",
                },
                "installer": {
                    "type": "apk",
                    "package": "glew-dev",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "checker": {
                    "type": "debian",
                    "source": "glew",
                },
                "installer": {
                    "type": "apt",
                    "package": "libglew-dev",
                },
            },
        ],
    },
    "glib": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "prereqs": [
                    "wget",
                    "{triplet}-gcc",
                    "{triplet}-g++",
                    "{triplet}-pkg-config",
                    "meson",
                    "libpcre",
                    "libffi",
                    "zlib",
                    "libmount",
                    "libelf",
                ],
                "checker": {
                    "type": "custom",
                    "name": "glib",
                },
                "installer": {
                    "type": "custom",
                    "name": "glib",
                },
            },
            {
                "arch": ["any"],
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["musl"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "glib-dev",
                },
                "installer": {
                    "type": "apk",
                    "package": "glib-dev",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "checker": {
                    "type": "debian",
                    "source": "glib2.0",
                },
                "installer": {
                    "type": "apt",
                    "package": "libglib2.0-dev",
                },
            },
        ],
    },
    "glproto": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "prereqs": [
                    "wget",
                    "{triplet}-gcc",
                    "autoconf",
                    "make",
                    "xorg-macros",
                ],
                "checker": {
                    "type": "github",
                    "user": "freedesktop",
                    "repo": "glproto",
                    "ignoredTags": [
                        "xo-6_7_0",
                        "xf86-012804-2330",
                        "xf86-4_4_99_1",
                        "xf86-4_4_0",
                        "xf86-4_3_99_903",
                        "xf86-4_3_99_903_special",
                        "xf86-4_3_99_902",
                        "xf86-4_3_99_901",
                        "xf86-4_3_99_16",
                        "xf86-4_3_0_1",
                        "sco_port_update-base",
                        "rel-0-6-1",
                        "lg3d-rel-0-7-0",
                        "lg3d-rel-0-6-2",
                        "lg3d-base",
                    ],
                },
                "installer": {
                    "type": "custom",
                    "name": "glproto",
                },
            },
            {
                "arch": ["any"],
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["musl"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "xorgproto",
                },
                "installer": {
                    "type": "apk",
                    "package": "xorgproto",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["stretch"],
                "abi": ["gnu"],
                "checker": {
                    "type": "debian",
                    "source": "x11proto-gl",
                },
                "installer": {
                    "type": "apt",
                    "package": "x11proto-gl-dev",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["buster", "bullseye", "sid"],
                "abi": ["gnu"],
                "checker": {
                    "type": "debian",
                    "source": "xorgproto",
                },
                "installer": {
                    "type": "apt",
                    "package": "x11proto-gl-dev",
                },
            },
        ],
    },
    "gpg": {
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
                    "package": "gnupg",
                },
                "installer": {
                    "type": "apk",
                    "package": "gnupg",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "debian",
                    "source": "gnupg2",
                },
                "installer": {
                    "type": "not_needed",
                },
            },
        ],
    },
    "graphite2": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "prereqs": [
                    "wget",
                    "{triplet}-gcc",
                    "{triplet}-g++",
                    "make",
                    "cmake",

                ],
                "checker": {
                    "type": "github",
                    "user": "silnrsi",
                    "repo": "graphite",
                },
                "installer": {
                    "type": "custom",
                    "name": "graphite2",
                },
            },
            {
                "arch": ["any"],
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["musl"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "graphite2-dev",
                },
                "installer": {
                    "type": "apk",
                    "package": "graphite2-dev",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "checker": {
                    "type": "debian",
                    "source": "graphite2",
                },
                "installer": {
                    "type": "apt",
                    "package": "libgraphite2-dev",
                },
            },
        ],
    },
    "harfbuzz": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "prereqs": [
                    "wget",
                    "{triplet}-gcc",
                    "{triplet}-g++",
                    "{triplet}-pkg-config",
                    "make",
                    "cmake",
                    "freetype",
                    "graphite2",
                    "glib",
                    "icu",

                ],
                "postreqs": [
                    "freetype",
                ],
                "checker": {
                    "type": "github",
                    "user": "harfbuzz",
                    "repo": "harfbuzz",
                },
                "installer": {
                    "type": "custom",
                    "name": "harfbuzz",
                },
            },
            {
                "arch": ["any"],
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["musl"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "harfbuzz-dev",
                },
                "installer": {
                    "type": "apk",
                    "package": "harfbuzz-dev",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "checker": {
                    "type": "debian",
                    "source": "harfbuzz",
                },
                "installer": {
                    "type": "apt",
                    "package": "libharfbuzz-dev",
                },
            },
        ],
    },
    "i586-linux-musl-g++": {
        "platform": "host",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "prereqs": [
                    "i586-linux-musl-gcc",
                ],
                "checker": {
                    "type": "musl-cross-make",
                },
                "installer": {
                    "type": "dummy",
                },
            },
            {
                "arch": ["i686"],
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "g++",
                },
                "installer": {
                    "type": "apk",
                    "package": "g++",
                },
            },
        ],
    },
    "i586-linux-musl-gcc": {
        "platform": "host",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "prereqs": [
                    "wget",
                    "bsdtar",
                    "g++",
                    "make",
                ],
                "checker": {
                    "type": "musl-cross-make",
                },
                "installer": {
                    "type": "musl-cross-make",
                    "languages": "c,c++",
                    "triplet": "i586-linux-musl",
                },
            },
            {
                "arch": ["i686"],
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "gcc",
                },
                "installer": {
                    "type": "apk",
                    "package": "gcc",
                },
            },
        ],
    },
    "i686-linux-gnu-g++": {
        "platform": "host",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "prereqs": [
                    "i686-linux-gnu-gcc",
                ],
                "checker": {
                    "type": "gcc-src",
                },
                "installer": {
                    "type": "dummy",
                },
            },
            {
                "arch": ["i686"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "debian",
                    "source": "gcc-defaults",
                },
                "installer": {
                    "type": "not_needed",
                },
            },
            {
                "arch": ["x86_64"],
                "os": ["debian"],
                "osVersion": ["buster", "bullseye", "sid"],
                "abi": ["any"],
                "checker": {
                    "type": "debian",
                    "source": "gcc-defaults",
                },
                "installer": {
                    "type": "apt",
                    "package": "g++-i686-linux-gnu",
                },
            },
        ],
    },
    "i686-linux-gnu-gcc": {
        "platform": "host",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "prereqs": [
                    "bash",
                    "bison",
                    "bsdtar",
                    "g++",
                    "gawk",
                    "gpg",
                    "make",
                    "makeinfo",
                    "rsync",
                    "wget",
                ],
                "checker": {
                    "type": "gcc-src",
                },
                "installer": {
                    "type": "gcc-src",
                    "languages": "c,c++",
                    "triplet": "i686-linux-gnu",
                },
            },
            {
                "arch": ["i686"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "debian",
                    "source": "gcc-defaults",
                },
                "installer": {
                    "type": "not_needed",
                },
            },
            {
                "arch": ["x86_64"],
                "os": ["debian"],
                "osVersion": ["buster", "bullseye", "sid"],
                "abi": ["any"],
                "checker": {
                    "type": "debian",
                    "source": "gcc-defaults",
                },
                "installer": {
                    "type": "apt",
                    "package": "gcc-i686-linux-gnu",
                },
            },
        ],
    },
    "i686-linux-gnu-pkg-config": {
        "platform": "host",
        "projects": [
            {
                "arch": ["any"],
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "prereqs": [
                    "pkg-config",
                ],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "pkgconf",
                },
                "installer": {
                    "type": "pkg-config",
                    "triplet": "i686-linux-gnu",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "prereqs": [
                    "pkg-config",
                ],
                "checker": {
                    "type": "debian",
                    "source": "pkg-config",
                },
                "installer": {
                    "type": "pkg-config",
                    "triplet": "i686-linux-gnu",
                },
            },
            {
                "arch": ["i686"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "checker": {
                    "type": "debian",
                    "source": "pkg-config",
                },
                "installer": {
                    "type": "apt",
                    "package": "pkg-config",
                },
            },
        ],
    },
    "i686-linux-musl-g++": {
        "platform": "host",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "prereqs": [
                    "i686-linux-musl-gcc"
                ],
                "checker": {
                    "type": "musl-cross-make",
                },
                "installer": {
                    "type": "dummy",
                },
            },
        ],
    },
    "i686-linux-musl-gcc": {
        "platform": "host",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "prereqs": [
                    "wget",
                    "bsdtar",
                    "g++",
                    "make",
                ],
                "checker": {
                    "type": "musl-cross-make",
                },
                "installer": {
                    "type": "musl-cross-make",
                    "languages": "c,c++",
                    "triplet": "i686-linux-musl",
                },
            },
        ],
    },
    "i686-linux-musl-pkg-config": {
        "platform": "host",
        "projects": [
            {
                "arch": ["any"],
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["musl"],
                "prereqs": [
                    "pkg-config",
                ],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "pkgconf",
                },
                "installer": {
                    "type": "pkg-config",
                    "triplet": "i686-linux-musl",
                },
            },
            {
                "arch": ["i686"],
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["musl"],
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
                "osVersion": ["any"],
                "abi": ["musl"],
                "prereqs": [
                    "pkg-config",
                ],
                "checker": {
                    "type": "debian",
                    "source": "pkg-config",
                },
                "installer": {
                    "type": "pkg-config",
                    "triplet": "i686-linux-musl",
                },
            },
        ],
    },
    "i686-w64-mingw32-g++": {
        "platform": "host",
        "projects": [
            {
                "arch": ["i686"],
                "os": ["alpine"],
                "osVersion": ["edge"],
                "abi": ["any"],
                "checker": {
                    "type": "alpine",
                    "repo": "testing",
                    "package": "mingw-w64-gcc",
                },
                "installer": {
                    "type": "apk",
                    "package": "mingw-w64-gcc",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "debian",
                    "source": "gcc-mingw-w64",
                },
                "installer": {
                    "type": "apt",
                    "package": "g++-mingw-w64-i686",
                },
            },
        ],
    },
    "i686-w64-mingw32-gcc": {
        "platform": "host",
        "projects": [
            {
                "arch": ["i686"],
                "os": ["alpine"],
                "osVersion": ["edge"],
                "abi": ["any"],
                "checker": {
                    "type": "alpine",
                    "repo": "testing",
                    "package": "mingw-w64-gcc",
                },
                "installer": {
                    "type": "apk",
                    "package": "mingw-w64-gcc",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "debian",
                    "source": "gcc-mingw-w64",
                },
                "installer": {
                    "type": "apt",
                    "package": "gcc-mingw-w64-i686",
                },
            },
        ],
    },
    "icu": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "prereqs": [
                    "wget",
                    "{triplet}-gcc",
                    "{triplet}-g++",
                    "make",
                ],
                "checker": {
                    "type": "custom",
                    "name": "icu",
                },
                "installer": {
                    "type": "custom",
                    "name": "icu",
                },
            },
            {
                "arch": ["any"],
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["musl"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "icu-dev",
                },
                "installer": {
                    "type": "apk",
                    "package": "icu-dev",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "checker": {
                    "type": "debian",
                    "source": "icu",
                },
                "installer": {
                    "type": "apt",
                    "package": "libicu-dev",
                },
            },
        ],
    },
    "inih": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "prereqs": [
                    "wget",
                    "{triplet}-gcc",
                ],
                "checker": {
                    "type": "github",
                    "user": "benhoyt",
                    "repo": "inih",
                },
                "installer": {
                    "type": "custom",
                    "name": "inih",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["buster", "bullseye", "sid"],
                "abi": ["gnu"],
                "checker": {
                    "type": "debian",
                    "source": "libinih",
                },
                "installer": {
                    "type": "apt",
                    "package": "libinih-dev",
                },
            },
        ],
    },
    "inputproto": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "prereqs": [
                    "wget",
                    "{triplet}-gcc",
                    "make",
                ],
                "checker": {
                    "type": "custom",
                    "name": "inputproto",
                },
                "installer": {
                    "type": "custom",
                    "name": "inputproto",
                },
            },
            {
                "arch": ["any"],
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["musl"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "xorgproto",
                },
                "installer": {
                    "type": "apk",
                    "package": "xorgproto",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["stretch"],
                "abi": ["gnu"],
                "checker": {
                    "type": "debian",
                    "source": "x11proto-input",
                },
                "installer": {
                    "type": "apt",
                    "package": "x11proto-input-dev",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["buster", "bullseye", "sid"],
                "abi": ["gnu"],
                "checker": {
                    "type": "debian",
                    "source": "xorgproto",
                },
                "installer": {
                    "type": "apt",
                    "package": "x11proto-input-dev",
                },
            },
        ],
    },
    "jpeg": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "prereqs": [
                    "wget",
                    "{triplet}-gcc",
                    "make",
                ],
                "checker": {
                    "type": "custom",
                    "name": "jpeg",
                },
                "installer": {
                    "type": "custom",
                    "name": "jpeg",
                },
            },
            {
                "arch": ["any"],
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["musl"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "jpeg-dev",
                },
                "installer": {
                    "type": "apk",
                    "package": "jpeg-dev",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "checker": {
                    "type": "debian",
                    "source": "libjpeg-turbo",
                },
                "installer": {
                    "type": "apt",
                    "package": "libjpeg-dev",
                },
            },
        ],
    },
    "kbproto": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "prereqs": [
                    "wget",
                    "{triplet}-gcc",
                    "make",
                ],
                "checker": {
                    "type": "custom",
                    "name": "kbproto",
                },
                "installer": {
                    "type": "custom",
                    "name": "kbproto",
                },
            },
            {
                "arch": ["any"],
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["musl"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "xorgproto",
                },
                "installer": {
                    "type": "apk",
                    "package": "xorgproto",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "checker": {
                    "type": "debian",
                    "source": "x11proto-kb",
                },
                "installer": {
                    "type": "apt",
                    "package": "x11proto-kb-dev",
                },
            },
        ],
    },
    "lazy-winapi.c": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["windows"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "github",
                    "user": "DoumanAsh",
                    "repo": "lazy-winapi.c",
                },
                "installer": {
                    "type": "custom",
                    "name": "lazy-winapi.c",
                },
            },
        ],
    },
    "libbzip2": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "prereqs": [
                    "wget",
                    "{triplet}-gcc",
                    "make",
                ],
                "checker": {
                    "type": "sourceforge",
                    "project": "bzip2",
                },
                "installer": {
                    "type": "custom",
                    "name": "bzip2",
                },
            },
            {
                "arch": ["any"],
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["musl"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "bzip2-dev",
                },
                "installer": {
                    "type": "apk",
                    "package": "bzip2-dev",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "checker": {
                    "type": "debian",
                    "source": "bzip2",
                },
                "installer": {
                    "type": "apt",
                    "package": "libbz2-dev",
                },
            },
        ],
    },
    "libclipboard": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "prereqs": [
                    "wget",
                    "{triplet}-g++",
                    "make",
                    "{triplet}-pkg-config",
                    "cmake",
                    "xcb",
                ],
                "checker": {
                    "type": "github",
                    "user": "jtanx",
                    "repo": "libclipboard",
                },
                "installer": {
                    "type": "custom",
                    "name": "libclipboard",
                },
            },
        ],
    },
    "libdrm": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "prereqs": [
                    "wget",
                    "{triplet}-gcc",
                    "{triplet}-pkg-config",
                    "meson",
                    "xlib",
                    "libpciaccess",
                ],
                "checker": {
                    "type": "custom",
                    "name": "libdrm",
                },
                "installer": {
                    "type": "custom",
                    "name": "libdrm",
                },
            },
            {
                "arch": ["any"],
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["musl"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "libdrm-dev",
                },
                "installer": {
                    "type": "apk",
                    "package": "libdrm-dev",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "checker": {
                    "type": "debian",
                    "source": "libdrm",
                },
                "installer": {
                    "type": "apt",
                    "package": "libdrm-dev",
                },
            },
        ],
    },
    "libelf": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "prereqs": [
                    "wget",
                    "{triplet}-gcc",
                    "{triplet}-pkg-config",
                    "make",
                    "zlib",
                ],
                "checker": {
                    "type": "custom",
                    "name": "elfutils",
                },
                "installer": {
                    "type": "custom",
                    "name": "libelf",
                },
            },
            {
                "arch": ["any"],
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["musl"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "elfutils-dev",
                },
                "installer": {
                    "type": "apk",
                    "package": "elfutils-dev",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "checker": {
                    "type": "debian",
                    "source": "elfutils",
                },
                "installer": {
                    "type": "apt",
                    "package": "libelf-dev",
                },
            },
        ],
    },
    "libffi": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "prereqs": [
                    "wget",
                    "{triplet}-gcc",
                    "{triplet}-g++",
                    "make",
                ],
                "checker": {
                    "type": "custom",
                    "name": "libffi",
                },
                "installer": {
                    "type": "custom",
                    "name": "libffi",
                },
            },
            {
                "arch": ["any"],
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["musl"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "libffi-dev",
                },
                "installer": {
                    "type": "apk",
                    "package": "libffi-dev",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "checker": {
                    "type": "debian",
                    "source": "libffi",
                },
                "installer": {
                    "type": "apt",
                    "package": "libffi-dev",
                },
            },
        ],
    },
    "libflac": {
        "platform": "target",
        "projects": [
            {
                "arch": ["i686"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "prereqs": [
                    "wget",
                    "{triplet}-gcc",
                    "nasm",
                    "{triplet}-pkg-config",
                    "make",
                    "libogg",
                ],
                "checker": {
                    "type": "xiph",
                    "project": "libflac",
                },
                "installer": {
                    "type": "custom",
                    "name": "libflac",
                },
            },
            {
                "arch": ["x86_64"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "prereqs": [
                    "wget",
                    "{triplet}-gcc",
                    "{triplet}-pkg-config",
                    "make",
                    "libogg",
                ],
                "checker": {
                    "type": "xiph",
                    "project": "libflac",
                },
                "installer": {
                    "type": "custom",
                    "name": "libflac",
                },
            },
            {
                "arch": ["any"],
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["musl"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "flac-dev",
                },
                "installer": {
                    "type": "apk",
                    "package": "flac-dev",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "checker": {
                    "type": "debian",
                    "source": "flac",
                },
                "installer": {
                    "type": "apt",
                    "package": "libflac-dev",
                },
            },
        ],
    },
    "libiconv": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "custom",
                    "name": "libiconv",
                },
                "installer": {
                    "type": "custom",
                    "name": "libiconv",
                },
            },
            {
                "arch": ["any"],
                "os": ["alpine"],
                "osVersion": ["3.10", "edge"],
                "abi": ["gnu"],
                "checker": {
                    "type": "alpine",
                    "repo": "community",
                    "package": "gnu-libiconv-dev",
                },
                "installer": {
                    "type": "apk",
                    "package": "gnu-libiconv-dev",
                },
            },
            {
                "arch": ["any"],
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["musl"],
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
                "abi": ["gnu"],
                "checker": {
                    "type": "debian",
                    "source": "glibc",
                },
                "installer": {
                    "type": "not_needed",
                },
            },
        ],
    },
    "libintl": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["windows"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "github",
                    "user": "j-jorge",
                    "repo": "libintl-lite",
                },
                "installer": {
                    "type": "custom",
                    "name": "libintl-lite",
                },
            },
            {
                "arch": ["any"],
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["musl"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "gettext-dev",
                },
                "installer": {
                    "type": "apk",
                    "package": "gettext-dev",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "checker": {
                    "type": "debian",
                    "source": "glibc",
                },
                "installer": {
                    "type": "apt",
                    "package": "libc6-dev",
                },
            },
        ],
    },
    "liblzma": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["linux"],
                "osVersion": ["any"],
                "abi": ["any"],
                "prereqs": [
                    "wget",
                    "{triplet}-gcc",
                    "make",
                ],
                "checker": {
                    "type": "sourceforge",
                    "project": "lzmautils",
                },
                "installer": {
                    "type": "custom",
                    "name": "liblzma",
                },
            },
            {
                "arch": ["any"],
                "os": ["windows"],
                "osVersion": ["any"],
                "abi": ["any"],
                "prereqs": [
                    "wget",
                    "{triplet}-gcc",
                    "make",
                    "libintl",
                ],
                "checker": {
                    "type": "sourceforge",
                    "project": "lzmautils",
                },
                "installer": {
                    "type": "custom",
                    "name": "liblzma",
                },
            },
            {
                "arch": ["any"],
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["musl"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "xz-dev",
                },
                "installer": {
                    "type": "apk",
                    "package": "xz-dev",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "checker": {
                    "type": "debian",
                    "source": "xz-utils",
                },
                "installer": {
                    "type": "apt",
                    "package": "liblzma-dev",
                },
            },
        ],
    },
    "libmodplug": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "prereqs": [
                    "wget",
                    "{triplet}-gcc",
                    "{triplet}-g++",
                    "make",
                ],
                "checker": {
                    "type": "sourceforge",
                    "project": "modplug-xmms",
                },
                "installer": {
                    "type": "custom",
                    "name": "libmodplug",
                },
            },
            {
                "arch": ["any"],
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["musl"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "libmodplug-dev",
                },
                "installer": {
                    "type": "apk",
                    "package": "libmodplug-dev",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "checker": {
                    "type": "debian",
                    "source": "libmodplug",
                },
                "installer": {
                    "type": "apt",
                    "package": "libmodplug-dev",
                },
            },
        ],
    },
    "libmount": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "prereqs": [
                    "wget",
                    "{triplet}-gcc",
                    "{triplet}-pkg-config",
                    "make",
                    "autopoint",
                    "autoconf",
                    "bison",
                    "libtool",
                    "automake",
                    "gettext",
                ],
                "checker": {
                    "type": "custom",
                    "name": "util-linux",
                },
                "installer": {
                    "type": "custom",
                    "name": "libmount",
                },
            },
            {
                "arch": ["any"],
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["musl"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "util-linux-dev",
                },
                "installer": {
                    "type": "apk",
                    "package": "util-linux-dev",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "debian",
                    "source": "util-linux",
                },
                "installer": {
                    "type": "apt",
                    "package": "libmount-dev",
                },
            },
        ],
    },
    "libogg": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
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
                "checker": {
                    "type": "debian",
                    "source": "libogg",
                },
                "installer": {
                    "type": "apt",
                    "package": "libogg-dev",
                },
            },
        ],
    },
    "libpciaccess": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
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
                "checker": {
                    "type": "debian",
                    "source": "libpciaccess",
                },
                "installer": {
                    "type": "apt",
                    "package": "libpciaccess-dev",
                },
            },
        ],
    },
    "libpcre": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
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
                "checker": {
                    "type": "debian",
                    "source": "pcre3",
                },
                "installer": {
                    "type": "apt",
                    "package": "libpcre3-dev",
                },
            },
        ],
    },
    "libpcre2": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
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
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
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
                "checker": {
                    "type": "debian",
                    "source": "libpng1.6",
                },
                "installer": {
                    "type": "apt",
                    "package": "libpng-dev",
                },
            },
        ],
    },
    "libsensors": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
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
                "osVersion": ["any"],
                "abi": ["gnu"],
                "checker": {
                    "type": "debian",
                    "source": "lm-sensors",
                },
                "installer": {
                    "type": "apt",
                    "package": "libsensors4-dev",
                },
            },
        ],
    },
    "libtiff": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
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
                "checker": {
                    "type": "debian",
                    "source": "tiff",
                },
                "installer": {
                    "type": "apt",
                    "package": "libtiff-dev",
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
                "osVersion": ["any"],
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
        ],
    },
    "libva": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
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
                "checker": {
                    "type": "debian",
                    "source": "libva",
                },
                "installer": {
                    "type": "apt",
                    "package": "libva-dev",
                },
            },
        ],
    },
    "libvdpau": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "prereqs": [
                    "wget",
                    "{triplet}-pkg-config",
                    "{triplet}-gcc",
                    "meson",
                    "dri2proto",
                    "libxext",
                    "xlib",
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
                "checker": {
                    "type": "debian",
                    "source": " libvdpau",
                },
                "installer": {
                    "type": "apt",
                    "package": " libvdpau-dev",
                },
            },
        ],
    },
    "libvorbis": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "xiph",
                    "project": "libvorbis",
                },
                "installer": {
                    "type": "custom",
                    "project": "libvorbis",
                },
            },
            {
                "arch": ["any"],
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["musl"],
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
                "checker": {
                    "type": "debian",
                    "source": "libvorbis",
                },
                "installer": {
                    "type": "apt",
                    "package": "libvorbis-dev",
                },
            },
        ],
    },
    "libwebp": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
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
                "checker": {
                    "type": "debian",
                    "source": "libwebp",
                },
                "installer": {
                    "type": "apt",
                    "package": "libwebp-dev",
                },
            },
        ],
    },
    "libxext": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "prereqs": [
                    "wget",
                    "autoconf",
                    "libtool",
                    "make",
                    "{triplet}-gcc",
                    "{triplet}-pkg-config",
                    "xorg-macros",
                    "xlib",
                    "xproto",
                    "xextproto",
                ],
                "checker": {
                    "type": "github",
                    "user": "freedesktop",
                    "repo": "libXext",
                    "ignoredTags": [
                        "xo-6_7_0",
                        "xf86-012804-2330",
                        "xf86-4_4_99_1",
                        "xf86-4_4_0",
                        "xf86-4_3_99_903",
                        "xf86-4_3_99_903_special",
                        "xf86-4_3_99_902",
                        "xf86-4_3_99_901",
                        "xf86-4_3_99_16",
                        "xf86-4_3_0_1",
                        "sco_port_update-base",
                        "rel-0-6-1",
                        "lg3d-rel-0-7-0",
                    ],
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
                "checker": {
                    "type": "debian",
                    "source": "libxext",
                },
                "installer": {
                    "type": "apt",
                    "package": "libxext-dev",
                },
            },
        ],
    },
    "libxfixes": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "prereqs": [
                    "wget",
                    "autoconf",
                    "libtool",
                    "{triplet}-pkg-config",
                    "{triplet}-gcc",
                    "make",
                    "xorg-macros",
                    "xlib",
                    "xproto",
                    "fixesproto",
                    "xextproto",
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
                "checker": {
                    "type": "debian",
                    "source": " libxfixes",
                },
                "installer": {
                    "type": "apt",
                    "package": " libxfixes-dev",
                },
            },
        ],
    },
    "libxml2": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
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
                "checker": {
                    "type": "debian",
                    "source": "libxml2",
                },
                "installer": {
                    "type": "apt",
                    "package": "libxml2-dev",
                },
            },
        ],
    },
    "libxrandr": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "prereqs": [
                    "wget",
                    "autoconf",
                    "libtool",
                    "{triplet}-pkg-config",
                    "{triplet}-gcc",
                    "make",
                    "xorg-macros",
                    "xlib",
                    "randrproto",
                    "libxext",
                    "xextproto",
                    "xrender",
                    "renderproto",
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
                "checker": {
                    "type": "debian",
                    "source": "libxrandr",
                },
                "installer": {
                    "type": "apt",
                    "package": "libxrandr-dev",
                },
            },
        ],
    },
    "libxxf86vm": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "prereqs": [
                    "wget",
                    "autoconf",
                    "libtool",
                    "{triplet}-pkg-config",
                    "{triplet}-gcc",
                    "make",
                    "xorg-macros",
                    "xproto",
                    "xlib",
                    "xextproto",
                    "libxext",
                    "xf86vidmodeproto",
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
                "checker": {
                    "type": "debian",
                    "source": "libxxf86vm",
                },
                "installer": {
                    "type": "apt",
                    "package": "libxxf86vm-dev",
                },
            },
        ],
    },
    "linux-headers-i686": {
        "platform": "target",
        "projects": [
            {
                "arch": ["i686"],
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["any"],
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
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["any"],
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
                "osVersion": ["buster", "bullseye", "sid"],
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
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
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
                "osVersion": ["any"],
                "abi": ["gnu"],
                "checker": {
                    "type": "debian",
                    "source": "lua5.3",
                },
                "installer": {
                    "type": "apt",
                    "package": "liblua5.3-dev",
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
        ],
    },
    "meson": {
        "platform": "host",
        "projects": [
            {
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
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "prereqs": [
                    "git",
                    "{triplet}-gcc"
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
                "osVersion": ["buster", "bullseye", "sid"],
                "abi": ["gnu"],
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
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
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
                "checker": {
                    "type": "debian",
                    "source": "libmpg123",
                },
                "installer": {
                    "type": "apt",
                    "package": "libmpg123-dev",
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
        ],
    },
    "nuklear": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "prereqs": [
                    "wget",
                ],
                "checker": {
                    "type": "github",
                    "user": "vurtun",
                    "repo": "nuklear",
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
                "checker": {
                    "type": "debian",
                    "source": "mesa",
                },
                "installer": {
                    "type": "apt",
                    "package": "libgl1-mesa-dev",
                },
            },
        ],
    },
    "p7": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "prereqs": [
                    "wget",
                    "unzip",
                    "{triplet}-g++",
                    "make",
                    "linux-headers-{arch}",
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
        ],
    },
    "physfs": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "prereqs": [
                    "wget",
                    "{triplet}-gcc",
                    "{triplet}-g++",
                    "make",
                    "cmake",
                ],
                "fallback_prereqs": [
                    "git",
                ],
                "checker": {
                    "type": "custom",
                    "name": "physfs",
                    "fallback": {
                        "type": "github",
                        "user": "criptych",
                        "repo": "physfs",
                        "ignoreReleases": True,
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
                "checker": {
                    "type": "debian",
                    "source": "libphysfs",
                },
                "installer": {
                    "type": "apt",
                    "package": "libphysfs-dev",
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
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "debian",
                    "source": "pkg-config",
                },
                "installer": {
                    "type": "apt",
                    "package": "pkg-config",
                },
            },
        ],
    },
    "portaudio": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
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
                "checker": {
                    "type": "debian",
                    "source": "portaudio19",
                },
                "installer": {
                    "type": "apt",
                    "package": "portaudio19-dev",
                },
            },
        ],
    },
    "pthread-stubs": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "prereqs": [
                    "wget",
                    "{triplet}-gcc",
                    "make",
                ],
                "checker": {
                    "type": "custom",
                    "name": "pthread-stubs",
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
                "checker": {
                    "type": "debian",
                    "source": "pthread-stubs",
                },
                "installer": {
                    "type": "apt",
                    "package": "libpthread-stubs0-dev",
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
                "osVersion": ["any"],
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
        ],
    },
    "python2-pyyaml": {
        "platform": "host",
        "projects": [
            {
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
        ],
    },
    "python3-mako": {
        "platform": "host",
        "projects": [
            {
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
        ],
    },
    "randrproto": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "prereqs": [
                    "wget",
                    "{triplet}-gcc",
                    "make",
                ],
                "checker": {
                    "type": "custom",
                    "name": "randrproto",
                },
                "installer": {
                    "type": "custom",
                    "name": "randrproto",
                },
            },
            {
                "arch": ["any"],
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["musl"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "xorgproto",
                },
                "installer": {
                    "type": "apk",
                    "package": "xorgproto",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["stretch"],
                "abi": ["gnu"],
                "checker": {
                    "type": "debian",
                    "source": "x11proto-randr",
                },
                "installer": {
                    "type": "apt",
                    "package": "x11proto-randr-dev",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["buster", "bullseye", "sid"],
                "abi": ["gnu"],
                "checker": {
                    "type": "debian",
                    "source": "xorgproto",
                },
                "installer": {
                    "type": "apt",
                    "package": "x11proto-randr-dev",
                },
            },
        ],
    },
    "renderproto": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "prereqs": [
                    "wget",
                    "{triplet}-gcc",
                    "make",
                ],
                "checker": {
                    "type": "custom",
                    "name": "renderproto",
                },
                "installer": {
                    "type": "custom",
                    "name": "renderproto",
                },
            },
            {
                "arch": ["any"],
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["musl"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "xorgproto",
                },
                "installer": {
                    "type": "apk",
                    "package": "xorgproto",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["stretch"],
                "abi": ["gnu"],
                "checker": {
                    "type": "debian",
                    "source": "x11proto-render",
                },
                "installer": {
                    "type": "apt",
                    "package": "x11proto-render-dev",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["buster", "bullseye", "sid"],
                "abi": ["gnu"],
                "checker": {
                    "type": "debian",
                    "source": "xorgproto",
                },
                "installer": {
                    "type": "apt",
                    "package": "x11proto-render-dev",
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
        ],
    },
    "saneopt": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
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
    "sdl2": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
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
                "checker": {
                    "type": "debian",
                    "source": "libsdl2",
                },
                "installer": {
                    "type": "apt",
                    "package": "libsdl2-dev",
                },
            },
        ],
    },
    "sdl2_gfx": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
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
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
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
                    "type": "github",
                    "user": "grimfang4",
                    "repo": "sdl-gpu",
                    "ignoreReleases": True,
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
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "custom",
                    "name": "sdl2_image",
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
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "custom",
                    "name": "sdl2_mixer",
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
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "custom",
                    "name": "sdl2_ttf",
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
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
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
                "osVersion": ["any"],
                "abi": ["gnu"],
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
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
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
                "osVersion": ["buster", "bullseye", "sid"],
                "abi": ["any"],
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
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
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
                "osVersion": ["buster", "bullseye", "sid"],
                "abi": ["any"],
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
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
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
                "osVersion": ["buster", "bullseye", "sid"],
                "abi": ["any"],
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
    "tinyfiledialogs": {
        "type": "library",
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "prereqs": [
                    "wget",
                    "{triplet}-gcc",
                ],
                "checker": {
                    "type": "custom",
                    "name": "tinyfiledialogs",
                },
                "installer": {
                    "type": "custom",
                    "name": "tinyfiledialogs",
                },
            },
        ],
    },
    "unzip": {
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
                    "package": "unzip",
                },
                "installer": {
                    "type": "apk",
                    "package": "unzip",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "debian",
                    "source": "unzip",
                },
                "installer": {
                    "type": "apt",
                    "package": "unzip",
                },
            },
        ],
    },
    "utf": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "prereqs": [
                    "git",
                    "{triplet}-gcc",
                ],
                "checker": {
                    "type": "github",
                    "user": "andlabs",
                    "repo": "utf",
                },
                "installer": {
                    "type": "custom",
                    "name": "utf",
                },
            },
        ],
    },
    "utf8": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "prereqs": [
                    "git",
                    "{triplet}-gcc",
                ],
                "checker": {
                    "type": "github",
                    "user": "haipome",
                    "repo": "utf8",
                },
                "installer": {
                    "type": "custom",
                    "name": "utf8",
                },
            },
        ],
    },
    "wayland-egl-backend": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "prereqs": [
                    "wget",
                    "{triplet}-gcc",
                    "{triplet}-g++",
                    "{triplet}-pkg-config",
                    "make",
                    "libffi",
                    "libxml2",
                ],
                "checker": {
                    "type": "custom",
                    "name": "wayland",
                },
                "installer": {
                    "type": "custom",
                    "name": "wayland",
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
                    "package": "wayland-dev",
                },
                "installer": {
                    "type": "apk",
                    "package": "wayland-dev",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "debian",
                    "source": "wayland",
                },
                "installer": {
                    "type": "apt",
                    "package": "libwayland-egl-backend-dev",
                },
            },
        ],
    },
    "wayland-protocols": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "prereqs": [
                    "wget",
                    "{triplet}-pkg-config",
                    "autoconf",
                    "make",
                    "wayland-scanner",
                ],
                "checker": {
                    "type": "github",
                    "user": "wayland-project",
                    "repo": "wayland-protocols",
                },
                "installer": {
                    "type": "custom",
                    "name": "wayland-protocols",
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
                    "package": "wayland-protocols",
                },
                "installer": {
                    "type": "apk",
                    "package": "wayland-protocols",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "debian",
                    "source": "wayland-protocols",
                },
                "installer": {
                    "type": "apt",
                    "package": "wayland-protocols",
                },
            },
        ],
    },
    "wayland-scanner": {
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
                    "package": "wayland-dev",
                },
                "installer": {
                    "type": "apk",
                    "package": "wayland-dev",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "debian",
                    "source": "wayland",
                },
                "installer": {
                    "type": "apt",
                    "package": ["libwayland-bin", "libwayland-dev"],
                },
            },
        ],
    },
    "wget": {
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
                    "package": "wget",
                },
                "installer": {
                    "type": "pkg-config",
                    "triplet": "x86_64-linux-gnu",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "debian",
                    "source": "wget",
                },
                "installer": {
                    "type": "apt",
                    "package": "wget",
                },
            },
        ],
    },
    "x86_64-linux-gnu-g++": {
        "platform": "host",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "prereqs": [
                    "x86_64-linux-gnu-gcc",
                ],
                "checker": {
                    "type": "gcc-src",
                },
                "installer": {
                    "type": "dummy",
                },
            },
            {
                "arch": ["i686"],
                "os": ["debian"],
                "osVersion": ["buster", "bullseye", "sid"],
                "abi": ["any"],
                "checker": {
                    "type": "debian",
                    "source": "gcc-defaults",
                },
                "installer": {
                    "type": "apt",
                    "package": "g++-x86-64-linux-gnu",
                },
            },
            {
                "arch": ["x86_64"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "debian",
                    "source": "gcc-defaults",
                },
                "installer": {
                    "type": "not_needed",
                },
            },
        ],
    },
    "x86_64-linux-gnu-gcc": {
        "platform": "host",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "prereqs": [
                    "bash",
                    "bison",
                    "bsdtar",
                    "g++",
                    "gawk",
                    "gpg",
                    "make",
                    "makeinfo",
                    "rsync",
                    "wget",
                ],
                "checker": {
                    "type": "gcc-src",
                },
                "installer": {
                    "type": "gcc-src",
                    "languages": "c",
                    "triplet": "x86_64-linux-gnu",
                },
            },
            {
                "arch": ["i686"],
                "os": ["debian"],
                "osVersion": ["buster", "bullseye", "sid"],
                "abi": ["any"],
                "checker": {
                    "type": "debian",
                    "source": "gcc-defaults",
                },
                "installer": {
                    "type": "apt",
                    "package": "gcc-x86-64-linux-gnu",
                },
            },
            {
                "arch": ["x86_64"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "debian",
                    "source": "gcc-defaults",
                },
                "installer": {
                    "type": "not_needed",
                },
            },
        ],
    },
    "x86_64-linux-gnu-pkg-config": {
        "platform": "host",
        "projects": [
            {
                "arch": ["any"],
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "prereqs": [
                    "pkg-config",
                ],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "pkgconf",
                },
                "installer": {
                    "type": "pkg-config",
                    "triplet": "x86_64-linux-gnu",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "prereqs": [
                    "pkg-config",
                ],
                "checker": {
                    "type": "debian",
                    "source": "pkg-config",
                },
                "installer": {
                    "type": "pkg-config",
                    "triplet": "x86_64-linux-gnu",
                },
            },
            {
                "arch": ["x86_64"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "checker": {
                    "type": "debian",
                    "source": "pkg-config",
                },
                "installer": {
                    "type": "apt",
                    "package": "pkg-config",
                },
            },
        ],
    },
    "x86_64-linux-musl-g++": {
        "platform": "host",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "prereqs": [
                    "x86_64-linux-musl-gcc",
                ],
                "checker": {
                    "type": "musl-cross-make",
                },
                "installer": {
                    "type": "dummy",
                },
            },
            {
                "arch": ["x86_64"],
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "g++",
                },
                "installer": {
                    "type": "apk",
                    "package": "g++",
                },
            },
        ],
    },
    "x86_64-linux-musl-gcc": {
        "platform": "host",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "prereqs": [
                    "wget",
                    "bsdtar",
                    "g++",
                    "make",
                ],
                "checker": {
                    "type": "musl-cross-make",
                },
                "installer": {
                    "type": "musl-cross-make",
                    "languages": "c,c++",
                    "triplet": "x86_64-linux-musl",
                },
            },
            {
                "arch": ["x86_64"],
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["any"],
                "prereqs": [
                    "musl",
                ],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "gcc",
                },
                "installer": {
                    "type": "apk",
                    "package": "gcc",
                },
            },
        ],
    },
    "x86_64-linux-musl-pkg-config": {
        "platform": "host",
        "projects": [
            {
                "arch": ["any"],
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["musl"],
                "prereqs": [
                    "pkg-config",
                ],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "pkgconf",
                },
                "installer": {
                    "type": "pkg-config",
                    "triplet": "x86_64-linux-musl",
                },
            },
            {
                "arch": ["x86_64"],
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["musl"],
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
                "osVersion": ["any"],
                "abi": ["musl"],
                "prereqs": [
                    "pkg-config",
                ],
                "checker": {
                    "type": "debian",
                    "source": "pkg-config",
                },
                "installer": {
                    "type": "pkg-config",
                    "triplet": "x86_64-linux-musl",
                },
            },
        ],
    },
    "x86_64-w64-mingw32-g++": {
        "platform": "host",
        "projects": [
            {
                "arch": ["x86_64"],
                "os": ["alpine"],
                "osVersion": ["edge"],
                "abi": ["any"],
                "checker": {
                    "type": "alpine",
                    "repo": "testing",
                    "package": "mingw-w64-gcc",
                },
                "installer": {
                    "type": "apk",
                    "package": "mingw-w64-gcc",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "debian",
                    "source": "gcc-mingw-w64",
                },
                "installer": {
                    "type": "apt",
                    "package": "g++-mingw-w64-x86-64",
                },
            },
        ],
    },
    "x86_64-w64-mingw32-gcc": {
        "platform": "host",
        "projects": [
            {
                "arch": ["x86_64"],
                "os": ["alpine"],
                "osVersion": ["edge"],
                "abi": ["any"],
                "checker": {
                    "type": "alpine",
                    "repo": "testing",
                    "package": "mingw-w64-gcc",
                },
                "installer": {
                    "type": "apk",
                    "package": "mingw-w64-gcc",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "debian",
                    "source": "gcc-mingw-w64",
                },
                "installer": {
                    "type": "apt",
                    "package": "gcc-mingw-w64-x86-64",
                },
            },
        ],
    },
    "xau": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "prereqs": [
                    "wget",
                    "{triplet}-gcc",
                    "make",
                    "{triplet}-pkg-config",
                    "xproto"
                ],
                "checker": {
                    "type": "custom",
                    "name": "xau",
                },
                "installer": {
                    "type": "custom",
                    "name": "xau",
                },
            },
            {
                "arch": ["any"],
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["musl"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "libxau-dev",
                },
                "installer": {
                    "type": "apk",
                    "package": "libxau-dev",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "checker": {
                    "type": "debian",
                    "source": "libxau",
                },
                "installer": {
                    "type": "apt",
                    "package": "libxau-dev",
                },
            },
        ],
    },
    "xcb": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "prereqs": [
                    "wget",
                    "{triplet}-gcc",
                    "make",
                    "{triplet}-pkg-config",
                    "xcb-proto",
                    "pthread-stubs",
                    "xau",
                ],
                "checker": {
                    "type": "custom",
                    "name": "xcb",
                },
                "installer": {
                    "type": "custom",
                    "name": "xcb",
                },
            },
            {
                "arch": ["any"],
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["musl"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "libxcb-dev",
                },
                "installer": {
                    "type": "apk",
                    "package": "libxcb-dev",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "checker": {
                    "type": "debian",
                    "source": "libx11",
                },
                "installer": {
                    "type": "apt",
                    "package": "libx11-xcb-dev",
                },
            },
        ],
    },
    "xcb-proto": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "prereqs": [
                    "wget",
                    "make",
                ],
                "checker": {
                    "type": "custom",
                    "name": "xcb-proto",
                },
                "installer": {
                    "type": "custom",
                    "name": "xcb-proto",
                },
            },
            {
                "arch": ["any"],
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["musl"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "xcb-proto",
                },
                "installer": {
                    "type": "apk",
                    "package": "xcb-proto",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "checker": {
                    "type": "debian",
                    "source": "xcb-proto",
                },
                "installer": {
                    "type": "apt",
                    "package": "xcb-proto",
                },
            },
        ],
    },
    "xdamage": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "prereqs": [
                    "wget",
                    "make",
                    "{triplet}-gcc",
                    "{triplet}-pkg-config",
                    "xorg-macros",
                    "damageproto",
                    "libxfixes",
                    "fixesproto",
                    "xextproto",
                    "xlib",
                ],
                "checker": {
                    "type": "custom",
                    "name": "xdamage",
                },
                "installer": {
                    "type": "custom",
                    "name": "xdamage",
                },
            },
            {
                "arch": ["any"],
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["musl"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "libxdamage-dev",
                },
                "installer": {
                    "type": "apk",
                    "package": "libxdamage-dev",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "checker": {
                    "type": "debian",
                    "source": "libxdamage",
                },
                "installer": {
                    "type": "apt",
                    "package": "libxdamage-dev",
                },
            },
        ],
    },
    "xextproto": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "prereqs": [
                    "wget",
                    "{triplet}-gcc",
                    "make",
                ],
                "checker": {
                    "type": "custom",
                    "name": "xextproto",
                },
                "installer": {
                    "type": "custom",
                    "name": "xextproto",
                },
            },
            {
                "arch": ["any"],
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["musl"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "xorgproto",
                },
                "installer": {
                    "type": "apk",
                    "package": "xorgproto",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "checker": {
                    "type": "debian",
                    "source": "x11proto-xext",
                },
                "installer": {
                    "type": "apt",
                    "package": "x11proto-xext-dev",
                },
            },
        ],
    },
    "xf86vidmodeproto": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "prereqs": [
                    "wget",
                    "{triplet}-gcc",
                    "make",
                ],
                "checker": {
                    "type": "custom",
                    "name": "xf86vidmodeproto",
                },
                "installer": {
                    "type": "custom",
                    "name": "xf86vidmodeproto",
                },
            },
            {
                "arch": ["any"],
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["musl"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "xorgproto",
                },
                "installer": {
                    "type": "apk",
                    "package": "xorgproto",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["stretch"],
                "abi": ["gnu"],
                "checker": {
                    "type": "debian",
                    "source": "x11proto-xf86vidmode",
                },
                "installer": {
                    "type": "apt",
                    "package": "x11proto-xf86vidmode-dev",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["buster", "bullseye", "sid"],
                "abi": ["gnu"],
                "checker": {
                    "type": "debian",
                    "source": "xorgproto",
                },
                "installer": {
                    "type": "apt",
                    "package": "x11proto-xf86vidmode-dev",
                },
            },
        ],
    },
    "xlib": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "prereqs": [
                    "wget",
                    "{triplet}-gcc",
                    "make",
                    "{triplet}-pkg-config",
                    "xproto",
                    "xextproto",
                    "xtrans",
                    "xcb",
                    "kbproto",
                    "inputproto",
                ],
                "checker": {
                    "type": "custom",
                    "name": "xlib",
                },
                "installer": {
                    "type": "custom",
                    "name": "xlib",
                },
            },
            {
                "arch": ["any"],
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["musl"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "libx11-dev",
                },
                "installer": {
                    "type": "apk",
                    "package": "libx11-dev",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "checker": {
                    "type": "debian",
                    "source": "libx11",
                },
                "installer": {
                    "type": "apt",
                    "package": "libx11-dev",
                },
            },
        ],
    },
    "xorg-macros": {
        "platform": "host",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "prereqs": [
                    "wget",
                    "autoconf",
                    "make",
                ],
                "checker": {
                    "type": "github",
                    "user": "freedesktop",
                    "repo": "xorg-macros",
                },
                "installer": {
                    "type": "custom",
                    "name": "xorg-macros",
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
                    "package": "util-macros",
                },
                "installer": {
                    "type": "apk",
                    "package": "util-macros",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "debian",
                    "source": "xutils-dev",
                },
                "installer": {
                    "type": "apt",
                    "package": "xutils-dev",
                },
            },
        ],
    },
    "xproto": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "prereqs": [
                    "wget",
                    "{triplet}-gcc",
                    "make",
                ],
                "checker": {
                    "type": "custom",
                    "name": "xproto",
                },
                "installer": {
                    "type": "custom",
                    "name": "xproto",
                },
            },
            {
                "arch": ["any"],
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["musl"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "xorgproto",
                },
                "installer": {
                    "type": "apk",
                    "package": "xorgproto",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "checker": {
                    "type": "debian",
                    "source": "xorgproto",
                },
                "installer": {
                    "type": "apt",
                    "package": "x11proto-dev",
                },
            },
        ],
    },
    "xrender": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "prereqs": [
                    "wget",
                    "autoconf",
                    "libtool",
                    "{triplet}-gcc",
                    "{triplet}-pkg-config",
                    "make",
                    "xorg-macros",
                    "xlib",
                    "renderproto",
                ],
                "checker": {
                    "type": "github",
                    "user": "freedesktop",
                    "repo": "xorg-libXrender",
                    "ignoredTags": [
                        "xo-6_7_0",
                        "xf86-012804-2330",
                        "xf86-4_4_99_1",
                        "xf86-4_4_0",
                        "xf86-4_3_99_903",
                        "xf86-4_3_99_903_special",
                        "xf86-4_3_99_902",
                        "xf86-4_3_99_901",
                        "xf86-4_3_99_16",
                        "xf86-4_3_0_1",
                        "sco_port_update-base",
                        "rel-0-6-1",
                    ],
                },
                "installer": {
                    "type": "custom",
                    "name": "xrender",
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
                    "package": "libxrender-dev",
                },
                "installer": {
                    "type": "apk",
                    "package": "libxrender-dev",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "debian",
                    "source": "libxrender",
                },
                "installer": {
                    "type": "apt",
                    "package": "libxrender-dev",
                },
            },
        ],
    },
    "xshmfence": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "prereqs": [
                    "wget",
                    "{triplet}-gcc",
                    "{triplet}-pkg-config",
                    "make",
                    "xorg-macros",
                    "xproto",
                ],
                "checker": {
                    "type": "custom",
                    "name": "xshmfence",
                },
                "installer": {
                    "type": "custom",
                    "name": "xshmfence",
                },
            },
            {
                "arch": ["any"],
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["musl"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "libxshmfence-dev",
                },
                "installer": {
                    "type": "apk",
                    "package": "libxshmfence-dev",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "checker": {
                    "type": "debian",
                    "source": "libxshmfence",
                },
                "installer": {
                    "type": "apt",
                    "package": "libxshmfence-dev",
                },
            },
        ],
    },
    "xtrans": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "prereqs": [
                    "wget",
                    "{triplet}-gcc",
                    "make",
                ],
                "checker": {
                    "type": "custom",
                    "name": "xtrans",
                },
                "installer": {
                    "type": "custom",
                    "name": "xtrans",
                },
            },
            {
                "arch": ["any"],
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["musl"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "xtrans",
                },
                "installer": {
                    "type": "apk",
                    "package": "xtrans",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "checker": {
                    "type": "debian",
                    "source": "xtrans",
                },
                "installer": {
                    "type": "apt",
                    "package": "xtrans-dev",
                },
            },
        ],
    },
    "zlib": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "prereqs": [
                    "wget",
                    "{triplet}-gcc",
                    "make",
                ],
                "checker": {
                    "type": "custom",
                    "name": "zlib",
                },
                "installer": {
                    "type": "custom",
                    "name": "zlib",
                },
            },
            {
                "arch": ["any"],
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["musl"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "zlib-dev",
                },
                "installer": {
                    "type": "apk",
                    "package": "zlib-dev",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "checker": {
                    "type": "debian",
                    "source": "zlib",
                },
                "installer": {
                    "type": "apt",
                    "package": "zlib1g-dev",
                },
            },
        ],
    },
}

class SoftwareData:
    def __init__(self, customData = {}):
        self.data = {**data, **customData}

    def AddData(self, customData):
        self.data = {**self.data, **customData}

    def GetData(self):
        return self.data
