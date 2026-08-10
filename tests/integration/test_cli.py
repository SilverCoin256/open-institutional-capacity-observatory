from __future__ import annotations

import contextlib
import io
import unittest

from oico.cli.main import main


class CliIntegrationTests(unittest.TestCase):
    def run_command(self, *args: str) -> str:
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            code = main(list(args))
        self.assertEqual(code, 0, args)
        return output.getvalue()

    def test_public_commands(self) -> None:
        self.assertIn('"status": "pass"', self.run_command("build-data"))
        self.assertIn('"status": "pass"', self.run_command("validate-data"))
        self.assertIn("figures", self.run_command("make-figures"))
        self.assertIn("results", self.run_command("run-benchmarks"))
        self.assertIn("research_question", self.run_command("run-flagship"))
        self.assertIn("queue_observations", self.run_command("summary"))
        self.assertIn("raw_snapshot_policy", self.run_command("config"))
        self.assertIn("0.5", self.run_command("compute-qai", "--pending", "10", "--previous-pending", "9", "--completed", "2"))
        self.assertIn('"status": "pass"', self.run_command("audit-release"))

    def test_full_reproduction_command(self) -> None:
        output = self.run_command("reproduce")
        self.assertIn('"flagship"', output)
        self.assertIn('"release_audit"', output)
