data = {
    "g++": {
        "platform": "host",
        "projects": [
            {
                "arch": ["any"],
                "os": ["archlinux"],
                "osVersion": ["latest"],
                "abi": ["any"],
                "changelog": "https://gcc.gnu.org/",
                "prereqs": ["gcc"],
                "checker": {
                    "type": "pacman",
                    "package": "gcc",
                },
                "installer": {
                    "type": "not-needed",
                },
            },
            {
                "arch": ["any"],
                "os": ["fedora"],
                "osVersion": ["40"],
                "abi": ["any"],
                "changelog": "https://gcc.gnu.org/",
                "checker": {
                    "type": "dnf",
                    "package": "gcc-c++",
                },
                "installer": {
                    "type": "dnf",
                    "package": "gcc-c++",
                },
            },
            {
                "arch": ["any"],
                "os": ["oraclelinux"],
                "osVersion": ["7"],
                "abi": ["any"],
                "changelog": "https://gcc.gnu.org/",
                "checker": {
                    "type": "yum",
                    "package": "gcc-c++",
                },
                "installer": {
                    "type": "yum",
                    "package": "gcc-c++",
                },
            },
        ],
    },
    "gcc": {
        "platform": "host",
        "projects": [
            {
                "arch": ["any"],
                "os": ["archlinux"],
                "osVersion": ["latest"],
                "abi": ["any"],
                "changelog": "https://gcc.gnu.org/",
                "checker": {
                    "type": "pacman",
                    "package": "gcc",
                },
                "installer": {
                    "type": "pacman",
                    "package": "gcc",
                },
            },
            {
                "arch": ["any"],
                "os": ["fedora"],
                "osVersion": ["40"],
                "abi": ["gnu"],
                "changelog": "https://gcc.gnu.org/",
                "checker": {
                    "type": "dnf",
                    "package": "gcc",
                },
                "installer": {
                    "type": "dnf",
                    "package": "gcc",
                },
            },
            {
                "arch": ["any"],
                "os": ["oraclelinux"],
                "osVersion": ["7"],
                "abi": ["gnu"],
                "changelog": "https://gcc.gnu.org/",
                "checker": {
                    "type": "yum",
                    "package": "gcc",
                },
                "installer": {
                    "type": "yum",
                    "package": "gcc",
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
    "help2man": {
        "platform": "host",
        "projects": [
            {
                "arch": ["any"],
                "os": ["archlinux"],
                "osVersion": ["latest"],
                "abi": ["any"],
                "changelog": "https://savannah.gnu.org/news/?group=coreutils",
                "checker": {
                    "type": "pacman",
                    "package": "help2man",
                },
                "installer": {
                    "type": "pacman",
                    "package": "help2man",
                },
            },
            {
                "arch": ["any"],
                "os": ["oraclelinux"],
                "osVersion": ["7"],
                "abi": ["any"],
                "changelog": "https://savannah.gnu.org/news/?group=coreutils",
                "checker": {
                    "type": "yum",
                    "repo": "ol7_optional_latest",
                    "package": "help2man",
                },
                "installer": {
                    "type": "yum",
                    "repo": "ol7_optional_latest",
                    "package": "help2man",
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
                    "{triplet}-gcc",
                    "{triplet}-g++",
                    "g++",
                    "gcc",
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
                "os": ["archlinux"],
                "osVersion": ["latest"],
                "abi": ["gnu"],
                "license": ["unicode", "icu", "bsd-3", "naist", "bsd-2"],
                "changelog": "https://github.com/unicode-org/icu/releases",
                "checker": {
                    "type": "pacman",
                    "package": "icu",
                },
                "installer": {
                    "type": "pacman",
                    "package": "icu",
                },
            },
            {
                "arch": ["any"],
                "os": ["fedora"],
                "osVersion": ["40"],
                "abi": ["gnu"],
                "license": ["unicode", "icu", "bsd-3", "naist", "bsd-2"],
                "changelog": "https://github.com/unicode-org/icu/releases",
                "checker": {
                    "type": "dnf",
                    "package": "libicu-devel",
                },
                "installer": {
                    "type": "dnf",
                    "package": "libicu-devel",
                },
            },
            {
                "fallback": True,
                "arch": ["any"],
                "os": ["oraclelinux"],
                "osVersion": ["7"],
                "abi": ["gnu"],
                "license": ["unicode", "icu", "bsd-3", "naist", "bsd-2"],
                "changelog": "https://github.com/unicode-org/icu/releases",
                "prereqs": [
                    "{triplet}-gcc",
                    "{triplet}-g++",
                    "g++",
                    "gcc",
                    "make",
                ],
                "checker": {
                    "type": "fixed",
                    "version": "67.1",
                },
                "installer": {
                    "type": "custom",
                    "name": "icu-67",
                },
            },
        ],
    },
    "icu-54.2": {
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
                    "{triplet}-gcc",
                    "{triplet}-g++",
                    "g++",
                    "gcc",
                    "make",
                ],
                "checker": {
                    "type": "fixed",
                    "version": "54.2",
                },
                "installer": {
                    "type": "custom",
                    "name": "icu_54_2",
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
                "os": ["archlinux"],
                "osVersion": ["latest"],
                "abi": ["gnu"],
                "license": ["bsd-3"],
                "changelog": "https://github.com/benhoyt/inih/releases",
                "checker": {
                    "type": "pacman",
                    "package": "libinih",
                },
                "installer": {
                    "type": "pacman",
                    "package": "libinih",
                },
            },
            {
                "arch": ["any"],
                "os": ["fedora"],
                "osVersion": ["40"],
                "abi": ["gnu"],
                "license": ["bsd-3"],
                "changelog": "https://github.com/benhoyt/inih/releases",
                "checker": {
                    "type": "dnf",
                    "package": "inih-devel",
                },
                "installer": {
                    "type": "dnf",
                    "package": "inih-devel",
                },
            },
        ],
    },
    "iwyu": {
        "platform": "host",
        "projects": [
            {
                "fallback": True,
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "license": ["bsd-3"],
                "changelog": "https://include-what-you-use.org/",
                "prereqs": [
                    "clang",
                    "cmake",
                    "g++",
                    "llvm",
                    "make",
                ],
                "checker": {
                    "type": "git",
                    "url": "https://github.com/include-what-you-use/include-what-you-use.git",
                    "hint": r'\d.\d+',
                },
                "installer": {
                    "type": "custom",
                    "name": "iwyu",
                },
            },
            {
                "arch": ["any"],
                "os": ["fedora"],
                "osVersion": ["40"],
                "abi": ["any"],
                "license": ["bsd-3"],
                "changelog": "https://include-what-you-use.org/",
                "checker": {
                    "type": "dnf",
                    "package": "iwyu",
                },
                "installer": {
                    "type": "dnf",
                    "package": "iwyu",
                },
            },
        ],
    },
}
