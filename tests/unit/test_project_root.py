from __future__ import annotations

import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from oico.io import find_project_root


def make_checkout(path: Path) -> Path:
    path.mkdir(parents=True)
    (path / "datasets").mkdir()
    (path / "pyproject.toml").write_text("[project]\nname = 'oico'\n", encoding="utf-8")
    return path.resolve()


class ProjectRootTests(unittest.TestCase):
    def test_current_checkout_wins_over_installed_package(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            base = Path(temp)
            checkout = make_checkout(base / "checkout")
            notebook_dir = checkout / "notebooks"
            notebook_dir.mkdir()
            installed_package = base / "venv" / "site-packages"
            installed_package.mkdir(parents=True)

            root = find_project_root(start=notebook_dir, package_root=installed_package)

            self.assertEqual(root, checkout)

    def test_environment_override_is_validated(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            checkout = make_checkout(Path(temp) / "checkout")
            with patch.dict(os.environ, {"OICO_PROJECT_ROOT": str(checkout)}):
                self.assertEqual(find_project_root(), checkout)

            with patch.dict(os.environ, {"OICO_PROJECT_ROOT": str(checkout / "missing")}):
                with self.assertRaises(RuntimeError):
                    find_project_root()


if __name__ == "__main__":
    unittest.main()
