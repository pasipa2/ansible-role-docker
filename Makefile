default: build
.PHONY: build

prepare:
	pip install pipenv
	pipenv install

build:
	pipenv run molecule test

