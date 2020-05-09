#!/bin/sh
export PYTHONPATH=$(pwd):$(pwd)/starchaser:$(pwd)/starchaser/starchaser:
python -m pip install virtualenv
python -m virtualenv pymote_env_linux
source pymote_env_linux/bin/activate
dos2unix requirements.txt
pip install -r requirements.txt

echo '

To initialize the database some or all of the following commands:
 python starchaser/manage.py import_metadata starchaser/training_set_metadata.csv
 python starchaser/manage.py import_timeseries starchaser/training_set.csv
 python starchaser/manage.py createsu
 python starchaser/manage.py makemigrations
 python starchaser/manage.py migrate

To run the server:
 python starchaser/manage.py runserver
'
