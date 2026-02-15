# JSON Transform Task

## Objective
Transform the input JSON data by extracting specific fields and restructuring them into a new format.

## Input
- File: `/app/input.json`
- Format: JSON array of user objects with fields: id, name, email, age, city

## Output
- File: `/app/output.json`
- Format: JSON array with only essential fields: id, name, city

## Requirements
1. Read the input JSON file from `/app/input.json`
2. Extract the following fields from each user object: id, name, city
3. Create a new JSON array with the extracted fields
4. Write the transformed data to `/app/output.json`
5. The output should be a valid JSON file

## Example
Input:
```
json
[
  {"id": 1, "name": "John Doe", "email": "john@example.com", "age": 30, "city": "New York"},
  {"id": 2, "name": "Jane Smith", "email": "jane@example.com", "age": 25, "city": "Los Angeles"}
]
```

Expected Output:
```
json
[
  {"id": 1, "name": "John Doe", "city": "New York"},
  {"id": 2, "name": "Jane Smith", "city": "Los Angeles"}
]
```

## Notes
- Do not modify the original input file
- Ensure the output JSON is properly formatted
- Handle any errors gracefully
