from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def code_cells(path: Path) -> list[str]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    cells = []
    for cell in payload.get("cells", []):
        if cell.get("cell_type") == "code":
            source = cell.get("source", "")
            cells.append("".join(source) if isinstance(source, list) else str(source))
    return cells


def main() -> int:
    notebooks = sorted((ROOT / "notebooks").glob("*.ipynb"))
    for notebook in notebooks:
        source = "\n\n".join(code_cells(notebook))
        with tempfile.NamedTemporaryFile("w", suffix=".py", delete=False, encoding="utf-8") as handle:
            handle.write(source)
            temp_path = Path(handle.name)
        env = os.environ.copy()
        existing = env.get("PYTHONPATH")
        env["PYTHONPATH"] = str(ROOT) if not existing else f"{ROOT}{os.pathsep}{existing}"
        code = subprocess.call([sys.executable, str(temp_path)], cwd=ROOT, env=env)
        temp_path.unlink(missing_ok=True)
        if code != 0:
            print(f"Notebook failed: {notebook}")
            return code
        print(f"Notebook executed: {notebook.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
