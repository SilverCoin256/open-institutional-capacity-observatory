# Example Solution

This solution shows the expected level of reasoning. Students should not copy the specific examples.

## Reproduction

The release is reproduced with:

```bash
python -m oico.cli.main reproduce
```

The validation report should pass, while retaining warnings where source snapshots are incomplete.

## Dataset Trace

Example: EOIR workload data starts as `datasets/raw/eoir_annual.csv`, is normalized into `datasets/processed/queue_observations.csv`, and is documented in `datasets/metadata/source_register.csv` and `datasets/metadata/transformation_log.md`.

## Metric Critique

QAI is useful because it normalizes backlog change by completions. It is limited because it cannot identify whether backlog change is caused by arrivals, staffing, policy, reporting changes, or operational disruption.

## Benchmark Critique

The saturation detection task uses proxy labels derived from SEDI distribution. It is useful for teaching and regression tests, but it should not be treated as independently labeled ground truth.

## Extension Proposal

A credible extension would add a public benefits-appeals queue if the source reports pending cases and completions over adjacent periods. The extension must document source terms, checksums, missing periods, and any definition changes.
