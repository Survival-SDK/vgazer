#!/usr/bin/env python3

from vgazer.vgazer import Vgazer

def main():
    gazer = Vgazer()
    #gazer = Vgazer(arch="x86_64", os="linux", osVersion="any", compiler="gcc")

    print("host:", gazer.platform["host"].arch, gazer.platform["host"].os,
     gazer.platform["host"].osVersion, gazer.platform["host"].compiler)
    print("target:", gazer.platform["target"].arch, gazer.platform["target"].os,
     gazer.platform["target"].osVersion, gazer.platform["target"].compiler)

    # Launching on Debian Stretch
    #print("zlib:", gazer.CheckVersion("zlib")) # Present in Stretch
    #print("wget:", gazer.CheckVersion("wget"))
    #print("cjson:", gazer.CheckVersion("cjson")) # Present in Buster but not in Stretch
    #print("nuklear:", gazer.CheckVersion("nuklear")) # Not present in Debian repos
    #gazer.Install("zlib", verbose=True)
    #gazer.Install("git", verbose=True)
    gazer.Install("wget", verbose=True)
    gazer.Install("cmake", verbose=True)
    gazer.Install("cjson", verbose=True)

if __name__ == "__main__":
    main()
