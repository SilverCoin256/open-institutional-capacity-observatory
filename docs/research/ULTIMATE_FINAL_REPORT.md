# OICO Ultimate Final Report

Audit date: 2026-08-10. This report is an internal research and engineering audit. It is not an admissions prediction, peer-review decision, or external validation record.

## A. ONE-SENTENCE VERDICT

OICO is now a public, versioned, low-dependency research-infrastructure package with a bounded four-system descriptive study and a reproducible clean-room route, but it has not yet earned external scientific or academic adoption.

## B. FINAL SCIENTIFIC CONTRIBUTION

The defensible contribution is an auditable workflow for turning frozen public administrative traces into provenance-linked tables, transparent workload measures, reproducible figures, benchmark baselines, and explicit non-claims. Study 1 shows that queue signals agree directionally within EOIR and USCIS, while CFPB and SEC indicators move differently enough to reject a single pooled institutional-capacity ranking. The contribution is measurement infrastructure and disciplined comparison, not a new capacity theory or validated universal index.

## C. STUDY 1

| Field | Final specification |
|---|---|
| RQ | Do standardized workload signals reveal consistent processing pressure within multiple public administrative systems beyond simpler conventional measures? |
| Data | Frozen public snapshots: EOIR annual, USCIS quarterly, CFPB monthly, SEC annual. |
| N | EOIR: 9 authoritative periods; USCIS: 12 periods; CFPB: 168 months / 14 annual groups; SEC: 19 years. |
| Institutions | EOIR, USCIS, CFPB, SEC. |
| Period | EOIR primary inference FY2016-FY2024; USCIS, CFPB, and SEC use the periods recorded in their source snapshots. |
| Method | Within-system change, backlog growth, clearance, backlog/completions, QAI, volume and intensity baselines; sign agreement, descriptive Pearson association, aggregation comparison, and trend slopes. |
| Result | EOIR QAI positive in 8/8 transitions, mean 1.095125; USCIS positive in 11/11, mean 0.016438. CFPB annual volume/substantive-rate r=0.690828; SEC volume/review-intensity r=0.841144 but volume/response-intensity r=-0.097657. |
| Uncertainty | No inferential intervals are reported for small aggregate queue panels. Associations are descriptive, not causal. |
| Baselines | Absolute pending change, percentage growth, clearance ratio, backlog/completions, volume, operational rate, substantive rate, review intensity, and response intensity. |
| Robustness | FY2025/FY2026 excluded from authoritative EOIR inference; missing completions remain missing; monthly versus annual CFPB results are compared; SEC is tested against two intensity definitions; pooled ranking is rejected. |
| Biggest limitation | No independently recovered waiting-time, case-age, staffing, intervention, or service-outcome series establishes construct validity. |

The executable plan is [`STUDY1_ANALYSIS_PLAN.md`](STUDY1_ANALYSIS_PLAN.md), the results are [`STUDY1_RESULTS.md`](STUDY1_RESULTS.md), and the machine-readable output is `research/outputs/study1_results.json`.

## D. NOVELTY

- **Metric novelty: low.** QAI is a named implementation convention for normalized backlog change, not new mathematics.
- **Empirical novelty: low to moderate.** The frozen EOIR and comparative traces are useful artifacts, but the underlying administrative patterns are not claimed as newly discovered.
- **Framework novelty: moderate.** The provenance, scope, noncomparability, validation, and benchmark contract is more integrated than a one-off analysis, but it is an incremental research-infrastructure contribution.
- **Software novelty: moderate.** The package combines deterministic data builds, source quarantine, checksums, reproducible figures, benchmarks, CLI workflows, release audits, and teaching-facing materials in one public artifact.

## E. RESEARCH-RIGOR SELF-AUDIT

This is a self-audit against the current ISEF-style research benchmark, not an official score. The official criteria emphasize the question, methodology, execution, creativity/potential impact, and presentation/interview, including interpretation and limitations. OICO's internal score is **73/100**:

| Criterion | Score | Reason |
|---|---:|---|
| Research question | 8/10 | Clear as a descriptive measurement question; broad platform language remains narrower in the actual evidence. |
| Design and methodology | 9/15 | Explicit baselines and boundaries; no matched cohort, intervention, or external target. |
| Execution | 14/20 | Strong deterministic software and artifact controls; small aggregate panels and inherited source limitations remain. |
| Creativity and potential impact | 13/20 | Coherent infrastructure and comparative workflow; metric and empirical result are not highly novel. |
| Presentation and interview | 29/35 | Public documentation, Q&A, figures, and limitations are unusually complete; outside scrutiny is absent. |

The score is a calibration tool, not a claim of finalist quality.

## F. PASSION-PROJECT DIFFERENTIATION SCORE

The controlled internal differentiation score is **84/100**, with **external consequence scored 0/5**. Evidence is recorded in [`PROJECT_DIFFERENTIATION_SCORECARD.md`](../../PROJECT_DIFFERENTIATION_SCORECARD.md): intellectual coherence 14/15, research depth 10/15, technical creation 14/15, original judgment 9/10, scientific integrity 10/10, external auditability 9/10, public usefulness 9/10, communication 5/5, sustained history 4/5, external consequence 0/5. This score is not an admissions probability.

## G. WHAT WAS KILLED

- QAI as a new mathematical index, validated capacity measure, causal estimator, or diagnostic of staffing, intent, legality, or institutional failure.
- A universal pooled ranking across EOIR, USCIS, CFPB, and SEC.
- FY2025/FY2026 as authoritative EOIR evidence.
- Experimental SEDI, Authorization Saturation, and Procedural Capacity modules as flagship findings.
- Synthetic or proxy-label benchmarks as evidence of real-world predictive performance.
- Causal, intervention, leaderboard, DOI, PyPI, citation, adoption, professor, course, lab, and conference claims without evidence.
- Further metric and dashboard expansion before external scrutiny.

## H. PUBLIC STATE

- GitHub: [SilverCoin256/open-institutional-capacity-observatory](https://github.com/SilverCoin256/open-institutional-capacity-observatory)
- Final commit: the tagged commit published with `v1.1.0` after this audit.
- Release: `v1.1.0`, a new minor release; existing `v1.0.0` remains unchanged.
- Site: [OICO public research site](https://silvercoin256.github.io/open-institutional-capacity-observatory/)
- DOI: none issued.
- PyPI: no publication claimed.
- Reproduction: `oico reproduce` for the core workflow; `oico reproduce --full` for Study 1.
- Break OICO: [public adversarial review page](https://silvercoin256.github.io/open-institutional-capacity-observatory/break.html)

## I. TECHNICAL STATE

- 25 tests pass; overall coverage is 91% and QAI coverage is 95%.
- CI is configured for Python 3.10, 3.11, and 3.12 on Ubuntu.
- Wheel and source distribution metadata pass `twine check`; the installed wheel reports `oico 1.1.0`.
- A fresh extracted `v1.1.0` source archive installs successfully and passes `oico reproduce --full`.
- The full workflow regenerates validated data, six figures, five benchmark outputs, the EOIR flagship, Study 1 outputs, release manifests, and the release audit.
- Runtime dependencies remain intentionally minimal; the project is distributed as a Python package with a CLI and static public site.

## J. EXTERNAL CAMPAIGN

- Targets researched: 60 relevant researchers and labs in the private operations register.
- Verified professional contacts: 4.
- Messages sent: 0.
- Follow-ups scheduled: 0.
- Areas represented: computational social science, public administration, AI governance, organizational research, administrative burden, research software, and reproducibility.
- **OUTREACH BLOCKED BY AUTHENTICATED SENDER.** No authenticated scholarly email identity or approved sender connector was available, so no message was sent and no outreach was represented as underway.

## K. EXTERNAL EVIDENCE

Verified as of 2026-08-10: independent reproductions 0; methodological critiques 0; external issues 0; external pull requests 0; named labs using OICO 0; professor recommendations 0; university course links 0; published citations 0; conference posters or demos built with OICO 0; collaborations 0; DOI 0; PyPI publication 0. Internal tests, repository existence, self-authored examples, and this report do not count.

## L. APPLICATION VALUE

The previous repository mainly revealed persistence and implementation ability. This final OICO state reveals something more specific: the creator can turn a broad intellectual interest into a bounded research program, recover from an initially overclaimed metric, separate stable from experimental work, preserve inconvenient source rows without using them, write an executable analysis plan, compare four unlike administrative systems without forcing a false ranking, and publish the negative results and missing validation as part of the artifact. It also shows ownership of the entire research chain: question, source register, transformations, code, tests, figures, release process, public explanation, adversarial review, and evidence ledger. The strongest signal is not that the project is already influential. It is that the creator understands why influence cannot be claimed before another person has used, challenged, reproduced, or cited the work. That distinction was not visible in the earlier repository. No admissions probability is inferred.

## M. BIGGEST REMAINING WEAKNESS

Construct validity: the package still has no independent outcome or intervention showing that its workload signals measure a theoretically distinct form of institutional capacity rather than reporting volume, stock-flow arithmetic, or source-definition artifacts.

## N. TRUE BLOCKERS

The remaining blockers are external-human or authentication dependencies only: an independent researcher must reproduce or critique the work; a scholarly sender identity is required to send the prepared campaign; a Zenodo account is required for a DOI; a package-index owner is required for PyPI; and outside users must create any adoption, course, citation, collaboration, or conference evidence.

## O. SECURITY

No credential is stored in the repository, documentation, release archives, or public site. Secret scanning, documentation checks, diff checks, tests, and release audits pass. Temporary virtual environments and clean-room directories were created outside the repository for validation and are disposable; no credential was placed in them. The local public-API monitor remains installed without storing credentials. The GitHub credential previously pasted in conversation should be revoked and replaced.

## P. FINAL STATE

**NOT FINISHED**

All controllable research, engineering, publication-surface, and validation-preparation work is complete. External validation has not begun because outreach was blocked by the missing authenticated sender; therefore this report does not claim that outside responses are pending.
