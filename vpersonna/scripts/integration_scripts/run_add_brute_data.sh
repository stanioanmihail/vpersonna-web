#!/bin/bash
export PYTHONPATH="../.."

echo "### Add brute packets ####"
python add_brute_data.py

echo "### Process brute packets ####"
python process_brute_data.py 
