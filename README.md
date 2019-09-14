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
Build docker image:
```
$ make image_build
```
Run test image:
```
$ make image_launch
```
Clean unused images:
```
$ make images_clean
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
