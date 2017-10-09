#!/bin/sh

cat table_out1.json | sed "s/tableId\": [0-9]/tableId\": ${1}/" > table_out.json

python insert_rule.py table_out.json

cat table_out2.json | sed "s/tableId\": [0-9]/tableId\": ${1}/" > table_out.json

python insert_rule.py table_out.json

rm table_out.json
