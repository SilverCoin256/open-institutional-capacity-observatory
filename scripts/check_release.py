from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def run(args: list[str]) -> int:
    print("$ " + " ".join(args))
    return subprocess.call(args, cwd=ROOT)


def main() -> int:
    checks = [
        [sys.executable, "scripts/scan_secrets.py"],
        [sys.executable, "scripts/check_docs.py"],
        [sys.executable, "scripts/package_release.py"],
        [sys.executable, "-m", "unittest", "discover", "-s", "tests"],
        [sys.executable, "scripts/execute_notebooks.py"],
        [sys.executable, "scripts/package_release.py"],
        [sys.executable, "-m", "oico.cli.main", "audit-release"],
    ]
    for check in checks:
        code = run(check)
        if code != 0:
            return code
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
