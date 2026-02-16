#!/bin/bash

# Read input file, filter empty lines, convert to numbers, sort numerically, and convert to JSON array
python3 << 'EOF'
import json

numbers = []
with open('/app/input.txt', 'r') as f:
    for line in f:
        line = line.strip()
        if line:  # Skip empty lines
            try:
                # Try to convert to float first (handles both int and float)
                num = float(line)
                # Convert to int if it's a whole number, otherwise keep as float
                if num.is_integer():
                    numbers.append(int(num))
                else:
                    numbers.append(num)
            except ValueError:
                # Skip invalid lines
                pass

# Sort numbers numerically
numbers.sort()

# Write to output JSON file
with open('/app/output.json', 'w') as f:
    json.dump(numbers, f)

print("Sorting successful")
EOF

if [ $? -eq 0 ]; then
    echo "Transformation successful"
    exit 0
else
    echo "Transformation failed"
    exit 1
fi
