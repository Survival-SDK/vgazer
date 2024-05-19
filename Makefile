ifeq ($(shell uname -m),x86_64)
	ARCH=x86_64
endif

.PHONY: samples

samples:
	./generate_samples.py

image-x86_64-archlinux-latest-build:
ifeq ($(ARCH),x86_64)
	docker build --network=host --progress=plain $(DOCKER_NO_CACHE) \
     -f dockerfiles/vgazer-deps-x86_64-archlinux-latest.dockerfile \
     -t vgazer-deps:x86_64-archlinux-latest .
else
	echo "Error: host system's arch is not x86_64"
endif

image-x86_64-fedora-40-build:
ifeq ($(ARCH),x86_64)
	docker build --network=host --progress=plain $(DOCKER_NO_CACHE) \
     -f dockerfiles/vgazer-deps-x86_64-fedora-40.dockerfile \
     -t vgazer-deps:x86_64-fedora-40 .
else
	echo "Error: host system's arch is not x86_64"
endif

image-x86_64-oraclelinux-7-build:
ifeq ($(ARCH),x86_64)
	docker build --network=host --progress=plain $(DOCKER_NO_CACHE) \
     -f dockerfiles/vgazer-deps-x86_64-oraclelinux-7.dockerfile \
     -t vgazer-deps:x86_64-oraclelinux-7 .
else
	echo "Error: host system's arch is not x86_64"
endif

ifneq ($(and $(arch),$(os),$(ver)),)
image-build: image-$(arch)-$(os)-$(ver)-build
else
image-build:
	@echo 'Error: variables "arch", "os" and "ver" must be defined'
endif

ifneq ($(and $(arch),$(os),$(ver)),)
DOCKER_NO_CACHE=--no-cache
image-build-no-cache: image-$(arch)-$(os)-$(ver)-build
else
image-build-no-cache:
	@echo 'Error: variables "arch", "os" and "ver" must be defined'
endif

ifneq ($(and $(arch),$(os),$(ver)),)
image-launch: image-$(arch)-$(os)-$(ver)-launch
else
image-launch:
	@echo 'Error: variables "arch", "os" and "ver" must be defined'
endif

ifneq ($(and $(harch),$(hos),$(hver),$(software),$(tarch),$(tos),$(tabi)),)
sample-version: sample-$(harch)-$(hos)-$(hver)-version-$(software)-$(tarch)-$(tos)-$(tabi)
else ifneq ($(and $(arch),$(os),$(ver),$(software)),)
sample-version: sample-$(arch)-$(os)-$(ver)-version-$(software)
else
sample-version:
	@echo 'Error: variables "arch", "os", "ver" and "software" must be defined'
endif

ifneq ($(and $(harch),$(hos),$(hver),$(software),$(tarch),$(tos),$(tabi)),)
sample-install: sample-$(harch)-$(hos)-$(hver)-install-$(software)-$(tarch)-$(tos)-$(tabi)
else ifneq ($(and $(arch),$(os),$(ver),$(software)),)
sample-install: sample-$(arch)-$(os)-$(ver)-install-$(software)
else
sample-install:
	@echo 'Error: variables "arch", "os", "ver" and "software" must be defined'
endif

lint:
	-pylama -i E128,E131,E272,E302,E305 ./libvgazer ./first_run.py \
     ./generate_samples.py ./setup.py | tee pylama.log

package-build:
	rm -r -f ./build ./dist ./vgazer.egg-info
	python3 setup.py sdist bdist_wheel

package-upload:
	twine upload dist/*

-include ./sample_targets.mk
