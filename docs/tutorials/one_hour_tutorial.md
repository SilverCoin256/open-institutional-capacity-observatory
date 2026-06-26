# One-Hour Tutorial

## Audience

Graduate students, research assistants, and policy researchers who need a fast but honest introduction to reproducible institutional measurement.

## Agenda

### 0-10 Minutes: Reproduce

Run:

```bash
python -m oico.cli.main reproduce
```

Inspect `releases/github/reproduction_report.json`.

### 10-25 Minutes: Trace One Dataset

Open:

- `datasets/raw/eoir_annual.csv`
- `datasets/processed/queue_observations.csv`
- `datasets/metadata/transformation_log.md`

Question: which assumptions are needed before QAI is interpretable?

### 25-40 Minutes: Critique One Metric

Read `docs/concepts/metrics.md`.

Pick QAI, SEDI, or ASI and identify one valid use and one misuse.

### 40-55 Minutes: Run A Baseline

Run:

```bash
python -m oico.cli.main run-benchmarks
```

Inspect one `baseline_results.json` file.

### 55-60 Minutes: Exit Ticket

Write one source you would add, one validation risk, and one reason a professor should or should not assign OICO.
