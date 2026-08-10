from __future__ import annotations

import unittest

from oico.metrics.asi import score_document
from oico.metrics.qai import compute_qai_series, queue_acceleration_index
from oico.metrics.sedi import logistic, rolling_sedi, sedi_from_indicators
from oico.models.authorization import authorization_quality, intervention_scenarios
from oico.models.procedural_capacity import procedural_failure_risk, simulate_procedural_days


class MetricTests(unittest.TestCase):
    def test_qai_formula(self) -> None:
        value = queue_acceleration_index(1108300, 975977, 195145)
        self.assertAlmostEqual(value, 0.6781, places=3)

    def test_qai_missing_or_zero_completions_is_undefined(self) -> None:
        self.assertIsNone(queue_acceleration_index(10, 9, 0))
        self.assertIsNone(queue_acceleration_index(10, 9, None))

    def test_qai_rejects_negative_completions(self) -> None:
        with self.assertRaises(ValueError):
            queue_acceleration_index(10, 9, -1)

    def test_qai_series_preserves_first_and_missing_periods(self) -> None:
        values = compute_qai_series([
            {"pending": 10, "completed": 2},
            {"pending": 14, "completed": 2},
            {"pending": "", "completed": 2},
            {"pending": 20, "completed": 2},
        ])
        self.assertEqual(values, [None, 2.0, None, None])

    def test_qai_rejects_non_numeric_series_values(self) -> None:
        with self.assertRaises(ValueError):
            compute_qai_series([{"pending": "not-a-number", "completed": 1}])

    def test_sedi_bounds(self) -> None:
        value = sedi_from_indicators(
            {"pressure": 10.0, "health": 2.0},
            {"pressure": [1.0, 2.0, 3.0], "health": [5.0, 6.0, 7.0]},
            positive_indicators=["pressure"],
            negative_indicators=["health"],
        )
        self.assertGreaterEqual(value, 0.0)
        self.assertLessEqual(value, 1.0)

    def test_sedi_handles_missing_indicators_neutrally(self) -> None:
        value = sedi_from_indicators({}, {"pressure": [1.0, 2.0]}, ["pressure"], [])
        self.assertEqual(value, 0.5)

    def test_sedi_logistic_is_stable_at_extremes(self) -> None:
        self.assertEqual(logistic(-1000), 0.0)
        self.assertEqual(logistic(1000), 1.0)

    def test_sedi_rejects_invalid_configuration(self) -> None:
        with self.assertRaises(ValueError):
            sedi_from_indicators({"x": 1.0}, {"x": [0.0]}, ["x"], ["x"])
        with self.assertRaises(ValueError):
            rolling_sedi([], [], [], window=1)

    def test_asi_score(self) -> None:
        row = {
            "named_accountable_actor": 2,
            "decision_authority": 2,
            "review_obligation": 1,
            "override_authority": 0,
            "documentation_duty": 1,
            "appeal_or_contestability": 2,
            "audit_obligation": 1,
            "error_ownership": 2,
        }
        self.assertEqual(score_document(row), 11)

    def test_asi_rejects_missing_or_nonordinal_dimensions(self) -> None:
        with self.assertRaises(ValueError):
            score_document({})
        row = {dimension: 1 for dimension in [
            "named_accountable_actor", "decision_authority", "review_obligation", "override_authority",
            "documentation_duty", "appeal_or_contestability", "audit_obligation", "error_ownership",
        ]}
        row["error_ownership"] = 1.5
        with self.assertRaises(ValueError):
            score_document(row)

    def test_authorization_quality_bounds(self) -> None:
        value = authorization_quality(0.7, k=1.0)
        self.assertGreaterEqual(value, 0.0)
        self.assertLessEqual(value, 1.0)

    def test_authorization_rejects_invalid_parameters(self) -> None:
        with self.assertRaises(ValueError):
            authorization_quality(-0.1)
        with self.assertRaises(ValueError):
            authorization_quality(0.7, q_ceremonial=1.1)

    def test_throughput_and_capacity_scenarios_diverge(self) -> None:
        scenarios = {row["scenario"]: row for row in intervention_scenarios(0.7)}
        self.assertLess(scenarios["double_capacity"]["rho_s"], scenarios["baseline"]["rho_s"])
        self.assertGreater(scenarios["halve_throughput"]["rho_s"], scenarios["baseline"]["rho_s"])

    def test_procedural_risk_bounds(self) -> None:
        value = procedural_failure_risk(140, 100, 0.5, 1.0)
        self.assertGreaterEqual(value, 0.0)
        self.assertLessEqual(value, 1.0)

    def test_procedural_risk_handles_zero_capacity(self) -> None:
        self.assertEqual(procedural_failure_risk(10, 0, 0.5, 0.5), 1.0)

    def test_procedural_model_rejects_invalid_inputs(self) -> None:
        with self.assertRaises(ValueError):
            procedural_failure_risk(-1, 10, 0.5, 0.5)
        with self.assertRaises(ValueError):
            procedural_failure_risk(10, 10, 1.1, 0.5)
        with self.assertRaises(ValueError):
            simulate_procedural_days(-1)


if __name__ == "__main__":
    unittest.main()
