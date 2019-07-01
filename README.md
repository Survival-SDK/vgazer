#Description
Python library for tracking versions of various software in network

#Requirements
This software required for working vgazer:

* python3
* pip3

Also required these packages:

* requests
* bs4

Optional Requirements for running test example (Linux only):

* docker

Installing requirements on Debian:

```
# apt-get install python3
# apt-get install python3-pip
$ pip3 install requests
$ pip3 install bs4
# apt-get install docker
```

#Usage
For use vgazer you need write simple script. Look usage example in file test.py

#Working with test example (Linux only)
Build docker image:
```
$ make test_build
```
Run test image:
```
$ make test_run
```
Run test image in interactive mode:
```
$ make test_runi
```
Clean unused images:
```
$ make test_clean
```

#Copying:
Source code of library released to public domain (CC0 license)
