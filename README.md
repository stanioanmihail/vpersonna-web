# VPersonna Web Interface
(Ioan-Mihail Stan stanioanmihail@gmail.com)

## Environment setup:

1. clone the repo

        git clone https://github.com/stanioanmihail/vpersonna-web
        cd vpersonna-web/

2. install django

        sudo apt-get install python-pip
        sudo pip install virtualenv
        sudo pip install virtualenvwrapper
        sudo pip install django
        sudo pip install dateutils

3. virtual environment setup

        virtualenv sandbox
        source sandbox/bin/activate
        pip install django

4.  database setup

        cd vpersonna/
        ./manage.py migrate
        cd scripts/
        ./add_entries.sh 
    
    this script is generating some test database entries

5. run a http server

        cd ..
        ./manage.py runserver 

    the server is available on localhost port 8000, but not in LAN

    alternative:

        ./manage.py runserver 0.0.0.0:8000 

    the server will be available in LAN on port 8000

6. manage the database

        ./manage.py createsuperuser

    It will require: username, password, password confirmation
    The admin console is available accessing from browser IP:port/admin (ex: 127.0.0.1:8000/admin)

## Test platform details:

The static platform adopts 03-June-2015 22:30 as today's date and time.
