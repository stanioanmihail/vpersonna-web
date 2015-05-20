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

from vprofile.models import Offer 

# Setup Django environment.
UTF8Writer = codecs.getwriter('utf8')
sys.stdout = UTF8Writer(sys.stdout)

def add_data(offer_type, offer_description, cost_per_min):
    offer = Offer()
    offer.offer_name = offer_type 
    offer.offer_description = offer_description 
    offer.cost_per_min = cost_per_min
    offer.save()

def remove_all_data():
    offers = Offer.objects.all()
    for o in offers:
        o.delete()

def read_all_data():
    offers = Offer.objects.all()
    for o in offers:
        print o.__dict__

def main():
    remove_all_data()
    add_data('Extra Bandwidth', 'Add extra bandwidth', 0.5)
    add_data('Leased Lines','', 2)
    add_data('15% Burst','', '1')

    read_all_data()

if __name__ == "__main__":
    sys.exit(main())
