from __future__ import annotations

import unittest

from oico.benchmarks import run_all_benchmarks
from oico.datasets import build_all
from oico.visualization import make_all_figures


class ReproductionTests(unittest.TestCase):
    def test_reproduction_components(self) -> None:
        data_report = build_all()
        figures = make_all_figures()
        benchmarks = run_all_benchmarks()
        self.assertEqual(data_report["status"], "pass")
        self.assertEqual(len(figures), 6)
        self.assertEqual(len(benchmarks), 5)


if __name__ == "__main__":
    unittest.main()
