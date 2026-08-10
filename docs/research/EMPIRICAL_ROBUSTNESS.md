# Empirical Robustness Audit

Audit date: 2026-08-10.

## Estimand

The estimand is descriptive: the change in reported EOIR pending matters between adjacent fiscal years, scaled by reported completions in the later year:

```text
QAI_t = (Pending_t - Pending_(t-1)) / Completions_t
```

This is not a latent capacity estimate and is not a causal estimand.

## Analysis window

The authoritative window is FY2016-FY2024. The frozen file contains FY2025 and FY2026 rows, but those rows are not treated as completed observations for this audit: FY2026 is not a complete fiscal year as of 2026-08-10, and the inherited snapshot has no recoverable retrieval timestamp or independent provenance trail for the later rows. They remain in the v1 archive so that the released artifact is not silently rewritten.

## Results

| Quantity | Result |
|---|---:|
| Observations in authoritative window | 9 |
| Comparable transitions | 8 |
| Pending matters, FY2016 | 826,488 |
| Peak pending matters | 3,925,351 in FY2024 |
| Peak / FY2016 pending | 4.749435x |
| Positive QAI transitions | 8 of 8 |
| Mean QAI | 1.095125 |
| Population SD of QAI | 0.302332 |
| Peak QAI | 1.579835 in FY2024 |

## Baseline and sensitivity checks

The following alternatives use the same eight transitions:

| Signal | Positive transitions | Pearson correlation with QAI |
|---|---:|---:|
| Raw pending change | 8 | 0.824706 |
| Pending change / prior pending | 8 | 0.893965 |
| Pending change / average pending | 8 | 0.910023 |
| Pending change / current plus prior completions | 8 | 0.942698 |

Every denominator choice preserves the positive/negative sign pattern. This is a robustness result for the direction of the descriptive pattern, not evidence that QAI captures a distinct construct. The correlations are expected because all alternatives are transformations of the same two-period workload observations.

## Leave-one-transition-out check

Dropping one transition at a time leaves the mean QAI between 0.727432 and 1.095125. Dropping any of the 2017-2024 transitions leaves 7 positive transitions; dropping either excluded later transition is not part of the authoritative check. The sample is too small for a meaningful asymptotic confidence interval, external generalization, or model selection claim.

## Falsification criteria

The flagship interpretation should be weakened or withdrawn if any of the following occur:

1. The agency source revises the pending or completion definitions so adjacent values are not comparable.
2. An independent extraction shows material disagreement with the frozen values and the discrepancy cannot be reconciled by a documented revision.
3. A complete authoritative series shows that the sign pattern is an artifact of snapshot or boundary errors.
4. The observed result disappears under a preregistered, substantively justified denominator or a complete alternate source.
5. Independent replication identifies a calculation or provenance error.

## Conclusion

The descriptive direction is stable across simple normalizations within this snapshot. The evidence does not support a claim of causal institutional capacity, staffing failure, governance quality, or AI effect. The reproducible value is the auditability of the data-to-claim path and the explicit separation of observable workload pressure from latent institutional interpretation.
