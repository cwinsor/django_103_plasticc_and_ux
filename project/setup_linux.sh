#!/bin/sh

# This is setup script and instructions to deploy StarChaser on AWS including the PostgreSQL data subset
# It is intended to be run on the EC2

start the Ubuntu and ssh in
https://linuxhint.com/how-to-install-postgresql-on-aws-ec2/
sudo apt-get update
sudo apt-get upgrade
sudo apt install postgresql -y

On add port 5432 to EC2 inbound network security channel

--------------------
good instructions at: 
   https://medium.com/ruralscript/install-and-setuppostgresql-on-ubuntu-amazon-ec2-5d1af79b4fca

Access the postgres account on your server by typing:

$ sudo -i -u postgres
Now you can immediately access Postgres prompt by typing:

$ psql
postgres=#
You will be logged in and able to interact with the Postgres database management system.

To list the databases:

postgres=# \l
You can exit Postgres prompt by typing:

postgres=# \q
------------------------
Change the password for postgres user
Connect to the server using psql:

postgres=# \password
Enter new password:
Enter it again:
postgres=#
----------------------------
Allow remote connections to PostgreSQL database server
90  cd /etc/postgresql/12/main/
sudo vi pg_hba.conf
host  all        all        0.0.0.0/0        md5

sudo vi postgresql.conf
listen_addresses = '*'                # what IP address(es) to listen on;

81  sudo systemctl restart postgresql.service

at this point you should be able to use PGADMIN to connect 

--------------------------
for ubuntu on EC2... need venv...
assuming here python is 3.8...

205  sudo apt install python3.8-venv
206  python -m venv venv

--------------------------

#export PYTHONPATH=$(pwd):$(pwd)/starchaser:$(pwd)/starchaser/starchaser:
#python -m pip install virtualenv
#python -m virtualenv pymote_env_linux
#source pymote_env_linux/bin/activate
#dos2unix requirements.txt
#pip install -r requirements.txt

----------------------------
200  python --version
205  sudo apt install python3.8-venv
206  python -m venv venv
210  source venv/bin/activate
213  sudo apt install dos2unix
214  dos2unix requirements.txt
220  pip install -r requirements.txt

----------------------------

This is setup script and instructions to deploy StarChaser on AWS including the PostgreSQL data subset
It is intended to be run on the EC2  

242  export PYTHONPATH=$(pwd):$(pwd)/starchaser:$(pwd)/starchaser/starchaser:

252  vi  starchaser/passwords.yml (copy from passwords.yml.EXAMPLE)

257  sudo -u postgres createdb plasticc
sudo -u postgres psql
\l


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
