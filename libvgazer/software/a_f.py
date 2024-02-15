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
                },
                "installer": {
                    "type": "custom",
                    "name": "alsa-lib",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "license": ["lgpl-2.1"],
                "changelog": "https://www.alsa-project.org/wiki/Main_Page_News",
                "checker": {
                    "type": "apt-cache",
                    "package": "libasound2-dev",
                },
                "installer": {
                    "type": "apt",
                    "package": "libasound2-dev",
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
                "os": ["debian"],
                # autoconf >=2.70 required for building xlib
                # Debian bullseye has only 2.69
                "osVersion": ["bookworm", "trixie", "sid"],
                "abi": ["any"],
                "changelog": "https://fossies.org/linux/autoconf/NEWS",
                "checker": {
                    "type": "apt-cache",
                    "package": "autoconf",
                },
                "installer": {
                    "type": "apt",
                    "package": "autoconf",
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
                "os": ["debian"],
                # autoconf >=2.70 required for building xlib
                # Debian bullseye has only 2.69
                # automake depends on autoconf
                "osVersion": ["bookworm", "trixie", "sid"],
                "abi": ["any"],
                "changelog": "https://fossies.org/linux/automake/NEWS",
                "checker": {
                    "type": "apt-cache",
                    "package": "automake",
                },
                "installer": {
                    "type": "apt",
                    "package": "automake",
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
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["any"],
                "changelog": "https://fossies.org/linux/gettext/ChangeLog",
                "checker": {
                    "type": "apt-cache",
                    "package": "autopoint",
                },
                "installer": {
                    "type": "apt",
                    "package": "autopoint",
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
                },
                "installer": {
                    "type": "custom",
                    "name": "cjson",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "license": ["mit"],
                "changelog": "https://github.com/DaveGamble/cJSON/blob/master/CHANGELOG.md",
                "checker": {
                    "type": "apt-cache",
                    "package": "libcjson-dev",
                },
                "installer": {
                    "type": "apt",
                    "package": "libcjson-dev",
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
    "clang-tidy": {
        "platform": "host",
        "projects": [
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["any"],
                "changelog": "https://clang.llvm.org/extra/ReleaseNotes.html#improvements-to-clang-tidy",
                "checker": {
                    "type": "apt-cache",
                    "package": "clang-tidy",
                },
                "installer": {
                    "type": "apt",
                    "package": "clang-tidy",
                },
            },
        ],
    },
    "cmake": {
        "platform": "host",
        "projects": [
            # This project por that case when we can not install cmake via
            # package manager
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
                },
                "installer": {
                    "type": "custom",
                    "name": "cmake",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["any"],
                "changelog": "https://cmake.org/cmake/help/latest/release/index.html",
                "checker": {
                    "type": "apt-cache",
                    "package": "cmake",
                },
                "installer": {
                    "type": "apt",
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
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "license": ["apache-2.0"],
                "changelog": "https://cmocka.org/#news",
                "checker": {
                    "type": "apt-cache",
                    "package": "libcmocka-dev",
                },
                "installer": {
                    "type": "apt",
                    "package": "libcmocka-dev",
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
}
