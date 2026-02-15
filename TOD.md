# Harbor Task - JSON Transform

## Task Status

### Completed
- ✅ Created task structure at harbor_tasks/json-transform/
- ✅ task.toml - Task metadata
- ✅ instruction.md - Task instructions
- ✅ environment/Dockerfile - Container setup
- ✅ environment/input.json - Input data
- ✅ solution/solve.sh - Reference solution
- ✅ tests/test.sh - Test runner
- ✅ tests/test_outputs.py - Test cases
- ✅ Ruff linting passed
- ✅ Docker image built successfully
- ✅ Solution tested - output.json created with correct data

### Unable to Complete
- ❌ Oracle test - Requires Python 3.12+ (system has 3.11.9)
- ❌ NOP test - Requires Python 3.12+ (system has 3.11.9)
- ❌ Pull request - No git repository in the project

## Verification
- The solution was tested and produces correct output
- output.json contains the correctly transformed data with id, name, and city fields
- All 5 user records are properly transformed

## Notes
- The task is a simple JSON transform task that extracts id, name, and city fields from input JSON
- The solution uses jq to transform the data
- The Docker image builds successfully
- Ruff linting passes
- The validation tests cannot be run due to Python version mismatch (Harbor requires Python 3.12+)
- No git repository exists to create a PR

## Task Details
- Name: json-transform
- Category: data-processing
- Difficulty: easy
- Input: environment/input.json (JSON array of user objects)
- Output: output.json (JSON array with id, name, city fields)
