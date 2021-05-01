all: build install

requirements = dev_requirements install_requirements
cleaners = clean_build clean_install clean_venv

dev_requirements:
	PIPENV_VENV_IN_PROJECT=yes pipenv sync --dev

install_requirements:
	PIPENV_VENV_IN_PROJECT=yes pipenv sync

test: $(requirements)
	pipenv run pytest -vvv -s

build:
	python3 setup.py sdist

install: build
	pip3 install ./dist/*.tar.gz

clean_build:
	rm -rf ./dist
	rm -rf ./src/**.egg**
	rm -rf ./.eggs

clean_install:
	pip3 uninstall srp6a_py -y

clean_venv:
	pipenv --rm || true

clean: $(cleaners)
	rm -rf .pytest_cache
	echo "Successfully cleaned up."
