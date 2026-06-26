from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Field:
    name: str
    dtype: str
    description: str
    nullable: bool = False


INSTITUTIONS = [
    Field("institution_id", "string", "Stable OICO identifier."),
    Field("name", "string", "Human-readable institution name."),
    Field("jurisdiction", "string", "Primary jurisdiction represented by the dataset."),
    Field("sector", "string", "Public, private, higher education, or mixed sector."),
    Field("domain", "string", "Research domain represented by the institution."),
    Field("unit_of_observation", "string", "Primary analytical unit available in v1."),
    Field("source_dataset_id", "string", "Dataset family that introduced the institution."),
]

QUEUE_OBSERVATIONS = [
    Field("observation_id", "string", "Stable row identifier."),
    Field("institution_id", "string", "Foreign key to institutions.csv."),
    Field("period", "string", "Reported fiscal year, quarter, month, or date label."),
    Field("period_start", "string", "ISO-style start date where inferable.", True),
    Field("period_end", "string", "ISO-style end date where inferable.", True),
    Field("pending", "integer", "Cases/items pending at the reporting boundary."),
    Field("received", "integer", "Cases/items received during the period.", True),
    Field("completed", "integer", "Cases/items completed during the period.", True),
    Field("qai", "number", "Queue Acceleration Index recomputed by OICO.", True),
    Field("source_qai", "number", "QAI value inherited from the source snapshot.", True),
    Field("qai_delta", "number", "Difference between recomputed and inherited QAI.", True),
    Field("quality_flags", "string", "Pipe-separated validation notes."),
    Field("source_dataset_id", "string", "Source dataset family."),
]

INSTITUTIONAL_INDICATORS = [
    Field("observation_id", "string", "Stable row identifier."),
    Field("institution_id", "string", "Foreign key to institutions.csv."),
    Field("period", "string", "Reported period."),
    Field("indicator_family", "string", "CFPB, SEC, or other indicator family."),
    Field("volume", "number", "Observed public workload volume."),
    Field("operational_rate", "number", "Public operational-throughput or timeliness rate.", True),
    Field("substantive_rate", "number", "Outcome-quality proxy rate.", True),
    Field("review_intensity", "number", "Review output divided by review base.", True),
    Field("sedi", "number", "Saturation/erosion degradation index recomputed by OICO.", True),
    Field("quality_flags", "string", "Pipe-separated validation notes."),
    Field("source_dataset_id", "string", "Source dataset family."),
]

ASI_SCORES = [
    Field("document_id", "string", "ASI corpus document identifier."),
    Field("institution_name", "string", "Institution or source body named in the corpus."),
    Field("institution_category", "string", "Corpus category."),
    Field("sector", "string", "Sector label from the corpus manifest."),
    Field("jurisdiction", "string", "Jurisdiction label from the corpus manifest."),
    Field("document_title", "string", "Document title."),
    Field("document_type", "string", "Source document type."),
    Field("document_stratum", "string", "Corpus stratum."),
    Field("domain", "string", "Policy or governance domain."),
    Field("published_or_updated_date", "string", "Publication/update date when known.", True),
    Field("source_url", "string", "Official source URL recorded in the corpus manifest.", True),
    Field("total_asi_score", "integer", "Recomputed total ASI score, 0-16."),
    Field("coding_confidence", "string", "Coder confidence label."),
    Field("quality_flags", "string", "Pipe-separated validation notes."),
]

METRIC_CATALOG = [
    Field("metric_id", "string", "Stable metric identifier."),
    Field("name", "string", "Metric name."),
    Field("definition", "string", "Formal definition."),
    Field("mathematical_intuition", "string", "Short intuition for the computation."),
    Field("assumptions", "string", "Pipe-separated assumptions."),
    Field("limitations", "string", "Pipe-separated limitations."),
    Field("failure_modes", "string", "Pipe-separated failure modes."),
    Field("expected_misuse", "string", "Known misuse to avoid."),
]


SCHEMAS = {
    "institutions": INSTITUTIONS,
    "queue_observations": QUEUE_OBSERVATIONS,
    "institutional_indicators": INSTITUTIONAL_INDICATORS,
    "asi_scores": ASI_SCORES,
    "metric_catalog": METRIC_CATALOG,
}


def fieldnames(name: str) -> list[str]:
    return [field.name for field in SCHEMAS[name]]


def schema_as_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for table, fields in SCHEMAS.items():
        for field in fields:
            rows.append(
                {
                    "table": table,
                    "field": field.name,
                    "dtype": field.dtype,
                    "nullable": field.nullable,
                    "description": field.description,
                }
            )
    return rows
