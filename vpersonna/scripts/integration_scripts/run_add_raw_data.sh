#!/bin/bash
export PYTHONPATH="../.."

echo "### Add brute packets ####"
python add_raw_data.py

echo "### Process brute packets ####"
python process_raw_data.py 
