# Number Sort Task

## Objective
Read a text file containing numbers (one per line), sort them in ascending order, and output the sorted numbers as a JSON array.

## Input
- File: `/app/input.txt`
- Format: Text file with one number per line
- Numbers can be integers or decimals
- Empty lines should be ignored

## Output
- File: `/app/output.json`
- Format: JSON array of numbers sorted in ascending order
- Numbers should maintain their original type (integer or decimal)

## Requirements
1. Read the input file from `/app/input.txt`
2. Parse each line as a number (skip empty lines)
3. Sort all numbers in ascending order
4. Write the sorted numbers as a JSON array to `/app/output.json`
5. The output should be a valid JSON file

## Example
Input (`input.txt`):
```
42
3.14
100
7
2.5
```

Expected Output (`output.json`):
```json
[2.5, 3.14, 7, 42, 100]
```

## Notes
- Empty lines in the input should be ignored
- Numbers should be sorted numerically (not lexicographically)
- The output JSON should be properly formatted
- Handle any parsing errors gracefully
