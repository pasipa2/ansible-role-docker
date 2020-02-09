#!usr/bin/env bash

apt-get update
apt-get install git build-essential make -y

pip install pipenv
pipenv install
