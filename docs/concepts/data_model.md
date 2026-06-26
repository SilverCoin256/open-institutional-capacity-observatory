# Canonical Data Model

The v1 data model is intentionally small but future-proofed around institutional measurement.

## Entities

- `institutions`: agencies, regulators, or corpora represented by OICO.
- `queue_observations`: workload queues with pending, received, completed, and QAI fields.
- `institutional_indicators`: public signals such as complaint volume, relief proxy, timeliness proxy, review intensity, and SEDI.
- `asi_scores`: document-level AI governance accountability scores.
- `metric_catalog`: formal metric documentation and misuse warnings.

## Ontology Boundary

OICO treats institutions as observable systems with public traces:

- workload pressure
- throughput
- oversight output
- substantive proxy outcomes
- governance text
- procedural safeguards
- provenance and data quality

The model does not assume that every institution exposes the same variables. New domains should add mapped indicators first, then only add new tables when the existing schema cannot represent the phenomenon without distortion.

## Extension Rules

1. Add a source register row before adding processed data.
2. Preserve raw snapshots and checksums.
3. Map new variables to an existing table where possible.
4. Add metric documentation before adding a metric result.
5. Mark proxy labels as proxy labels unless independently validated.

## Source Rights

The source-by-source redistribution basis and unresolved caveats are recorded in
[`datasets/metadata/license_review.md`](../../datasets/metadata/license_review.md).
Review it alongside the source register before publishing or depositing derived data.
