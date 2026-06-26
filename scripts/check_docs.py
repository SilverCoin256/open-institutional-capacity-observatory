from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
HREF_RE = re.compile(r'href="([^"]+)"')


def main() -> int:
    failures = []
    for path in list(ROOT.rglob("*.md")) + list((ROOT / "website").glob("*.html")):
        if ".git" in path.parts:
            continue
        text = path.read_text(encoding="utf-8")
        patterns = [LINK_RE]
        if path.suffix == ".html":
            patterns.append(HREF_RE)
        for pattern in patterns:
            matches = pattern.finditer(text)
            for match in matches:
                target = match.group(1).split("#", 1)[0]
                if not target or target.startswith(("http://", "https://", "mailto:", "#")):
                    continue
                candidate = (path.parent / target).resolve()
                if not candidate.exists():
                    failures.append(f"{path.relative_to(ROOT)} -> {target}")
    if failures:
        print("Broken local documentation links:")
        for failure in failures:
            print(failure)
        return 1
    print("Documentation link check passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
