#!/usr/bin/env python3

from vgazer.vgazer import Vgazer

def main():
    gazer = Vgazer()
    # Launching on Debian Stretch
    print("zlib:", gazer.CheckVersion("zlib")) # Present in Stretch
    print("cjson:", gazer.CheckVersion("cjson")) # Present in Buster but not in Stretch
    print("nuklear:", gazer.CheckVersion("nuklear")) # Not present in Debian repos

if __name__ == "__main__":
    main()
