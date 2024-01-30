data = {
    "ketopt": {
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
                "fallback_prereqs": [
                    "git",
                ],
                "checker": {
                    "type": "github",
                    "user": "attractivechaos",
                    "repo": "klib",
                    "ignoreReleases": True,
                },
                "installer": {
                    "type": "custom",
                    "name": "ketopt",
                    "fallback": {
                        "type": "custom",
                        "name": "ketopt-master",
                    }
                },
            },
        ],
    },
    "libclipboard": {
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
            {
                "arch": ["any"],
                "os": ["windows"],
                "osVersion": ["any"],
                "abi": ["any"],
                "license": ["mit"],
                "prereqs": [
                    "wget",
                    "{triplet}-g++",
                    "make",
                    "{triplet}-pkg-config",
                    "cmake",
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
                "fallback": True,
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "license": ["mit"],
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
                "license": ["mit"],
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
                "license": ["mit"],
                "checker": {
                    "type": "debian",
                    "source": "libdrm",
                },
                "installer": {
                    "type": "apt",
                    "package": "libdrm-dev",
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
                    "source": "libdrm",
                },
                "installer": {
                    "type": "not_needed",
                },
            },
        ],
    },
    "libffi": {
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
                "license": ["mit"],
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
                "license": ["mit"],
                "checker": {
                    "type": "debian",
                    "source": "libffi",
                },
                "installer": {
                    "type": "apt",
                    "package": "libffi-dev",
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
                    "source": "libffi",
                },
                "installer": {
                    "type": "not_needed",
                },
            },
        ],
    },
    "libiconv": {
        "platform": "target",
        # TODO
        "projects": [
            {
                "fallback": True,
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "license": ["lgpl-2"],
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
                "license": ["lgpl-2"],
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
                "license": ["lgpl-2"],
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
                "license": ["lgpl-2"],
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
    # libintl under GNU LGPL 2.1
    # libintl-lite under version 1 of the Boost Software License
    "libintl": {
        "platform": "target",
        # TODO
        "projects": [
            {
                "arch": ["any"],
                "os": ["windows"],
                "osVersion": ["any"],
                "abi": ["any"],
                "license": ["bsl-1.0"],
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
                "license": ["lgpl-2.1"],
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
                "license": ["lgpl-2.1"],
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
                "license": ["pd"],
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
                "license": ["pd"],
                "prereqs": [
                    "wget",
                    "{triplet}-gcc",
                    "make",
                    # "libintl",
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
                "license": ["pd"],
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
                "license": ["pd"],
                "checker": {
                    "type": "debian",
                    "source": "xz-utils",
                },
                "installer": {
                    "type": "apt",
                    "package": "liblzma-dev",
                },
            },
            {
                "arch": ["any"],
                "os": ["steamrt"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "license": ["pd"],
                "checker": {
                    "type": "launchpad",
                    "distribution": "precise",
                    "source": "xz-utils",
                },
                "installer": {
                    "type": "not_needed",
                },
            },
        ],
    },
}
