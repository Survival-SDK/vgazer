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
                    "type": "custom",
                    "name": "alsa-lib",
                },
                "installer": {
                    "type": "custom",
                    "name": "alsa-lib",
                },
            },
            {
                "arch": ["any"],
                "os": ["alpine"],
                "osVersion": ["any"],
                "abi": ["musl"],
                "license": ["lgpl-2.1"],
                "checker": {
                    "type": "alpine",
                    "repo": "main",
                    "package": "alsa-lib-dev",
                },
                "installer": {
                    "type": "apk",
                    "package": "alsa-lib-dev",
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
                    "type": "custom",
                    "name": "automake",
                },
                "installer": {
                    "type": "custom",
                    "name": "automake",
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
    "automake1.11": {
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
            {
                "arch": ["any"],
                "os": ["steamrt"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "launchpad",
                    "distribution": "precise",
                    "source": "gettext",
                },
                "installer": {
                    "type": "not_needed",
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
            {
                "arch": ["any"],
                "os": ["steamrt"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "launchpad",
                    "distribution": "precise",
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
            {
                "arch": ["any"],
                "os": ["steamrt"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "launchpad",
                    "distribution": "precise",
                    "source": "bison",
                },
                "installer": {
                    "type": "not_needed",
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
            {
                "arch": ["any"],
                "os": ["steamrt"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "launchpad",
                    "distribution": "precise",
                    "source": "libarchive",
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
                "fallback_prereqs": [
                    "git",
                ],
                "checker": {
                    "type": "github",
                    "user": "Malvineous",
                    "repo": "cfgpath",
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
                    "type": "custom",
                    "name": "cmake",
                },
                "installer": {
                    "type": "custom",
                    "name": "cmake",
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
                "prereqs": [
                    "git",
                ],
                "checker": {
                    "type": "github",
                    "user": "edomin",
                    "repo": "cmake_barebones",
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
                "license": ["apache-2.0"],
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
                    "type": "custom",
                    "name": "codecoverage",
                },
                "installer": {
                    "type": "custom",
                    "name": "codecoverage",
                },
            },
        ],
    },
    "crc32c-hw": {
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
                ],
                "checker": {
                    "type": "github",
                    "user": "robertvazan",
                    "repo": "crc32c-hw",
                },
                "installer": {
                    "type": "custom",
                    "name": "crc32c-hw",
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
    "duktape": {
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
                "license": ["mit"],
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
            {
                "arch": ["any"],
                "os": ["steamrt"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "launchpad",
                    "distribution": "precise",
                    "source": "file",
                },
                "installer": {
                    "type": "not_needed",
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
            {
                "arch": ["any"],
                "os": ["steamrt"],
                "osVersion": ["any"],
                "abi": ["any"],
                "checker": {
                    "type": "launchpad",
                    "distribution": "precise",
                    "source": "flex",
                },
                "installer": {
                    "type": "not_needed",
                },
            },
        ],
    },
    "fnv_hash": {
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

                ],
                "checker": {
                    "type": "github",
                    "user": "anholt",
                    "repo": "hash_table",
                },
                "installer": {
                    "type": "custom",
                    "name": "fnv_hash",
                },
            },
        ],
    },
    # TODO(edomin): Add custom checker
    "freebsd-queue": {
        "platform": "target",
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
                    "type": "github",
                    "user": "opensource-mirrors",
                    "repo": "freebsd-queue",
                },
                "installer": {
                    "type": "custom",
                    "name": "freebsd-queue",
                },
            },
        ],
    },
    "freetype": {
        "platform": "target",
        "projects": [
            {
                "fallback": True,
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "license": ["ftl", "mit"],
                "prereqs": [
                    "wget",
                    "{triplet}-gcc",
                    "{triplet}-pkg-config",
                    "make",
                    "zlib",
                    "libbzip2",
                    "libpng",
                ],
                # Building SDL2_ttf with harfbuzzed Freetype have some issues
                # "postreqsOnce": [
                #     "harfbuzz",
                # ],
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
                "license": ["ftl", "mit"],
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
                "osVersion": ["stretch", "buster"],
                "abi": ["gnu"],
                "license": ["ftl", "mit"],
                "checker": {
                    "type": "debian",
                    "source": "freetype",
                },
                "installer": {
                    "type": "apt",
                    "package": "libfreetype6-dev",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["bullseye", "bookworm"],
                "abi": ["gnu"],
                "license": ["ftl", "mit"],
                "checker": {
                    "type": "debian",
                    "source": "freetype",
                },
                "installer": {
                    "type": "apt",
                    "package": "libfreetype-dev",
                },
            },
            {
                "arch": ["any"],
                "os": ["steamrt"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "license": ["ftl", "mit"],
                "checker": {
                    "type": "launchpad",
                    "distribution": "precise",
                    "source": "freetype",
                },
                "installer": {
                    "type": "not_needed",
                },
            },
        ],
    },
}
