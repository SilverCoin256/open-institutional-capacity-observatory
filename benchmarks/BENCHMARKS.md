# OICO Benchmarks

These are baseline tasks for reproducibility, teaching, and method comparison.
They are intentionally conservative: v1 contains small public-data pilots and proxy labels, not hidden ground truth.

| task | baseline | metric | caveat |
|---|---|---|---|
| `queue_forecasting` | Persistence baseline: QAI_t_hat = QAI_{t-1}. | mean_absolute_error | Small v1 sample; intended as a format and baseline, not a leaderboard-quality forecasting corpus. |
| `saturation_detection` | Threshold SEDI at 0.5 against institution-specific median proxy labels. | accuracy_against_proxy_labels | Labels are proxy labels derived from SEDI distribution, not independent ground truth. |
| `intervention_simulation` | Deterministic scenario grid plus seeded procedural-risk simulation. | mean_quality_and_mean_failure_risk | Synthetic benchmark only; parameters are not calibrated to a live institution. |
| `accountability_specificity` | Median training-set total ASI score. | mean_absolute_error | V1 corpus is small and useful mainly for codebook testing and teaching; text-feature baselines require source-text licensing review. |
| `cross_institution_comparison` | Rank the latest available QAI or SEDI signal within each institution. | descriptive_ranking_only | QAI and SEDI are not directly commensurate; ranking is for interface testing, not substantive comparison. |

## Leaderboard Policy

No public leaderboard should be advertised until independent labels, frozen train/test splits, and data-license review are complete.
For v1, benchmark results are regression tests and classroom exercises.
