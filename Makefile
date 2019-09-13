container_build:
	docker build -f dockerfiles/test_debian_stretch.dockerfile -t vgazer_test .

container_launch:
	docker run --entrypoint /bin/bash -i -t -v ~/.vgazer/github:/home/test_user/.vgazer/github vgazer_test

test_clean:
	docker image prune -f

package:
	python3 setup.py sdist

sample_lv_linux64:
	./samples/libraries_versions_x86_64_linux_gnu.py

sample_install_cjson_linux64:
	docker run -i -t -v ~/.vgazer/github:/home/test_user/.vgazer/github \
     -v `pwd`:/vgazer --entrypoint sudo vgazer_test -E sh -c ./samples/install_cjson_x86_64_linux_gnu.py
