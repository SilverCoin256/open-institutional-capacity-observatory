# OICO v1.1.1

OICO v1.1.1 is the final frozen release of the bounded comparative research layer and stable reproducible software core.

## Included

- EOIR flagship case with explicit FY2016-FY2024 authoritative window.
- Exploratory Study 1 across EOIR, USCIS, CFPB, and SEC frozen snapshots.
- Conventional baselines, within-system associations, noncomparability rules, robustness, falsification, and construct-validity records.
- `oico study1` and `oico reproduce --full`.
- Explicit distinction between the 11-row frozen EOIR artifact window and the FY2016-FY2024 authoritative Study 1 inference window (9 observations, 8 transitions).
- Official EOIR provenance note distinguishing mutable publication from the frozen snapshot used by this release.
- Full Study 1 reproduction on the Python 3.12 CI lane.
- Public Why This Exists page, ultimate baseline/standards audits, ownership audit, and project differentiation scorecard.
- Existing tests, notebooks, checksums, source register, license review, and clean-room release path.

## Evidence boundary

This release does not claim a DOI, PyPI publication, independent reproduction, external adoption, causal identification, institutional-quality measurement, or legal-compliance finding. QAI remains a transparent normalized backlog-change signal, not claimed as new mathematics. ASI is beta; SEDI, Authorization Saturation, and Procedural Capacity remain experimental.

## Reproduce

```bash
python -m pip install -e .
oico reproduce --full
python -m unittest discover -s tests
```
