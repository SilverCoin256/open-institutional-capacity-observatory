from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PATTERNS = {
    "github_token": re.compile(r"gh[pousr]_[A-Za-z0-9_]{20,}"),
    "generic_secret_assignment": re.compile(r"(?i)(api[_-]?key|secret|token)\s*[:=]\s*['\"][A-Za-z0-9_\-]{16,}['\"]"),
    "aws_access_key": re.compile(r"AKIA[0-9A-Z]{16}"),
}
SKIP_SUFFIXES = {".svg", ".png", ".jpg", ".jpeg", ".pdf", ".pyc"}
SKIP_DIRS = {".git", "__pycache__", ".pytest_cache", ".mypy_cache", "node_modules"}


def iter_files() -> list[Path]:
    files: list[Path] = []
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        if path.suffix.lower() in SKIP_SUFFIXES:
            continue
        files.append(path)
    return files


def main() -> int:
    findings = []
    for path in iter_files():
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for name, pattern in PATTERNS.items():
            for match in pattern.finditer(text):
                findings.append({"pattern": name, "path": path.relative_to(ROOT).as_posix(), "offset": match.start()})
    if findings:
        for finding in findings:
            print(f"{finding['pattern']} {finding['path']} offset={finding['offset']}")
        return 1
    print("No high-risk credential patterns found in repository files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
