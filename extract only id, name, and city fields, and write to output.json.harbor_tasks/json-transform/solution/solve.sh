#!/bin/bash

# Read the input JSON file and transform it to extract only id, name, and city fields
# Using jq to transform the JSON data

jq '[.[] | {id: .id, name: .name, city: .city}]' /app/input.json > /app/output.json

# Check if the transformation was successful
if [ $? -eq 0 ]; then
    echo "Transformation successful"
    exit 0
else
    echo "Transformation failed"
    exit 1
fi
