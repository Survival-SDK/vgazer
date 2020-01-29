ifeq ($(shell uname -m),x86_64)
	ARCH=x86_64
endif

.PHONY: .FORCE

samples:
	./generate_samples.py

first_run:
	./first_run.py

image_x86_64_debian_stretch_build:
ifeq ($(ARCH),x86_64)
	docker build \
     -f dockerfiles/vgazer_min_env_x86_64_debian_stretch.dockerfile \
     -t vgazer_min_env_x86_64_debian_stretch .
else
	echo "Error: host system's arch is not x86_64"
endif

image_x86_64_debian_buster_build:
ifeq ($(ARCH),x86_64)
	docker build \
     -f dockerfiles/vgazer_min_env_x86_64_debian_buster.dockerfile \
     -t vgazer_min_env_x86_64_debian_buster .
else
	echo "Error: host system's arch is not x86_64"
endif

image_x86_64_alpine_3.9_build:
ifeq ($(ARCH),x86_64)
	docker build \
     -f dockerfiles/vgazer_min_env_x86_64_alpine_3.9.dockerfile \
     -t vgazer_min_env_x86_64_alpine_3.9 .
else
	echo "Error: host system's arch is not x86_64"
endif

ifneq ($(and $(arch),$(os),$(ver)),)
image_build: image_$(arch)_$(os)_$(ver)_build
else
image_build:
	@echo 'Error: variables "arch", "os" and "ver" must be defined'
endif

ifneq ($(and $(arch),$(os),$(ver)),)
image_launch: image_$(arch)_$(os)_$(ver)_launch
else
image_launch:
	@echo 'Error: variables "arch", "os" and "ver" must be defined'
endif

ifneq ($(and $(arch),$(os),$(ver)),)
sample_platform: sample_$(arch)_$(os)_$(ver)_check_platform
else
sample_platform:
	@echo 'Error: variables "arch", "os" and "ver" must be defined'
endif

ifneq ($(and $(harch),$(hos),$(hver),$(tarch),$(tos),$(tabi)),)
sample_versions: sample_$(harch)_$(hos)_$(hver)_software_versions_$(tarch)_$(tos)_$(tabi)
else ifneq ($(and $(arch),$(os),$(ver)),)
sample_versions: sample_$(arch)_$(os)_$(ver)_software_versions_host
else
sample_versions:
	@echo 'Error: variables "arch", "os" and "ver" must be defined'
endif

ifneq ($(and $(harch),$(hos),$(hver),$(lib),$(tarch),$(tos),$(tabi)),)
sample_library: sample_$(harch)_$(hos)_$(hver)_install_$(lib)_$(tarch)_$(tos)_$(tabi)
else ifneq ($(and $(arch),$(os),$(ver),$(lib)),)
sample_library: sample_$(arch)_$(os)_$(ver)_install_$(lib)_host
else
sample_library:
	@echo 'Error: variables "arch", "os", "ver" and "lib" must be defined'
endif

ifneq ($(and $(arch),$(os),$(ver),$(tool)),)
sample_tool: sample_$(arch)_$(os)_$(ver)_install_$(tool)
else
sample_tool:
	@echo 'Error: variables "arch", "os", "ver" and "tool" must be defined'
endif

lint:
	-pylama -i E128,E272,E302,E305 ./vgazer ./first_run.py ./generate_samples.py \
     ./setup.py | tee pylama.log

package:
	python3 setup.py sdist

-include ./sample_targets.mk
