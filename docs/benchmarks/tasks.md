# Benchmark Tasks

OICO v1 includes five benchmark-shaped tasks. They exist to make methods comparable and teachable, not to claim a mature leaderboard.

## Queue Forecasting

Problem: predict next-period QAI from public workload history.

Baseline: persistence, where the next QAI equals the previous QAI.

Metric: mean absolute error.

Expected output: a table with institution, period, actual QAI, and predicted QAI.

Limitation: v1 sample size is small.

## Saturation Detection

Problem: detect high-degradation periods from public institutional indicators.

Baseline: threshold SEDI at 0.5.

Metric: accuracy against institution-specific median proxy labels.

Expected output: period-level proxy labels and predictions.

Limitation: proxy labels are not independent ground truth.

## Intervention Simulation

Problem: compare simple capacity and quality interventions in an authorization-saturation model.

Baseline: deterministic scenario grid and seeded procedural-risk days.

Metric: mean authorization quality and mean procedural failure risk.

Limitation: synthetic only.

## Accountability Specificity

Problem: predict held-out document ASI totals.

Baseline: median training-set ASI score.

Metric: mean absolute error.

Expected output: document-level held-out predictions.

Limitation: the corpus is small and text-feature models require source-text licensing review.

## Cross-Institution Comparison

Problem: produce a versioned stress-signal ranking across available public series.

Baseline: latest QAI or SEDI signal per institution.

Metric: descriptive ranking only.

Limitation: QAI and SEDI are not directly commensurate.
