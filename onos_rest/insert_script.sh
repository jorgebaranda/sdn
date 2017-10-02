#!/bin/sh

I=1

while [ "$I" != 9 ]
do
    python insert_rule.py ruletable_${I}.json
    I=$((I + 1))
done
