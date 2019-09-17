# Description
Library for tracking and installing new versions of software

# Requirements
This software required for working vgazer:

* python3
* pip3

Also required these python packages:

* requests
* bs4

Optional Requirements for running samples (Linux only):

* docker

Installing requirements on Debian:

```
# apt-get install python3 python3-pip docker
$ pip3 install requests bs4
```

# Store your github data on PC
Library gets some data about repositories from Github via Rest API. For this 
reason it important to store your authentification data on your PC. Library will 
use your authentification data for interacting with Github. 

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
```
$ make first_run
```
```
$ ./first_run.py
```

# Usage
For use vgazer you need write simple script. Look sample files in "samples" 
directory

More usage coming soon

# Working with samples (Linux only)
### Generating make targets
Before trying samples you need generate Makefile targets for launching samples.
Generate make targets with one on this commands:
```
$ make sample_targets
```
```
$ ./generate_sample_targets.py
```
### Sample target's parameters
Parameters of sample's targets passing to make command via name of target.

Example of make target's command format:
```
$ make sample_<host_arch>_<host_os>_<host_version>_install_<software>_<target_arch>_<target_os>_<target_abi>
```
Example of make target's command:
```
$ make sample_x86_64_debian_stretch_install_x86_64_linux_gnu
```
#### Description of parameters:
**host_arch** - must be same as your PC architecture. Currently supported:

* x86_64

**host_os** and **host_version** - OS or Linux Distribution and version of OS or 
Linux Distribution. This is not OS and OS's version of your PC. Typically it is 
OS and OS's version of base Docker image. Currently supported:

* alpine
    * 3.9
* debian
    * stretch

**target_arch** - architecture of device for crossplatform compiling libraries. 
Currently supported:

* x86_64

**target_os** - generic name of target's OS. Currently supported:

* linux

**target_abi** - target's ABI. Currently supported:

* gnu
* musl

**software** - tool or library. Currently supported:

TODO complete list

### Building Docker images
Build docker image of environment with given architecture, OS and version of OS:
```
$ make image_<host_arch>_<host_os>_<host_version>_build
```
**Example**. Build docker image of environment with x86_64 architecture (your 
PC's arch must be x86_64) and Debian Stretch as base image:
```
$ make image_x86_64_debian_stretch_build
```

### Run test image in interactive mode (bash or sh)
```
$ make image_<host_arch>_<host_os>_<host_version>_launch
```
**Example**. Launch docker image of environment with x86_64 architecture and 
Debian Stretch as base image in interactive mode:
```
$ make image_x86_64_debian_stretch_launch
```

### Output host platform of image
```
$ make sample_<host_arch>_<host_os>_<host_version>_check_platform
```
**Example**. Output info about host platform in environment with x86_64 
architecture and Debian Stretch as base image:
```
$ make sample_x86_64_debian_stretch_check_platform
```

### Output last versions of all software for target platform on given host
Versions of host software (compilers, git, cmake etc) may be different on 
various docker images.
```
$ make sample_<host_arch>_<host_os>_<host_version>_software_versions_<target_arch>_<target_os>_<target_abi>
```
**Example**. Output last versions of all tools for building libraries to 
x86-linux-gnu target and last versions of all libraries that can be built for 
x86-linux-gnu target in environment with x86_64 architecture and Debian Stretch 
as base image:
```
$ make sample_x86_64_debian_stretch_software_versions_x86_64_linux_gnu
```

### Output last versions of all software for host platform
For most software this is last versions of appropriate packages in repos of OS 
distribution.
```
$ make sample_<host_arch>_<host_os>_<host_version>_software_versions_native
```
**Example**. Output last versions of all tools and all libraries that can be 
installed with apt-get or built manually on host environment with x86_64 
architecture and Debian Stretch as base image.
```
$ make sample_x86_64_debian_stretch_software_versions_native
```

### Install tool on host platform
For most software this is last versions of appropriate packages in repos of OS 
distribution.
```
$ make sample_<host_arch>_<host_os>_<host_version>_install_<software>
```
**Example**. Install CMake via apt-get on host environment with x86_64 
architecture and Debian Stretch as base image.
```
$ make sample_x86_64_debian_stretch_install_cmake
```

### Install library for target platform on host platform
```
$ make sample_<host_arch>_<host_os>_<host_version>_install_<software>_<target_arch>_<target_os>_<target_abi>
```
**Example**. Install manually (download, build and copy to system path) cjson 
library for x86-linux-gnu target on host environment with x86_64 architecture 
and Debian Stretch as base image.
```
$ make sample_x86_64_debian_stretch_install_cjson_x86_64_linux_gnu
```

### Install library for host platform on host platform
Install library from repos of OS's distribution if available. Else library will
be downloaded, builded and installed to system paths.
```
$ make sample_<host_arch>_<host_os>_<host_version>_install_<software>_native
```
**Example 1**. Install zlib library via apt-get on host environment with x86_64 
architecture and Debian Stretch as base image.
```
$ make sample_x86_64_debian_stretch_install_zlib_native
```
**Example 2**. Try to install cjson library via apt-get on host environment with 
x86_64 architecture and Debian Stretch as base image. Repos of Debian Stretch do 
not have libcjson-dev package. This is why in this case library will be 
downloaded, built and installed manually.
```
$ make sample_x86_64_debian_stretch_install_cjson_native
```

### Clean unused images
```
$ make images_clean
```

# Copying:
Source code of library released to public domain (CC0 license)
