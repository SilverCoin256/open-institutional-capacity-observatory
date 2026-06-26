# Professor Guide

OICO is suitable for a one-week module in computational social science, public administration, AI governance, or reproducibility methods.

## Learning Objectives

- Distinguish public observables from latent institutional capacity.
- Reproduce a research data pipeline from raw snapshots.
- Critique proxy metrics and benchmark labels.
- Compare measurement infrastructure with one-off empirical papers.
- Practice ethical communication of uncertain institutional scores.

## Suggested Class Session

1. Students clone the repository and run `python -m oico.cli.main reproduce`.
2. The class reads `docs/concepts/metrics.md`.
3. Students inspect `datasets/metadata/source_register.csv` and identify provenance gaps.
4. Small groups critique one benchmark task and propose an independent validation design.
5. Students submit a short extension memo for a new institution or domain.

## Assignment

Ask students to add one new public institutional series conceptually, without coding:

- source URL
- license status
- raw variables
- canonical table mapping
- metric choice
- validation risks
- likely misuse

## Grading Rubric

- Provenance and licensing: 25%
- Measurement validity: 25%
- Reproducibility plan: 20%
- Ethical caveats: 15%
- Clarity and extensibility: 15%
