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

from vprofile.models import RawData, IPAllocation
from random import randint

# Setup Django environment.
UTF8Writer = codecs.getwriter('utf8')
sys.stdout = UTF8Writer(sys.stdout)

def add_data(ip_src, port_src, ip_dst, port_dst, transport_protocol, host, ptype, timestamp_start, timestamp_end, no_bytes, no_packets):
    rpacket = RawData()
    rpacket.ip_src = ip_src
    rpacket.port_src = port_src
    rpacket.ip_dst = ip_dst
    rpacket.port_dst = port_dst
    rpacket.transport_protocol = transport_protocol 
    rpacket.host_address = host
    rpacket.traffic_type = ptype
    rpacket.timestamp_start = timestamp_start
    rpacket.timestamp_end = timestamp_end
    rpacket.no_bytes = no_bytes
    rpacket.no_packets = no_packets
    rpacket.save()
    

def remove_all_data():
    rpackets = RawData.objects.all()
    for rp in rpackets:
        rp.delete()

def read_all_data():
    rpackets = RawData.objects.all()
    for rp in rpackets:
        print rp.__dict__

def main():
    remove_all_data()
   
    #HARDCODED DATE
    #test data 3 June 2015 
    #end_date_string = '03-06-2015 22:30'
    #start_date_string = '03-06-2015 22:15'
    #date_format = '%d-%m-%Y %H:%M'
    #start_date = datetime.datetime.strptime(start_date_string, date_format)
    #end_date = datetime.datetime.strptime(end_date_string, date_format)

    start_date = datetime.datetime.today() - datetime.timedelta(hours = 2) - datetime.timedelta(minutes = 15)
    end_date = datetime.datetime.today() - datetime.timedelta(minutes = 15)
    crt_date = start_date
    
    ip_allocation_list = IPAllocation.objects.all()
    number_of_clients = len(ip_allocation_list)

    while crt_date <= end_date:
        one_min_later = crt_date + datetime.timedelta(minutes = 1)
        
        add_data("92.81.85.239", 12111, "91.189.92.151", "6882", "TCP", 'releases.ubuntu.com', 'TORRENT', crt_date, one_min_later, 120, 10)
        add_data("92.81.85.239", 12112, "5.134.209.113", "443", "TCP", 'olx.ro','DEFAULT', crt_date, one_min_later, 120, 10)
        add_data("92.81.85.239", 12113, "173.252.120.6", "443", "TCP", 'facebook.com', 'DEFAULT', crt_date, one_min_later, 120, 10),
        add_data("92.81.85.239", 12114, "216.58.209.174", "443", "TCP",'youtube.com', 'VIDEO', crt_date, one_min_later, 120, 10)
        add_data("92.81.85.239", 12115, "92.81.85.238", "443", "UDP",'', 'AUDIO', crt_date, one_min_later, 120, 10)
        crt_date += datetime.timedelta(minutes = 1)
    
    read_all_data()

if __name__ == "__main__":
    sys.exit(main())
