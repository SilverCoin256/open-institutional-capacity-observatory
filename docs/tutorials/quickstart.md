# Quickstart

## Install From The Repository

```bash
python -m pip install -e .
```

No third-party Python dependencies are required for the v1 stable technical release.

Run data, benchmark, figure, and notebook workflows from the repository checkout. If an
automation runner starts elsewhere, set `OICO_PROJECT_ROOT` to the checkout's absolute
path; the value is validated before any files are read or written.

## Reproduce Everything

```bash
python -m oico.cli.main reproduce
```

Expected outputs:

- processed tables in `datasets/processed/`
- data dictionary and source register in `datasets/metadata/`
- validation report in `datasets/validation_reports/`
- SVG figures in `figures/gallery/`
- benchmark baselines in `benchmarks/`
- release audit files in `releases/github/`

## Inspect The Data

```bash
python -m oico.cli.main summary
```

## Compute A Single QAI Value

```bash
python -m oico.cli.main compute-qai --pending 1108300 --previous-pending 975977 --completed 195145
```

## Add A New Dataset

1. Place the raw snapshot under `datasets/raw/`.
2. Add source metadata to the source register configuration in the builder.
3. Map it into a canonical processed table.
4. Add validation rules and documentation.
5. Regenerate checksums and manifests.
