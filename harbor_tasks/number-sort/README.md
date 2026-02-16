# Number Sort Task

A Harbor data-processing task: read numbers from a text file, sort them in ascending order, and output as a JSON array.

## Task Description

The agent must:
1. Read numbers from `/app/input.txt` (one number per line)
2. Parse and sort the numbers numerically
3. Output the sorted numbers as a JSON array to `/app/output.json`

## Validation (run from repository root)

From **WSL or Linux** (recommended; on Windows, use WSL per assignment prerequisites):

```bash
cd harbor
uv sync
uv run harbor run --agent oracle --path ../harbor_tasks/number-sort --job-name test-oracle
uv run harbor run --agent nop --path ../harbor_tasks/number-sort --job-name test-nop
uvx ruff check ../harbor_tasks/number-sort
```

- **Oracle** should return mean **1.0**
- **NOP** should return mean **0.0**
- **Ruff** should pass with no errors

## Task Structure

```
number-sort/
├── task.toml              # Task metadata
├── instruction.md         # Agent instructions
├── environment/
│   ├── Dockerfile         # Container setup
│   └── input.txt          # Input data (10 numbers)
├── solution/
│   └── solve.sh           # Reference solution (Python-based)
└── tests/
    ├── test.sh            # Test runner
    └── test_outputs.py    # Test cases
```

## Expected Behavior

- Input: 10 numbers (integers and decimals) in random order
- Output: JSON array with numbers sorted in ascending order
- Numbers maintain their original type (integers stay as int, decimals as float)
