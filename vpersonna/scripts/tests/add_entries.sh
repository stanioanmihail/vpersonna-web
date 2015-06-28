#!/bin/bash

export PYTHONPATH="../.."

if [ $# -ne 1 ]; then
    echo "Expected just one argument"
    exit -1
fi

if [ "$1" == "init" ]; then
    echo "Initial config"
    echo "### Add services ####"
    python add_type_of_services.py
    echo "### Add clients ####"
    python add_clients.py  
    echo "### Add traffic stats - short ####"
    python add_service_statistics_short.py
    echo "### Add top sites ###"
    python add_top_sites.py
elif [ "$1" == "rawdata" ]; then
    echo "Adding and processing raw data"
    echo "### Add top sites ###"
    python add_raw_data.py
    echo "### Process raw data ###"
    python process_raw_data.py
else
    exit -2
fi

exit 0
