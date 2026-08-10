# Research Integration

## Closest existing research line

The closest OICO research line is the prior queue and benchmark work on administrative workload, especially the EOIR and USCIS backlog observations. OICO does not retroactively claim that every earlier manuscript used the package.

## Current integration

OICO now incorporates the public reproduction pipeline for the EOIR workload analysis:

- Research question: whether pending workload grew faster than recorded completions.
- OICO component: stable QAI and the flagship runner.
- Data: frozen `datasets/raw/eoir_annual.csv` snapshot, with source-register provenance.
- Analysis: adjacent-period pending change divided by recorded completions.
- Result: pending workload rises to a 2024 peak of 3,925,351, while QAI is positive in eight comparable periods from 2017 through 2024.
- Exact path: `oico reproduce` or `oico run-flagship`.

## Boundaries

This integration demonstrates reproducible infrastructure around a descriptive analysis. It does not claim that the original paper or any unpublished manuscript was authored with OICO, and it does not transform QAI into a causal capacity estimate.
