test_build:
	docker build -f Dockerfile.test -t vgazer_test .

test_run:
	docker run -i -t -v ~/.vgazer/github:/home/test_user/.vgazer/github vgazer_test

# Not working if error occured while running entry point
test_runi:
	docker run --entrypoint /bin/bash -i -t -v ~/.vgazer/github:/home/test_user/.vgazer/github vgazer_test

test_clean:
	docker image prune -f

package:
	python setup.py sdist
