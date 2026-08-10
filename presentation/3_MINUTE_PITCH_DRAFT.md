# Three-Minute Pitch Draft

## 0:00-0:30 - Problem

Institutions increasingly publish fragments of their workload: what arrived, what was completed, and what remains pending. Researchers can usually calculate a ratio, but reproducing the source, transformation, license, figure, and limitation often requires rebuilding the same infrastructure from scratch. A number can look precise while its provenance and construct validity remain unclear.

## 0:30-1:05 - Question

Can an open, reproducible package measure observable administrative workload pressure while keeping the boundary between a public trace and institutional capacity explicit?

## 1:05-1:45 - What I built

OICO is a Python package and research artifact. It contains frozen public snapshots, checksums, schemas, source and license notes, deterministic transformations, a CLI, tests, executable notebooks, benchmark pilots, figures, release archives, and a public reproduction route. The package assigns different evidence statuses: QAI is stable as a descriptive flow metric; ASI is beta; several models remain experimental.

## 1:45-2:20 - Empirical case

The flagship uses a frozen EOIR annual workload snapshot. Pending matters rose from 826,488 in FY2016 to 3,925,351 in FY2024, or 4.749 times the starting value. Across the eight comparable FY2017-FY2024 transitions, pending change was positive and QAI was positive, reaching 1.579835 in FY2024. Alternative simple denominators preserve the sign pattern.

## 2:20-2:45 - What the result means

It means reported pending workload expanded relative to recorded completions in that frozen window. It does not identify staffing, case mix, causes, quality, intent, legal compliance, or AI impact. The later snapshot rows are preserved but excluded from the authoritative claim because their provenance is not independently recoverable and FY2026 is incomplete.

## 2:45-3:00 - Contribution and invitation

The contribution is the auditable measurement and replication infrastructure around a bounded descriptive result, not a claim that QAI is new mathematics. OICO is public and ready for an outside researcher to reproduce, challenge, or extend. The next milestone is not another feature. It is the first independently documented validation.
