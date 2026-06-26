from __future__ import annotations

import csv
import hashlib
import json
import os
from pathlib import Path
from typing import Iterable


def _is_project_root(path: Path) -> bool:
    return (path / "pyproject.toml").is_file() and (path / "datasets").is_dir()


def find_project_root(start: Path | None = None, package_root: Path | None = None) -> Path:
    configured = os.environ.get("OICO_PROJECT_ROOT")
    if configured:
        root = Path(configured).expanduser().resolve()
        if not _is_project_root(root):
            raise RuntimeError(f"OICO_PROJECT_ROOT is not an OICO checkout: {root}")
        return root

    origin = (start or Path.cwd()).resolve()
    for candidate in (origin, *origin.parents):
        if _is_project_root(candidate):
            return candidate

    installed_from = (package_root or Path(__file__).resolve().parents[1]).resolve()
    if _is_project_root(installed_from):
        return installed_from
    return installed_from


ROOT = find_project_root()


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8-sig") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: Iterable[dict[str, object]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow({name: row.get(name, "") for name in fieldnames})


def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def read_json(path: Path) -> object:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def relative(path: Path) -> str:
    try:
        return path.resolve().relative_to(ROOT).as_posix()
    except ValueError:
        return path.as_posix()


def as_float(value: object, default: float | None = None) -> float | None:
    if value in (None, ""):
        return default
    try:
        return float(str(value).replace(",", ""))
    except ValueError:
        return default
