#!/bin/sh
export PYTHONPATH=$(pwd):$(pwd)/starchaser:$(pwd)/starchaser/starchaser:
python -m pip install virtualenv
python -m virtualenv pymote_env_linux
source pymote_env_linux/bin/activate
dos2unix requirements.txt
pip install -r requirements.txt

