from __future__ import annotations

import math


def queue_acceleration_index(
    pending_t: float | None,
    pending_previous: float | None,
    completions_t: float | None,
) -> float | None:
    """Return QAI = (pending_t - pending_previous) / completions_t.

    QAI is undefined when completions are zero or missing. It is a normalized
    backlog-change signal, not a direct estimate of staffing capacity.
    """
    if pending_t is None or pending_previous is None or completions_t is None:
        return None
    pending = float(pending_t)
    previous = float(pending_previous)
    completions = float(completions_t)
    if not all(math.isfinite(value) for value in (pending, previous, completions)):
        raise ValueError("QAI inputs must be finite")
    if completions < 0:
        raise ValueError("completions_t must be non-negative")
    if completions == 0:
        return None
    return (pending - previous) / completions


def compute_qai_series(records: list[dict[str, object]], pending_key: str = "pending", completions_key: str = "completed") -> list[float | None]:
    values: list[float | None] = []
    previous: float | None = None
    for record in records:
        raw_pending = record.get(pending_key)
        raw_completed = record.get(completions_key)
        pending = None if raw_pending in (None, "") else float(raw_pending)
        completed = None if raw_completed in (None, "") else float(raw_completed)
        if previous is None or pending is None:
            values.append(None)
        else:
            values.append(queue_acceleration_index(pending, previous, completed))
        previous = pending
    return values


METRIC_DOCUMENTATION = {
    "definition": "QAI_t = (Pending_t - Pending_{t-1}) / Completions_t",
    "mathematical_intuition": "Backlog growth normalized by throughput; positive values indicate backlog expansion relative to completed work.",
    "assumptions": ["Pending and completions are comparable over adjacent periods.", "Administrative definitions remain stable enough for period-to-period comparison."],
    "limitations": ["Not a causal capacity estimate.", "Sensitive to reporting-definition changes.", "Cannot identify why backlog changed."],
    "failure_modes": ["Zero completions makes the metric undefined.", "Boundary changes can mimic backlog growth.", "Seasonality can be mistaken for structural pressure."],
    "expected_misuse": "Using QAI alone to claim institutional failure or staff underperformance.",
}
