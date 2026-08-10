from __future__ import annotations

import math
from collections import Counter
from pathlib import Path

from oico import __version__
from oico.io import ROOT, as_float, read_csv, relative, sha256, write_csv, write_json
from oico.metrics.asi import ASI_DIMENSIONS, METRIC_DOCUMENTATION as ASI_DOC, score_document, validate_asi_row
from oico.metrics.qai import METRIC_DOCUMENTATION as QAI_DOC, queue_acceleration_index
from oico.metrics.sedi import METRIC_DOCUMENTATION as SEDI_DOC, rolling_sedi, sedi_from_indicators
from oico.models.authorization import MODEL_DOCUMENTATION as AUTHORIZATION_DOC
from oico.models.procedural_capacity import MODEL_DOCUMENTATION as PROCEDURAL_DOC
from oico.schema import fieldnames, schema_as_rows


RAW = ROOT / "datasets" / "raw"
PROCESSED = ROOT / "datasets" / "processed"
METADATA = ROOT / "datasets" / "metadata"
MANIFESTS = ROOT / "datasets" / "manifests"
CHECKSUMS = ROOT / "datasets" / "checksums"
VALIDATION = ROOT / "datasets" / "validation_reports"
QUARANTINE = ROOT / "datasets" / "quarantine"
RELEASE_TIMESTAMP_UTC = "2026-08-10T00:00:00+00:00"


SOURCE_SPECS = [
    {
        "source_dataset_id": "eoir_workload_annual",
        "raw_file": "eoir_annual.csv",
        "title": "EOIR annual immigration court workload snapshot",
        "institution_id": "eoir",
        "institution_name": "Executive Office for Immigration Review",
        "source_url": "https://www.justice.gov/eoir/reports-statistics",
        "terms_url": "https://www.justice.gov/legalpolicies",
        "source_license": "DOJ states site information is public domain unless otherwise indicated; cite DOJ and exclude seals or identified third-party material.",
        "provenance_note": "Inherited from prior QAI research package and frozen as a v1 reproducibility snapshot.",
        "release_status": "included_public_domain_site_policy",
        "raw_redistribution": "yes_with_exclusions",
        "derived_redistribution": "yes",
        "attribution": "U.S. Department of Justice and EOIR",
        "notes": "Snapshot retrieval date is not recoverable; policy page reviewed 2026-08-10.",
    },
    {
        "source_dataset_id": "uscis_workload_quarterly",
        "raw_file": "uscis_quarterly.csv",
        "title": "USCIS quarterly workload snapshot",
        "institution_id": "uscis",
        "institution_name": "U.S. Citizenship and Immigration Services",
        "source_url": "https://www.uscis.gov/about/reports-and-studies",
        "terms_url": "https://uscode.house.gov/view.xhtml?edition=prelim&path=%2Fprelim%40title17%2Fchapter1",
        "source_license": "U.S. federal government work under 17 U.S.C. 105; attribution requested and identified third-party material remains excluded.",
        "provenance_note": "Inherited from prior QAI research package and frozen as a v1 reproducibility snapshot.",
        "release_status": "included_federal_work_with_third_party_caveat",
        "raw_redistribution": "yes_for_agency-produced material only",
        "derived_redistribution": "yes",
        "attribution": "U.S. Citizenship and Immigration Services",
        "notes": "Snapshot retrieval date is not recoverable; recheck dataset-specific terms before archival deposit.",
    },
    {
        "source_dataset_id": "cfpb_complaints_monthly",
        "raw_file": "cfpb_monthly.csv",
        "title": "CFPB Consumer Complaint Database monthly aggregates",
        "institution_id": "cfpb",
        "institution_name": "Consumer Financial Protection Bureau",
        "source_url": "https://www.consumerfinance.gov/data-research/consumer-complaints/search/api/v1/",
        "terms_url": "https://www.consumerfinance.gov/data-research/consumer-complaints/",
        "source_license": "CFPB states published complaint data are freely available for anyone to use, analyze, and build on; cite CFPB.",
        "provenance_note": "Inherited from prior oversight-saturation analysis and frozen as a v1 reproducibility snapshot.",
        "release_status": "included_reuse_explicitly_permitted",
        "raw_redistribution": "yes",
        "derived_redistribution": "yes",
        "attribution": "Consumer Financial Protection Bureau",
        "notes": "Complaint data are not a representative statistical sample.",
    },
    {
        "source_dataset_id": "sec_edgar_yearly",
        "raw_file": "sec_yearly.csv",
        "title": "SEC EDGAR yearly filing and comment-letter counts",
        "institution_id": "sec",
        "institution_name": "U.S. Securities and Exchange Commission",
        "source_url": "https://www.sec.gov/edgar/search/",
        "terms_url": "https://www.sec.gov/about/privacy-information",
        "source_license": "SEC permits copying and further distribution of sec.gov public information; cite SEC, exclude seals/logos, and respect SEC/EDGAR marks.",
        "provenance_note": "Inherited from prior oversight-saturation analysis and frozen as a v1 reproducibility snapshot.",
        "release_status": "included_copy_and_redistribute_permitted",
        "raw_redistribution": "yes_for_public_information",
        "derived_redistribution": "yes",
        "attribution": "U.S. Securities and Exchange Commission",
        "notes": "Exclude seals and logos; future live fetchers must respect SEC fair-access rules.",
    },
    {
        "source_dataset_id": "asi_document_corpus_manifest",
        "raw_file": "asi_corpus_manifest.csv",
        "title": "Accountability Specificity Index corpus manifest",
        "institution_id": "asi_corpus",
        "institution_name": "Accountability Specificity Index document corpus",
        "source_url": "Per-document official URLs in the source_url column.",
        "terms_url": "Per-document official terms, if any.",
        "source_license": "OICO metadata released under CC BY 4.0; linked source documents are not redistributed and retain their original terms.",
        "provenance_note": "Inherited from AIES accountability-specificity reproducibility package.",
        "release_status": "included_derived_metadata_only",
        "raw_redistribution": "no_full_text_not_stored",
        "derived_redistribution": "yes_under_CC_BY_4_0",
        "attribution": "OICO metadata; original document publishers retain their terms",
        "notes": "Linked documents are not bundled; per-document terms require user review.",
    },
    {
        "source_dataset_id": "asi_adjudicated_scores",
        "raw_file": "asi_adjudicated_matrix.csv",
        "title": "Accountability Specificity Index adjudicated scores",
        "institution_id": "asi_corpus",
        "institution_name": "Accountability Specificity Index document corpus",
        "source_url": "Per-document official URLs in the source_url column of the corpus manifest.",
        "terms_url": "Per-document official terms, if any.",
        "source_license": "OICO-derived coding metadata released under CC BY 4.0; no full source text is redistributed.",
        "provenance_note": "Adjudicated 23-document matrix from AIES reproducibility package.",
        "release_status": "included_derived_metadata_only",
        "raw_redistribution": "no_full_text_not_stored",
        "derived_redistribution": "yes_under_CC_BY_4_0",
        "attribution": "OICO-derived coding metadata",
        "notes": "Short source excerpts are not bundled; per-document terms require user review.",
    },
]


INSTITUTIONS = [
    {
        "institution_id": "eoir",
        "name": "Executive Office for Immigration Review",
        "jurisdiction": "United States",
        "sector": "public",
        "domain": "immigration adjudication",
        "unit_of_observation": "fiscal year",
        "source_dataset_id": "eoir_workload_annual",
    },
    {
        "institution_id": "uscis",
        "name": "U.S. Citizenship and Immigration Services",
        "jurisdiction": "United States",
        "sector": "public",
        "domain": "immigration benefits adjudication",
        "unit_of_observation": "fiscal quarter",
        "source_dataset_id": "uscis_workload_quarterly",
    },
    {
        "institution_id": "cfpb",
        "name": "Consumer Financial Protection Bureau",
        "jurisdiction": "United States",
        "sector": "public",
        "domain": "consumer complaint processing",
        "unit_of_observation": "month",
        "source_dataset_id": "cfpb_complaints_monthly",
    },
    {
        "institution_id": "sec",
        "name": "U.S. Securities and Exchange Commission",
        "jurisdiction": "United States",
        "sector": "public",
        "domain": "corporate disclosure review",
        "unit_of_observation": "calendar year",
        "source_dataset_id": "sec_edgar_yearly",
    },
    {
        "institution_id": "asi_corpus",
        "name": "Accountability Specificity Index document corpus",
        "jurisdiction": "mixed",
        "sector": "mixed",
        "domain": "AI governance documentation",
        "unit_of_observation": "policy or terms document",
        "source_dataset_id": "asi_document_corpus_manifest",
    },
]


def _clean_int(value: object) -> int | None:
    number = as_float(value)
    if number is None or math.isnan(number):
        return None
    return int(round(number))


def _clean_number(value: object, places: int = 6) -> float | None:
    number = as_float(value)
    if number is None or math.isnan(number):
        return None
    return round(number, places)


def _quality_flags(flags: list[str]) -> str:
    return "|".join(flags) if flags else "ok"


def _period_bounds(label: str) -> tuple[str, str]:
    if label.startswith("FY") and "Q" in label:
        year = int(label[2:6])
        quarter = int(label[-1])
        month_start = (quarter - 1) * 3 + 1
        month_end = month_start + 2
        return f"{year}-{month_start:02d}-01", f"{year}-{month_end:02d}-28"
    if len(label) == 4 and label.isdigit():
        year = int(label)
        return f"{year}-10-01", f"{year + 1}-09-30"
    if len(label) == 7 and label[4] == "-":
        return f"{label}-01", f"{label}-28"
    return "", ""


def build_queue_observations() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for dataset_id, institution_id, filename, period_key in [
        ("eoir_workload_annual", "eoir", "eoir_annual.csv", "FY"),
        ("uscis_workload_quarterly", "uscis", "uscis_quarterly.csv", "Quarter"),
    ]:
        previous_pending: int | None = None
        for raw in read_csv(RAW / filename):
            period = str(raw[period_key])
            pending = _clean_int(raw.get("Pending"))
            received = _clean_int(raw.get("Received"))
            completed = _clean_int(raw.get("Completions"))
            source_qai = _clean_number(raw.get("QAI"), places=3)
            flags: list[str] = []
            qai: float | None = None
            qai_delta: float | None = None
            if pending is None:
                flags.append("missing_pending")
            if completed is None:
                flags.append("missing_completions")
            if received is None and institution_id == "uscis":
                flags.append("received_not_reported_in_snapshot")
            if previous_pending is None:
                flags.append("first_period_qai_undefined")
            if pending is not None and previous_pending is not None and completed is not None:
                raw_qai = queue_acceleration_index(pending, previous_pending, completed)
                qai = None if raw_qai is None else round(raw_qai, 6)
                if source_qai is not None and qai is not None:
                    qai_delta = round(qai - source_qai, 6)
                    if abs(qai_delta) > 0.002:
                        flags.append("source_qai_rounding_or_mismatch")
            if pending is not None:
                previous_pending = pending
            start, end = _period_bounds(period)
            rows.append(
                {
                    "observation_id": f"{institution_id}_{period.lower()}",
                    "institution_id": institution_id,
                    "period": period,
                    "period_start": start,
                    "period_end": end,
                    "pending": pending,
                    "received": received,
                    "completed": completed,
                    "qai": qai,
                    "source_qai": source_qai,
                    "qai_delta": qai_delta,
                    "quality_flags": _quality_flags(flags),
                    "source_dataset_id": dataset_id,
                }
            )
    return rows


def _cfpb_indicator_rows() -> list[dict[str, object]]:
    raw_rows = read_csv(RAW / "cfpb_monthly.csv")
    numeric_rows: list[dict[str, float]] = []
    for raw in raw_rows:
        total = float(raw["total"])
        closed = float(raw["closed_total"]) if float(raw["closed_total"]) else total
        timely_rate = 1.0 - (float(raw["untimely_resp_n"]) / closed if closed else 0.0)
        substantive_rate = float(raw["relief_n"]) / closed if closed else 0.0
        numeric_rows.append(
            {
                "volume": total,
                "operational_rate": timely_rate,
                "substantive_rate": substantive_rate,
                "in_progress_rate": float(raw["in_progress_n"]) / total if total else 0.0,
            }
        )
    sedi_values = rolling_sedi(
        numeric_rows,
        positive_indicators=["volume", "in_progress_rate"],
        negative_indicators=["operational_rate", "substantive_rate"],
        window=12,
    )
    rows: list[dict[str, object]] = []
    for raw, numeric, sedi_value in zip(raw_rows, numeric_rows, sedi_values):
        flags = []
        if sedi_value is None:
            flags.append("insufficient_history_for_rolling_sedi")
        rows.append(
            {
                "observation_id": f"cfpb_{raw['ym']}",
                "institution_id": "cfpb",
                "period": raw["ym"],
                "indicator_family": "consumer_complaints",
                "volume": int(float(raw["total"])),
                "operational_rate": round(numeric["operational_rate"], 6),
                "substantive_rate": round(numeric["substantive_rate"], 6),
                "review_intensity": "",
                "sedi": "" if sedi_value is None else round(sedi_value, 6),
                "quality_flags": _quality_flags(flags),
                "source_dataset_id": "cfpb_complaints_monthly",
            }
        )
    return rows


def _sec_indicator_rows() -> list[dict[str, object]]:
    raw_rows = read_csv(RAW / "sec_yearly.csv")
    numeric_rows: list[dict[str, float]] = []
    for raw in raw_rows:
        tenk = float(raw["tenk"])
        upload = float(raw["upload"])
        corresp = float(raw["corresp"])
        numeric_rows.append(
            {
                "volume": tenk,
                "review_intensity": upload / tenk if tenk else 0.0,
                "response_intensity": corresp / tenk if tenk else 0.0,
            }
        )
    rows: list[dict[str, object]] = []
    for idx, (raw, numeric) in enumerate(zip(raw_rows, numeric_rows)):
        flags = []
        if idx < 3:
            sedi_value = None
            flags.append("short_history_sedi_uses_first_three_years_after_warmup")
        else:
            history = numeric_rows[:idx]
            sedi_value = sedi_from_indicators(
                numeric,
                {
                    "volume": [row["volume"] for row in history],
                    "review_intensity": [row["review_intensity"] for row in history],
                    "response_intensity": [row["response_intensity"] for row in history],
                },
                positive_indicators=["volume"],
                negative_indicators=["review_intensity", "response_intensity"],
            )
        rows.append(
            {
                "observation_id": f"sec_{raw['year']}",
                "institution_id": "sec",
                "period": raw["year"],
                "indicator_family": "edgar_review",
                "volume": int(float(raw["tenk"])),
                "operational_rate": "",
                "substantive_rate": "",
                "review_intensity": round(numeric["review_intensity"], 6),
                "sedi": "" if sedi_value is None else round(sedi_value, 6),
                "quality_flags": _quality_flags(flags),
                "source_dataset_id": "sec_edgar_yearly",
            }
        )
    return rows


def build_institutional_indicators() -> list[dict[str, object]]:
    return _cfpb_indicator_rows() + _sec_indicator_rows()


def build_asi_scores() -> list[dict[str, object]]:
    manifest = {row["document_id"]: row for row in read_csv(RAW / "asi_corpus_manifest.csv")}
    score_rows = read_csv(RAW / "asi_adjudicated_matrix.csv")
    output: list[dict[str, object]] = []
    for row in score_rows:
        doc = manifest.get(row["document_id"], {})
        issues = validate_asi_row(row)
        if doc.get("source_url", "") == "":
            issues.append("missing_source_url")
        if doc.get("excerpt_validation_status") not in ("excerpt_verified", "provision_level_extraction"):
            issues.append(f"excerpt_status={doc.get('excerpt_validation_status', 'missing')}")
        output.append(
            {
                "document_id": row["document_id"],
                "institution_name": doc.get("institution_name", ""),
                "institution_category": doc.get("institution_category", ""),
                "sector": doc.get("sector", ""),
                "jurisdiction": doc.get("jurisdiction", ""),
                "document_title": doc.get("document_title", ""),
                "document_type": doc.get("document_type", ""),
                "document_stratum": doc.get("document_stratum", ""),
                "domain": doc.get("domain", ""),
                "published_or_updated_date": doc.get("published_or_updated_date", ""),
                "source_url": doc.get("source_url", ""),
                "total_asi_score": score_document(row),
                "coding_confidence": row.get("coding_confidence", ""),
                "quality_flags": _quality_flags(issues),
            }
        )
    return output


def build_metric_catalog() -> list[dict[str, object]]:
    docs = [
        ("qai", "Queue Acceleration Index", QAI_DOC),
        ("sedi", "Saturation/Erosion Degradation Index", SEDI_DOC),
        ("asi", "Accountability Specificity Index", ASI_DOC),
        ("authorization_saturation", "Authorization Saturation Model", AUTHORIZATION_DOC),
        ("procedural_capacity", "Procedural Capacity Risk Model", PROCEDURAL_DOC),
    ]
    rows = []
    for metric_id, name, doc in docs:
        rows.append(
            {
                "metric_id": metric_id,
                "name": name,
                "definition": doc["definition"],
                "mathematical_intuition": doc["mathematical_intuition"],
                "assumptions": "|".join(doc["assumptions"]),
                "limitations": "|".join(doc["limitations"]),
                "failure_modes": "|".join(doc["failure_modes"]),
                "expected_misuse": doc["expected_misuse"],
            }
        )
    return rows


def build_source_register() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for spec in SOURCE_SPECS:
        path = RAW / spec["raw_file"]
        rows.append(
            {
                "source_dataset_id": spec["source_dataset_id"],
                "title": spec["title"],
                "raw_file": relative(path),
                "raw_sha256": sha256(path),
                "rows": len(read_csv(path)),
                "institution_id": spec["institution_id"],
                "institution_name": spec["institution_name"],
                "source_url": spec["source_url"],
                "terms_url": spec["terms_url"],
                "retrieved_at": "not_recoverable_for_inherited_snapshot",
                "license_audit_date": "2026-08-10",
                "source_license": spec["source_license"],
                "raw_redistribution": spec["raw_redistribution"],
                "derived_redistribution": spec["derived_redistribution"],
                "attribution": spec["attribution"],
                "local_snapshot": "yes",
                "provenance_note": spec["provenance_note"],
                "release_status": spec["release_status"],
                "audit_status": "derived_metadata_only" if spec["release_status"] == "included_derived_metadata_only" else "cleared_with_caveat",
                "notes": spec["notes"],
            }
        )
    return rows


def write_data_dictionary() -> None:
    lines = [
        "# OICO Data Dictionary",
        "",
        "This dictionary describes the canonical v1 tables generated from frozen public-data snapshots.",
        "Every table is regenerated by `oico reproduce`; do not edit processed tables by hand.",
        "",
    ]
    current = None
    for row in schema_as_rows():
        if row["table"] != current:
            current = row["table"]
            lines.extend([f"## {current}", "", "| field | type | nullable | description |", "|---|---:|---:|---|"])
        lines.append(f"| {row['field']} | {row['dtype']} | {row['nullable']} | {row['description']} |")
    lines.append("")
    lines.append("## Metric Boundaries")
    lines.append("")
    lines.append("- QAI is a descriptive flow metric, not a causal capacity estimate.")
    lines.append("- SEDI is a theory-guided degradation index, not validated ground truth.")
    lines.append("- ASI measures textual accountability specificity, not operational enforcement.")
    METADATA.joinpath("data_dictionary.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_transformation_log(outputs: dict[str, Path]) -> None:
    lines = [
        "# Transformation Log",
        "",
        f"Generated at: {RELEASE_TIMESTAMP_UTC}",
        f"OICO version: {__version__}",
        "",
        "## Raw Inputs",
        "",
    ]
    for spec in SOURCE_SPECS:
        path = RAW / spec["raw_file"]
        lines.append(f"- `{relative(path)}` -> sha256 `{sha256(path)}`; {spec['provenance_note']}")
    lines.extend(
        [
            "",
            "## Processing Steps",
            "",
            "1. EOIR and USCIS workload snapshots are normalized into `queue_observations.csv`.",
            "2. QAI is recomputed from pending and completion counts; inherited rounded QAI values are retained for audit.",
            "3. CFPB monthly complaint aggregates are normalized into `institutional_indicators.csv` with volume, timely-response proxy, relief proxy, and rolling SEDI.",
            "4. SEC EDGAR yearly counts are normalized into `institutional_indicators.csv` with review intensity and expanding-baseline SEDI.",
            "5. ASI document manifest and adjudicated coding matrix are joined into `asi_scores.csv`; ASI totals are recomputed from the eight dimensions.",
            "6. A machine-readable manifest and checksum file are regenerated from raw, processed, metadata, benchmark, and figure artifacts.",
            "",
            "## Non-Transformations",
            "",
            "- The v1 pipeline does not re-fetch live agency data. It reproduces the release from frozen source snapshots.",
            "- No private credentials, personal tokens, or authenticated APIs are required.",
            "- No adoption, citation, or external-use claims are inferred from the existence of the repository.",
            "",
            "## Outputs",
            "",
        ]
    )
    for label, path in outputs.items():
        lines.append(f"- {label}: `{relative(path)}`")
    METADATA.joinpath("transformation_log.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def validate_outputs() -> dict[str, object]:
    issues: list[dict[str, str]] = []
    table_counts: dict[str, int] = {}
    for table, filename in [
        ("institutions", "institutions.csv"),
        ("queue_observations", "queue_observations.csv"),
        ("institutional_indicators", "institutional_indicators.csv"),
        ("asi_scores", "asi_scores.csv"),
        ("metric_catalog", "metric_catalog.csv"),
    ]:
        rows = read_csv(PROCESSED / filename)
        table_counts[table] = len(rows)
        expected = fieldnames(table)
        if rows:
            observed = list(rows[0].keys())
            if observed != expected:
                issues.append({"severity": "error", "table": table, "issue": f"schema mismatch: {observed} != {expected}"})
        for idx, row in enumerate(rows, start=2):
            for name in expected:
                if name not in row:
                    issues.append({"severity": "error", "table": table, "issue": f"missing field {name} at row {idx}"})
            if row.get("quality_flags") and "missing" in row.get("quality_flags", ""):
                issues.append({"severity": "warning", "table": table, "issue": f"row {idx}: {row.get('quality_flags')}"})
        id_fields = [field for field in ("observation_id", "document_id", "institution_id", "metric_id") if rows and field in rows[0]]
        if id_fields:
            id_field = id_fields[0]
            seen: set[str] = set()
            for row in rows:
                identifier = row.get(id_field, "")
                if identifier in seen:
                    issues.append({"severity": "error", "table": table, "issue": f"duplicate {id_field}: {identifier}"})
                seen.add(identifier)
    queue_rows = read_csv(PROCESSED / "queue_observations.csv")
    for row in queue_rows:
        if row["qai"] not in ("", None):
            value = float(row["qai"])
            if value < -5 or value > 5:
                issues.append({"severity": "warning", "table": "queue_observations", "issue": f"unusual QAI {value} in {row['observation_id']}"})
    asi_rows = read_csv(PROCESSED / "asi_scores.csv")
    distribution = Counter(int(row["total_asi_score"]) for row in asi_rows)
    return {
        "status": "pass" if not any(issue["severity"] == "error" for issue in issues) else "fail",
        "table_counts": table_counts,
        "issues": issues,
        "asi_score_distribution": dict(sorted(distribution.items())),
    }


def write_manifest(extra_paths: list[Path] | None = None) -> None:
    candidates = []
    for base in [RAW, PROCESSED, METADATA, VALIDATION, QUARANTINE]:
        candidates.extend(path for path in base.rglob("*") if path.is_file())
    if extra_paths:
        candidates.extend(path for path in extra_paths if path.exists())
    files = []
    for path in sorted(set(candidates)):
        files.append(
            {
                "path": relative(path),
                "sha256": sha256(path),
                "bytes": path.stat().st_size,
            }
        )
    payload = {
        "name": f"Open Institutional Capacity Observatory v{__version__}",
        "version": __version__,
        "generated_at_utc": RELEASE_TIMESTAMP_UTC,
        "license_code": "MIT",
        "license_data": "CC-BY-4.0 for OICO metadata and derived tables; source files retain original terms.",
        "files": files,
    }
    write_json(MANIFESTS / "dataset_manifest.json", payload)
    lines = [f"{item['sha256']}  {item['path']}" for item in files]
    CHECKSUMS.joinpath("sha256sums.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")


def build_all() -> dict[str, object]:
    PROCESSED.mkdir(parents=True, exist_ok=True)
    METADATA.mkdir(parents=True, exist_ok=True)
    MANIFESTS.mkdir(parents=True, exist_ok=True)
    CHECKSUMS.mkdir(parents=True, exist_ok=True)
    VALIDATION.mkdir(parents=True, exist_ok=True)
    QUARANTINE.mkdir(parents=True, exist_ok=True)

    source_register = build_source_register()
    queue_rows = build_queue_observations()
    indicator_rows = build_institutional_indicators()
    asi_rows = build_asi_scores()
    metric_rows = build_metric_catalog()

    outputs = {
        "institutions": PROCESSED / "institutions.csv",
        "queue_observations": PROCESSED / "queue_observations.csv",
        "institutional_indicators": PROCESSED / "institutional_indicators.csv",
        "asi_scores": PROCESSED / "asi_scores.csv",
        "metric_catalog": PROCESSED / "metric_catalog.csv",
        "source_register": METADATA / "source_register.csv",
        "schema": METADATA / "schema.csv",
    }
    write_csv(outputs["institutions"], INSTITUTIONS, fieldnames("institutions"))
    write_csv(outputs["queue_observations"], queue_rows, fieldnames("queue_observations"))
    write_csv(outputs["institutional_indicators"], indicator_rows, fieldnames("institutional_indicators"))
    write_csv(outputs["asi_scores"], asi_rows, fieldnames("asi_scores"))
    write_csv(outputs["metric_catalog"], metric_rows, fieldnames("metric_catalog"))
    write_csv(outputs["source_register"], source_register, list(source_register[0].keys()))
    write_csv(outputs["schema"], schema_as_rows(), ["table", "field", "dtype", "nullable", "description"])
    write_data_dictionary()
    write_transformation_log(outputs)
    validation = validate_outputs()
    write_json(VALIDATION / "data_validation_report.json", validation)
    write_validation_markdown(validation)
    write_quarantine_report(validation)
    write_manifest(list(outputs.values()))
    return validation


def write_validation_markdown(validation: dict[str, object]) -> None:
    lines = [
        "# Data Validation Report",
        "",
        f"Status: **{validation['status']}**",
        "",
        "## Table Counts",
        "",
        "| table | rows |",
        "|---|---:|",
    ]
    for table, count in validation["table_counts"].items():
        lines.append(f"| {table} | {count} |")
    lines.extend(["", "## Issues", ""])
    issues = validation["issues"]
    if issues:
        for issue in issues:
            lines.append(f"- {issue['severity']}: {issue['table']} - {issue['issue']}")
    else:
        lines.append("- No errors or warnings.")
    lines.extend(["", "Warnings are carried forward as provenance limits rather than hidden."])
    VALIDATION.joinpath("data_validation_report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_quarantine_report(validation: dict[str, object]) -> None:
    quarantined = [issue for issue in validation["issues"] if issue["severity"] == "error"]
    report = {
        "status": "no_quarantined_rows" if not quarantined else "quarantine_required",
        "policy": "Rows with schema errors, duplicate stable identifiers, impossible metric ranges, or corrupted source hashes must be quarantined rather than silently repaired.",
        "quarantined_issue_count": len(quarantined),
        "quarantined_issues": quarantined,
    }
    write_json(QUARANTINE / "quarantine_report.json", report)
    lines = [
        "# Quarantine Report",
        "",
        f"Status: **{report['status']}**",
        "",
        report["policy"],
        "",
    ]
    if quarantined:
        lines.append("## Quarantined Issues")
        for issue in quarantined:
            lines.append(f"- {issue['table']}: {issue['issue']}")
    else:
        lines.append(f"No rows are quarantined in v{__version__}.")
    (QUARANTINE / "README.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
