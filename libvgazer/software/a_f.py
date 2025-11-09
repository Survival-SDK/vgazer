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
            # {
            #     "arch": ["any"],
            #     "os": ["fedora"],
            #     "osVersion": ["40"],
            #     "abi": ["gnu"],
            #     "license": ["lgpl-2.1"],
            #     "changelog": "https://www.alsa-project.org/wiki/Main_Page_News",
            #     "checker": {
            #         "type": "dnf",
            #         "package": "alsa-lib-devel",
            #     },
            #     "installer": {
            #         "type": "dnf",
            #         "package": "alsa-lib-devel",
            #     },
            # },
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
                "os": ["amazonlinux"],
                "osVersion": ["2"],
                "abi": ["any"],
                "changelog": "https://fossies.org/linux/autoconf/NEWS",
                "prereqs": [
                    "m4",
                    "make",
                    "perl-data-dumper",
                    "tar",
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
                "os": ["fedora"],
                "osVersion": ["43"],
                "abi": ["gnu"],
                "changelog": "https://fossies.org/linux/autoconf/NEWS",
                "checker": {
                    "type": "dnf",
                    "package": "autoconf",
                },
                "installer": {
                    "type": "dnf",
                    "package": "autoconf",
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
                "os": ["amazonlinux"],
                # autoconf >=2.70 required for building xlib
                # Amazon Linux 7 has only 2.69
                # automake depends on autoconf
                "osVersion": ["2"],
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
                "os": ["fedora"],
                "osVersion": ["43"],
                "abi": ["gnu"],
                "changelog": "https://fossies.org/linux/automake/NEWS",
                "checker": {
                    "type": "dnf",
                    "package": "automake",
                },
                "installer": {
                    "type": "dnf",
                    "package": "automake",
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
            # {
            #     "arch": ["any"],
            #     "os": ["fedora"],
            #     "osVersion": ["40"],
            #     "abi": ["gnu"],
            #     "license": ["mit"],
            #     "changelog": "https://github.com/DaveGamble/cJSON/blob/master/CHANGELOG.md",
            #     "checker": {
            #         "type": "dnf",
            #         "package": "cjson",
            #     },
            #     "installer": {
            #         "type": "dnf",
            #         "package": "cjson",
            #     },
            # },
        ],
    },
    "clang-tidy": {
        "platform": "host",
        "projects": [
            {
                "arch": ["any"],
                "os": ["fedora"],
                "osVersion": ["43"],
                "abi": ["any"],
                "changelog": "https://clang.llvm.org/extra/ReleaseNotes.html#improvements-to-clang-tidy",
                "checker": {
                    "type": "dnf",
                    "package": "clang-tools-extra",
                },
                "installer": {
                    "type": "dnf",
                    "package": "clang-tools-extra",
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
                "os": ["amazonlinux"],
                "osVersion": ["2"],
                "abi": ["any"],
                "changelog": "https://cmake.org/cmake/help/latest/release/index.html",
                "checker": {
                    "type": "yum",
                    "package": "cmake3",
                },
                "installer": {
                    "type": "yum",
                    "package": "cmake3",
                    "postInstallCommands": [
                        [
                            "ln", "-s", "/usr/bin/cmake3",
                            "/usr/local/bin/cmake"
                        ],
                    ],
                },
            },
            {
                "arch": ["any"],
                "os": ["fedora"],
                "osVersion": ["43"],
                "abi": ["any"],
                "changelog": "https://cmake.org/cmake/help/latest/release/index.html",
                "checker": {
                    "type": "dnf",
                    "package": "cmake",
                },
                "installer": {
                    "type": "dnf",
                    "package": "cmake",
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
                "changelog": "https://github.com/Survival-SDK/cmake_barebones/commits/main/",
                "checker": {
                    "type": "git",
                    "url": "https://github.com/Survival-SDK/cmake_barebones.git"
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
            # {
            #     "arch": ["any"],
            #     "os": ["fedora"],
            #     "osVersion": ["40"],
            #     "abi": ["gnu"],
            #     "license": ["apache-2.0"],
            #     "changelog": "https://cmocka.org/#news",
            #     "checker": {
            #         "type": "dnf",
            #         "package": "libcmocka-devel",
            #     },
            #     "installer": {
            #         "type": "dnf",
            #         "package": "libcmocka-devel",
            #     },
            # },
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
    "cwalk": {
        "platform": "target",
        "projects": [
            {
                "fallback": True,
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "license": ["mit"],
                "changelog": "https://github.com/likle/cwalk/releases",
                "prereqs": [
                    "{triplet}-gcc",
                    "make",
                    "cmake",
                ],
                "checker": {
                    "type": "git",
                    "url": "https://github.com/likle/cwalk",
                },
                "installer": {
                    "type": "custom",
                    "name": "cwalk",
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
            # {
            #     "arch": ["any"],
            #     "os": ["fedora"],
            #     "osVersion": ["40"],
            #     "abi": ["gnu"],
            #     "license": ["unlicense"],
            #     "changelog": "https://github.com/mackron/dr_libs/blob/master/dr_wav.h#L8351",
            #     "checker": {
            #         "type": "dnf",
            #         "package": "dr_wav-devel",
            #     },
            #     "installer": {
            #         "type": "dnf",
            #         "package": "dr_wav-devel",
            #     },
            # },
        ],
    },
}
