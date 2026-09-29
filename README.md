# pytest-context-report

`pytest-context-report` is a pytest plugin that adds a compact session summary with test counts, outcome totals, and the slowest test phases.

## Setup

```sh
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -e .
pytest
```

The package registers its `pytest11` entry point during installation, so pytest loads the session reporter automatically. The summary appears after the normal pytest result line.

## Report

The report includes:

- collected, passed, skipped, and failed test counts;
- total and per-phase elapsed time;
- the three slowest test phases.

No configuration is required for the default report.
