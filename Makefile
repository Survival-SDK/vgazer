ifeq ($(shell uname -m),x86_64)
	ARCH=x86_64
endif

.PHONY: samples

samples:
	./generate_samples.py

first_run:
	./first_run.py

image_x86_64_debian_stretch_build:
ifeq ($(ARCH),x86_64)
	docker build --network=host --progress=plain $(DOCKER_NO_CACHE) \
     -f dockerfiles/vgazer_min_env_x86_64_debian_stretch.dockerfile \
     -t vgazer_min_env_x86_64_debian_stretch .
else
	echo "Error: host system's arch is not x86_64"
endif

image_x86_64_debian_buster_build:
ifeq ($(ARCH),x86_64)
	docker build --network=host --progress=plain $(DOCKER_NO_CACHE) \
     -f dockerfiles/vgazer_min_env_x86_64_debian_buster.dockerfile \
     -t vgazer_min_env_x86_64_debian_buster .
else
	echo "Error: host system's arch is not x86_64"
endif

image_x86_64_debian_bullseye_build:
ifeq ($(ARCH),x86_64)
	docker build --network=host --progress=plain $(DOCKER_NO_CACHE) \
     -f dockerfiles/vgazer_min_env_x86_64_debian_bullseye.dockerfile \
     -t vgazer_min_env_x86_64_debian_bullseye .
else
	echo "Error: host system's arch is not x86_64"
endif

image_x86_64_debian_bookworm_build:
ifeq ($(ARCH),x86_64)
	docker build --network=host --progress=plain $(DOCKER_NO_CACHE) \
     -f dockerfiles/vgazer_min_env_x86_64_debian_bookworm.dockerfile \
     -t vgazer_min_env_x86_64_debian_bookworm .
else
	echo "Error: host system's arch is not x86_64"
endif

image_x86_64_alpine_3.9_build:
ifeq ($(ARCH),x86_64)
	docker build --network=host --progress=plain $(DOCKER_NO_CACHE) \
     -f dockerfiles/vgazer_min_env_x86_64_alpine_3.9.dockerfile \
     -t vgazer_min_env_x86_64_alpine_3.9 .
else
	echo "Error: host system's arch is not x86_64"
endif

image_x86_64_steamrt_latest_build:
ifeq ($(ARCH),x86_64)
	docker build --network=host --progress=plain $(DOCKER_NO_CACHE) \
     -f dockerfiles/vgazer_min_env_x86_64_steamrt_latest.dockerfile \
     -t vgazer_min_env_x86_64_steamrt_latest .
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
DOCKER_NO_CACHE=--no-cache
image_build_no_cache: image_$(arch)_$(os)_$(ver)_build
else
image_build_no_cache:
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

ifneq ($(and $(harch),$(hos),$(hver),$(tool),$(tarch),$(tos),$(tabi)),)
sample_tool: sample_$(harch)_$(hos)_$(hver)_install_$(tool)_$(tarch)_$(tos)_$(tabi)
else ifneq ($(and $(arch),$(os),$(ver),$(tool)),)
sample_tool: sample_$(arch)_$(os)_$(ver)_install_$(tool)
else
sample_tool:
	@echo 'Error: variables "arch", "os", "ver" and "tool" must be defined'
endif

lint:
	-pylama -i E128,E131,E272,E302,E305 ./vgazer ./first_run.py \
     ./generate_samples.py ./setup.py ./samples/check_platform.py \
     | tee pylama.log

package_build:
	rm -r -f ./build ./dist ./vgazer.egg-info
	python3 setup.py sdist bdist_wheel

package_upload:
	python3 -m twine upload --repository-url https://test.pypi.org/legacy/ \
     dist/*

-include ./sample_targets.mk
