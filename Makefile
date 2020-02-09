default: build
.PHONY: build

prepare:
	apt-get update
  apt-get install git build-essential make -y
	pip install pipenv
	pipenv install

build:
	pipenv run molecule test

