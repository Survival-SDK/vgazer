image_build:
	docker build \
     -f dockerfiles/vgazer_min_env_debian_stretch.dockerfile.dockerfile \
     -t vgazer_min_env_debian_stretch .

image_launch:
	docker run --entrypoint /bin/bash -i -t \
     -v ~/.vgazer/github:/home/vgazer_user/.vgazer/github \
     vgazer_min_env_debian_stretch

images_clean:
	docker image prune -f

package:
	python3 setup.py sdist

sample_lv_linux64:
	./samples/libraries_versions_x86_64_linux_gnu.py

sample_install_cjson_linux64:
	docker run -i -t -v ~/.vgazer/github:/home/vgazer_user/.vgazer/github \
     -v `pwd`:/vgazer --entrypoint \
     sudo vgazer_min_env_debian_stretch -E sh \
     -c ./samples/install_cjson_x86_64_linux_gnu.py
