# VPersonna Web Interface
(Ioan-Mihail Stan stanioanmihail@gmail.com)

## Environment setup:

1. clone the repo

        git clone https://github.com/stanioanmihail/vpersonna-web
        cd vpersonna-web/

2. install django

        sudo apt-get install python-pip
        sudo apt-get install python-dev
        sudo apt-get install libpq-dev
        sudo apt-get install postgresql postgresql-contrib
        sudo pip install virtualenv
        sudo pip install virtualenvwrapper

3. virtual environment setup

        virtualenv sandbox
        source sandbox/bin/activate
        pip install django
        pip install dateutils
        pip install psycopg2 

4.  database setup

        sudo apt-get install postgresql postgresql-contrib
        sudo su - postgres
        createdb vpersonna
        createuser -P vpersonna
        psql
        GRANT ALL PRIVILEGES ON DATABASE vpersonna TO vpersonna;
    Ctrl+D x 2

        cd vpersonna/
        ./manage.py migrate
        cd scripts/
        ./add_entries.sh 
        cd integration_scripts/ 
        ./run_add_brute_data.sh
    
    these scripts are generating some test database entries

5. manage the database

        cd ../..
        ./manage.py createsuperuser

    It will require: username, email, password, password confirmation
    The admin console is available accessing from browser IP:port/admin (ex: 127.0.0.1:8000/admin)

6. run a http server

        ./manage.py runserver 

    the server is available on localhost port 8000, but not in LAN

    alternative:

        ./manage.py runserver 0.0.0.0:8000 

    the server will be available in LAN on port 8000


## Test data details:

The static platform adopts 03-June-2015 22:30 as today's date and time.
