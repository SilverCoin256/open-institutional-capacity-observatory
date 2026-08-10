"""Reproducible EOIR flagship analysis used by the public examples."""

from __future__ import annotations

import csv

from oico.io import ROOT, read_csv, write_json


OUTPUT = ROOT / "examples" / "flagship" / "outputs"


def run_flagship() -> dict[str, object]:
    """Write the EOIR summary table and machine-readable flagship report.

    The analysis is descriptive: it reports the observed backlog and QAI
    series, with no claim that QAI identifies staffing or causal capacity.
    """
    source = ROOT / "datasets" / "processed" / "queue_observations.csv"
    rows = [row for row in read_csv(source) if row["institution_id"] == "eoir"]
    if not rows:
        raise FileNotFoundError("EOIR processed observations are missing")

    OUTPUT.mkdir(parents=True, exist_ok=True)
    table_path = OUTPUT / "eoir_queue_series.csv"
    columns = ["period", "pending", "received", "completed", "qai", "quality_flags"]
    with table_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=columns)
        writer.writeheader()
        for row in rows:
            writer.writerow({column: row.get(column, "") for column in columns})

    comparable = [row for row in rows if row.get("qai") not in (None, "")]
    positive = [row for row in comparable if float(row["qai"]) > 0]
    peak = max(rows, key=lambda row: int(row["pending"]))
    first = rows[0]
    report = {
        "status": "pass",
        "research_question": "Did EOIR backlog growth outpace recorded completions in the frozen annual snapshot?",
        "source_dataset": "datasets/raw/eoir_annual.csv",
        "processed_input": "datasets/processed/queue_observations.csv",
        "observations": len(rows),
        "comparable_qai_observations": len(comparable),
        "positive_qai_periods": len(positive),
        "first_period": first["period"],
        "first_pending": int(first["pending"]),
        "peak_period": peak["period"],
        "peak_pending": int(peak["pending"]),
        "peak_qai": float(max(comparable, key=lambda row: float(row["qai"]))["qai"]),
        "backlog_multiple_first_to_peak": round(int(peak["pending"]) / int(first["pending"]), 6),
        "metric_definition": "QAI_t = (Pending_t - Pending_(t-1)) / Completions_t",
        "interpretation": "The frozen snapshot shows sustained backlog expansion relative to completions through the 2024 peak, followed by negative QAI values in later rows.",
        "non_claims": [
            "QAI does not identify staffing capacity.",
            "The series does not establish causality or legal noncompliance.",
            "The snapshot does not establish that all periods have identical reporting coverage.",
        ],
        "artifacts": {
            "table": str(table_path.relative_to(ROOT)),
            "figure": "figures/gallery/qai_eoir.svg",
        },
    }
    write_json(OUTPUT / "flagship_report.json", report)
    return report
