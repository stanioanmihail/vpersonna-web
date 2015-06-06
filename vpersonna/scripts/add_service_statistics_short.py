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

from vprofile.models import ServiceType, ServiceUtilizationStatistics, Client
from random import randint
import datetime
from dateutil.relativedelta import relativedelta

# Setup Django environment.
UTF8Writer = codecs.getwriter('utf8')
sys.stdout = UTF8Writer(sys.stdout)

def add_data(client, service, date_string, date_format, num_accesses):
    utilization_stats = ServiceUtilizationStatistics()
    utilization_stats.client = client
    utilization_stats.service = service
    #for future formats, support for other formats
    utilization_stats.date = datetime.datetime.strptime(date_string, date_format)
    utilization_stats.num_accesses = num_accesses 

    utilization_stats.save()

def remove_all_data():
    utilization_stats_list = ServiceUtilizationStatistics.objects.all()
    for us in utilization_stats_list:
        us.delete()

def read_all_data():
    utilization_stats_list = ServiceUtilizationStatistics.objects.all()
    for us in utilization_stats_list:
        print us.__dict__

def daterange(start_date, end_date, delta=datetime.timedelta(days=1)):
    crt_date = start_date
    while crt_date < end_date:
        yield crt_date
        crt_date +=delta

def main():

    date_format = '%Y-%m-%d %H:%M' #06/22/2015 14:21
    clients = Client.objects.all()
    services = ServiceType.objects.all()

    remove_all_data()

    #today's date is hardcoded 
    today = datetime.datetime.strptime("2015-06-03 22:30", date_format)
    end_date = today
    start_ref_date = end_date + relativedelta(months=-3)
    start_date = start_ref_date.replace(hour = 8, minute = today.minute)
        
    print "Clean tables: done!"
    for c in clients:
        print "Generate data for:", c
        for single_date in daterange(start_date, end_date, delta=datetime.timedelta(hours=12)):
            for s in services:
                
                num_accesses = randint(10,110)
                add_data(c,s, single_date.strftime("%Y-%m-%d %H:%M"), date_format, num_accesses)
               # print c,",",s,",",single_date.strftime("%Y-%m-%d %H:%M"),",",num_accesses
                
    
    #read_all_data()

if __name__ == "__main__":
    sys.exit(main())
