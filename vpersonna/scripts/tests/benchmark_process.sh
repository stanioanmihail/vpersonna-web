#!/bin/bash

FILE_OUTPUT="values.out"
export PYTHONPATH="../.."

if [ $# -ne 3 ]; then
    echo "Expected 3 arguments (ratio, limit, start)"
    exit -1
fi
echo "ratio, limit, start"
ration=$1
limit=$2
start_value=$3


iterator=$start_value
> $FILE_OUTPUT
while [ $iterator -le $limit ]; do
    echo "No. entries: $iterator "
    python add_raw_data_bench.py $iterator
    echo "$iterator : $( (time python process_raw_data.py) 2>&1 | grep 'user' | cut -d $'\t' -f 2)" >> $FILE_OUTPUT 
    iterator=$(($ration * $iterator))
done

exit 0
