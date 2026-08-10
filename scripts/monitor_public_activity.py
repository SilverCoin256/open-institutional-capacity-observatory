#!/usr/bin/env python3
"""Record low-volume public GitHub activity without reading private data."""

from __future__ import annotations

import json
import os
import sys
import urllib.request
from datetime import datetime, timezone
from pathlib import Path


REPOSITORY = "SilverCoin256/open-institutional-capacity-observatory"
API_ROOT = f"https://api.github.com/repos/{REPOSITORY}"
DEFAULT_ROOT = Path.home() / "Library" / "Application Support" / "OICO" / "monitor"


def fetch(path: str) -> object:
    request = urllib.request.Request(
        f"{API_ROOT}{path}",
        headers={"Accept": "application/vnd.github+json", "User-Agent": "OICO-public-monitor"},
    )
    with urllib.request.urlopen(request, timeout=20) as response:
        return json.load(response)


def main() -> int:
    root = Path(os.environ.get("OICO_MONITOR_DIR", DEFAULT_ROOT))
    root.mkdir(parents=True, exist_ok=True)
    state_path = root / "state.json"
    event_path = root / "events.jsonl"
    previous = json.loads(state_path.read_text()) if state_path.exists() else {}
    current = {
        "issues": fetch("/issues?state=all&per_page=30"),
        "releases": fetch("/releases?per_page=10"),
    }
    previous_ids = set(previous.get("seen_ids", []))
    events: list[dict[str, object]] = []
    for item in current["issues"]:  # type: ignore[index]
        kind = "pull_request" if "pull_request" in item else "issue"
        identifier = f"{kind}:{item['id']}"
        if identifier not in previous_ids:
            events.append({"kind": kind, "id": identifier, "title": item["title"], "url": item["html_url"]})
        previous_ids.add(identifier)
    for item in current["releases"]:  # type: ignore[index]
        identifier = f"release:{item['id']}"
        if identifier not in previous_ids:
            events.append({"kind": "release", "id": identifier, "title": item["name"], "url": item["html_url"]})
        previous_ids.add(identifier)
    now = datetime.now(timezone.utc).isoformat()
    with event_path.open("a", encoding="utf-8") as stream:
        for event in events:
            stream.write(json.dumps({"observed_at": now, **event}, sort_keys=True) + "\n")
    if event_path.exists() and event_path.stat().st_size > 200_000:
        lines = event_path.read_text(encoding="utf-8").splitlines()[-500:]
        event_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    state_path.write_text(json.dumps({"checked_at": now, "seen_ids": sorted(previous_ids)}, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"checked_at": now, "new_events": len(events), "state": str(state_path)}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
