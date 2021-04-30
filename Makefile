all: build install

install:
	pipenv sync

build:
	echo "toto"

test:
	pipenv run pytest ./tests -vvv -s
