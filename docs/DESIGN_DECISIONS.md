# Design Decisions

## D1: One flagship analysis

Problem: the RC exposed five modules without a clear intellectual anchor.

Alternatives: lead with a catalog of all metrics, lead with the AI-governance corpus, or lead with the strongest public workload series.

Chosen: EOIR QAI. It has the clearest inputs, interpretable transformation, and strongest provenance among the stored datasets.

Downside: it is narrower than the full institutional-capacity vision. Reconsider when a second dataset has comparable provenance and a defensible cross-institution design.

## D2: Status hierarchy

Problem: mathematical completeness was being confused with empirical validation.

Chosen: QAI stable, ASI beta, SEDI and the two formal models experimental.

Validation: module-by-module adversarial review in `docs/METRIC_STATUS.md`.

Downside: fewer headline features appear mature. That is the scientifically honest trade-off.

## D3: Frozen snapshots

Problem: live public endpoints can change and make historical reproduction impossible.

Chosen: ship frozen snapshots with source URLs, dates, checksums, and a transformation log.

Downside: a frozen snapshot can become stale. Reconsider through a versioned source-refresh release, never by silently replacing inputs.

## D4: No missing-value imputation by default

Problem: treating missing public reporting as zero would create false precision.

Chosen: preserve missingness and emit quality flags; metrics return undefined or require explicit inputs.

Downside: some panels are less complete. Reconsider only with a documented imputation model and sensitivity analysis.

## D5: Baselines are not ground truth

Problem: benchmark outputs could be mistaken for validated institutional labels.

Chosen: label current tasks as baseline and teaching tasks until independent labels or outcomes exist.

Downside: no leaderboard claim yet. Reconsider after a preregistered evaluation design and external validation set.

## D6: DOI is a real external state

Problem: citation files can imply archival permanence before an archive exists.

Chosen: include citation metadata without a DOI and document the Zenodo gate.

Downside: citation convenience is lower until deposit. Reconsider only after an authenticated archive is published and verified.

## D7: Static site with a generated figure

Problem: the research story was buried in a generic documentation landing page.

Chosen: keep static HTML/CSS and place the flagship figure in the first substantive section.

Downside: no dynamic explorer yet. Reconsider after a real researcher use case justifies the maintenance cost.
