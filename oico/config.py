from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from oico.io import ROOT


DEFAULT_CONFIG = ROOT / "config" / "oico.release.json"


def load_config(path: Path | None = None) -> dict[str, Any]:
    config_path = path or DEFAULT_CONFIG
    return json.loads(config_path.read_text(encoding="utf-8"))
