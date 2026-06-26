from __future__ import annotations

from statistics import mean, median

from oico.io import ROOT, read_csv, write_csv, write_json
from oico.models.authorization import intervention_scenarios
from oico.models.procedural_capacity import simulate_procedural_days


BENCHMARKS = ROOT / "benchmarks"


def _mae(actual: list[float], predicted: list[float]) -> float:
    if not actual:
        return 0.0
    return sum(abs(a - p) for a, p in zip(actual, predicted)) / len(actual)


def queue_forecasting() -> dict[str, object]:
    rows = [row for row in read_csv(ROOT / "datasets" / "processed" / "queue_observations.csv") if row["qai"] not in ("", None)]
    outputs = []
    actual: list[float] = []
    predicted: list[float] = []
    for institution in sorted({row["institution_id"] for row in rows}):
        inst = [row for row in rows if row["institution_id"] == institution]
        for idx in range(1, len(inst)):
            pred = float(inst[idx - 1]["qai"])
            obs = float(inst[idx]["qai"])
            actual.append(obs)
            predicted.append(pred)
            outputs.append({"institution_id": institution, "period": inst[idx]["period"], "actual_qai": obs, "predicted_qai": pred})
    result = {
        "task": "queue_forecasting",
        "problem_statement": "Predict next-period QAI from public workload history.",
        "baseline": "Persistence baseline: QAI_t_hat = QAI_{t-1}.",
        "evaluation_metric": "mean_absolute_error",
        "n_test_observations": len(actual),
        "mean_absolute_error": round(_mae(actual, predicted), 6),
        "limitations": "Small v1 sample; intended as a format and baseline, not a leaderboard-quality forecasting corpus.",
    }
    write_csv(BENCHMARKS / "queue_forecasting" / "baseline_predictions.csv", outputs, ["institution_id", "period", "actual_qai", "predicted_qai"])
    write_json(BENCHMARKS / "queue_forecasting" / "baseline_results.json", result)
    return result


def saturation_detection() -> dict[str, object]:
    rows = [row for row in read_csv(ROOT / "datasets" / "processed" / "institutional_indicators.csv") if row["sedi"] not in ("", None)]
    actual: list[float] = []
    predicted: list[float] = []
    outputs = []
    for institution in sorted({row["institution_id"] for row in rows}):
        inst = [row for row in rows if row["institution_id"] == institution]
        values = [float(row["sedi"]) for row in inst]
        threshold = median(values)
        for row in inst:
            obs = 1.0 if float(row["sedi"]) >= threshold else 0.0
            pred = 1.0 if float(row["sedi"]) >= 0.5 else 0.0
            actual.append(obs)
            predicted.append(pred)
            outputs.append({"institution_id": row["institution_id"], "period": row["period"], "proxy_label": int(obs), "prediction": int(pred), "sedi": row["sedi"]})
    accuracy = sum(1 for a, p in zip(actual, predicted) if a == p) / len(actual) if actual else 0.0
    result = {
        "task": "saturation_detection",
        "problem_statement": "Detect high-degradation periods from public institutional indicators.",
        "baseline": "Threshold SEDI at 0.5 against institution-specific median proxy labels.",
        "evaluation_metric": "accuracy_against_proxy_labels",
        "n_test_observations": len(actual),
        "accuracy": round(accuracy, 6),
        "limitations": "Labels are proxy labels derived from SEDI distribution, not independent ground truth.",
    }
    write_csv(BENCHMARKS / "saturation_detection" / "baseline_predictions.csv", outputs, ["institution_id", "period", "proxy_label", "prediction", "sedi"])
    write_json(BENCHMARKS / "saturation_detection" / "baseline_results.json", result)
    return result


def intervention_simulation() -> dict[str, object]:
    scenario_rows = intervention_scenarios()
    procedural_rows = simulate_procedural_days(60)
    result = {
        "task": "intervention_simulation",
        "problem_statement": "Compare simple capacity and quality interventions under authorization saturation.",
        "baseline": "Deterministic scenario grid plus seeded procedural-risk simulation.",
        "evaluation_metric": "mean_quality_and_mean_failure_risk",
        "mean_authorization_quality": round(mean(float(row["quality"]) for row in scenario_rows), 6),
        "mean_procedural_failure_risk": round(mean(float(row["failure_risk"]) for row in procedural_rows), 6),
        "limitations": "Synthetic benchmark only; parameters are not calibrated to a live institution.",
    }
    write_csv(BENCHMARKS / "intervention_simulation" / "authorization_scenarios.csv", scenario_rows, ["scenario", "rho_s", "k", "q_ceremonial", "quality"])
    write_csv(BENCHMARKS / "intervention_simulation" / "procedural_days.csv", procedural_rows, ["day", "ai_output_volume", "review_capacity", "contestation", "accountable_ownership", "failure_risk"])
    write_json(BENCHMARKS / "intervention_simulation" / "baseline_results.json", result)
    return result


def accountability_specificity() -> dict[str, object]:
    rows = sorted(read_csv(ROOT / "datasets" / "processed" / "asi_scores.csv"), key=lambda row: row["document_id"])
    train = [row for idx, row in enumerate(rows) if idx % 5 != 0]
    test = [row for idx, row in enumerate(rows) if idx % 5 == 0]
    baseline = median(int(row["total_asi_score"]) for row in train)
    actual = [int(row["total_asi_score"]) for row in test]
    predicted = [baseline for _ in test]
    outputs = [{"document_id": row["document_id"], "actual_total_asi": row["total_asi_score"], "predicted_total_asi": baseline} for row in test]
    result = {
        "task": "accountability_specificity",
        "problem_statement": "Predict total ASI score from held-out document metadata or text features.",
        "baseline": "Median training-set total ASI score.",
        "evaluation_metric": "mean_absolute_error",
        "n_train": len(train),
        "n_test": len(test),
        "mean_absolute_error": round(_mae(actual, predicted), 6),
        "limitations": "V1 corpus is small and useful mainly for codebook testing and teaching; text-feature baselines require source-text licensing review.",
    }
    write_csv(BENCHMARKS / "accountability_specificity" / "baseline_predictions.csv", outputs, ["document_id", "actual_total_asi", "predicted_total_asi"])
    write_json(BENCHMARKS / "accountability_specificity" / "baseline_results.json", result)
    return result


def cross_institution_comparison() -> dict[str, object]:
    queue = read_csv(ROOT / "datasets" / "processed" / "queue_observations.csv")
    indicators = read_csv(ROOT / "datasets" / "processed" / "institutional_indicators.csv")
    latest: dict[str, dict[str, object]] = {}
    for row in queue:
        if row["qai"] not in ("", None):
            latest[row["institution_id"]] = {"institution_id": row["institution_id"], "period": row["period"], "signal_type": "qai", "signal": float(row["qai"])}
    for row in indicators:
        if row["sedi"] not in ("", None):
            latest[row["institution_id"]] = {"institution_id": row["institution_id"], "period": row["period"], "signal_type": "sedi", "signal": float(row["sedi"])}
    ranked = sorted(latest.values(), key=lambda row: float(row["signal"]), reverse=True)
    for rank, row in enumerate(ranked, start=1):
        row["rank"] = rank
    result = {
        "task": "cross_institution_comparison",
        "problem_statement": "Produce a transparent, versioned stress-signal ranking across available public series.",
        "baseline": "Rank the latest available QAI or SEDI signal within each institution.",
        "evaluation_metric": "descriptive_ranking_only",
        "n_institutions": len(ranked),
        "limitations": "QAI and SEDI are not directly commensurate; ranking is for interface testing, not substantive comparison.",
    }
    write_csv(BENCHMARKS / "cross_institution_comparison" / "latest_signal_ranking.csv", ranked, ["rank", "institution_id", "period", "signal_type", "signal"])
    write_json(BENCHMARKS / "cross_institution_comparison" / "baseline_results.json", result)
    return result


def write_benchmark_docs(results: list[dict[str, object]]) -> None:
    lines = [
        "# OICO Benchmarks",
        "",
        "These are baseline tasks for reproducibility, teaching, and method comparison.",
        "They are intentionally conservative: v1 contains small public-data pilots and proxy labels, not hidden ground truth.",
        "",
        "| task | baseline | metric | caveat |",
        "|---|---|---|---|",
    ]
    for result in results:
        lines.append(f"| `{result['task']}` | {result['baseline']} | {result['evaluation_metric']} | {result['limitations']} |")
    lines.extend(
        [
            "",
            "## Leaderboard Policy",
            "",
            "No public leaderboard should be advertised until independent labels, frozen train/test splits, and data-license review are complete.",
            "For v1, benchmark results are regression tests and classroom exercises.",
        ]
    )
    (BENCHMARKS / "BENCHMARKS.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_frozen_splits() -> None:
    rows = []
    queue = [row for row in read_csv(ROOT / "datasets" / "processed" / "queue_observations.csv") if row["qai"] not in ("", None)]
    for institution in sorted({row["institution_id"] for row in queue}):
        inst = [row for row in queue if row["institution_id"] == institution]
        for idx, row in enumerate(inst):
            split = "test" if idx >= max(1, int(len(inst) * 0.7)) else "train"
            rows.append({"task": "queue_forecasting", "unit_id": row["observation_id"], "split": split, "split_rule": "last_30_percent_by_institution"})
    indicators = [row for row in read_csv(ROOT / "datasets" / "processed" / "institutional_indicators.csv") if row["sedi"] not in ("", None)]
    for institution in sorted({row["institution_id"] for row in indicators}):
        inst = [row for row in indicators if row["institution_id"] == institution]
        for idx, row in enumerate(inst):
            split = "test" if idx % 5 == 0 else "train"
            rows.append({"task": "saturation_detection", "unit_id": row["observation_id"], "split": split, "split_rule": "deterministic_every_fifth_observation"})
    asi = sorted(read_csv(ROOT / "datasets" / "processed" / "asi_scores.csv"), key=lambda row: row["document_id"])
    for idx, row in enumerate(asi):
        split = "test" if idx % 5 == 0 else "train"
        rows.append({"task": "accountability_specificity", "unit_id": row["document_id"], "split": split, "split_rule": "deterministic_every_fifth_document"})
    write_csv(BENCHMARKS / "frozen_splits.csv", rows, ["task", "unit_id", "split", "split_rule"])


def write_leaderboard_spec() -> None:
    lines = [
        "# Leaderboard Specification",
        "",
        "OICO v1 does not operate a public leaderboard. This file specifies the conditions required before one is launched.",
        "",
        "## Required Before Public Ranking",
        "",
        "- Independent labels or externally validated targets.",
        "- Frozen train/test splits published in `benchmarks/frozen_splits.csv`.",
        "- Baseline scores produced by `python -m oico.cli.main run-benchmarks`.",
        "- Submission format and metric definitions documented per task.",
        "- License review for any model inputs that include source text.",
        "",
        "## Current v1 Status",
        "",
        "The current splits and baselines support reproducibility tests, methods tutorials, and classroom assignments. They should not be advertised as evidence of state-of-the-art performance.",
    ]
    (BENCHMARKS / "leaderboard_spec.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def run_all_benchmarks() -> list[dict[str, object]]:
    for subdir in [
        "queue_forecasting",
        "saturation_detection",
        "intervention_simulation",
        "accountability_specificity",
        "cross_institution_comparison",
    ]:
        (BENCHMARKS / subdir).mkdir(parents=True, exist_ok=True)
    results = [
        queue_forecasting(),
        saturation_detection(),
        intervention_simulation(),
        accountability_specificity(),
        cross_institution_comparison(),
    ]
    write_frozen_splits()
    write_leaderboard_spec()
    write_benchmark_docs(results)
    write_json(BENCHMARKS / "benchmark_results.json", {"results": results})
    return results
