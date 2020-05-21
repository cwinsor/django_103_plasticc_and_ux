#!/bin/sh
export PYTHONPATH=$(pwd):$(pwd)/starchaser:$(pwd)/starchaser/starchaser:
python -m pip install virtualenv
python -m virtualenv pymote_env_linux
source pymote_env_linux/bin/activate
dos2unix requirements.txt
pip install -r requirements.txt

echo '

To initialize the database:
 python starchaser/manage.py makemigrations
 python starchaser/manage.py migrate
 python starchaser/manage.py createsu

To populate the database with small subset of data:
 python starchaser/manage.py import_metadata   starchaser/training_set_metadata.csv
 python starchaser/manage.py import_timeseries starchaser/training_set.csv

To populate the database with all training data:
 python starchaser/manage.py import_metadata   ../../code_kaggle_plasticc___shared_data/PLAsTiCC-2018/training_set_metadata.csv
 python starchaser/manage.py import_timeseries ../../code_kaggle_plasticc___shared_data/PLAsTiCC-2018/training_set.csv

To run the server:
 python starchaser/manage.py runserver
<or on AWS>
 python starchaser/manage.py runserver 0.0.0.0:8000
 curl ec2-3-22-167-114.us-east-2.compute.amazonaws.com:8000

If you get "could not connect to server: Connection refused"
then confirm postgres is running - from start -> "pgadmin" and open the database
to start postgres:
 su postgres
 cd
 service postgresql status
 mv logfile logfile200510
 sudo mkdir /run/postgresql
 sudo chmod 777 /run/postgresql/
 mkdir /run/postgresql/10-wsl_cluster.pg_stat_tmp
 /usr/lib/postgresql/10/bin/pg_ctl -D /etc/postgresql/10/wsl_cluster/    -l logfile start
 exit 
'
