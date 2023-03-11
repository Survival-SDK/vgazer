data = {
    "apache-2.0": {
        "name": "Apache-2.0",
        "fullName": "Apache License 2.0",
        "rules": {
            "appendNoticeFileIfExists": True,
            "distributeOriginalLicenseText": True,
        }
    },
    "beerware": {
        "name": "Beerware",
        "fullName": "Beerware",
        "rules": {}
    },
    "bsd-1": {
        "name": "BSD 1-clause",
        "fullName": "BSD 1-Clause License",
        "rules": {}
    },
    "bsd-2": {
        "name": "BSD 2-clause",
        "fullName": "Simplified BSD License",
        "rules": {
            "distributeOriginalLicenseText": True,
        }
    },
    "bsd-3": {
        "name": "BSD 3-clause",
        "fullName": "Modified BSD License",
        "rules": {
            "distributeOriginalLicenseText": True,
        }
    },
    "bsl-1.0": {
        "name": "BSD 3-clause",
        "fullName": "Modified BSD License",
        "rules": {}
    },
    "bzip2-1.0.6": {
        "name": "bzip2-1.0.6",
        "fullName": "bzip2 and libbzip2 License v1.0.6",
        "rules": {}
    },
    "cc0": {
        "name": "CC0",
        "fullName": "CC0",
        "rules": {}
    },
    "ftl": {
        "name": "FTL",
        "fullName": "MIT License",
        "rules": {
            "mentionSource": True,
        }
    },
    "gpl-2-lsn": {
        "name": "GPL-2.0 WITH Linux-syscall-note",
        "fullName":
            "GNU General Public License Version 2.0 WITH Linux-syscall-note",
        "rules": {}
    },
    "hpnd": {
        "name": "HPND",
        "fullName": "Historical Permission Notice and Disclaimer",
        "rules": {
            "distributeOriginalLicenseText": True,
        }
    },
    "hpnd-sv": {
        "name": "HPND-sell-variant",
        "fullName":
            "Historical Permission Notice and Disclaimer - sell variant",
        "rules": {
            "distributeOriginalLicenseText": True,
        }
    },
    "icu": {
        "name": "ICU",
        "fullName": "ICU License",
        "rules": {
            "distributeOriginalLicenseText": True,
        }
    },
    "ijg": {
        "name": "IJG",
        "fullName": "Independent JPEG Group License",
        "rules": {
            "mentionSource": True,
        }
    },
    "isc": {
        "name": "ISC",
        "fullName": "ISC license",
        "rules": {
            "distributeOriginalLicenseText": True,
        }
    },
    "lgpl-2": {
        "name": "LGPL-2",
        "fullName": "GNU Lesser General Public License Version 2.0",
        "rules": {
            "noStaticLink": True,
        }
    },
    "lgpl-2.1": {
        "name": "LGPL-2.1",
        "fullName": "GNU Lesser General Public License Version 2.1",
        "rules": {
            "noStaticLink": True,
        }
    },
    "lgpl-2.1+": {
        "name": "LGPL-2.1 or later",
        "fullName": "GNU Lesser General Public License Version 2.1 or later",
        "rules": {
            "noStaticLink": True,
        }
    },
    "lgpl-3": {
        "name": "LGPL-3",
        "fullName": "GNU Lesser General Public License Version 3",
        "rules": {
            "noStaticLink": True,
        }
    },
    "libpng-2.0": {
        "name": "libpng-2.0",
        "fullName": "PNG Reference Library License version 2",
        "rules": {}
    },
    "libtiff": {
        "name": "libtiff",
        "fullName": "libtiff License",
        "rules": {
            "distributeOriginalLicenseText": True,
        }
    },
    "mit": {
        "name": "MIT",
        "fullName": "MIT License",
        "rules": {
            "distributeOriginalLicenseText": True,
        }
    },
    "naist": {
        "name": "NAIST-2003",
        "fullName": "Nara Institute License 2003",
        "rules": {
            "distributeOriginalLicenseText": True,
        }
    },
    "pd": {
        "name": "Public Domain",
        "fullName": "Public Domain",
        "rules": {}
    },
    "sgi-b-1.1": {
        "name": "SGI-B-1.1",
        "fullName": "SGI Free Software License B v1.1",
        "rules": {
            "distributeOriginalLicenseText": True,
        }
    },
    "sgi-b-2.0": {
        "name": "SGI-B-2.0",
        "fullName": "SGI Free Software License B v2.0",
        "rules": {
            "distributeOriginalLicenseText": True,
        }
    },
    "smlnj": {
        "name": "SML/NJ",
        "fullName":
            "Standard ML of New Jersey Copyright Notice, License And "
            "Disclaimer",
        "rules": {
            "distributeOriginalLicenseText": True,
        }
    },
    "unicode": {
        "name": "Unicode",
        "fullName":
            "Unicode, Inc. License Agreement - Data Files And Software",
        "rules": {
            "distributeOriginalLicenseText": True,
        }
    },
    "unlicense": {
        "name": "Unlicense",
        "fullName": "Unlicense",
        "rules": {}
    },
    "x11": {
        "name": "X11",
        "fullName": "X11 License",
        "rules": {
            "distributeOriginalLicenseText": True,
        }
    },
    "zlib": {
        "name": "Zlib",
        "fullName":
            "Unicode, Inc. License Agreement - Data Files And Software",
        "rules": {}
    },
}

class LicensesData:
    def __init__(self, customData={}):
        self.data = {**data, **customData}

    def AddData(self, customData):
        self.data = {**self.data, **customData}

    def GetData(self):
        return self.data
