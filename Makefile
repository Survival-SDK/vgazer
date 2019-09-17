ifeq ($(shell uname -m),x86_64)
	ARCH=x86_64
endif

sample_targets:
	./generate_sample_targets.py

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

image_x86_64_alpine_3.9_build:
ifeq ($(ARCH),x86_64)
	docker build \
     -f dockerfiles/vgazer_min_env_x86_64_alpine_3.9.dockerfile \
     -t vgazer_min_env_x86_64_alpine_3.9 .
else
	echo "Error: host system's arch is not x86_64"
endif

images_clean:
	docker image prune -f

package:
	python3 setup.py sdist

-include ./sample_targets.mk
