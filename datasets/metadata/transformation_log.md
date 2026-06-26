# Transformation Log

Generated at: 2026-07-01T00:00:00+00:00
OICO version: 1.0.0-rc1

## Raw Inputs

- `datasets/raw/eoir_annual.csv` -> sha256 `512e19dbfe1d5d0065dfa4320460a188510ba231104868b44d76490f1e1712f1`; Inherited from prior QAI research package and frozen as a v1 reproducibility snapshot.
- `datasets/raw/uscis_quarterly.csv` -> sha256 `dc51a54a1aad1fb0e9ce20e0e4e17d1eab8388d5376a6fc69bf79a2a962fb14a`; Inherited from prior QAI research package and frozen as a v1 reproducibility snapshot.
- `datasets/raw/cfpb_monthly.csv` -> sha256 `68b2fbc3d59af567bb4207179d4ffe1ae68a635c5cf2be70209c715aa4de5857`; Inherited from prior oversight-saturation analysis and frozen as a v1 reproducibility snapshot.
- `datasets/raw/sec_yearly.csv` -> sha256 `7cdec41e31058401c23d291388c4d76c40b02d9cc6bb404618ede81fec6422ac`; Inherited from prior oversight-saturation analysis and frozen as a v1 reproducibility snapshot.
- `datasets/raw/asi_corpus_manifest.csv` -> sha256 `23fe6ee96dab46bc5c304b608df13c50352413967009e809da739503ad227e36`; Inherited from AIES accountability-specificity reproducibility package.
- `datasets/raw/asi_adjudicated_matrix.csv` -> sha256 `9756b6af0601c0fc64c3a435393f3fa839650dff240dec90c56a892ddb575a3d`; Adjudicated 23-document matrix from AIES reproducibility package.

## Processing Steps

1. EOIR and USCIS workload snapshots are normalized into `queue_observations.csv`.
2. QAI is recomputed from pending and completion counts; inherited rounded QAI values are retained for audit.
3. CFPB monthly complaint aggregates are normalized into `institutional_indicators.csv` with volume, timely-response proxy, relief proxy, and rolling SEDI.
4. SEC EDGAR yearly counts are normalized into `institutional_indicators.csv` with review intensity and expanding-baseline SEDI.
5. ASI document manifest and adjudicated coding matrix are joined into `asi_scores.csv`; ASI totals are recomputed from the eight dimensions.
6. A machine-readable manifest and checksum file are regenerated from raw, processed, metadata, benchmark, and figure artifacts.

## Non-Transformations

- The v1 pipeline does not re-fetch live agency data. It reproduces the release from frozen source snapshots.
- No private credentials, personal tokens, or authenticated APIs are required.
- No adoption, citation, or external-use claims are inferred from the existence of the repository.

## Outputs

- institutions: `datasets/processed/institutions.csv`
- queue_observations: `datasets/processed/queue_observations.csv`
- institutional_indicators: `datasets/processed/institutional_indicators.csv`
- asi_scores: `datasets/processed/asi_scores.csv`
- metric_catalog: `datasets/processed/metric_catalog.csv`
- source_register: `datasets/metadata/source_register.csv`
- schema: `datasets/metadata/schema.csv`
