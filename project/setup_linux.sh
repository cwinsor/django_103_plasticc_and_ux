#!/bin/sh
export PYTHONPATH=$(pwd):$(pwd)/starchaser:$(pwd)/starchaser/starchaser:
python -m pip install virtualenv
python -m virtualenv pymote_env_linux
source pymote_env_linux/bin/activate
dos2unix requirements.txt
pip install -r requirements.txt

echo '

To initialize the database:
 python starchaser/manage.py createsu
 python starchaser/manage.py makemigrations
 python starchaser/manage.py migrate

To populate the database with small subset of data:
 python starchaser/manage.py import_metadata   starchaser/training_set_metadata.csv
 python starchaser/manage.py import_timeseries starchaser/training_set.csv

To populate the database with all training data:
 python starchaser/manage.py import_metadata   ../../code_kaggle_plasticc___shared_data/PLAsTiCC-2018/training_set_metadata.csv
 python starchaser/manage.py import_timeseries ../../code_kaggle_plasticc___shared_data/PLAsTiCC-2018/training_set.csv

To run the server:
 python starchaser/manage.py runserver
'
