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

from vprofile.models import BrutePacket, IPAllocation
from random import randint

# Setup Django environment.
UTF8Writer = codecs.getwriter('utf8')
sys.stdout = UTF8Writer(sys.stdout)

def add_data(ip_src, port_src, ip_dst, port_dst, transport_protocol, host, ptype, timestamp):
    bpacket = BrutePacket()
    bpacket.ip_src = ip_src
    bpacket.port_src = port_src
    bpacket.ip_dst = ip_src
    bpacket.port_dst = port_dst
    bpacket.transport_protocol = transport_protocol 
    bpacket.host_address = host
    bpacket.traffic_type = ptype
    bpacket.timestamp = timestamp
    bpacket.save()
    

def remove_all_data():
    bpackets = BrutePacket.objects.all()
    for bp in bpackets:
        bp.delete()

def read_all_data():
    bpackets = BrutePacket.objects.all()
    for bp in bpackets:
        print bp.__dict__

def main():
    remove_all_data()
   
     
    end_date_string = '03-06-2015 22:30'
    start_date_string = '03-06-2015 22:15'
    date_format = '%d-%m-%Y %H:%M'
    start_date = datetime.datetime.strptime(start_date_string, date_format)
    end_date = datetime.datetime.strptime(end_date_string, date_format)
    crt_date = start_date
    
    ip_allocation_list = IPAllocation.objects.all()
    number_of_clients = len(ip_allocation_list)

    while crt_date <= end_date:
        
        add_data(ip_allocation_list[randint(0, number_of_clients - 1)].ip_addr, 12345, "216.58.209.174", "443", 1, 
                                                                        'google.com', 'Default', crt_date)
        add_data(ip_allocation_list[randint(0, number_of_clients - 1)].ip_addr, 12345, "173.252.120.6", "443", 1, 
                                                                        'facebook.com','Video', crt_date)
        add_data(ip_allocation_list[randint(0, number_of_clients - 1)].ip_addr, 12345, "54.215.82.230", "443", 1, 
                                                                        '9gag.com', 'Default', crt_date)
        add_data(ip_allocation_list[randint(0, number_of_clients - 1)].ip_addr, 12345, "216.58.209.174", "443", 1, 
                                                                        'youtube.com', 'Video', crt_date)
        add_data(ip_allocation_list[randint(0, number_of_clients - 1)].ip_addr, 12345, "216.58.209.174", "443", 0, 
                                                                        'mail.google.com', 'Audio', crt_date)
        add_data(ip_allocation_list[randint(0, number_of_clients - 1)].ip_addr, 12345, "4.4.4.4", "6882", 1, 
                                                                        'ubuntu.com', 'BitTorrent', crt_date)
        add_data(ip_allocation_list[randint(0, number_of_clients - 1)].ip_addr, 12345, "5.5.5.5", "6883", 1, 
                                                                        'ubuntu.com', 'BitTorrent', crt_date)

        crt_date += datetime.timedelta(minutes = 1)
    
    read_all_data()

if __name__ == "__main__":
    sys.exit(main())
