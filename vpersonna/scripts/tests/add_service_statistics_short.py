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
from random import randint, seed
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

def daterange_work(start_ref_date, end_date):
    delta_1H=datetime.timedelta(hours=1) 
    delta_2H=datetime.timedelta(hours=2) 
    delta_15H=datetime.timedelta(hours=15) 
    start_date = start_ref_date.replace(day = 1, hour = 9, minute = start_ref_date.minute) 
    crt_date = start_date
    while crt_date < end_date:
        yield crt_date
        if (crt_date.hour >= 9 and crt_date.hour < 12) or (crt_date.hour >= 14 and crt_date.hour < 18):
            crt_date +=delta_1H
        elif crt_date.hour == 18:
            crt_date +=delta_15H
        elif crt_date.hour == 12:
            crt_date +=delta_2H
            
def main():

    date_format = '%Y-%m-%d %H:%M' #06/22/2015 14:21
    clients = Client.objects.all()
    services = ServiceType.objects.all()

    remove_all_data()

    #HARDCODED DATE
    #today's date is hardcoded 
    #today = datetime.datetime.strptime("2015-06-03 22:30", date_format)
    today = datetime.datetime.today()

    end_date = today
    start_date = end_date + relativedelta(months=-3)
    
    seed(1)    
    print "Clean tables: done!"
    for c in clients:
        print "Generate data for:", c
        for single_date in daterange_work(start_date, end_date):
            for s in services:
                
                num_accesses = randint(10,110)
                add_data(c,s, single_date.strftime("%Y-%m-%d %H:%M"), date_format, num_accesses)
                
    
    #read_all_data()

if __name__ == "__main__":
    sys.exit(main())
