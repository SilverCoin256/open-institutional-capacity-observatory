# Metric Reference

Every OICO metric is treated as a transparent research construct, not a magic score.

## Queue Acceleration Index

Definition: `QAI_t = (Pending_t - Pending_{t-1}) / Completions_t`.

Mathematical intuition: backlog growth is normalized by completed work. A positive value means the queue grew relative to throughput; values above 1 mean backlog increased by more than one period of completions.

Assumptions: adjacent periods use comparable definitions, pending counts are reported consistently, and completions are a meaningful denominator.

Limitations: QAI is not causal, cannot identify staffing, and cannot distinguish demand shocks from policy shocks.

Failure modes: boundary changes, reporting revisions, or one-time operational shocks can masquerade as capacity change.

Expected misuse: claiming an agency failed because QAI is positive without institutional context.

## Saturation/Erosion Degradation Index

Definition: SEDI standardizes selected public indicators against a local baseline and maps the mean pressure signal into `[0, 1]`.

Mathematical intuition: pressure indicators move upward; health indicators move downward; standardization makes the direction inspectable.

Assumptions: the selected proxies have theoretical links to oversight quality, and the baseline window is defensible.

Limitations: SEDI is not ground truth and should be validated against external outcomes before policy use.

Failure modes: proxy drift, missing variables, and distribution shifts can dominate the index.

Expected misuse: treating a bounded index as an official quality score.

## Accountability Specificity Index

Definition: ASI sums eight 0-2 document coding dimensions: named actor, decision authority, review duty, override authority, documentation duty, appeal/contestability, audit obligation, and error ownership.

Mathematical intuition: more explicit textual assignment of responsibility receives higher scores.

Assumptions: document text is a useful but incomplete signal of accountability architecture.

Limitations: specificity does not prove enforcement; small corpora require conservative claims.

Failure modes: highly specific but unenforced text, ambiguous source excerpts, and coder disagreement.

Expected misuse: ranking institutions as operationally accountable from text alone.

## Authorization Saturation

Definition: authorization quality is modeled as a mixture of substantive and ceremonial review as utilization crosses a tolerance threshold.

Mathematical intuition: as workload pressure rises, review can become formally present but substantively thin.

Assumptions: review quality can be approximated with a smooth transition and a small number of interpretable parameters.

Limitations: the model is illustrative until calibrated.

Failure modes: users may treat scenario outputs as empirical policy estimates.

Expected misuse: claiming a real agency will improve by the simulated amount.

## Procedural Capacity

Definition: procedural failure risk rises with AI output volume relative to review capacity and falls with contestability and ownership safeguards.

Mathematical intuition: overload increases risk; safeguards moderate but do not erase overload.

Assumptions: safeguards can be represented on a normalized scale.

Limitations: not a validated legal-risk score.

Failure modes: synthetic days can be mistaken for observed days.

Expected misuse: certification of a live AI governance system without audit.
