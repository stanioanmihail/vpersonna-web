#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import sys
import os
import codecs
import datetime
import hashlib
# export PYTHONPATH=..

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "vpersonna.settings")
import django
django.setup()

from vprofile.models import Client, IPAllocation, RawData 
from django.contrib.auth.models import User

# Setup Django environment.
UTF8Writer = codecs.getwriter('utf8')
sys.stdout = UTF8Writer(sys.stdout)

def add_data(client_name, client_email, client_addr, pnumber, CNP, contract_nb, uname, pwd, ip_addr):
    client = Client()
    client.name = client_name 
    client.email = client_email
    client.address = client_addr
    client.phone_number = pnumber
    client.card_id = CNP
    client.contract_id = contract_nb
    client.username = uname
    client.password = hashlib.sha1(pwd).hexdigest()
    client.user = User.objects.create_user(username=uname, email=client_email, password=pwd)
    client.save()

    ip_alloc = IPAllocation()
    ip_alloc.ip_addr = ip_addr
    ip_alloc.client = Client.objects.get(email = client_email)
    ip_alloc.save()
    

def remove_all_data():

    ip_alloc_list = IPAllocation.objects.all()
    for ia in ip_alloc_list:
        ia.delete()
    clients = Client.objects.all()
    for c in clients:
        c.user.delete()
        c.delete()
    raw_data = RawData.objects.all()
    for rd in raw_data:
        rd.delete()


def read_all_data():
    ip_alloc_list = IPAllocation.objects.all()
    for ia in ip_alloc_list:
        print ia.__dict__
    clients = Client.objects.all()
    for c in clients:
        print c.__dict__

def main():
    remove_all_data()

    add_data('Stan N. Ioan-Mihail',
            'ioan.stan@cti.pub.ro', 
            'Str. G Nb 1', 
            '+40723261115', 
            '1234567890123', 
            'CONTR01_IOANSTAN', 
            'ioan.stan', 
            'test123.', 
            "92.81.85.239")

    read_all_data()

if __name__ == "__main__":
    sys.exit(main())
