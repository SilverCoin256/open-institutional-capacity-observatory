# Open Institutional Capacity Observatory

Open Institutional Capacity Observatory (OICO) is a lab-grade research platform for measuring institutional capacity, administrative congestion, oversight saturation, and governance specificity from transparent public data.

The project is intentionally conservative. It provides reproducible datasets, metrics, benchmarks, figures, teaching material, and release metadata, but it does not claim that public traces fully identify institutional quality, causality, staffing capacity, or legal compliance.

## What OICO Measures

- Queue pressure in public adjudicative systems.
- Observable degradation signals in administrative review systems.
- Authorization saturation in AI-governed decision pipelines.
- Procedural-capacity risk under review, contestation, and accountability constraints.
- Accountability specificity in AI governance documents.

## Version 1.0 Scope

Version 1.0 includes five canonical modules:

| Module | Purpose | Status |
|---|---|---|
| QAI | Queue Acceleration Index for public backlog panels | Release candidate |
| SEDI | State-Estimation Degradation Index for public observability traces | Release candidate |
| Authorization Saturation | Queueing model for substantive-to-ceremonial review shifts | Release candidate |
| Procedural Capacity | Transparent risk model for review/contestation/accountability constraints | Release candidate |
| ASI | Accountability Specificity Index aggregation and validation | Release candidate, corpus caveats |

The v1 data package includes EOIR, USCIS, CFPB, SEC, and ASI source snapshots. Invalid or weakly retrieved SSA/Meta snapshots discovered during archaeology are excluded.

## Quick Start

```bash
python -m oico.cli.main build-data
python -m oico.cli.main validate-data
python -m oico.cli.main make-figures
python -m oico.cli.main run-benchmarks
python -m oico.cli.main reproduce
python -m unittest discover -s tests
```

All outputs are generated locally from files in `datasets/raw/`.

## Why This Exists

Researchers studying AI governance, public administration, computational sociology, and organizational bottlenecks repeatedly rebuild the same fragile infrastructure: public-data scraping, queue metrics, provenance registers, validation reports, figure scripts, and teaching examples. OICO packages those foundations into one reproducible ecosystem.

## Scientific Boundaries

OICO metrics are descriptive and diagnostic unless a benchmark or study explicitly supplies stronger identification. In particular:

- QAI is close to normalized backlog change and should not be interpreted as latent capacity by itself.
- SEDI is an index of observable degradation signals, not a direct measure of human effort or intent.
- Authorization and procedural-capacity models are formal thought instruments unless externally calibrated.
- ASI measures textual specificity in documents, not whether institutions behave accordingly.

## Repository Map

```text
oico/                  Python package
datasets/              Raw snapshots, processed data, manifests, checksums
benchmarks/            Frozen task specs, baselines, outputs
docs/                  Research, teaching, API, and release documentation
notebooks/             Executable walkthrough notebooks
papers/                Data descriptor and methods-paper outlines
figures/               Reproducible SVG figure gallery
tests/                 Unit, data, integration, and reproduction tests
website/               Static documentation landing page
releases/              Zenodo, OSF, Dataverse release packets
community/             Contribution and governance materials
```

## Citation

Use the citation metadata in `CITATION.cff`. A DOI should be added only after a real Zenodo, OSF, Dataverse, or journal archive has minted one.

## License

Code is MIT. Derived documentation and dataset metadata are released under CC BY 4.0 unless a source-specific license requires stricter handling. Underlying public datasets retain their original source terms.

