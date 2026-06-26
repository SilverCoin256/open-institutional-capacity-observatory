from __future__ import annotations

import math
from statistics import mean, pstdev


def logistic(value: float) -> float:
    if not math.isfinite(value):
        raise ValueError("logistic input must be finite")
    if value >= 0:
        return 1.0 / (1.0 + math.exp(-value))
    exp_value = math.exp(value)
    return exp_value / (1.0 + exp_value)


def zscore(value: float, baseline: list[float]) -> float:
    if not baseline:
        return 0.0
    observed = float(value)
    history = [float(item) for item in baseline]
    if not math.isfinite(observed) or not all(math.isfinite(item) for item in history):
        raise ValueError("SEDI inputs must be finite")
    sd = pstdev(history)
    if sd == 0:
        return 0.0
    return (observed - mean(history)) / sd


def sedi_from_indicators(
    record: dict[str, float],
    baselines: dict[str, list[float]],
    positive_indicators: list[str],
    negative_indicators: list[str],
) -> float:
    """Compute a bounded descriptive degradation index from public indicators.

    Positive indicators are expected to rise under pressure. Negative indicators
    are expected to fall under pressure. The function standardizes each
    indicator against a supplied baseline and maps the mean signal through a
    logistic transform.
    """
    overlap = set(positive_indicators) & set(negative_indicators)
    if overlap:
        raise ValueError(f"indicators cannot have conflicting directions: {sorted(overlap)}")
    signals: list[float] = []
    for key in positive_indicators:
        if key in record and record[key] is not None:
            signals.append(zscore(record[key], baselines.get(key, [])))
    for key in negative_indicators:
        if key in record and record[key] is not None:
            signals.append(-zscore(record[key], baselines.get(key, [])))
    if not signals:
        return 0.5
    return logistic(sum(signals) / len(signals))


def rolling_sedi(
    records: list[dict[str, float]],
    positive_indicators: list[str],
    negative_indicators: list[str],
    window: int = 12,
) -> list[float | None]:
    if not isinstance(window, int) or window < 2:
        raise ValueError("window must be an integer of at least 2")
    output: list[float | None] = []
    keys = positive_indicators + negative_indicators
    for idx, record in enumerate(records):
        if idx < window:
            output.append(None)
            continue
        history = records[max(0, idx - window) : idx]
        baselines = {key: [row[key] for row in history if key in row] for key in keys}
        output.append(sedi_from_indicators(record, baselines, positive_indicators, negative_indicators))
    return output


METRIC_DOCUMENTATION = {
    "definition": "SEDI is a bounded index of public degradation signals after baseline standardization.",
    "mathematical_intuition": "Stress indicators are z-scored upward; health indicators are z-scored downward; their average is mapped to [0, 1].",
    "assumptions": ["Selected public indicators plausibly move with oversight pressure.", "The rolling baseline is a defensible local comparison set."],
    "limitations": ["Not a latent-ground-truth estimator unless externally validated.", "Indicator selection is theory-laden.", "Institutional reporting changes can dominate the index."],
    "failure_modes": ["Short histories produce unstable baselines.", "Missing indicators reduce interpretability.", "A single operational shock can be mistaken for saturation."],
    "expected_misuse": "Treating SEDI as proof of intentional neglect, legal noncompliance, or causal AI impact.",
}
