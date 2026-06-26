from __future__ import annotations

import math
import random


def procedural_failure_risk(
    ai_output_volume: float,
    review_capacity: float,
    contestation: float,
    accountable_ownership: float,
) -> float:
    """Return an illustrative procedural failure risk in [0, 1].

    Contestation and accountable ownership are normalized safeguards in [0, 1].
    The function is intentionally transparent and conservative: it is a
    benchmark model, not empirical validation.
    """
    values = (ai_output_volume, review_capacity, contestation, accountable_ownership)
    if not all(math.isfinite(value) for value in values):
        raise ValueError("procedural-capacity inputs must be finite")
    if ai_output_volume < 0:
        raise ValueError("ai_output_volume must be non-negative")
    if review_capacity < 0:
        raise ValueError("review_capacity must be non-negative")
    if not 0 <= contestation <= 1 or not 0 <= accountable_ownership <= 1:
        raise ValueError("safeguards must be in [0, 1]")
    if review_capacity == 0:
        return 1.0
    load_ratio = ai_output_volume / review_capacity
    overload = max(0.0, load_ratio - 1.0)
    safeguard = 0.55 * contestation + 0.45 * accountable_ownership
    risk = 1.0 - (1.0 / (1.0 + overload * (2.5 - 1.5 * safeguard)))
    return min(1.0, max(0.0, risk))


def simulate_procedural_days(days: int, seed: int = 20260626) -> list[dict[str, float | int]]:
    if not isinstance(days, int) or days < 0:
        raise ValueError("days must be a non-negative integer")
    rng = random.Random(seed)
    rows: list[dict[str, float | int]] = []
    for day in range(days):
        volume = rng.uniform(80, 180)
        capacity = rng.uniform(90, 130)
        contestation = rng.choice([0.0, 0.5, 1.0])
        ownership = rng.choice([0.0, 0.5, 1.0])
        risk = procedural_failure_risk(volume, capacity, contestation, ownership)
        rows.append(
            {
                "day": day + 1,
                "ai_output_volume": round(volume, 3),
                "review_capacity": round(capacity, 3),
                "contestation": contestation,
                "accountable_ownership": ownership,
                "failure_risk": round(risk, 6),
            }
        )
    return rows


MODEL_DOCUMENTATION = {
    "definition": "Procedural capacity risk is modeled as overload moderated by contestation and accountable ownership safeguards.",
    "mathematical_intuition": "Risk rises nonlinearly when AI output volume exceeds review capacity and falls when procedural safeguards are stronger.",
    "assumptions": ["Safeguards can be represented on a 0-1 scale.", "Overload is the primary pressure mechanism.", "Safeguards reduce but do not erase overload risk."],
    "limitations": ["Illustrative benchmark model, not an empirical estimator.", "No causal claim without external data.", "Does not represent legal heterogeneity."],
    "failure_modes": ["Interpreting synthetic days as observed institutional days.", "Treating safeguard weights as universal."],
    "expected_misuse": "Using the score to certify a live governance system without empirical audit.",
}
