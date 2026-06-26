from __future__ import annotations

import unittest

from oico.datasets import build_all
from oico.io import ROOT, read_csv, read_json


class DatasetBuildTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.report = build_all()

    def test_validation_passes(self) -> None:
        self.assertEqual(self.report["status"], "pass")

    def test_expected_processed_tables_exist(self) -> None:
        for name in ["institutions", "queue_observations", "institutional_indicators", "asi_scores", "metric_catalog"]:
            path = ROOT / "datasets" / "processed" / f"{name}.csv"
            self.assertTrue(path.exists(), path)
            self.assertGreater(len(read_csv(path)), 0)

    def test_manifest_has_raw_files(self) -> None:
        manifest = read_json(ROOT / "datasets" / "manifests" / "dataset_manifest.json")
        paths = {item["path"] for item in manifest["files"]}
        self.assertIn("datasets/raw/eoir_annual.csv", paths)
        self.assertIn("datasets/raw/asi_adjudicated_matrix.csv", paths)


if __name__ == "__main__":
    unittest.main()
