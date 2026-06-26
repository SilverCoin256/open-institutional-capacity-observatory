# Migration Guide For Future Contributors

## From One-Off Paper To OICO Module

1. Identify the reusable asset: dataset, metric, pipeline, figure, or benchmark.
2. Remove venue-specific formatting.
3. Add source metadata and license notes.
4. Place raw snapshots under `datasets/raw/`.
5. Map outputs into canonical tables.
6. Add validation and tests.
7. Document assumptions and misuse.
8. Add examples or teaching notes only if they are reproducible.

## Naming Rules

- Use stable lowercase identifiers.
- Keep institution names human-readable in data columns.
- Put paper-specific claims in papers, not canonical data tables.

## Deprecation Rules

Duplicate scripts should be archived by reference once a canonical package function exists.
