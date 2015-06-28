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

from vprofile.models import SiteAccess

# Setup Django environment.
UTF8Writer = codecs.getwriter('utf8')
sys.stdout = UTF8Writer(sys.stdout)

def add_data(url, num_accesses):
    site_a = SiteAccess()
    site_a.url = url
    site_a.num_accesses = num_accesses
    site_a.save()

def remove_all_data():
    sites = SiteAccess.objects.all()
    for sa in sites:
        sa.delete()

def read_all_data():
    sites = SiteAccess.objects.all()
    for sa in sites:
        print sa.__dict__

def main():
    #http://www.alexa.com/topsites/countries/RO
    remove_all_data()
    add_data("yahoo.com", 40000)
    add_data("google.ro", 1000000)
    add_data("wikipedia.com", 100)
    add_data("emag.ro", 25000)
    add_data("filelist.ro", 200)
    add_data("google.com", 800000)
    add_data("adevarul.ro", 10000)
    add_data("youtube.com", 700000)
    add_data("aliexpress.ro", 9000)
    add_data("imdb.com", 8000)
    add_data("facebook.com", 900000)
    add_data("olx.ro", 39900)
    read_all_data()

if __name__ == "__main__":
    sys.exit(main())
