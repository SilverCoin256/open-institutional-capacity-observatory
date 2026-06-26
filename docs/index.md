# Open Institutional Capacity Observatory

OICO is a reproducible public-data platform for measuring institutional capacity, administrative congestion, oversight saturation, and AI-governance accountability.

The v1 release candidate is deliberately narrow. It contains four public institutional time series and one 23-document AI-governance coding corpus. The purpose is to establish a credible, reproducible foundation that another lab can inspect, teach, extend, and critique.

## What Researchers Can Do

- Reproduce all processed tables from frozen raw snapshots.
- Recompute QAI, SEDI, ASI, authorization-saturation, and procedural-capacity examples.
- Run baseline benchmark tasks with documented limitations.
- Use the data dictionary and source register to extend the observatory to new institutions.
- Teach institutional measurement with a fully inspectable release candidate.

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

This is a release candidate for lab review and public-methods hardening. A DOI-bearing release should wait until a repository curator confirms the dated source-license record, benchmark tasks gain independent labels, and at least one external replication attempt is complete.
