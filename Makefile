ifeq ($(shell uname -m),x86_64)
	ARCH=x86_64
endif

.PHONY: samples

samples:
	./generate_samples.py

first-run:
	./first_run.py

image-x86_64-debian-buster-build:
ifeq ($(ARCH),x86_64)
	docker build --network=host --progress=plain $(DOCKER_NO_CACHE) \
     -f dockerfiles/vgazer-deps-x86_64-debian-buster.dockerfile \
     -t vgazer-deps:x86_64-debian-buster .
else
	echo "Error: host system's arch is not x86_64"
endif

image-x86_64-debian-bullseye-build:
ifeq ($(ARCH),x86_64)
	docker build --network=host --progress=plain $(DOCKER_NO_CACHE) \
     -f dockerfiles/vgazer-deps-x86_64-debian-bullseye.dockerfile \
     -t vgazer-deps:x86_64-debian-bullseye .
else
	echo "Error: host system's arch is not x86_64"
endif

image-x86_64-debian-bookworm-build:
ifeq ($(ARCH),x86_64)
	docker build --network=host --progress=plain $(DOCKER_NO_CACHE) \
     -f dockerfiles/vgazer-deps-x86_64-debian-bookworm.dockerfile \
     -t vgazer-deps:x86_64-debian-bookworm .
else
	echo "Error: host system's arch is not x86_64"
endif

image-x86_64-steamrt-scout-build:
ifeq ($(ARCH),x86_64)
	docker build --network=host --progress=plain $(DOCKER_NO_CACHE) \
     -f dockerfiles/vgazer-deps-x86_64-steamrt-scout.dockerfile \
     -t vgazer-deps:x86_64-steamrt-scout .
else
	echo "Error: host system's arch is not x86_64"
endif

image-x86_64-steamrt-sniper-build:
ifeq ($(ARCH),x86_64)
	docker build --network=host --progress=plain $(DOCKER_NO_CACHE) \
     -f dockerfiles/vgazer-deps-x86_64-steamrt-sniper.dockerfile \
     -t vgazer-deps:x86_64-steamrt-sniper .
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
	python3 -m twine upload -r testpypi dist/*

-include ./sample_targets.mk
