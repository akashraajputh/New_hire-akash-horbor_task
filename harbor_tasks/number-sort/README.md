# Number Sort Task

A Harbor data-processing task: read numbers from a text file, sort them in ascending order, and output as a JSON array.

## Overview

This task requires an agent to:
1. Read numbers from `/app/input.txt` (one number per line)
2. Parse and sort the numbers numerically (not lexicographically)
3. Output the sorted numbers as a JSON array to `/app/output.json`

**Difficulty:** Easy  
**Category:** data-processing  
**Tags:** numbers, sorting, json

## Task Description

The input file contains numbers (both integers and decimals) in random order, one per line. The agent must:
- Parse each line as a number (skip empty lines)
- Sort all numbers in ascending numerical order
- Write the sorted numbers as a JSON array
- Maintain number types (integers as int, decimals as float)

## Example

**Input** (`/app/input.txt`):
```
42
3.14
100
7
2.5
```

**Expected Output** (`/app/output.json`):
```json
[2.5, 3.14, 7, 42, 100]
```

## Validation

Run validation tests from the repository root:

From **WSL or Linux** (recommended; on Windows, use WSL per assignment prerequisites):

```bash
cd harbor
uv sync
uv run harbor run --agent oracle --path ../harbor_tasks/number-sort --job-name test-oracle
uv run harbor run --agent nop --path ../harbor_tasks/number-sort --job-name test-nop
uvx ruff check ../harbor_tasks/number-sort
```

**Expected Results:**
- **Oracle** should return mean **1.0** (solution works correctly)
- **NOP** should return mean **0.0** (no solution executed, tests fail)
- **Ruff** should pass with no errors

## Task Structure

```
number-sort/
├── task.toml              # Task metadata (memory_mb: 256, storage_mb: 128)
├── instruction.md         # Detailed agent instructions
├── environment/
│   ├── Dockerfile         # Container setup (Ubuntu 22.04, Python 3, jq)
│   └── input.txt          # Input data (10 numbers: integers and decimals)
├── solution/
│   └── solve.sh           # Reference solution (Python-based)
└── tests/
    ├── test.sh            # Test runner script
    └── test_outputs.py    # Comprehensive test cases
```

## Test Coverage

The test suite (`test_outputs.py`) validates:
- ✓ Output file exists at `/app/output.json`
- ✓ Output is valid JSON
- ✓ Output is a non-empty array
- ✓ Numbers are sorted in ascending order
- ✓ All input numbers are present in output
- ✓ Number types are preserved (int vs float)

## Requirements

- Uses absolute paths (`/app/input.txt`, `/app/output.json`)
- Solution computes answer dynamically (not hardcoded)
- Dockerfile does not copy `tests/` or `solution/` folders
- Handles empty lines gracefully
- Maintains number type distinction (integers vs floats)

## Solution Approach

The reference solution (`solution/solve.sh`) uses Python to:
1. Read the input file line by line
2. Strip whitespace and skip empty lines
3. Convert each line to a float, then to int if it's a whole number
4. Sort the numbers numerically
5. Write the sorted array as JSON

**Key Implementation Details:**
- Uses `float()` conversion to handle both integers and decimals
- Preserves type by converting whole numbers back to `int`
- Uses Python's built-in `sort()` for numerical sorting
- Uses `json.dump()` for proper JSON formatting

## Validation Results

After running the validation tests, check the results:

```bash
# View Oracle test results
cat jobs/test-oracle/result.json | jq '.stats.evals.oracle__adhoc.metrics[0].mean'
# Expected: 1.0

# View NOP test results  
cat jobs/test-nop/result.json | jq '.stats.evals.nop__adhoc.metrics[0].mean'
# Expected: 0.0
```

**Success Criteria:**
- ✅ Oracle test: Mean reward = **1.0** (confirms solution works)
- ✅ NOP test: Mean reward = **0.0** (confirms task doesn't auto-pass)
- ✅ Ruff linting: No errors

## Troubleshooting

**Common Issues:**

1. **Test fails with "output.json not found"**
   - Ensure the solution writes to `/app/output.json` (absolute path)
   - Check that the script has proper error handling

2. **Numbers not sorted correctly**
   - Verify numerical sorting (not string/lexicographic sorting)
   - Ensure decimals are handled properly (e.g., 2.5 < 3.14)

3. **Type errors in tests**
   - Integers should remain as `int` type in JSON
   - Decimals should remain as `float` type in JSON
   - Use `json.dump()` not `json.dumps()` for proper type preservation

4. **Docker build fails**
   - Ensure Dockerfile doesn't copy `tests/` or `solution/` directories
   - Verify all required packages are installed (python3, jq)

## Quick Reference

**Input File:** `/app/input.txt`  
**Output File:** `/app/output.json`  
**Solution Script:** `solution/solve.sh`  
**Test Script:** `tests/test.sh`  
**Test Cases:** `tests/test_outputs.py`

**Key Files:**
- `task.toml` - Task configuration (timeouts, memory, storage)
- `instruction.md` - Detailed instructions for the agent
- `environment/Dockerfile` - Container environment setup
- `environment/input.txt` - Test input data

## Implementation Tips

1. **Use Python for simplicity** - Python's `json` module handles type preservation automatically
2. **Handle edge cases** - Empty lines, invalid numbers, mixed types
3. **Test locally first** - Run the solution script manually before validation
4. **Check JSON format** - Ensure proper formatting (no trailing commas, valid syntax)

## Notes

- Empty lines in input should be ignored
- Numbers must be sorted numerically, not lexicographically
- Output JSON should be properly formatted
- Parsing errors should be handled gracefully
- The task uses absolute paths as required by Harbor specifications
- Solution must compute the answer dynamically (no hardcoded values)
