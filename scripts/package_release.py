from __future__ import annotations

import gzip
import hashlib
import json
import sys
import tarfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from oico import __version__


OUT = ROOT / "releases" / "github" / f"oico-{__version__}.tar.gz"
ARCHIVE_CHECKSUM = OUT.with_suffix(OUT.suffix + ".sha256")
ARTIFACT_MANIFEST = ROOT / "releases" / "artifact_manifest.json"
EXCLUDED_DIRS = {".git", "__pycache__", ".pytest_cache", ".mypy_cache", "dist", "build"}
EXCLUDED_FILES = {OUT, ARCHIVE_CHECKSUM, ARTIFACT_MANIFEST}
RELEASE_TIMESTAMP_UTC = "2026-08-10T00:00:00+00:00"
ARTIFACT_PATHS = [
    "README.md",
    "AI_USAGE.md",
    "REPLICATION.md",
    "replication/reference_manifest.json",
    "PROJECT_SCORECARD.md",
    "docs/standards_audit.md",
    "docs/METRIC_STATUS.md",
    "docs/FLAGSHIP_CASE_STUDY.md",
    "docs/REPRODUCIBILITY.md",
    "docs/DESIGN_DECISIONS.md",
    "docs/EXTERNAL_VALIDATION.md",
    "releases/reproduction_manifest.json",
    "examples/flagship/outputs/eoir_queue_series.csv",
    "examples/flagship/outputs/flagship_report.json",
    "LICENSE",
    "LICENSE-DATA",
    "CITATION.cff",
    "codemeta.json",
    "datasets/manifests/dataset_manifest.json",
    "datasets/checksums/sha256sums.txt",
    "datasets/metadata/license_review.md",
    "datasets/validation_reports/data_validation_report.json",
    "benchmarks/benchmark_results.json",
    "benchmarks/frozen_splits.csv",
    "benchmarks/leaderboard_spec.md",
    "figures/gallery/FIGURE_MANIFEST.md",
    "notebooks/01_reproduce_and_inspect.ipynb",
    "notebooks/02_metric_examples.ipynb",
    "notebooks/03_research_showcase.ipynb",
    "notebooks/04_replication_walkthrough.ipynb",
    "notebooks/05_five_minute_demo.ipynb",
    "docs/release/release_candidate_report.md",
    "releases/RELEASE_CHECKLIST.md",
    "releases/github/RELEASE_NOTES.md",
    "releases/github/reproduction_report.json",
]


def include(path: Path) -> bool:
    parts = path.relative_to(ROOT).parts
    if any(part in EXCLUDED_DIRS or part.endswith(".egg-info") for part in parts):
        return False
    if path.name in {".DS_Store", ".coverage"}:
        return False
    if path.suffix in {".pyc"}:
        return False
    if path in EXCLUDED_FILES:
        return False
    return True


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def write_artifact_manifest() -> None:
    paths = [ROOT / path for path in ARTIFACT_PATHS] + [OUT, ARCHIVE_CHECKSUM]
    missing = [path.relative_to(ROOT).as_posix() for path in paths if not path.is_file()]
    if missing:
        raise FileNotFoundError(f"release artifacts missing: {', '.join(missing)}")
    artifacts = [
        {
            "path": path.relative_to(ROOT).as_posix(),
            "bytes": path.stat().st_size,
            "sha256": sha256(path),
        }
        for path in paths
    ]
    payload = {
        "name": "Open Institutional Capacity Observatory release artifacts",
        "version": __version__,
        "generated_at_utc": RELEASE_TIMESTAMP_UTC,
        "artifacts": artifacts,
    }
    ARTIFACT_MANIFEST.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def normalize(info: tarfile.TarInfo) -> tarfile.TarInfo:
    info.uid = 0
    info.gid = 0
    info.uname = ""
    info.gname = ""
    info.mtime = 0
    return info


def main() -> int:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    if OUT.exists():
        OUT.unlink()
    with OUT.open("wb") as raw, gzip.GzipFile(fileobj=raw, mode="wb", mtime=0) as gz:
        with tarfile.open(fileobj=gz, mode="w") as archive:
            for path in sorted(ROOT.rglob("*")):
                if path.is_file() and include(path):
                    archive.add(path, arcname=Path(f"oico-{__version__}") / path.relative_to(ROOT), filter=normalize)
    archive_sha256 = sha256(OUT)
    ARCHIVE_CHECKSUM.write_text(f"{archive_sha256}  {OUT.name}\n", encoding="utf-8")
    write_artifact_manifest()
    print(f"Wrote {OUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
