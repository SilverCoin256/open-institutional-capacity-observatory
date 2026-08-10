"""Run the canonical EOIR flagship case study."""

from __future__ import annotations

import json

from oico.flagship import run_flagship


if __name__ == "__main__":
    print(json.dumps(run_flagship(), indent=2, sort_keys=True))
