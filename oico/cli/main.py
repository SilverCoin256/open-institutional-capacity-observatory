from __future__ import annotations

import argparse
import json
import logging
import platform
import subprocess
import sys

from oico import __version__
from oico.benchmarks import run_all_benchmarks
from oico.config import load_config
from oico.datasets import build_all
from oico.flagship import run_flagship
from oico.io import ROOT, read_csv, sha256, write_json
from oico.logging_utils import configure_logging
from oico.metrics.qai import queue_acceleration_index
from oico.validation import audit_release
from oico.visualization import make_all_figures


def cmd_build_data(_: argparse.Namespace) -> int:
    result = build_all()
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["status"] == "pass" else 1


def cmd_validate_data(_: argparse.Namespace) -> int:
    result = build_all()
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["status"] == "pass" else 1


def cmd_make_figures(_: argparse.Namespace) -> int:
    paths = make_all_figures()
    print(json.dumps({"figures": [str(path.relative_to(ROOT)) for path in paths]}, indent=2))
    return 0


def cmd_run_benchmarks(_: argparse.Namespace) -> int:
    results = run_all_benchmarks()
    print(json.dumps({"results": results}, indent=2, sort_keys=True))
    return 0


def cmd_run_flagship(_: argparse.Namespace) -> int:
    result = run_flagship()
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


def cmd_compute_qai(args: argparse.Namespace) -> int:
    result = queue_acceleration_index(args.pending, args.previous_pending, args.completed)
    print(json.dumps({"qai": result}))
    return 0


def package_release() -> None:
    subprocess.check_call([sys.executable, str(ROOT / "scripts" / "package_release.py")], cwd=ROOT)


def write_reproduction_manifest(report: dict[str, object]) -> None:
    paths = [
        ROOT / "datasets" / "raw" / "eoir_annual.csv",
        ROOT / "datasets" / "processed" / "queue_observations.csv",
        ROOT / "examples" / "flagship" / "outputs" / "eoir_queue_series.csv",
        ROOT / "examples" / "flagship" / "outputs" / "flagship_report.json",
        ROOT / "figures" / "gallery" / "qai_eoir.svg",
    ]
    artifacts = []
    for path in paths:
        if path.is_file():
            artifacts.append({"path": str(path.relative_to(ROOT)), "sha256": sha256(path), "bytes": path.stat().st_size})
    payload = {
        "version": __version__,
        "status": report.get("release_audit", {}).get("status", "pending"),
        "environment": {"python": platform.python_version(), "platform": platform.platform()},
        "input_manifest": "datasets/manifests/dataset_manifest.json",
        "artifacts": artifacts,
        "deterministic_outputs": True,
        "external_validation_level": 0,
    }
    write_json(ROOT / "releases" / "reproduction_manifest.json", payload)


def cmd_reproduce(_: argparse.Namespace) -> int:
    validation = build_all()
    figures = make_all_figures()
    benchmarks = run_all_benchmarks()
    flagship = run_flagship()
    payload = {
        "version": __version__,
        "data_validation": validation,
        "figure_count": len(figures),
        "benchmark_count": len(benchmarks),
        "flagship": flagship,
        "release_audit": {"status": "pending"},
    }
    write_json(ROOT / "releases" / "github" / "reproduction_report.json", payload)
    write_reproduction_manifest(payload)
    package_release()
    release = audit_release()
    payload["release_audit"] = release
    write_json(ROOT / "releases" / "github" / "reproduction_report.json", payload)
    write_reproduction_manifest(payload)
    package_release()
    release = audit_release()
    payload["release_audit"] = release
    write_json(ROOT / "releases" / "github" / "reproduction_report.json", payload)
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0 if validation["status"] == "pass" and release["status"] == "pass" else 1


def cmd_audit_release(_: argparse.Namespace) -> int:
    report = audit_release()
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0 if report["status"] == "pass" else 1


def cmd_summary(_: argparse.Namespace) -> int:
    summary = {}
    for name in ["institutions", "queue_observations", "institutional_indicators", "asi_scores", "metric_catalog"]:
        path = ROOT / "datasets" / "processed" / f"{name}.csv"
        summary[name] = len(read_csv(path)) if path.exists() else "missing"
    print(json.dumps(summary, indent=2, sort_keys=True))
    return 0


def cmd_config(_: argparse.Namespace) -> int:
    print(json.dumps(load_config(), indent=2, sort_keys=True))
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="oico", description="Open Institutional Capacity Observatory CLI")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose logging.")
    parser.add_argument("--version", action="version", version=f"oico {__version__}")
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("build-data", help="Build processed data and metadata from frozen raw snapshots.").set_defaults(func=cmd_build_data)
    sub.add_parser("validate-data", help="Rebuild and validate processed data.").set_defaults(func=cmd_validate_data)
    sub.add_parser("make-figures", help="Generate deterministic SVG figures.").set_defaults(func=cmd_make_figures)
    sub.add_parser("run-benchmarks", help="Run baseline benchmark tasks.").set_defaults(func=cmd_run_benchmarks)
    sub.add_parser("run-flagship", help="Run the EOIR flagship case study.").set_defaults(func=cmd_run_flagship)
    sub.add_parser("reproduce", help="Run the complete v1 reproduction workflow.").set_defaults(func=cmd_reproduce)
    sub.add_parser("audit-release", help="Check release-candidate completeness and checksums.").set_defaults(func=cmd_audit_release)
    sub.add_parser("summary", help="Print processed table row counts.").set_defaults(func=cmd_summary)
    sub.add_parser("config", help="Print release configuration.").set_defaults(func=cmd_config)
    qai = sub.add_parser("compute-qai", help="Compute QAI from three numbers.")
    qai.add_argument("--pending", type=float, required=True)
    qai.add_argument("--previous-pending", type=float, required=True)
    qai.add_argument("--completed", type=float, required=True)
    qai.set_defaults(func=cmd_compute_qai)
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    configure_logging(args.verbose)
    logging.getLogger("oico").debug("running command %s", args.command)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
