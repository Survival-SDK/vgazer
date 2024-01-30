# Description
Library for tracking and installing new versions of software

# Requirements
This software required for working vgazer:

* python3

Also required these python packages:

* requests
* bs4

Optional Requirements for running samples (Linux only):

* docker

Installing requirements on Debian:

```console
# apt-get install python3 python3-requests python3-bs4 docker
```

# Store your github data on PC
Library gets some data about repositories from Github via Rest API. For this
reason it important to store your authentification data on your PC. Library
will use your authentification data for interacting with Github.

If you will skip this steps before using library you will be asked your
authentification data on first run.

I know it is uncertain security way but I can not find out better way for
interacting with Github API. Feel free to offer better way for resolving this
problem.
### Step 1:
Generate new access token.

1. Open settings of your Github profile.

2. Choose "Developer Settings". Then choose "Personal access tokens".

3. Click "Generate new token".

4. Important: for security reasons deselect all scopes of access.

5. Then click "Generate token".

### Step 2:
Copy or write your token.
### Step 3:
Store your authentification data on your PC.
#### Variant 1 (Linux only):

1. Create directory ".vgazer" in your home directory.

2. Create directory "~/.vgazer/github"

3. Create file "~/.vgazer/github/username" and store your Github username in
this file.

4. Create file "~/.vgazer/github/token" and store your Github access token in
this file.

#### Variant 2:
Run one of this commands and input your autentification data:
```console
$ make first_run
```
```console
$ ./first_run.py
```

# Usage
For use vgazer you need write simple script. Look sample files in "samples"
directory

More usage coming soon

# Working with samples (Linux only)
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

Description of parameters:

**harch** - must be same as your PC architecture. Currently supported:

* x86_64

**hos** and **hver** - OS or Linux Distribution and version of OS or Linux
Distribution. This is not OS and OS's version of your PC. Typically it is OS
and OS's version of base Docker image. Currently supported:

* debian
    * stretch (possibly not working yet)
    * buster
    * bullseye
    * bookworm
* steamrt
    * latest

**tarch** - architecture of device for crossplatform compiling libraries.
Currently supported:

* x86_64

**tos** - generic name of target's OS. Currently supported:

* linux
* windows

**tabi** - target's ABI. Currently supported:

* gnu
* mingw32

**arch**, **os** and **ver** - same as **harch**, **hos** and **hver** in that
cases when not used target platform parameters such as **tarch**, **tos** and
**tabi**

**tool** - tool for installing on host platform. Currently supported:

TODO complete list

**lib** - library for host or target platform that must be installed in system
paths on host platform. Currently supported:

TODO complete list

### Building Docker images
Build docker image of environment with given architecture, OS and version of
OS:
```console
$ make image_build arch=<host_arch> os=<host_os> ver=<host_os_version>
```
**Example**. Build docker image of environment with x86_64 architecture (your
PC's arch must be x86_64) and Debian Bullseye as base image:
```console
$ make image_build arch=x86_64 os=debian ver=bullseye
```

### Run test image in interactive mode (bash or sh)
```console
$ make image_launch arch=<host_arch> os=<host_os> ver=<host_os_version>
```
**Example**. Launch docker image of environment with x86_64 architecture and
Debian Bullseye as base image in interactive mode:
```console
$ make image_launch arch=x86_64 os=debian ver=bullseye
```

### Output host platform of image
```console
$ make sample_platform arch=<host_arch> os=<host_os> ver=<host_os_version>
```
**Example**. Output info about host platform in environment with x86_64
architecture and Debian Bullseye as base image:
```console
$ make sample_platform arch=x86_64 os=debian ver=bullseye
```

### Output last versions of all software for target platform on given host
Versions of host software (compilers, git, cmake etc) may be different on
various docker images.
```console
$ make sample_versions harch=<host_arch> hos=<host_os> hver=<host_os_version> \
    tarch=<target_arch> tos=<target_os> tabi=<target_abi>
```
**Example**. Output last versions of all tools for building libraries to
x86-linux-gnu target and last versions of all libraries that can be built for
x86-linux-gnu target in environment with x86_64 architecture and Debian Bullseye
as base image:
```console
$ make sample_versions harch=x86_64 hos=debian hver=bullseye tarch=x86_64 \
    tos=linux tabi=gnu
```

### Output last versions of all software for host platform
For most software this is last versions of appropriate packages in repos of OS
distribution.
```console
$ make sample_versions arch=<host_arch> os=<host_os> ver=<host_os_version>
```
**Example**. Output last versions of all tools and all libraries that can be
installed with apt-get or built manually on host environment with x86_64
architecture and Debian Bullseye as base image.
```console
$ make sample_versions arch=x86_64 os=debian ver=bullseye
```

### Install tool on host platform
For most software this is last versions of appropriate packages in repos of OS
distribution.
```console
$ make sample_tool tool=<tool> arch=<host_arch> os=<host_os> \
    ver=<host_os_version>
```
**Example**. Install CMake via apt-get on host environment with x86_64
architecture and Debian Bullseye as base image.
```console
$ make sample_tool tool=cmake arch=x86_64 os=debian ver=bullseye
```

### Install library for target platform on host platform
```console
$ make sample_library lib=<library> harch=<host_arch> hos=<host_os> \
    hver=<host_os_version> tarch=<target_arch> tos=<target_os> \
    tabi=<target_abi>
```
**Example**. Install manually (download, build and copy to system path) cjson
library for x86-linux-gnu target on host environment with x86_64 architecture
and Debian Bullseye as base image.
```console
$ make sample_library lib=cjson harch=x86_64 hos=debian hver=bullseye \
    tarch=x86_64 tos=linux tabi=gnu
```

### Install library for host platform on host platform
Install library from repos of OS's distribution if available. Else library will
be downloaded, builded and installed to system paths.
```console
$ make sample_library lib=<library> arch=<host_arch> os=<host_os> \
    ver=<host_os_version>
```
**Example 1**. Install zlib library via apt-get on host environment with x86_64
architecture and Debian Bullseye as base image.
```console
$ make sample_library lib=zlib arch=x86_64 os=debian ver=bullseye
```
**Example 2**. Try to install cjson library via apt-get on host environment
with x86_64 architecture and Debian Stretch as base image. Repos of Debian
Stretch do not have libcjson-dev package. This is why in this case library will
be downloaded, built and installed manually.
```console
$ make sample_library lib=cjson arch=x86_64 os=debian ver=stretch
```

# For developers:
### Additional requirements
Project use pylama for check code errors and some style errors. On Debian you
can install it with command:
```console
# apt-get install pylama
```
You can also use pip but I did try install it with pip and pylama did not
available in bash out of the box.

### Check code
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
