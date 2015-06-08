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

def add_data(ip_src, port_src, ip_dst, port_dst):
    bpacket = BrutePacket()
    bpacket.ip_src = ip_src
    bpacket.port_src = port_src
    bpacket.ip_dst = ip_src
    bpacket.port_dst = port_dst
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
    
    ip_allocation_list = IPAllocation.objects.all()
    number_of_clients = len(ip_allocation_list)
    add_data(ip_allocation_list[randint(0, number_of_clients - 1)].ip_addr, 12345, "216.58.209.174", "80")
    add_data(ip_allocation_list[randint(0, number_of_clients - 1)].ip_addr, 12345, "173.252.120.6", "80")
    add_data(ip_allocation_list[randint(0, number_of_clients - 1)].ip_addr, 12345, "176.34.112.194", "80")

    
    read_all_data()

if __name__ == "__main__":
    sys.exit(main())
