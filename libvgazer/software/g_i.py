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
            {
                "arch": ["any"],
                "os": ["steamrt"],
                "osVersion": ["any"],
                "abi": ["any"],
                "changelog": "https://gcc.gnu.org/",
                "prereqs": [
                    "gcc",
                ],
                "checker": {
                    "type": "apt-cache",
                    "package": "gcc-12-monolithic",
                },
                "installer": {
                    "type": "cmd",
                    "cmds": [
                        [
                            "update-alternatives", "--install", "/usr/bin/g++",
                            "g++", "/usr/bin/g++-12", "1"
                        ],
                    ],
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
            {
                "arch": ["any"],
                "os": ["steamrt"],
                "osVersion": ["any"],
                "abi": ["any"],
                "changelog": "https://gcc.gnu.org/",
                "checker": {
                    "type": "apt-cache",
                    "package": "gcc-12-monolithic",
                },
                "installer": {
                    "type": "apt",
                    "package": "gcc-12-monolithic",
                    "postInstallCommands": [
                        [
                            "update-alternatives", "--install", "/usr/bin/cpp",
                            "cpp", "/usr/bin/cpp-12", "1"
                        ],
                        [
                            "update-alternatives", "--set", "/usr/bin/cpp",
                            "cpp-bin", "/usr/bin/cpp-12", "1"
                        ],
                        [
                            "update-alternatives", "--install", "/usr/bin/gcc",
                            "gcc", "/usr/bin/gcc-12", "1"
                        ],
                        [
                            "update-alternatives", "--install",
                            "/usr/bin/gcc-ar", "gcc-ar", "/usr/bin/gcc-ar-12",
                            "1"
                        ],
                        [
                            "update-alternatives", "--install",
                            "/usr/bin/gcc-nm", "gcc-nm", "/usr/bin/gcc-nm-12",
                            "1"
                        ],
                        [
                            "update-alternatives", "--install",
                            "/usr/bin/gcc-ranlib", "gcc-ranlib",
                            "/usr/bin/gcc-ranlib-12", "1"
                        ],
                        [
                            "update-alternatives", "--install",
                            "/usr/bin/gcov", "gcov", "/usr/bin/gcov-12", "1"
                        ]
                    ],
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
                "os": ["archlinux"],
                "osVersion": ["latest"],
                "abi": ["gnu"],
                "license": ["sgi-b-1.1", "sgi-b-2.0"],
                "changelog": "https://gitlab.freedesktop.org/mesa/glu/-/tags",
                "checker": {
                    "type": "pacman",
                    "package": "glu",
                },
                "installer": {
                    "type": "pacman",
                    "package": "glu",
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
                    "type": "apt-cache",
                    "package": "libglu1-mesa-dev",
                },
                "installer": {
                    "type": "not-needed",
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
            {
                "arch": ["any"],
                "os": ["steamrt"],
                "osVersion": ["any"],
                "abi": ["any"],
                "changelog": "https://savannah.gnu.org/news/?group=coreutils",
                "checker": {
                    "type": "apt-cache",
                    "package": "help2man",
                },
                "installer": {
                    "type": "not-needed",
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
            {
                "arch": ["any"],
                "os": ["steamrt"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "license": ["unicode", "icu", "bsd-3", "naist", "bsd-2"],
                "changelog": "https://github.com/unicode-org/icu/releases",
                "checker": {
                    "type": "apt-cache",
                    "package": "libicu-dev",
                },
                "installer": {
                    "type": "not-needed",
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
            # Temporary stub
            {
                "arch": ["any"],
                "os": ["steamrt"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "license": ["bsd-3"],
                "changelog": "https://github.com/benhoyt/inih/releases",
                "checker": {
                    "type": "apt-cache",
                    "package": "libinih-dev",
                },
                "installer": {
                    "type": "not-needed",
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
        ],
    },
}
