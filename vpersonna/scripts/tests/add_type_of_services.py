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

from vprofile.models import ServiceType 

# Setup Django environment.
UTF8Writer = codecs.getwriter('utf8')
sys.stdout = UTF8Writer(sys.stdout)

def add_data(service_type):
    service = ServiceType()
    service.service_name = service_type  
    service.save()

def remove_all_data():
    services = ServiceType.objects.all()
    for s in services:
        s.delete()

def read_all_data():
    services = ServiceType.objects.all()
    for s in services:
        print s.__dict__

def main():
    remove_all_data()
    add_data('Video')
    add_data('VoIP')
    add_data('Torrent')
    add_data('Default')

    read_all_data()

if __name__ == "__main__":
    sys.exit(main())
