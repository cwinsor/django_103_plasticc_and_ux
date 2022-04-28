Step by step instructions - to stand up an EC2 running this game...

Commission the EC2 (Ubuntu 20 tier 2). Include SSH but do **NOT** include HTTP (this will install and start Apache which we don't want)

In addition to the baseline security group - add the "Starchaser" security group.  This adds 5432 (SQL) and 8000 (the port our Django server will answer on)
iIPv4	All ICMP - IPv4	ICMP	All	0.0.0.0/0	–
IPv4	PostgreSQL	TCP	5432	0.0.0.0/0	–
IPv4	Custom TCP	TCP	8000	0.0.0.0/0	–


log in

############# prelinary ###################
sudo apt update 

### python, pip, dos2unix
sudo ln -s /usr/bin/python3 /usr/bin/python
sudo apt install python3-pip
sudo apt install dos2unix

### netstat 
sudo apt install net-tools

################### postgreSQL #########################
# as described in https://tecadmin.net/how-to-install-postgresql-in-ubuntu-20-04/

######################
sudo apt install wget curl ca-certificates 

######################
### Step 1 – Install PostgreSQL in Ubuntu 20.04
### First of all, Import the repository signing GPG key to your system. Open a terminal and use below command to import key:
wget -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add - 
### Next, create a PPA file for PostgreSQL on your Ubuntu 20.04 system.
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ focal-pgdg main" >> /etc/apt/sources.list.d/pgdg.list' 
### After adding the PPA to your system. Execute the following command to install the PostgreSQL server on your system.
sudo apt update 
sudo apt-get install postgresql postgresql-contrib 
### After successful installation verify the postgresql service:
sudo systemctl status postgresql 

######################
### Step 2 – Connection To PostgreSQL
### Now, establish a connection with the newly installed Postgres database server. First switch to the system’s postgres user account:
sudo su - postgres 
### then type “psql” to get the postgress prompt:
psql 
### Once you are connected to PostgreSQL and you can see the connection information’s details, use the following command:
postgres=# \conninfo
### The output displays information on the database name, the account you are logged in to, the socket path, and the port number.

######################################
### Step 3 – Secure PostgreSQL
### PostgreSQL installer creates a user “postgres” on your system. Default this user is not protected.
### First, create a password for “postgres” user account by running the following command.
sudo passwd postgres 
### Next, switch to the “postgres” account Then switch to the Postgres system account and create a secure and strong password for PostgreSQL administrative database user/role as follows.
su - postgres 
psql -c "ALTER USER postgres WITH PASSWORD 'secure_password_here';" 
exit 
### Restart the service to apply security changes.
sudo systemctl restart postgresql 

###############
### Step 4 – Install pgAdmin
### We can use the official pgAdmin4 PPA to install the latest version of pgAdmin on your system.
### First, import the repository signing GPG key and add the pgAdmin4 PPA to your system using the following commands.
curl https://www.pgadmin.org/static/packages_pgadmin_org.pub | sudo apt-key add -
sudo sh -c 'echo "deb https://ftp.postgresql.org/pub/pgadmin/pgadmin4/apt/focal pgadmin4 main" > /etc/apt/sources.list.d/pgadmin4.list' 
### After adding the PPA, update the Apt cache and install the pgAdmin4 package on your system.
sudo apt update
sudo apt install pgadmin4 
### The pgadmin4 package contains both pgadmin4-web and pgadmin4-desktop versions, Here:
### pgadmin4-web – Provides the web interface accessible in a web browser
### pgadmin4-desktop – Provides desktop application for Ubuntu system, which required Ubuntu Desktop system.
### You can install both or one of them of your choice. If you have installed both or pgadmin4-web, run the below command to configure it. This will add a login screen to the pgAdmin4 web dashboard.
sudo /usr/pgadmin4/bin/setup-web.sh 
### The above script will prompt you to create a user to access the web interface. Input an email address and password when prompted. Say “y” for other confirmation asked by the script.
### Once the script finished, you are good to access the pgAdmin web dashboard. It will be available at the below address:
### Access this in a web browser: http://localhost/pgadmin4


###########################
### Step X - give access from laptop pgAdmin to EC2 instance
### It is necessary to add to /etc/postgresql.conf and pg_hba.conf
pushd /etc/postgresql/XX/main
sudo cp postgresql.conf postgresql.conf.XXXXXX
sudo vi postgresql.conf
### add:
listen_addresses = '*'                  # what IP address(es) to listen on;
   
sudo cp pg_hba.conf  pg_hba.conf.XXXXXX
sudo vi pg_hba.conf
### add:
host    all             all              0.0.0.0/0                       md5
host    all             all              ::/0                            md5
  
sudo service postgresql restart

### with above ou should be able to use pgAdmin on laptop to "add" the server/database.
### Use the publicIpV4 address of the EC2


##############################
### Create the database "plasticc"
### It is necessary to create the (blank) database
### from laptop - run "pgadmin" (web app).  Connect to the server and database using username (postgres) and password (from above)
### create database "plasticc"

##################
### git clone the starchaser (django_103...)
git clone https://github.com/cwinsor/django_103_plasticc_and_ux.git
cd django_103_plasticc_and_ux/project/
export PYTHONPATH=$(pwd):$(pwd)/starchaser:$(pwd)/starchaser/starchaser:
python -m pip install virtualenv
python -m virtualenv pymote_env_linux
source pymote_env_linux/bin/activate
dos2unix requirements.txt
pip install -r requirements.txt
i
####################
### in the starchaser project - create a passwords.yml file from the example
cp starchaser/passwords.yml.EXAMPLE  starchaser/passwords.yml
vi starchaser/passwords.yml

####################
### in the starchaser project - edit settings.yml to include the IP addresses in "allowed hosts"
 '3.17.110.181' ['*']
