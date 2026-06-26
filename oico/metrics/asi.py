from __future__ import annotations


ASI_DIMENSIONS = [
    "named_accountable_actor",
    "decision_authority",
    "review_obligation",
    "override_authority",
    "documentation_duty",
    "appeal_or_contestability",
    "audit_obligation",
    "error_ownership",
]


def score_document(row: dict[str, object]) -> int:
    total = 0
    for dim in ASI_DIMENSIONS:
        if dim not in row or row[dim] in (None, ""):
            raise ValueError(f"ASI dimension {dim} is missing")
        numeric = float(row[dim])
        if not numeric.is_integer() or numeric not in (0.0, 1.0, 2.0):
            raise ValueError(f"ASI dimension {dim} must be one of 0, 1, or 2: {row[dim]}")
        total += int(numeric)
    return total


def validate_asi_row(row: dict[str, object]) -> list[str]:
    issues: list[str] = []
    total = score_document(row)
    reported = int(float(row.get("total_adjudicated_asi_score", row.get("total_asi_score", total)) or 0))
    if total != reported:
        issues.append(f"reported_total={reported} recomputed_total={total}")
    return issues


METRIC_DOCUMENTATION = {
    "definition": "ASI sums eight 0-2 document-coding dimensions of accountability specificity.",
    "mathematical_intuition": "Higher scores indicate more explicit assignment of actors, authority, documentation, contestability, audit, and error ownership.",
    "assumptions": ["The codebook dimensions are relevant to textual accountability.", "Coders apply the ordinal rubric consistently."],
    "limitations": ["Textual specificity does not prove operational accountability.", "Small corpora require conservative claims.", "Independent reliability should be reported before strong use."],
    "failure_modes": ["Ambiguous policy text can inflate disagreement.", "Documents can be specific but unenforced.", "Missing source text limits re-coding."],
    "expected_misuse": "Ranking institutions as substantively accountable solely from document text.",
}
