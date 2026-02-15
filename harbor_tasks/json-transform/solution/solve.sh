#!/bin/bash

jq '[.[] | {id: .id, name: .name, city: .city}]' /app/input.json > /app/output.json

if [ $? -eq 0 ]; then
    echo "Transformation successful"
    exit 0
else
    echo "Transformation failed"
    exit 1
fi
