#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import sys
import os
import codecs
import datetime
# export PYTHONPATH=..

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "vpersonna.settings")
import django
django.setup()

from vprofile.models import Client 

# Setup Django environment.
UTF8Writer = codecs.getwriter('utf8')
sys.stdout = UTF8Writer(sys.stdout)

def add_data(client_name, client_email, client_addr, pnumber, CNP, contract_nb, uname, pwd):
    client = Client()
    client.name = client_name 
    client.email = client_email
    client.address = client_addr
    client.phone_number = pnumber
    client.card_id = CNP
    client.contract_id = contract_nb
    client.username = uname
    client.password = pwd
    client.save()

def remove_all_data():
    clients = Client.objects.all()
    for c in clients:
        c.delete()

def read_all_data():
    clients = Client.objects.all()
    for c in clients:
        print c.__dict__

def main():
    remove_all_data()
    add_data('John Smith','john.smith@example.com', 'Str. A Nb 1', '+123456789', 'ABCDEFGHIJKLM', 'CONTR1', 'john.smith', 'Abcd123!')
    add_data('John Doe','john.doe@example.com', 'Str. B Nb 2', '+123456780', 'ABCDEFGHIJKLN', 'CONTR2', 'john.doe', 'Abcd123!')
    add_data('Dan Summer','dan.summer@example.com', 'Str. C Nb 3', '+123456770', 'ABCDEFGHIJKLO', 'CONTR3', 'dan.summer', 'Abcd123!')

    read_all_data()

if __name__ == "__main__":
    sys.exit(main())
