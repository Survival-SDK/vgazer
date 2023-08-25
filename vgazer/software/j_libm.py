data = {
    # IJG-JPEG under IJG Licence
    # libjpeg-turbo under IJG, BSD-3-clause and Zlib
    "jpeg": {
        "platform": "target",
        "projects": [
            {
                "fallback": True,
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "license": ["ijg"], # IJG-JPEG
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
                "license": ["ijg"], # IJG-JPEG
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
                "license": ["ijg", "bsd-3", "zlib"], # libjpeg-turbo
                "checker": {
                    "type": "debian",
                    "source": "libjpeg-turbo",
                },
                "installer": {
                    "type": "apt",
                    "package": "libjpeg-dev",
                },
            },
            {
                "arch": ["any"],
                "os": ["steamrt"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "license": ["ijg", "bsd-3", "zlib"], # libjpeg-turbo
                "checker": {
                    "type": "launchpad",
                    "distribution": "precise",
                    "source": "libjpeg-turbo",
                },
                "installer": {
                    "type": "not_needed",
                },
            },
        ],
    },
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
    "kvec": {
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
                    "name": "kvec",
                    "fallback": {
                        "type": "custom",
                        "name": "kvec-master",
                    }
                },
            },
        ],
    },
    # TODO
    "lazy-winapi.c": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["windows"],
                "osVersion": ["any"],
                "abi": ["any"],
                "license": ["mit"],
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
    # Original libbsd have some parts of code with BSD-4-clause license which
    # not suitable for this project
    "libbsd": {
        "platform": "target",
        "projects": [
            {
                "fallback": True,
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "license": ["bsd-2", "bsd-3", "isc"],
                "prereqs": [
                    "git",
                    "{triplet}-gcc",
                    "make",
                    "autoconf",
                    "automake",
                    "libtool",
                ],
                "checker": {
                    "type": "github",
                    "user": "AltSysrq",
                    "repo": "libbsd-minimal",
                },
                "installer": {
                    "type": "custom",
                    "name": "libbsd-minimal",
                },
            },
            {
                "arch": ["any"],
                "os": ["debian"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "license": ["beerware", "bsd-2", "bsd-3", "isc", "mit"],
                "checker": {
                    "type": "debian",
                    "source": "libbsd",
                },
                "installer": {
                    "type": "apt",
                    "package": "libbsd-dev",
                },
            },
        ],
    },
    "libbzip2": {
        "platform": "target",
        "projects": [
            {
                "fallback": True,
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "license": ["bzip2-1.0.6"],
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
                "license": ["bzip2-1.0.6"],
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
                "license": ["bzip2-1.0.6"],
                "checker": {
                    "type": "debian",
                    "source": "bzip2",
                },
                "installer": {
                    "type": "apt",
                    "package": "libbz2-dev",
                },
            },
            {
                "arch": ["any"],
                "os": ["steamrt"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "license": ["bzip2-1.0.6"],
                "checker": {
                    "type": "launchpad",
                    "distribution": "precise",
                    "source": "bzip2",
                },
                "installer": {
                    "type": "not_needed",
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
    "libelf": {
        "platform": "target",
        "projects": [
            {
                "fallback": True,
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "license": ["lgpl-3"],
                "prereqs": [
                    "{triplet}-gcc",
                    "{triplet}-pkg-config",
                    "make",
                    "wget",
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
                "license": ["lgpl-3"],
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
                "license": ["lgpl-3"],
                "checker": {
                    "type": "debian",
                    "source": "elfutils",
                },
                "installer": {
                    "type": "apt",
                    "package": "libelf-dev",
                },
            },
            {
                "arch": ["any"],
                "os": ["steamrt"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "license": ["lgpl-3"],
                "checker": {
                    "type": "launchpad",
                    "distribution": "precise",
                    "source": "libelf",
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
    "libflac": {
        "platform": "target",
        "projects": [
            {
                "arch": ["i686"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "license": ["bsd-3"],
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
                "license": ["bsd-3"],
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
                "license": ["bsd-3"],
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
                "license": ["bsd-3"],
                "checker": {
                    "type": "debian",
                    "source": "flac",
                },
                "installer": {
                    "type": "apt",
                    "package": "libflac-dev",
                },
            },
            {
                "arch": ["any"],
                "os": ["steamrt"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "license": ["bsd-3"],
                "checker": {
                    "type": "launchpad",
                    "distribution": "precise",
                    "source": "flac",
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
    "libmodplug": {
        "platform": "target",
        "projects": [
            {
                "fallback": True,
                "arch": ["any"],
                "os": ["any"],
                "osVersion": ["any"],
                "abi": ["any"],
                "license": ["pd"],
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
                "license": ["pd"],
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
                "license": ["pd"],
                "checker": {
                    "type": "debian",
                    "source": "libmodplug",
                },
                "installer": {
                    "type": "apt",
                    "package": "libmodplug-dev",
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
                    "source": "libmodplug",
                },
                "installer": {
                    "type": "not_needed",
                },
            },
        ],
    },
    "libmount": {
        "platform": "target",
        "projects": [
            {
                "arch": ["any"],
                "os": ["linux"],
                "osVersion": ["any"],
                "abi": ["any"],
                "license": ["lgpl-2.1+"],
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
                "license": ["lgpl-2.1+"],
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
                "license": ["lgpl-2.1+"],
                "checker": {
                    "type": "debian",
                    "source": "util-linux",
                },
                "installer": {
                    "type": "apt",
                    "package": "libmount-dev",
                },
            },
            {
                "arch": ["any"],
                "os": ["steamrt"],
                "osVersion": ["any"],
                "abi": ["gnu"],
                "license": ["lgpl-2.1+"],
                "checker": {
                    "type": "launchpad",
                    "distribution": "precise",
                    "source": "util-linux",
                },
                "installer": {
                    "type": "not_needed",
                },
            },
        ],
    },
}
