# EOIR Frozen-Snapshot Provenance

Audit date: 2026-09-04

OICO preserves `datasets/raw/eoir_annual.csv` as a historical reproducibility artifact. It is not presented as the latest official EOIR release.

## Official source check

The official source family is the U.S. Department of Justice, Executive Office for Immigration Review [Workload and Adjudication Statistics](https://www.justice.gov/eoir/workload-and-adjudication-statistics). The page links the current [Pending Cases, New Cases, and Total Completions PDF](https://www.justice.gov/eoir/media/1344791/dl?inline) and warns that EOIR staff frequently enter and update case-database information, so published statistics are subject to change.

The live PDF retrieved on 2026-09-04 is labelled “Data Generated: July 24, 2026.” Its historical values differ slightly from the preserved OICO rows, including FY2016 pending 826,505 and FY2024 pending 3,924,993. This is expected for a mutable official publication and is precisely why OICO does not silently replace its frozen input.

The preserved artifact contains the earlier publication state associated with the April 22, 2026 EOIR table: FY2016 pending 826,488; FY2024 pending 3,925,351; FY2025 pending 3,723,932; and FY2026 (Second Quarter) pending 3,570,145. The local byte-level checksum is recorded in `datasets/manifests/dataset_manifest.json` and `datasets/checksums/sha256sums.txt`.

## Two windows

- **Frozen artifact window:** all 11 stored rows in the preserved CSV, FY2016 through FY2026 (Second Quarter). Later rows remain available for exact reproduction and audit.
- **Study 1 authoritative inference window:** FY2016-FY2024 only, 9 annual observations and 8 year-to-year transitions. FY2025 and FY2026 are excluded from the authoritative EOIR inference because they are later partial/revised publication states and are not needed for the pre-specified primary result.

The frozen file and the authoritative inference window answer different questions. A current official download should not be expected to reproduce the frozen file without the same historical publication state.
