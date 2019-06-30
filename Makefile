test_build:
	docker build -f Dockerfile.test -t vgazer_test .

test_run:
	docker run -i -t -v ~/.vgazer:/home/test_user/.vgazer vgazer_test

# Not working if error occured while running entry point
#test_runi:
#	docker run -i -t -v ~/.vgazer:/home/test_user/.vgazer vgazer_test /bin/bash

test_clean:
	docker image prune -f
