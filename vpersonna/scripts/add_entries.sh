#!/bin/bash

export PYTHONPATH=".."

echo "### Add services ####"
python add_type_of_services.py
echo "### Add offers ####"
python add_offer_types.py  
echo "### Add clients ####"
python add_clients.py  
echo "### Add traffic stats - short ####"
python add_service_statistics_short.py
