data = {
    "alsa-lib": {
        "platform": "target",
        "projects": [
            {
                "fallback": True,
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "license": ["lgpl-2.1"],
                "changelog": "https://www.alsa-project.org/wiki/Main_Page_News",
                "prereqs": [
                    "{triplet}-gcc",
                    "automake",
                    "libtool",
                    "make",
                ],
                "checker": {
                    "type": "git",
                    "url": "https://github.com/alsa-project/alsa-lib.git",
                    "hint": r'v1\.2\.\d\d',
                },
                "installer": {
                    "type": "custom",
                    "name": "alsa-lib",
                },
            },
            {
                "arch": ["any"],
                "os": ["archlinux"],
                "osVersion": ["latest"],
                "abi": ["gnu"],
                "license": ["lgpl-2.1"],
                "changelog": "https://www.alsa-project.org/wiki/Main_Page_News",
                "checker": {
                    "type": "pacman",
                    "package": "alsa-lib",
                },
                "installer": {
                    "type": "pacman",
                    "package": "alsa-lib",
                },
            },
            {
                "arch": ["any"],
                "os": ["steamrt"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "license": ["lgpl-2.1"],
                "changelog": "https://www.alsa-project.org/wiki/Main_Page_News",
                "checker": {
                    "type": "apt-cache",
                    "package": "libasound2-dev",
                },
                "installer": {
                    "type": "not-needed",
                },
            },
        ],
    },
    "autoconf": {
        "platform": "host",
        "projects": [
            {
                "fallback": True,
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "changelog": "https://fossies.org/linux/autoconf/NEWS",
                "prereqs": [
                    "m4",
                    "make",
                    "wget",
                ],
                # Using custom checker and installer because we dont have
                # automake for generating .configure when building autoconf
                # from git source
                "checker": {
                    "type": "custom",
                    "name": "autoconf",
                },
                "installer": {
                    "type": "custom",
                    "name": "autoconf",
                },
            },
            {
                "arch": ["any"],
                "os": ["archlinux"],
                "osVersion": ["latest"],
                "abi": ["any"],
                "changelog": "https://fossies.org/linux/autoconf/NEWS",
                "checker": {
                    "type": "pacman",
                    "package": "autoconf",
                },
                "installer": {
                    "type": "pacman",
                    "package": "autoconf",
                },
            },
            {
                "arch": ["any"],
                "os": ["oraclelinux"],
                "osVersion": ["7"],
                "abi": ["any"],
                "changelog": "https://fossies.org/linux/autoconf/NEWS",
                "prereqs": [
                    "m4",
                    "make",
                    "perl-data-dumper",
                    "wget",
                ],
                "checker": {
                    "type": "custom",
                    "name": "autoconf",
                },
                "installer": {
                    "type": "custom",
                    "name": "autoconf",
                },
            },
            {
                "arch": ["any"],
                "os": ["steamrt"],
                "osVersion": ["any"],
                "abi": ["any"],
                "changelog": "https://fossies.org/linux/autoconf/NEWS",
                "checker": {
                    "type": "apt-cache",
                    "package": "autoconf",
                },
                "installer": {
                    "type": "not-needed",
                },
            },
        ],
    },
    "automake": {
        "platform": "host",
        "projects": [
            {
                "fallback": True,
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "changelog": "https://fossies.org/linux/automake/NEWS",
                "prereqs": [
                    "autoconf",
                    "gcc",
                    "make",
                ],
                "checker": {
                    "type": "git",
                    "url": "https://git.savannah.gnu.org/git/automake.git",
                    "hint": r'v\d\.\d+\w?(\.\d+)?$',
                },
                "installer": {
                    "type": "custom",
                    "name": "automake",
                },
            },
            {
                "arch": ["any"],
                "os": ["archlinux"],
                "osVersion": ["latest"],
                "abi": ["any"],
                "changelog": "https://fossies.org/linux/automake/NEWS",
                "checker": {
                    "type": "pacman",
                    "package": "automake",
                },
                "installer": {
                    "type": "pacman",
                    "package": "automake",
                },
            },
            {
                "arch": ["any"],
                "os": ["oraclelinux"],
                # autoconf >=2.70 required for building xlib
                # Oracle Linux 7 has only 2.69
                # automake depends on autoconf
                "osVersion": ["7"],
                "abi": ["any"],
                "changelog": "https://fossies.org/linux/automake/NEWS",
                "prereqs": [
                    "autoconf",
                    "gcc",
                    "make",
                    "perl-thread-queue",
                ],
                "checker": {
                    "type": "git",
                    "url": "https://git.savannah.gnu.org/git/automake.git",
                    "hint": r'v\d\.\d+\w?(\.\d+)?$',
                },
                "installer": {
                    "type": "custom",
                    "name": "automake",
                },
            },
            {
                "arch": ["any"],
                "os": ["steamrt"],
                "osVersion": ["any"],
                "abi": ["any"],
                "changelog": "https://fossies.org/linux/automake/NEWS",
                "checker": {
                    "type": "apt-cache",
                    "package": "automake",
                },
                "installer": {
                    "type": "not-needed",
                },
            },
        ],
    },
    "autopoint": {
        "platform": "host",
        "projects": [
            {
                "arch": ["any"],
                "os": ["archlinux"],
                "osVersion": ["latest"],
                "abi": ["any"],
                "changelog": "https://fossies.org/linux/gettext/ChangeLog",
                "checker": {
                    "type": "pacman",
                    "package": "gettext",
                },
                "installer": {
                    "type": "pacman",
                    "package": "gettext",
                },
            },
            {
                "arch": ["any"],
                "os": ["oraclelinux"],
                "osVersion": ["7"],
                "abi": ["any"],
                "changelog": "https://fossies.org/linux/gettext/ChangeLog",
                "checker": {
                    "type": "yum",
                    "package": "gettext-devel",
                },
                "installer": {
                    "type": "yum",
                    "package": "gettext-devel",
                },
            },
            # Temporary stub
            {
                "arch": ["any"],
                "os": ["steamrt"],
                "osVersion": ["any"],
                "abi": ["any"],
                "changelog": "https://fossies.org/linux/gettext/ChangeLog",
                "checker": {
                    "type": "apt-cache",
                    "package": "autopoint",
                },
                "installer": {
                    "type": "not-needed",
                },
            },
        ],
    },
    "cfgpath": {
        "platform": "target",
        "projects": [
            {
                "fallback": True,
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "license": ["unlicense"],
                "changelog": "https://github.com/Malvineous/cfgpath/commits/master/",
                "checker": {
                    "type": "git",
                    "url": "https://github.com/Malvineous/cfgpath.git",
                },
                "installer": {
                    "type": "custom",
                    "name": "cfgpath",
                },
            },
        ],
    },
    "cjson": {
        "platform": "target",
        "projects": [
            {
                "fallback": True,
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "license": ["mit"],
                "changelog": "https://github.com/DaveGamble/cJSON/blob/master/CHANGELOG.md",
                "prereqs": [
                    "{triplet}-gcc",
                    "make",
                    "cmake",
                ],
                "checker": {
                    "type": "git",
                    "url": "https://github.com/DaveGamble/cJSON.git",
                    "hint": r'v1\.7\.\d\d',
                },
                "installer": {
                    "type": "custom",
                    "name": "cjson",
                },
            },
            {
                "arch": ["any"],
                "os": ["archlinux"],
                "osVersion": ["latest"],
                "abi": ["gnu"],
                "license": ["mit"],
                "changelog": "https://github.com/DaveGamble/cJSON/blob/master/CHANGELOG.md",
                "checker": {
                    "type": "pacman",
                    "package": "cjson",
                },
                "installer": {
                    "type": "pacman",
                    "package": "cjson",
                },
            },
            {
                "arch": ["any"],
                "os": ["steamrt"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "license": ["mit"],
                "changelog": "https://github.com/DaveGamble/cJSON/blob/master/CHANGELOG.md",
                "checker": {
                    "type": "apt-cache",
                    "package": "libcjson-dev",
                },
                "installer": {
                    "type": "not-needed",
                },
            },
        ],
    },
    "clang": {
        "platform": "host",
        "projects": [
            {
                "arch": ["any"],
                "os": ["archlinux"],
                "osVersion": ["any"],
                "abi": ["any"],
                "changelog": "https://clang.llvm.org/extra/ReleaseNotes.html#what-s-new-in-extra-clang-tools-release",
                "checker": {
                    "type": "pacman",
                    "package": "clang",
                },
                "installer": {
                    "type": "pacman",
                    "package": "clang",
                },
            },
        ],
    },
    "clang-tidy": {
        "platform": "host",
        "projects": [
            {
                "arch": ["any"],
                "os": ["archlinux"],
                "osVersion": ["any"],
                "abi": ["any"],
                "changelog": "https://clang.llvm.org/extra/ReleaseNotes.html#improvements-to-clang-tidy",
                "prereqs": ["clang"],
                "checker": {
                    "type": "pacman",
                    "package": "clang",
                },
                "installer": {
                    "type": "not-needed",
                },
            },
        ],
    },
    "cmake": {
        "platform": "host",
        "projects": [
            {
                "fallback": True,
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "changelog": "https://cmake.org/cmake/help/latest/release/index.html",
                "prereqs": [
                    "g++",
                    "make",
                ],
                "checker": {
                    "type": "git",
                    "url": "https://gitlab.kitware.com/cmake/cmake.git",
                    "hint": r'v3\.\d\d\.\d+',
                },
                "installer": {
                    "type": "custom",
                    "name": "cmake",
                },
            },
            {
                "arch": ["any"],
                "os": ["archlinux"],
                "osVersion": ["latest"],
                "abi": ["any"],
                "changelog": "https://cmake.org/cmake/help/latest/release/index.html",
                "checker": {
                    "type": "pacman",
                    "package": "cmake",
                },
                "installer": {
                    "type": "pacman",
                    "package": "cmake",
                },
            },
            {
                "arch": ["any"],
                "os": ["steamrt"],
                "osVersion": ["any"],
                "abi": ["any"],
                "changelog": "https://cmake.org/cmake/help/latest/release/index.html",
                "checker": {
                    "type": "apt-cache",
                    "package": "cmake",
                },
                "installer": {
                    "type": "not-needed",
                },
            },
        ],
    },
    "cmake_barebones": {
        "platform": "host",
        "projects": [
            {
                "fallback": True,
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "license": ["cc0"],
                "changelog": "https://github.com/edomin/cmake_barebones/commits/main/",
                "checker": {
                    "type": "git",
                    "url": "https://github.com/edomin/cmake_barebones.git"
                },
                "installer": {
                    "type": "custom",
                    "name": "cmake_barebones",
                },
            },
        ],
    },
    "cmocka": {
        "platform": "target",
        "projects": [
            {
                "fallback": True,
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "license": ["apache-2.0"],
                "changelog": "https://cmocka.org/#news",
                "prereqs": [
                    "{triplet}-gcc",
                    "make",
                    "cmake",
                ],
                "checker": {
                    "type": "git",
                    "url": "https://git.cryptomilk.org/projects/cmocka.git",
                },
                "installer": {
                    "type": "custom",
                    "name": "cmocka",
                },
            },
            {
                "arch": ["any"],
                "os": ["archlinux"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "license": ["apache-2.0"],
                "changelog": "https://cmocka.org/#news",
                "checker": {
                    "type": "pacman",
                    "package": "cmocka",
                },
                "installer": {
                    "type": "pacman",
                    "package": "cmocka",
                },
            },
        ],
    },
    "codecoverage": {
        "platform": "host",
        "projects": [
            {
                "fallback": True,
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "license": ["bsd-3"],
                "changelog": "https://github.com/bilke/cmake-modules/blob/master/CodeCoverage.cmake#L29",
                "checker": {
                    "type": "git",
                    "url": "https://github.com/bilke/cmake-modules.git",
                    "files": ["CodeCoverage.cmake"],
                    "hint": r'\d{4}-\d{2}-\d{2}',
                },
                "installer": {
                    "type": "custom",
                    "name": "codecoverage",
                },
            },
        ],
    },
    "dr_wav": {
        "platform": "target",
        "projects": [
            {
                "fallback": True,
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "license": ["unlicense"],
                "changelog": "https://github.com/mackron/dr_libs/blob/master/dr_wav.h#L8351",
                "checker": {
                    "type": "git",
                    "url": "https://github.com/mackron/dr_libs.git",
                    "files": ["dr_wav.h"],
                    "hint": r'v\d\.\d+\.\d+',
                },
                "installer": {
                    "type": "custom",
                    "name": "dr_wav",
                },
            },
        ],
    },
    "expat": {
        "platform": "target",
        "projects": [
            {
                "fallback": True,
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "license": ["mit"],
                "changelog": "https://github.com/libexpat/libexpat/blob/master/expat/Changes",
                "prereqs": [
                    "{triplet}-g++",
                    "{triplet}-gcc",
                    "autoconf",
                    "automake",
                    "libtool",
                    "make",
                ],
                "checker": {
                    "type": "git",
                    "url": "https://github.com/libexpat/libexpat.git",
                    "hint": r'R_\d_\d_\d',
                },
                "installer": {
                    "type": "custom",
                    "name": "expat",
                },
            },
        ],
    },
}
