# Leaderboard Specification

OICO v1 does not operate a public leaderboard. This file specifies the conditions required before one is launched.

## Required Before Public Ranking

- Independent labels or externally validated targets.
- Frozen train/test splits published in `benchmarks/frozen_splits.csv`.
- Baseline scores produced by `python -m oico.cli.main run-benchmarks`.
- Submission format and metric definitions documented per task.
- License review for any model inputs that include source text.

## Current v1 Status

The current splits and baselines support reproducibility tests, methods tutorials, and classroom assignments. They should not be advertised as evidence of state-of-the-art performance.
