# Flagship Case Study: EOIR Queue Pressure

## Question

Did pending workload grow faster than recorded completions in the frozen annual workload snapshot for the U.S. Executive Office for Immigration Review?

## Observable data

The source snapshot is `datasets/raw/eoir_annual.csv`, registered as `eoir_workload_annual` in `datasets/metadata/source_register.csv`. It contains annual pending, received, and completion counts labeled 2016 through 2026. The release preserves the snapshot rather than silently replacing it with a live endpoint. The authoritative flagship interpretation is restricted to 2016 through 2024: FY2026 is incomplete as of the 2026-08-10 audit date, and the inherited retrieval provenance for the later rows is not independently recoverable.

## Calculation

For each period after the first:

```text
QAI_t = (Pending_t - Pending_(t-1)) / Completions_t
```

The first period is undefined because it has no preceding pending count. QAI is therefore a normalized backlog-change signal. It is close to a familiar descriptive statistic, and that limitation is part of the result rather than something hidden behind a new name.

## Result

In the authoritative window, pending matters rose from 826,488 in 2016 to a peak of 3,925,351 in 2024, a 4.749-fold increase. QAI was positive in all eight comparable periods from 2017 through 2024 and reached 1.580 in 2024. The 2025 and 2026 rows remain in the stored snapshot for audit, but are excluded from the primary inference; their negative QAI values are not treated as proof that the underlying capacity problem was resolved.

The tracked output table is `examples/flagship/outputs/eoir_queue_series.csv`, the machine-readable interpretation is `examples/flagship/outputs/flagship_report.json`, and the figure is `figures/gallery/qai_eoir.svg`.

## Reproduce

From the repository root:

```bash
python -m pip install -e .
oico run-flagship
```

The complete workflow is:

```bash
oico reproduce
```

## Interpretation

The case demonstrates how an openly documented public trace can show backlog pressure relative to recorded throughput. It does not show why the backlog changed. Possible explanations include inflows, reporting changes, staffing, policy, case mix, technology, or other institutional factors.

## Limitations

- The data are a frozen snapshot inherited from prior research, not a newly audited live extraction.
- Annual observations do not identify within-year queue dynamics.
- QAI depends on comparable definitions across periods.
- The presence of a backlog does not by itself establish inadequate staffing or failed oversight.
- Negative later values require source-coverage and reporting-definition review before substantive interpretation.
- QAI is a transparent normalized backlog-change signal, not claimed as mathematically novel.
