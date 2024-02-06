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
                "prereqs": [
                    "wget",
                    "{triplet}-gcc",
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
                "checker": {
                    "type": "debian",
                    "source": "alsa-lib",
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
                "checker": {
                    "type": "launchpad",
                    "distribution": "precise",
                    "source": "alsa-lib",
                },
                "installer": {
                    "type": "not_needed",
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
                "prereqs": [
                    "m4",
                    "make",
                    "wget",
                ],
                "checker": {
                    "type": "git",
                    "url": "git://git.sv.gnu.org/autoconf",
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
                "checker": {
                    "type": "debian",
                    "source": "autoconf",
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
                "checker": {
                    "type": "launchpad",
                    "distribution": "precise",
                    "source": "autoconf",
                },
                "installer": {
                    "type": "not_needed",
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
                "prereqs": [
                    "autoconf",
                    "make",
                    "wget",
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
                "checker": {
                    "type": "debian",
                    "source": "automake-1.16",
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
                "checker": {
                    "type": "launchpad",
                    "distribution": "precise",
                    "source": "automake1.11",
                },
                "installer": {
                    "type": "not_needed",
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
                "prereqs": [
                    "wget",
                ],
                "checker": {
                    "type": "git",
                    "url": "https://github.com/Malvineous/cfgpath.git",
                },
                "installer": {
                    "type": "custom",
                    "name": "cfgpath",
                    "fallback": {
                        "type": "custom",
                        "name": "cfgpath-master",
                    }
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
                "prereqs": [
                    "wget",
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
                "osVersion": ["buster", "bullseye", "bookworm", "sid"],
                "abi": ["gnu"],
                "license": ["mit"],
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
    "clang-tidy": {
        "platform": "host",
        "projects": [
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
                    "package": "clang-tidy",
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
                "prereqs": [
                    "wget",
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
                "checker": {
                    "type": "debian",
                    "source": "cmake",
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
                "checker": {
                    "type": "launchpad",
                    "distribution": "precise",
                    "source": "cmake",
                },
                "installer": {
                    "type": "not_needed",
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
                "prereqs": [
                    "wget",
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
                "prereqs": [
                    "wget",
                ],
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
                "prereqs": [
                    "wget",
                ],
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
