# CSV Filter and Sort Task

## Objective
Read a CSV file containing product data, filter products by minimum price, sort them by price in ascending order, and write the results to a JSON file.

## Input
- File: `/app/products.csv`
- Format: CSV file with headers: name, price, category
- The price column contains numeric values

## Output
- File: `/app/output.json`
- Format: JSON array of product objects
- Requirements:
  1. Filter products where price >= 50.0
  2. Sort the filtered products by price in ascending order
  3. Each object should have: name, price, category
  4. Price should be a number (not a string)

## Requirements
1. Read the input CSV file from `/app/products.csv`
2. Parse the CSV data (skip the header row)
3. Filter products where price >= 50.0
4. Sort the filtered products by price in ascending order
5. Convert the result to JSON format
6. Write the output to `/app/output.json`
7. The output should be a valid JSON file with proper formatting

## Example
Input (`products.csv`):
```csv
name,price,category
Laptop,999.99,Electronics
Pen,2.50,Office
Monitor,299.99,Electronics
Notebook,5.00,Office
Keyboard,75.00,Electronics
Mouse,25.00,Electronics
```

Expected Output (`output.json`):
```json
[
  {"name": "Keyboard", "price": 75.0, "category": "Electronics"},
  {"name": "Monitor", "price": 299.99, "category": "Electronics"},
  {"name": "Laptop", "price": 999.99, "category": "Electronics"}
]
```

## Notes
- The price threshold is 50.0 (inclusive)
- Products with price < 50.0 should be excluded
- Output must be sorted by price in ascending order (lowest to highest)
- Price values should be numbers, not strings
- Ensure the output JSON is properly formatted
