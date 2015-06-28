#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import sys
import os
import codecs
import datetime
# export PYTHONPATH=../..

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "vpersonna.settings")
import django
django.setup()

from vprofile.models import RawData, IPAllocation, ServiceUtilizationStatistics, SiteAccess, ServiceType
from random import randint
from django.core.exceptions import ObjectDoesNotExist

# Setup Django environment.
UTF8Writer = codecs.getwriter('utf8')
sys.stdout = UTF8Writer(sys.stdout)

def add_new_data_to_ServiceUtilizationStatistics(client, service, date):
    utilization_stats = ServiceUtilizationStatistics()
    utilization_stats.client = client
    utilization_stats.service = service
    #for future formats, support for other formats
    utilization_stats.date = date
    utilization_stats.num_accesses = 1 

    utilization_stats.save()

def add_new_data_to_SiteAccess(url):
    site_a = SiteAccess()
    site_a.url = url
    site_a.num_accesses = 1
    site_a.save()

def update_data_to_ServiceUtilizationStatistics(client, service, date):
    # filter by service, day and hour
    try:
        utilization_stats = ServiceUtilizationStatistics.objects.get(service = service,
                                                                date__year = date.year,
                                                                date__month = date.month,
                                                                date__day = date.day,
                                                                date__hour = date.hour,
                                                                client = client,)
    except ObjectDoesNotExist:
        utilization_stats = None

    if utilization_stats != None:
                                
        utilization_stats.num_accesses += 1 
        utilization_stats.save()
    else:
        add_new_data_to_ServiceUtilizationStatistics(client, service, date)

def update_data_to_SiteAccess(url):
    try:
        site_a = SiteAccess.objects.get(url = url)
    except ObjectDoesNotExist:
        site_a = None

    if site_a != None:
        site_a.num_accesses += 1
        site_a.save()
    else:
        add_new_data_to_SiteAccess(url)


def main():
   
    #HARDCODED DATE  
    #today_date_string = '03-06-2015 22:30'
    #date_format = '%d-%m-%Y %H:%M'
    #today_date_hour = datetime.datetime.strptime(today_date_string, date_format)
    today_date_hour = datetime.datetime.today()

    ref_date = today_date_hour - datetime.timedelta(minutes=5)

    # older than 5 minutes ago
    raw_packets = RawData.objects.filter(timestamp_end__lte = ref_date)

    for rp in raw_packets:
        client = (IPAllocation.objects.get(ip_addr = rp.ip_src)).client
        if rp.traffic_type == 'AUDIO':
            service = ServiceType.objects.get(service_name='VoIP')
        elif rp.traffic_type == 'VIDEO': 
            service = ServiceType.objects.get(service_name='Video')
        elif rp.traffic_type ==  'TORRENT': 
            service = ServiceType.objects.get(service_name='Torrent')
        else: 
            service = ServiceType.objects.get(service_name='Default')

        date_start = rp.timestamp_start 
        date_end = rp.timestamp_end
        url = rp.host_address if rp.host_address != None else rp.ip_dst
        
        if client != None: 
            print client, " ", service, " ", url, " ", date_start, " ", date_end
            update_data_to_SiteAccess(url)
            update_data_to_ServiceUtilizationStatistics(client, service, date_end)
        rp.delete()
            
    

if __name__ == "__main__":
    sys.exit(main())
