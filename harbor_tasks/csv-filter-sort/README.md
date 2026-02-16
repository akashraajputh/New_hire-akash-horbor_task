# CSV Filter and Sort Task

A Harbor data-processing task: read a CSV, filter by price ≥ 50, sort by price, write JSON.

## Validation (run from repository root)

From **WSL or Linux** (recommended; on Windows, use WSL per assignment prerequisites):

```bash
cd harbor
uv sync
uv run harbor run --agent oracle --path ../harbor_tasks/csv-filter-sort --job-name test-oracle
uv run harbor run --agent nop --path ../harbor_tasks/csv-filter-sort --job-name test-nop
uvx ruff check ../harbor_tasks/csv-filter-sort
```

- **Oracle** should return mean **1.0**
- **NOP** should return mean **0.0**
- **Ruff** should pass with no errors
