# Researcher Onboarding

## Is OICO relevant to you?

OICO is for researchers studying administrative workload, public decision systems, AI governance, organizational bottlenecks, or reproducible measurement from public data. It is useful when you need a transparent starting point for queue observations, source provenance, descriptive indices, or teaching examples.

OICO does not identify institutional quality, causal effects, staffing effort, legal compliance, or organizational intent. Three modules are experimental and need calibration before substantive use.

## Five-minute route

1. Open the [three-command reproduction page](https://silvercoin256.github.io/open-institutional-capacity-observatory/reproduce/).
2. Read [the flagship case](../docs/FLAGSHIP_CASE_STUDY.md).
3. Inspect `datasets/metadata/source_register.csv` and `datasets/metadata/license_review.md`.
4. Run `python -m pip install -e .` and `oico reproduce`.
5. Inspect `examples/flagship/outputs/` and the metric status table.
6. Read [REPLICATION.md](../REPLICATION.md) and [Break OICO](../BREAK_OICO.md) before making a claim about reproduction or validity.

The stable public API currently includes `oico.queue_acceleration_index`. The CLI and data layouts are designed to make extension inspectable rather than to hide assumptions in a large framework.

## How to object

Methodological objections are welcome. Open an issue with the construct, input, transformation, interpretation, or provenance problem; include a minimal example where possible; and distinguish a reproducibility defect from a disagreement about the research design.

## Citation

Use `CITATION.cff` for the software release. Cite the original public data sources listed in the source register when using a dataset.
