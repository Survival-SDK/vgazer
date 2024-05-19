# Description
Library for tracking and installing new versions of software

# Requirements
This software required for working vgazer:

* python3
* [beautifulsoup4](https://pypi.org/project/beautifulsoup4/)
* [requests](https://pypi.org/project/requests/)
* [multimethod](https://pypi.org/project/multimethod/)
* [yolk3k](https://pypi.org/project/yolk3k/)
* git

# Usage
```console
# vgazer [COMMAND] --target=<triplet> <SOFTWARE[ ...]>
```

commands:

- version - check versions of software
- install - install software

**target** (optional) - target platform for installation software and versions 
checking. Default - host platform

software - space separated list of software must be installed or version
checked. Can be file names that contains newline separated list of software of
subinclude files. For prevent vgazer mischoose filename instead software name
name your files with extension ("deps" for example)

# For developers
Optional Requirements for running samples (Linux only):

* docker
* pylama

### Generating samples
Before trying samples you need generate it.
Generate samples with one on this commands:
```console
$ make samples
```
```console
$ ./generate_samples.py
```
### Sample target's parameters
Parameters of sample's targets passing to make in key=value form.

#### Description of parameters:

**harch** - must be same as your PC architecture. Currently supported:

* x86_64

**hos** and **hver** - OS or Linux Distribution and version of OS or Linux
Distribution. This is not OS and OS's version of your PC. Typically it is OS
and OS's version of base Docker image. Currently supported:

* archlinux
    * latest
* fedora
    * 40
* oraclelinux
    * 7

**tarch** - architecture of device for crossplatform compiling libraries.
Currently supported:

* x86_64

**tos** - generic name of target's OS. Currently supported:

* linux
* windows (WIP)

**tabi** - target's ABI. Currently supported:

* gnu
* mingw32 (WIP)

**arch**, **os** and **ver** - same as **harch**, **hos** and **hver** in that
cases when not used target platform parameters such as **tarch**, **tos** and
**tabi**

**software** - library for host or target platform that must be installed in system
paths on host platform.

### Building Docker images
Build docker image of environment with given architecture, OS and version of
OS:
```console
$ make image-build arch=<host_arch> os=<host_os> ver=<host_os_version>
```
**Example**. Build docker image of environment with x86_64 architecture (your
PC's arch must be x86_64) and Oracle Linux 7 as base image:
```console
$ make image-build arch=x86_64 os=oraclelinux ver=7
```

### Run test image in interactive mode (bash or sh)
```console
$ make image_launch arch=<host_arch> os=<host_os> ver=<host_os_version>
```
**Example**. Launch docker image of environment with x86_64 architecture and
Oracle Linux 7 as base image in interactive mode:
```console
$ make image_launch arch=x86_64 os=oraclelinux ver=7
```

### Output most recent available version of software for host platform
For most software this is last versions of appropriate packages in repos of OS
distribution.
```console
$ make sample-version software=<software> arch=<host_arch> os=<host_os> \
    ver=<host_os_version>
```
**Example**. Output most recent available version of cmake that can be
installed with apt-get on host environment with x86_64 architecture and Oracle
Linux 7 as base image.
```console
$ make sample-version software=cmake arch=x86_64 os=oraclelinux ver=7
```

### Output most recent available version of software for target platform
Versions of host software (compilers, git, cmake etc) may be different on
various docker images.
```console
$ make sample-version software=<software> harch=<host_arch> hos=<host_os> \
    hver=<host_os_version> tarch=<target_arch> tos=<target_os> \
    tabi=<target_abi>
```
**Example**. Output most recent available version of cjson that can be
installed download, build and copy on host environment with x86_64 architecture
and Oracle Linux 7 as base image for x86_64-linux-gnu target.
```console
$ make sample-version software=cjson harch=x86_64 hos=oraclelinux hver=7 \
    tarch=x86_64 tos=linux tabi=gnu
```

### Install tool on host platform
For most software this is last versions of appropriate packages in repos of OS
distribution.
```console
$ make sample-install software=<tool> arch=<host_arch> os=<host_os> \
    ver=<host_os_version>
```
**Example**. Install CMake via apt-get on host environment with x86_64
architecture and Oracle Linux 7 as base image.
```console
$ make sample-install software=cmake arch=x86_64 os=oraclelinux ver=7
```

### Install library for target platform on host platform
```console
$ make sample-install software=<library> harch=<host_arch> hos=<host_os> \
    hver=<host_os_version> tarch=<target_arch> tos=<target_os> \
    tabi=<target_abi>
```
**Example**. Install manually (download, build and copy to system path) cjson
library for x86-linux-gnu target on host environment with x86_64 architecture
and Oracle Linux 7 as base image.
```console
$ make sample-install software=cjson harch=x86_64 hos=oraclelinux hver=7 \
    tarch=x86_64 tos=linux tabi=gnu
```

### Install library for host platform on host platform
Install library from repos of OS's distribution if available. Else library will
be downloaded, builded and installed to system paths.
```console
$ make sample-install software=<library> arch=<host_arch> os=<host_os> \
    ver=<host_os_version>
```
**Example**. Install zlib library via apt-get on host environment with x86_64
architecture and Oracle Linux 7 as base image.
```console
$ make sample-install software=zlib arch=x86_64 os=oraclelinux ver=7
```

## Check code
You can check code with command:
```console
$ make lint
```
Currently project ignores these errors and warnings:

* [**E128**](https://www.flake8rules.com/rules/E128.html)
* [**E131**](https://www.flake8rules.com/rules/E131.html)
* [**E272**](https://www.flake8rules.com/rules/E272.html)
* [**E302**](https://www.flake8rules.com/rules/E302.html)
* [**E305**](https://www.flake8rules.com/rules/E305.html)

# Copying:
Source code of library released to public domain (CC0 license)
