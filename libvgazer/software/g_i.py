data = {
    "g++": {
        "platform": "host",
        "projects": [
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["any"],
                "changelog": "https://gcc.gnu.org/",
                "checker": {
                    "type": "debian",
                    "source": "gcc-defaults",
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
                "changelog": "https://gcc.gnu.org/",
                "checker": {
                    "type": "launchpad",
                    "distribution": "precise",
                    "source": "gcc-4.6",
                },
                "installer": {
                    "type": "not_needed",
                },
            },
        ],
    },
    "gcc": {
        "platform": "host",
        "projects": [
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["any"],
                "changelog": "https://gcc.gnu.org/",
                "checker": {
                    "type": "debian",
                    "source": "gcc-defaults",
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
                "changelog": "https://gcc.gnu.org/",
                "checker": {
                    "type": "launchpad",
                    "distribution": "precise",
                    "source": "gcc-4.6",
                },
                "installer": {
                    "type": "not_needed",
                },
            },
        ],
    },
    "glslangvalidator": {
        "platform": "host",
        "projects": [
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["any"],
                "changelog": "https://github.com/KhronosGroup/glslang/blob/main/CHANGES.md",
                "checker": {
                    "type": "debian",
                    "source": "glslang",
                },
                "installer": {
                    "type": "apt",
                    "package": "glslang-tools",
                },
            },
        ],
    },
    "glu": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["linux"],
                "osVersion": ["any"],
                "abi": ["any"],
                "license": ["sgi-b-1.1", "sgi-b-2.0"],
                "changelog": "https://gitlab.freedesktop.org/mesa/glu/-/tags",
                "prereqs": [
                    "wget",
                    "{triplet}-gcc",
                    "{triplet}-g++",
                    "{triplet}-pkg-config",
                    "meson",
                    "ninja",
                    "opengl",
                ],
                "checker": {
                    "type": "git",
                    "url": "https://gitlab.freedesktop.org/mesa/glu.git",
                },
                "installer": {
                    "type": "custom",
                    "name": "mesa-glu",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "license": ["sgi-b-1.1", "sgi-b-2.0"],
                "changelog": "https://gitlab.freedesktop.org/mesa/glu/-/tags",
                "checker": {
                    "type": "debian",
                    "source": "libglu",
                },
                "installer": {
                    "type": "apt",
                    "package": "libglu1-mesa-dev",
                },
            },
            {
                "arch": ["any"],
                "os": ["steamrt"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "license": ["sgi-b-1.1", "sgi-b-2.0"],
                "changelog": "https://gitlab.freedesktop.org/mesa/glu/-/tags",
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
    "hash_table": {
        "platform": "target",
        "projects": [
            {
                "fallback": True,
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "license": ["mit"],
                "changelog": "https://github.com/anholt/hash_table/commits/master/",
                "prereqs": [
                    "{triplet}-gcc",
                ],
                "checker": {
                    "type": "git",
                    "url": "https://github.com/anholt/hash_table.git",
                    "files": ["meson.build"],
                    "hint": r'\d\.\d',
                },
                "installer": {
                    "type": "custom",
                    "name": "hash_table",
                },
            },
        ],
    },
    "icu": {
        "platform": "target",
        "projects": [
            {
                "fallback": True,
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "license": ["unicode", "icu", "bsd-3", "naist", "bsd-2"],
                "changelog": "https://github.com/unicode-org/icu/releases",
                "prereqs": [
                    "wget",
                    "{hostTriplet}-gcc",
                    "{hostTriplet}-g++",
                    "{triplet}-gcc",
                    "{triplet}-g++",
                    "make",
                ],
                "checker": {
                    "type": "git",
                    "url": "https://github.com/unicode-org/icu.git",
                    "hint": r'release-\d+-\d$',
                },
                "installer": {
                    "type": "custom",
                    "name": "icu",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "license": ["unicode", "icu", "bsd-3", "naist", "bsd-2"],
                "changelog": "https://github.com/unicode-org/icu/releases",
                "checker": {
                    "type": "debian",
                    "source": "icu",
                },
                "installer": {
                    "type": "apt",
                    "package": "libicu-dev",
                },
            },
            {
                "arch": ["any"],
                "os": ["steamrt"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "license": ["unicode", "icu", "bsd-3", "naist", "bsd-2"],
                "changelog": "https://github.com/unicode-org/icu/releases",
                "checker": {
                    "type": "launchpad",
                    "distribution": "precise",
                    "source": "icu",
                },
                "installer": {
                    "type": "not_needed",
                },
            },
        ],
    },
    "inih": {
        "platform": "target",
        "projects": [
            {
                "fallback": True,
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "license": ["bsd-3"],
                "changelog": "https://github.com/benhoyt/inih/releases",
                "prereqs": [
                    "wget",
                    "{triplet}-gcc",
                ],
                "checker": {
                    "type": "git",
                    "url": "https://github.com/benhoyt/inih.git",
                },
                "installer": {
                    "type": "custom",
                    "name": "inih",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["buster", "bullseye", "bookworm", "sid"],
                "abi": ["gnu"],
                "license": ["bsd-3"],
                "changelog": "https://github.com/benhoyt/inih/releases",
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
    "iwyu": {
        "platform": "host",
        "projects": [
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["any"],
                "changelog": "https://include-what-you-use.org/",
                "checker": {
                    "type": "debian",
                    "source": "iwyu",
                },
                "installer": {
                    "type": "apt",
                    "package": "iwyu",
                },
            },
        ],
    },
}
