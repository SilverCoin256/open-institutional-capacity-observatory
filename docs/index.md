# Open Institutional Capacity Observatory

OICO is a Python package for analysing public records of administrative work. The v1 release contains four public time series and a 23-document corpus on AI governance. The [immigration court case study](FLAGSHIP_CASE_STUDY.md) shows how to reproduce one measure from the recorded inputs.

## What Researchers Can Do

- Reproduce all processed tables from frozen raw snapshots.
- Recompute QAI, SEDI, ASI, authorization-saturation, and procedural-capacity examples.
- Run baseline benchmark tasks with documented limitations.
- Use the data dictionary and source register to extend the observatory to new institutions.
- Teach institutional measurement with a fully inspectable release.

## What Researchers Should Not Do

- Do not treat v1 benchmarks as a mature public leaderboard.
- Do not interpret QAI or SEDI as causal proof of institutional failure.
- Do not rank institutions substantively from the cross-institution demo; the signals are not commensurate yet.
- Do not claim external adoption, citation, or official endorsement until it exists.

## Reproduction

```bash
python -m oico.cli.main reproduce
```

The command rebuilds processed data, deterministic SVG figures, benchmark baselines, release audit files, and the reproduction report.

## Core Tables

- `datasets/processed/institutions.csv`
- `datasets/processed/queue_observations.csv`
- `datasets/processed/institutional_indicators.csv`
- `datasets/processed/asi_scores.csv`
- `datasets/processed/metric_catalog.csv`

## Release Boundary

This is a technically stable release for public review and independent replication. A DOI-bearing archive should wait until an authenticated depositor confirms the source record and final archive contents.
