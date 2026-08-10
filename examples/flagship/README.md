# EOIR Flagship Example

This directory is the canonical OICO case study. It answers whether pending workload grew faster than recorded completions in the frozen EOIR annual snapshot.

## Run

From the repository root after installation:

```bash
python examples/flagship/run_flagship.py
```

For the complete data, figure, benchmark, notebook, and release workflow, use:

```bash
oico reproduce
```

## Contents

- `run_flagship.py`: documented analysis entrypoint.
- `outputs/eoir_queue_series.csv`: tracked output table.
- `outputs/flagship_report.json`: machine-readable result and limitations.
- `../../docs/FLAGSHIP_CASE_STUDY.md`: interpretation and source provenance.
- `../../replication/reference_manifest.json`: expected output checksums.
- `../../figures/gallery/qai_eoir.svg`: deterministic figure generated from the same processed observations.
