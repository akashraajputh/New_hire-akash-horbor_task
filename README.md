# Harbor Task Repository

This repository contains custom Harbor tasks and examples for evaluating agents and language models using the [Harbor framework](https://github.com/laude-institute/harbor).

## Overview

Harbor is a framework for evaluating and optimizing agents and language models in container environments. This repository includes:

- **Harbor Framework** - The core Harbor framework in the `harbor/` directory
- **Custom Tasks** - Example Harbor tasks in the `harbor_tasks/` directory

## Custom Tasks

### Available Tasks

1. **number-sort** - A data-processing task that reads numbers from a text file, sorts them numerically, and outputs a JSON array.
   - **Difficulty:** Easy
   - **Category:** data-processing
   - **Location:** [`harbor_tasks/number-sort/`](harbor_tasks/number-sort/)
   - **Documentation:** [`harbor_tasks/number-sort/README.md`](harbor_tasks/number-sort/README.md)

2. **csv-filter-sort** - A data-processing task that reads a CSV file, filters products by minimum price, sorts them, and writes JSON output.
   - **Difficulty:** Medium
   - **Category:** data-processing
   - **Location:** [`harbor_tasks/csv-filter-sort/`](harbor_tasks/csv-filter-sort/)
   - **Documentation:** [`harbor_tasks/csv-filter-sort/README.md`](harbor_tasks/csv-filter-sort/README.md)

3. **json-transform** - A data-processing task that transforms JSON data by extracting specific fields.
   - **Location:** [`harbor_tasks/json-transform/`](harbor_tasks/json-transform/)

## Getting Started

### Prerequisites

- **Docker** - [Install Docker Desktop](https://www.docker.com/products/docker-desktop)
- **uv** - Install with: `curl -LsSf https://astral.sh/uv/install.sh | sh`
- **WSL** (Windows users) - Run `wsl --install` in PowerShell as Administrator

### Running a Custom Task

1. Navigate to the harbor directory:
   ```bash
   cd harbor
   ```

2. Install dependencies:
   ```bash
   uv sync
   ```

3. Run validation tests:
   ```bash
   # Oracle test (should return 1.0)
   uv run harbor run --agent oracle --path ../harbor_tasks/number-sort --job-name test-oracle
   
   # NOP test (should return 0.0)
   uv run harbor run --agent nop --path ../harbor_tasks/number-sort --job-name test-nop
   
   # Linting
   uvx ruff check ../harbor_tasks/number-sort
   ```

## Harbor Framework

For detailed information about the Harbor framework, see [`harbor/README.md`](harbor/README.md).

### Quick Start with Harbor

```bash
# Install Harbor
uv tool install harbor

# Run Terminal-Bench-2.0
export ANTHROPIC_API_KEY=<YOUR-KEY>
harbor run --dataset terminal-bench@2.0 \
   --agent claude-code \
   --model anthropic/claude-opus-4-1 \
   --n-concurrent 4
```

## Project Structure

```
.
├── harbor/                    # Harbor framework source code
│   └── README.md             # Harbor framework documentation
├── harbor_tasks/             # Custom Harbor tasks
│   ├── number-sort/         # Number sorting task
│   ├── csv-filter-sort/      # CSV filtering and sorting task
│   └── json-transform/     # JSON transformation task
└── README.md                 # This file
```

## Creating Your Own Task

To create a new Harbor task:

1. Create a directory in `harbor_tasks/<your-task-name>/`
2. Follow the structure:
   ```
   your-task-name/
   ├── task.toml              # Task metadata
   ├── instruction.md         # Instructions for the agent
   ├── environment/
   │   ├── Dockerfile         # Container setup
   │   └── input.txt          # Input data
   ├── solution/
   │   └── solve.sh           # Reference solution
   └── tests/
       ├── test.sh            # Test runner
       └── test_outputs.py   # Test cases
   ```
3. See [`harbor_tasks/number-sort/`](harbor_tasks/number-sort/) for a complete example

## Validation

Each task should pass:
- ✅ **Oracle test** - Returns mean reward of 1.0 (solution works)
- ✅ **NOP test** - Returns mean reward of 0.0 (task doesn't auto-pass)
- ✅ **Ruff linting** - No errors

## Contributing

When adding a new task:
1. Ensure it follows the Harbor task structure
2. Include comprehensive tests
3. Add a README.md with documentation
4. Validate with Oracle and NOP tests
5. Ensure linting passes

## License

See the Harbor framework license in [`harbor/`](harbor/) directory.

## Resources

- [Harbor Documentation](https://harborframework.com/docs)
- [Harbor GitHub Repository](https://github.com/laude-institute/harbor)
- [Terminal-Bench-2.0](https://github.com/laude-institute/terminal-bench-2)
