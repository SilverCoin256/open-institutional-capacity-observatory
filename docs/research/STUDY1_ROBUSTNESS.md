# Study 1 Robustness

## Tests completed

1. Recomputed QAI from raw pending and completion counts.
2. Compared QAI with absolute change, percentage backlog growth, clearance ratio, and backlog/completions.
3. Excluded EOIR FY2025/FY2026 from the primary analysis.
4. Preserved missing completions as missing.
5. Calculated within-system associations only.
6. Compared monthly and annual CFPB aggregation.
7. Compared SEC volume with two different intensity signals.

## Results

The EOIR sign pattern remains 8/8 positive under the conventional backlog-growth comparison. The USCIS sign pattern remains 11/11 positive. CFPB's volume/substantive-rate association is positive at both monthly (r=0.650484) and annual (r=0.690828) aggregation, but the aggregation choice changes the exact value. SEC's volume association differs sharply by intensity definition, demonstrating metric sensitivity.

## Tests not defensible with v1

- Leave-one-institution-out validation: the institutions do not share a common outcome or sampling frame.
- Out-of-sample prediction: panels are too small and no pre-specified external target exists.
- Bootstrap confidence intervals for the aggregate queue panel: would give false precision around a tiny, non-independent series.
- Placebo shocks: no independently documented intervention series is aligned to every source.
- Pooled panel model: would violate unit and construct comparability.

## Robustness verdict

The descriptive sign result is stable within the queue snapshots. The general claim that the framework measures institutional capacity is not validated. A stronger study requires independently recovered source histories and external outcomes.
