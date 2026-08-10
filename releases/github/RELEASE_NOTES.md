# OICO v1.1.0

OICO v1.1.0 adds a bounded comparative research layer to the stable reproducible software core.

## Included

- EOIR flagship case with explicit FY2016-FY2024 authoritative window.
- Exploratory Study 1 across EOIR, USCIS, CFPB, and SEC frozen snapshots.
- Conventional baselines, within-system associations, noncomparability rules, robustness, falsification, and construct-validity records.
- `oico study1` and `oico reproduce --full`.
- Public Why This Exists page, ultimate baseline/standards audits, ownership audit, and project differentiation scorecard.
- Existing tests, notebooks, checksums, source register, license review, and clean-room release path.

## Evidence boundary

This release does not claim a DOI, PyPI publication, independent reproduction, external adoption, causal identification, institutional-quality measurement, or legal-compliance finding. QAI remains a transparent normalized backlog-change signal, not claimed as new mathematics.

## Reproduce

```bash
python -m pip install -e .
oico reproduce --full
python -m unittest discover -s tests
```
