# Reproducibility Contract

OICO treats reproducibility as a release property, not a promise that every public source is complete or timeless.

## Clean checkout workflow

After installing Python 3.10 or newer, run:

```bash
python -m pip install -e .
oico reproduce
python -m unittest discover -s tests
```

`oico reproduce` rebuilds processed tables from the frozen raw snapshots, validates schemas and checksums, regenerates deterministic SVG figures, runs baseline benchmark tasks, writes the EOIR flagship outputs, packages the release, and runs the release audit.

The expanded research workflow is:

```bash
oico reproduce --full
```

This additionally runs the exploratory cross-institution Study 1 analysis. Study 1 keeps EOIR, USCIS, CFPB, and SEC in separate within-system analyses because their units and outcomes are not commensurate.

## Provenance

Inputs are listed in `datasets/metadata/source_register.csv`. The dataset manifest and SHA-256 file record source snapshots and processed outputs. `datasets/metadata/transformation_log.md` describes the raw-to-processed transformations. The license review records redistribution scope and unresolved source-specific caveats. For EOIR, `datasets/metadata/eoir_snapshot_provenance.md` distinguishes the 11-row frozen artifact window from the FY2016-FY2024 authoritative Study 1 inference window and records why the live official publication may differ.

## Determinism

Release archives normalize archive ownership and timestamps. Figures and tabular outputs are generated from tracked inputs. The reproduction manifest records the software version, input manifest, generated artifacts, and release-audit result. Execution time is not used as an analytical input.

## Independent environment

The clean-room audit uses a temporary directory and a fresh virtual environment with no editable checkout imports or developer caches. The test matrix covers Python 3.10, 3.11, and 3.12 in GitHub Actions. An independent researcher should report the exact tag or commit, operating system, Python version, install route, checksums, and deviations.

## Reproducibility boundaries

Reproducing an OICO result means reproducing the stored snapshot and transformations. It does not mean that the original agencies will return identical live data, that linked third-party documents remain available, or that a descriptive index has become a validated causal measure.
