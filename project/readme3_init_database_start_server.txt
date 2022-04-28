
cd ~/django_103_plasticc_and_ux/project

#################### configure virtualenv #################
export PYTHONPATH=$(pwd):$(pwd)/starchaser:$(pwd)/starchaser/starchaser:
python -m pip install virtualenv
python -m virtualenv pymote_env_linux
. pymote_env_linux/bin/activate
dos2unix requirements.txt
pip install -r requirements.txt

################# initialize the database (if not alredy done) ##############
### initial migration, migrate and create superuser
 python starchaser/manage.py makemigrations
 python starchaser/manage.py migrate
 python starchaser/manage.py createsuperuser

### populate the database with small subset of data:
 python starchaser/manage.py import_metadata   starchaser/training_set_metadata.csv
 python starchaser/manage.py import_timeseries starchaser/training_set.csv

### populate the database with all training data:
 python starchaser/manage.py import_metadata   ../../code_kaggle_plasticc___shared_data/PLAsTiCC-2018/training_set_metadata.csv
 python starchaser/manage.py import_timeseries ../../code_kaggle_plasticc___shared_data/PLAsTiCC-2018/training_set.csv

### run the server:
 python starchaser/manage.py runserver
<or on AWS>
 python starchaser/manage.py runserver 0.0.0.0:8000
### to send output to null and background...
 python starchaser/manage.py runserver 0.0.0.0:8000 > /dev/null 2>&1
<ctrl-z>
bg

### to check...
 curl ec2-3-22-167-114.us-east-2.compute.amazonaws.com:8000

### Basic access is at
http://3.17.110.181:8000
### Admin is at:
http://3.17.110.181:8000/admin/login/?next=/admin/



