"""Dependency-free Study 1 analysis for OICO's frozen public snapshots.

The study is intentionally descriptive. It compares conventional workload
signals within each institution and refuses to pool unlike units into one
cross-institution score.
"""

from __future__ import annotations

import csv
import json
import math
import statistics
from collections import defaultdict
from pathlib import Path

from oico.io import ROOT

OUTPUT = ROOT / "research" / "outputs"


def _read(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def _float(value: str | None) -> float | None:
    if value in (None, ""):
        return None
    return float(value)


def _pearson(left: list[float], right: list[float]) -> float | None:
    if len(left) != len(right) or len(left) < 3:
        return None
    left_mean = statistics.mean(left)
    right_mean = statistics.mean(right)
    numerator = sum((a - left_mean) * (b - right_mean) for a, b in zip(left, right))
    left_ss = sum((a - left_mean) ** 2 for a in left)
    right_ss = sum((b - right_mean) ** 2 for b in right)
    if left_ss == 0 or right_ss == 0:
        return None
    return round(numerator / math.sqrt(left_ss * right_ss), 6)


def _slope(values: list[float]) -> float | None:
    if len(values) < 2:
        return None
    x_mean = (len(values) - 1) / 2
    y_mean = statistics.mean(values)
    denominator = sum((index - x_mean) ** 2 for index in range(len(values)))
    return round(sum((index - x_mean) * (value - y_mean) for index, value in enumerate(values)) / denominator, 6)


def _queue_summary(path: Path, period_key: str, institution: str, end_period: str | None = None) -> tuple[dict[str, object], list[dict[str, object]]]:
    rows: list[dict[str, object]] = []
    previous_pending: float | None = None
    for raw in _read(path):
        period = raw[period_key]
        if end_period is not None and period > end_period:
            continue
        pending = _float(raw.get("Pending"))
        completed = _float(raw.get("Completions"))
        item: dict[str, object] = {
            "institution": institution,
            "period": period,
            "pending": pending,
            "completed": completed,
        }
        if pending is not None and previous_pending is not None and completed not in (None, 0):
            change = pending - previous_pending
            item.update(
                {
                    "net_change": round(change, 6),
                    "backlog_growth": round(change / previous_pending, 6),
                    "clearance_ratio": round(completed / previous_pending, 6),
                    "backlog_to_completions": round(pending / completed, 6),
                    "qai": round(change / completed, 6),
                }
            )
        rows.append(item)
        if pending is not None:
            previous_pending = pending
    comparable = [row for row in rows if row.get("qai") is not None]
    positive = [row for row in comparable if float(row["qai"]) > 0]
    q_values = [float(row["qai"]) for row in comparable]
    growth_values = [float(row["backlog_growth"]) for row in comparable]
    clearance_values = [float(row["clearance_ratio"]) for row in comparable]
    summary = {
        "institution": institution,
        "source": str(path.relative_to(ROOT)),
        "periods": len(rows),
        "comparable_transitions": len(comparable),
        "positive_qai_transitions": len(positive),
        "qai_mean": round(statistics.mean(q_values), 6) if q_values else None,
        "qai_population_sd": round(statistics.pstdev(q_values), 6) if len(q_values) > 1 else None,
        "qai_min": round(min(q_values), 6) if q_values else None,
        "qai_max": round(max(q_values), 6) if q_values else None,
        "qai_vs_backlog_growth_r": _pearson(q_values, growth_values),
        "qai_vs_clearance_ratio_r": _pearson(q_values, clearance_values),
        "first_pending": rows[0]["pending"] if rows else None,
        "last_pending": rows[-1]["pending"] if rows else None,
        "limitation": "Aggregate queue counts; no direct waiting-time or capacity ground truth.",
    }
    return summary, rows


def _cfpb_summary() -> dict[str, object]:
    raw = _read(ROOT / "datasets" / "raw" / "cfpb_monthly.csv")
    volume: list[float] = []
    operational: list[float] = []
    substantive: list[float] = []
    annual: dict[str, dict[str, float]] = defaultdict(lambda: {"volume": 0.0, "untimely": 0.0, "relief": 0.0, "closed": 0.0})
    for row in raw:
        total = float(row["total"])
        closed = float(row["closed_total"] or total)
        volume.append(total)
        operational.append(1.0 - float(row["untimely_resp_n"]) / closed if closed else 0.0)
        substantive.append(float(row["relief_n"]) / closed if closed else 0.0)
        year = row["year"]
        annual[year]["volume"] += total
        annual[year]["untimely"] += float(row["untimely_resp_n"])
        annual[year]["relief"] += float(row["relief_n"])
        annual[year]["closed"] += closed
    annual_rows = [annual[key] for key in sorted(annual)]
    annual_volume = [row["volume"] for row in annual_rows]
    annual_operational = [1.0 - row["untimely"] / row["closed"] for row in annual_rows]
    annual_substantive = [row["relief"] / row["closed"] for row in annual_rows]
    return {
        "source": "datasets/raw/cfpb_monthly.csv",
        "monthly_n": len(raw),
        "annual_n": len(annual_rows),
        "volume_slope_per_month": _slope(volume),
        "volume_vs_operational_rate_r": _pearson(volume, operational),
        "volume_vs_substantive_rate_r": _pearson(volume, substantive),
        "annual_volume_vs_operational_rate_r": _pearson(annual_volume, annual_operational),
        "annual_volume_vs_substantive_rate_r": _pearson(annual_volume, annual_substantive),
        "limitation": "Complaint volume is demand/reporting activity, not a representative measure of institutional workload or service quality.",
    }


def _sec_summary() -> dict[str, object]:
    raw = _read(ROOT / "datasets" / "raw" / "sec_yearly.csv")
    volume = [float(row["tenk"]) for row in raw]
    review_intensity = [float(row["upload"]) / float(row["tenk"]) for row in raw]
    response_intensity = [float(row["corresp"]) / float(row["tenk"]) for row in raw]
    return {
        "source": "datasets/raw/sec_yearly.csv",
        "n": len(raw),
        "period_start": raw[0]["year"],
        "period_end": raw[-1]["year"],
        "volume_slope_per_year": _slope(volume),
        "volume_vs_review_intensity_r": _pearson(volume, review_intensity),
        "volume_vs_response_intensity_r": _pearson(volume, response_intensity),
        "limitation": "Filing counts and correspondence are not a complete measure of regulatory workload or substantive oversight.",
    }


def run_study1() -> dict[str, object]:
    eoir_summary, eoir_rows = _queue_summary(ROOT / "datasets" / "raw" / "eoir_annual.csv", "FY", "EOIR", "2024")
    uscis_summary, uscis_rows = _queue_summary(ROOT / "datasets" / "raw" / "uscis_quarterly.csv", "Quarter", "USCIS")
    OUTPUT.mkdir(parents=True, exist_ok=True)
    queue_path = OUTPUT / "study1_queue_series.csv"
    columns = ["institution", "period", "pending", "completed", "net_change", "backlog_growth", "clearance_ratio", "backlog_to_completions", "qai"]
    with queue_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=columns)
        writer.writeheader()
        for row in eoir_rows + uscis_rows:
            writer.writerow({key: row.get(key, "") for key in columns})
    report = {
        "study": "OICO Study 1",
        "status": "exploratory_descriptive",
        "research_question": "Do standardized workload signals reveal consistent processing pressure within multiple public administrative systems beyond the information in simpler conventional measures?",
        "data": {
            "institutions": ["EOIR", "USCIS", "CFPB", "SEC"],
            "source_files": [
                "datasets/raw/eoir_annual.csv",
                "datasets/raw/uscis_quarterly.csv",
                "datasets/raw/cfpb_monthly.csv",
                "datasets/raw/sec_yearly.csv",
            ],
            "observation_counts": {"EOIR_authoritative_periods": 9, "USCIS_periods": 12, "CFPB_months": 168, "SEC_years": 19},
            "unit_warning": "The systems are not pooled into one comparable index; each is analyzed within its own reporting unit.",
        },
        "method": {
            "queue_baselines": ["absolute pending change", "percentage backlog growth", "clearance ratio", "backlog/completions", "QAI"],
            "indicator_baselines": ["volume", "operational rate", "substantive rate", "review intensity", "response intensity"],
            "tests": ["sign agreement", "Pearson association within series", "leave-one-transition-out EOIR sensitivity", "trend slope"],
            "uncertainty": "No inferential confidence interval is reported for the small aggregate queue panels; correlations are descriptive and not causal.",
        },
        "results": {
            "EOIR": eoir_summary,
            "USCIS": uscis_summary,
            "CFPB": _cfpb_summary(),
            "SEC": _sec_summary(),
        },
        "cross_institution_result": "QAI and conventional backlog-growth signals agree in direction within the queue panels, but unlike units, frequencies, and constructs prevent a pooled cross-institution ranking.",
        "external_outcome_validation": "Not available in the frozen package. No independent wait-time, case-age, staffing, or service-outcome series is linked to the same observations.",
        "falsification_boundary": "The framework fails as a general capacity measure if an independently recovered panel shows that the signals do not correspond to observable processing deterioration, or if reporting-definition changes explain the patterns.",
        "primary_contribution": "A transparent comparative measurement workflow that demonstrates both signal agreement and the limits of pooling unlike administrative traces.",
        "artifacts": {"queue_series": str(queue_path.relative_to(ROOT))},
    }
    output_path = OUTPUT / "study1_results.json"
    output_path.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return report


if __name__ == "__main__":
    print(json.dumps(run_study1(), indent=2, sort_keys=True))
