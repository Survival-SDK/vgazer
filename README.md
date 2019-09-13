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

# Usage
For use vgazer you need write simple script. Look sample files in "samples" 
directory

More usage coming soon

# Working with samples (Linux only)
Build docker image:
```
$ make image_build
```
Run test image:
```
$ make image_run
```
Clean unused images:
```
$ make test_clean
```
Run sample for checking versions of all software for x86_64-linux-gnu target.
Versions of host software (compilers, git, cmake etc) may be different on 
various machines. This sample runs not in docker.
```
$ make sample_lv_linux64
```
Run sample for installing cjson and all dependencies for x86_64-linux-gnu 
target:
```
$ make sample_install_cjson_linux64
```

# Copying:
Source code of library released to public domain (CC0 license)
