#!/bin/bash
set -e

# Read CSV, filter by price >= 50.0, sort by price, convert to JSON
python3 -c "
import csv
import json
import sys

try:
    products = []
    with open('/app/products.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            price = float(row['price'])
            if price >= 50.0:
                products.append({
                    'name': row['name'],
                    'price': price,
                    'category': row['category']
                })
    products.sort(key=lambda x: x['price'])
    with open('/app/output.json', 'w') as f:
        json.dump(products, f, indent=2)
    print('Filtered and sorted', len(products), 'products')
except Exception as e:
    print('Error:', e, file=sys.stderr)
    sys.exit(1)
"
