# Pre-Finalization Audit

Audit date: 2026-08-10. Baseline was taken from the public `v1.0.0-rc1` checkout before finalization changes.

## Repository state

- Remote: `https://github.com/SilverCoin256/open-institutional-capacity-observatory`
- Branch: `main`
- Baseline commit: `18b4335` (`Release OICO v1.0.0-rc1`)
- Baseline tag: `v1.0.0-rc1`
- Baseline GitHub release: public prerelease with archive, checksum, and artifact manifest.
- Baseline worktree: clean.

## Baseline checks

| Check | Baseline result | Evidence |
|---|---|---|
| Unit/data/reproduction tests | Pass, 21 tests | Existing local release gate and test suite. |
| Data validation | Pass | `datasets/validation_reports/`. |
| Figure generation | Pass, six SVG figures | `figures/gallery/FIGURE_MANIFEST.md`. |
| Notebook execution | Pass, five notebooks | Existing release gate. |
| Clean-room archive install | Pass | Existing isolated archive validation. |
| Documentation links | Pass | `scripts/check_docs.py`. |
| Secret scan | Pass | `scripts/scan_secrets.py`. |
| Package metadata | Buildable, minimal metadata | `pyproject.toml` lacked URLs, classifiers, and a stable scientific status. |
| Coverage floor | Not enforced | No CI coverage job or threshold existed. |
| Public GitHub metadata | Incomplete | No description, homepage, topics, Pages site, or DOI. |

## Scientific inventory

| Asset | Existing role | Finding |
|---|---|---|
| EOIR and USCIS workload snapshots | Queue observations and QAI | Strongest reproducible descriptive foundation; EOIR selected as flagship. |
| CFPB monthly aggregates | SEDI inputs | Useful exploratory panel, but indicator choice and ground truth are unresolved. |
| SEC yearly counts | Review-intensity signal | Descriptive context, not an institutional capacity estimator. |
| ASI corpus and coding matrix | Textual accountability index | Reusable beta corpus with small sample and coding limitations. |
| Authorization model | Queueing thought experiment | Preserve as experimental scenario analysis until calibrated. |
| Procedural Capacity model | Transparent risk scenario | Preserve as experimental model, not an observed measure. |
| Benchmarks | Teaching and baseline tasks | Keep, but label proxy labels and non-leaderboard status explicitly. |
| Notebooks and SVG figures | Demonstration and communication | Keep as executable public evidence. |

## High-risk findings addressed

1. The opening claim used “lab-grade” without an objective external basis. The public positioning now uses concrete, bounded language.
2. All five modules appeared to have equal maturity. They now have stable, beta, or experimental status.
3. There was no canonical flagship workflow. The EOIR case now has a command, table, report, figure, and limitations.
4. External validation, DOI, PyPI publication, and adoption were not cleanly separated from internal quality. New evidence ledgers do so.
5. The package metadata and CI did not communicate a maintained research-software release. These are now strengthened, with remaining external service states documented honestly.
