# OICO v1.0.0

OICO v1.0.0 is a technically stable release of open research software for measuring observable administrative congestion and oversight constraints from reproducible public data.

## Included

- EOIR flagship case study with output table, JSON report, figure, and limitations.
- Stable QAI indicator with explicit descriptive interpretation.
- Beta ASI corpus and experimental SEDI, Authorization Saturation, and Procedural Capacity modules.
- Frozen public-data snapshots, provenance register, license review, schemas, transformations, and checksums.
- Python package, CLI, tests, notebooks, benchmark baselines, teaching material, and static research site.
- Clean-room audit, replication protocol, external-validation tracker, AI disclosure, and JOSS readiness record.

## Evidence boundary

This release does not claim a DOI, external adoption, independent reproduction, causal identification, institutional-quality measurement, or legal-compliance finding. Those states require evidence outside the author's own execution.

## Reproduce

```bash
python -m pip install -e .
oico reproduce
python -m unittest discover -s tests
```
