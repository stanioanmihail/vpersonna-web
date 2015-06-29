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
def geometric_sequence(ratio = 2, limit = 3000, start = 5):
    i = start
    while i <= limit:
        yield i
        i = i * ratio

def main(argv):
    remove_all_data()
   
    #HARDCODED DATE
    #test data 3 June 2015 
    #end_date_string = '03-06-2015 22:30'
    #start_date_string = '03-06-2015 22:15'
    #date_format = '%d-%m-%Y %H:%M'
    #start_date = datetime.datetime.strptime(start_date_string, date_format)
    #end_date = datetime.datetime.strptime(end_date_string, date_format)

    today = datetime.datetime.today().replace(hour=20, minute = 0) 
    #start_date = today - datetime.timedelta(hours = 2) - datetime.timedelta(minutes = 16)
    #end_date = today - datetime.timedelta(minutes = 16)
    crt_date = today
    one_min_later = crt_date + datetime.timedelta(minutes = 1)
    
    i = 0
    limit = int(argv[0])
    while i < limit:
        i += 1
        add_data("92.81.85.239", 12111, "92.87.156.93", "443", "TCP", 'google.com', 'DEFAULT', crt_date, one_min_later, 120, 10)
    
    #read_all_data()

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
