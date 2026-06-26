# Canonicalization Decisions

Prompt 1 and Prompt 2 identified overlapping research strands around institutional queues, oversight saturation, and AI governance accountability. OICO consolidates them into one observatory.

## Kept

- EOIR and USCIS workload snapshots survive as the v1 QAI queue module.
- CFPB and SEC EDGAR aggregates survive as the v1 SEDI institutional-indicator module.
- ASI corpus manifest and adjudicated matrix survive as the v1 accountability-specificity module.
- Metric definitions and limitations survive in `metric_catalog.csv` and the docs.

## Merged

- Queue Acceleration Index work merges into `oico.metrics.qai` and `queue_observations.csv`.
- Oversight saturation work merges into `oico.metrics.sedi`, `oico.models.authorization`, `oico.models.procedural_capacity`, and `institutional_indicators.csv`.
- AI accountability document coding merges into `oico.metrics.asi` and `asi_scores.csv`.

## Archived By Reference

Original paper drafts, manuscript-specific scripts, and venue-specific formatting assets are not copied into the canonical implementation. They remain prior work and can inform papers, but OICO treats the reproducible data/model layer as canonical.

## Quarantined

- Any source requiring private credentials.
- Any live-fetch script that cannot be run deterministically in CI.
- Any claim of external adoption not backed by a named lab, professor, course, paper, or conference artifact.

## Excluded

- Admissions-portfolio framing.
- Unverified broad claims about AI causing institutional failure.
- Leaderboard marketing before independent labels exist.
