#!/bin/sh

I=9

while [ "$I" != 255 ]
do
    cat ruletable_1.json | sed -e "s/\"tableId\": 1/\"tableId\": ${I}/g" | sed -e "s/\"tableId\": \"2\"/\"tableId\": \"$((I + 1))\"/g" > ruletable_${I}.json
    I=$((I + 1))
done
