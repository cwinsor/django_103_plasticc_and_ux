#!/bin/sh
export PYTHONPATH=$PYTHONPATH:$(pwd):.
python -m pip install virtualenv
python -m virtualenv pymote_env
source pymote_env/bin/activate
dos2unix requirements.txt
pip install -r requirements.txt

