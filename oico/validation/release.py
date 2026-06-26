from __future__ import annotations

from pathlib import Path

from oico.io import ROOT, read_json, sha256, write_json


REQUIRED_PATHS = [
    "README.md",
    "LICENSE",
    "LICENSE-DATA",
    "CITATION.cff",
    "codemeta.json",
    "pyproject.toml",
    "datasets/raw/eoir_annual.csv",
    "datasets/raw/uscis_quarterly.csv",
    "datasets/raw/cfpb_monthly.csv",
    "datasets/raw/sec_yearly.csv",
    "datasets/raw/asi_corpus_manifest.csv",
    "datasets/raw/asi_adjudicated_matrix.csv",
    "datasets/processed/institutions.csv",
    "datasets/processed/queue_observations.csv",
    "datasets/processed/institutional_indicators.csv",
    "datasets/processed/asi_scores.csv",
    "datasets/processed/metric_catalog.csv",
    "datasets/metadata/source_register.csv",
    "datasets/metadata/license_review.md",
    "datasets/metadata/data_dictionary.md",
    "datasets/metadata/transformation_log.md",
    "datasets/manifests/dataset_manifest.json",
    "datasets/checksums/sha256sums.txt",
    "datasets/validation_reports/data_validation_report.json",
    "datasets/quarantine/quarantine_report.json",
    "benchmarks/BENCHMARKS.md",
    "benchmarks/frozen_splits.csv",
    "benchmarks/leaderboard_spec.md",
    "figures/gallery/FIGURE_MANIFEST.md",
    "docs/index.md",
    "docs/faq.md",
    "docs/citation.md",
    "docs/tutorials/one_hour_tutorial.md",
    "docs/tutorials/methods_tutorial.md",
    "docs/teaching/professor_guide.md",
    "docs/teaching/example_assignment.md",
    "docs/teaching/example_solution.md",
    "docs/adoption/professor_overview.md",
    "docs/adoption/lab_overview.md",
    "docs/adoption/course_adoption_guide.md",
    "docs/adoption/skeptical_faq.md",
    "docs/adoption/migration_guide.md",
    "docs/adoption/v2_roadmap.md",
    "docs/publication/conference_poster_outline.md",
    "docs/publication/lightning_talk_outline.md",
    "docs/publication/methods_paper_outline.md",
    "docs/release/release_candidate_report.md",
    "community/CONTRIBUTING.md",
    "community/CODE_OF_CONDUCT.md",
    "website/index.html",
    "website/datasets.html",
    "website/metrics.html",
    "website/benchmarks.html",
    "website/downloads.html",
    "website/citation.html",
    "website/faq.html",
    "releases/conference_artifact/README.md",
    "releases/journal_supplement/README.md",
    "releases/poster_assets/outline.md",
    "releases/demo_assets/README.md",
    "releases/RELEASE_CHECKLIST.md",
    "releases/artifact_manifest.json",
    "releases/github/RELEASE_NOTES.md",
    "releases/github/oico-1.0.0-rc1.tar.gz",
    "releases/github/oico-1.0.0-rc1.tar.gz.sha256",
    "releases/github/reproduction_report.json",
]


def audit_release() -> dict[str, object]:
    missing = [path for path in REQUIRED_PATHS if not (ROOT / path).exists()]
    manifest_path = ROOT / "datasets" / "manifests" / "dataset_manifest.json"
    checksum_issues: list[str] = []
    if manifest_path.exists():
        manifest = read_json(manifest_path)
        for item in manifest.get("files", []):
            path = ROOT / item["path"]
            if not path.exists():
                checksum_issues.append(f"manifest path missing: {item['path']}")
            elif sha256(path) != item["sha256"]:
                checksum_issues.append(f"checksum mismatch: {item['path']}")
    else:
        checksum_issues.append("missing dataset_manifest.json")
    artifact_manifest_path = ROOT / "releases" / "artifact_manifest.json"
    if artifact_manifest_path.exists():
        artifact_manifest = read_json(artifact_manifest_path)
        for item in artifact_manifest.get("artifacts", []):
            path = ROOT / item["path"]
            if not path.exists():
                checksum_issues.append(f"artifact path missing: {item['path']}")
            elif sha256(path) != item["sha256"]:
                checksum_issues.append(f"artifact checksum mismatch: {item['path']}")
    else:
        checksum_issues.append("missing artifact_manifest.json")
    report = {
        "status": "pass" if not missing and not checksum_issues else "fail",
        "missing_required_paths": missing,
        "checksum_issues": checksum_issues,
    }
    write_json(ROOT / "releases" / "github" / "release_audit.json", report)
    return report
