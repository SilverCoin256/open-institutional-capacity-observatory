# Final Clean-Room Audit

Audit date: 2026-08-10

## Acquisition

- Artifact: `releases/github/oico-1.0.0.tar.gz`
- Archive SHA-256: verified against `releases/github/oico-1.0.0.tar.gz.sha256` and the top-level artifact manifest.
- Environment: macOS 26.5.2 arm64, Python 3.12.13
- Method: extracted into a new temporary directory, created a fresh virtual environment with system site packages, installed the local sdist without an editable checkout, then ran the documented workflow.

## Exact outsider path executed

```bash
python -m pip install --no-index --no-build-isolation /temporary/path/oico-1.0.0
python -m oico.cli.main reproduce
python -m unittest discover -s tests
```

## Results

- Package installation: PASS.
- Import and CLI: PASS.
- Data build and validation: PASS, 5 tables and 23 queue observations.
- Flagship output: PASS, 11 observations, 10 comparable QAI values, 8 positive periods, 2024 peak pending 3,925,351.
- Figures: PASS, six deterministic SVGs.
- Benchmarks: PASS, five baseline tasks.
- Release audit: PASS, no checksum issues and no missing required paths.
- Tests: PASS, 25 tests.
- Notebook execution: PASS in the development release gate; the archive contains all five notebooks and their dependencies are stdlib-only.

## Reference outputs

The expected flagship output checksums are recorded in `replication/reference_manifest.json`. Internal clean-room success is not counted as external validation; the project remains external evidence Level 0 until another person reports an independent attempt.
