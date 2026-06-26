# Release Candidate Report

Version: `1.0.0-rc1`

Status: release candidate suitable for internal lab review, external reproduction, and course pilot use. It should not yet be presented as a mature public leaderboard or DOI-bearing archival release.

## 1. Everything Created

- Standalone repository scaffold for the Open Institutional Capacity Observatory.
- Dependency-light Python package `oico` with CLI commands for data build, validation, figure generation, benchmarks, reproduction, configuration, release audit, and QAI examples.
- Canonical data directories for raw snapshots, processed tables, metadata, manifests, checksums, validation reports, and quarantine reports.
- Processed canonical tables: institutions, queue observations, institutional indicators, ASI scores, and metric catalog.
- Metric implementations for QAI, SEDI, ASI, authorization saturation, and procedural capacity.
- Deterministic SVG figure gallery and figure manifest.
- Five benchmark tasks with reference baselines, frozen splits, expected outputs, and leaderboard caveats.
- Executable notebooks for reproduction, metric examples, research showcase, replication walkthrough, and a five-minute demo.
- Tests for metrics, dataset build, and reproduction.
- Credential scan, documentation link check, release audit, deterministic release archive, checksum sidecar, artifact manifest, and publication checklist.
- Static website portal with landing page, dataset explorer, metric glossary, benchmark page, examples, downloads, citation, and FAQ.
- Teaching assets: quickstart, one-hour tutorial, methods tutorial, professor guide, lab onboarding guide, assignment, and solution.
- Adoption assets: professor overview, lab overview, course adoption guide, skeptical FAQ, migration guide, and v2 roadmap.
- Publication assets: data descriptor outline, methods paper outline, journal supplement plan, conference artifact plan, poster outline, lightning talk outline, demo assets, release notes, CITATION.cff, and codemeta.
- Community files: contributing guide, code of conduct, governance policy, roadmap, issue templates, and discussion template.

## 2. Everything Merged

- EOIR and USCIS workload snapshots were merged into the QAI queue module and `queue_observations.csv`.
- CFPB Consumer Complaint Database aggregates and SEC EDGAR yearly review counts were merged into the institutional-indicator and SEDI module.
- ASI corpus manifest and adjudicated coding matrix were merged into the AI-governance accountability module and `asi_scores.csv`.
- Prior one-off metric language was canonicalized into `metric_catalog.csv` and `docs/concepts/metrics.md`.
- Prior reproducibility-package logic was consolidated into package functions, CLI commands, tests, notebooks, and release scripts.

## 3. Everything Archived

- Venue-specific manuscripts, old figures, and formatting assets are archived by reference rather than copied into the canonical release.
- Exploratory scripts from earlier projects are superseded by package modules where a canonical implementation now exists.
- `archive/README.md` records the policy: the archive is a decision log, not a dumping ground.

## 4. Everything Intentionally Excluded

- Invalid or weakly retrieved sources that could not satisfy provenance requirements.
- Private credentials and authenticated data access.
- Live scraping/fetching in the v1 release path.
- Claims of external adoption, citations, official endorsement, or benchmark status.
- DOI claims before an actual DOI is minted.
- Institution rankings that imply QAI and SEDI are substantively commensurate.
- Causal claims that AI caused observed institutional congestion.

## 5. Remaining Scientific Limitations

- V1 data coverage is small: 5 institutions/corpora, 23 queue observations, 187 institutional indicator observations, and 23 ASI documents.
- Several benchmark labels are proxy labels or synthetic targets, not independently adjudicated ground truth.
- Public traces do not reveal internal staffing, legal mandates, budget shocks, or case complexity.
- QAI, SEDI, and ASI are descriptive constructs unless a separate study supplies stronger identification.
- Official source policies are documented per dataset; a repository curator or legal reviewer should still confirm the record before a DOI-bearing deposit.
- ASI source-text modeling requires careful licensing and reliability review.

## 6. Remaining Engineering Limitations

- The v1 release uses frozen snapshots rather than live update modules.
- Schema validation is intentionally lightweight and dependency-free.
- The website is static HTML rather than a searchable documentation build.
- The R interface and REST API are planned but not implemented in v1.
- Benchmark baselines are simple reference implementations rather than strong models.
- The intended GitHub remote is not yet created and this machine has no authenticated GitHub session; citation metadata deliberately omits a repository URL until publication.

## 7. Remaining Adoption Risks

- Researchers may dismiss v1 as too small unless the project is framed as infrastructure plus a pilot corpus.
- Benchmark credibility depends on independent labels and external replication.
- Faculty adoption requires a clean class-tested workflow and likely one more round of teaching polish.
- Policy researchers may overinterpret scores unless caveats stay visible.
- A lab will need confidence that the dated source-license record is sufficient for its jurisdiction and repository policy.

## 8. Suggested First External Users

- A computational social science methods seminar studying reproducibility and public administrative data.
- A public administration or organizational sociology lab interested in queues, bottlenecks, and institutional capacity.
- An AI governance research group studying accountability documents and oversight capacity.
- A policy school data-science course that needs a reproducible, critique-friendly public-data assignment.
- A conference artifact-review audience for reproducible measurement infrastructure.

## 9. Recommended Publication Sequence

1. Software archive: tag `v1.0.0-rc1`, attach the GitHub release archive, and solicit clean-room reproduction.
2. Dataset archive: after source-license review, deposit frozen raw snapshots, processed tables, manifests, and checksums on Zenodo, OSF, or Dataverse.
3. Data descriptor: submit a short data descriptor emphasizing provenance, schemas, validation, and extension pathways.
4. Benchmark paper: only after independent labels or stronger targets exist for at least one benchmark task.
5. Methods paper: present the broader measurement framework, formal metrics, limitations, and cross-domain extension results.

## 10. Brutally Honest Assessment

OICO v1 is genuinely useful as research infrastructure, but it is not yet a field benchmark. Its strongest value is that it turns scattered paper-specific assets into a reproducible, teachable, extensible platform with visible provenance and conservative claims. A professor could assign it now as a methods and reproducibility module; a lab could extend it without reverse engineering; a PhD student could reproduce the outputs from a clean clone.

The project still needs more data, independent labels, formal source-license review, and external replication before it can credibly claim broad academic adoption or benchmark status. The correct public posture is: serious release candidate, not final authority.

## Verification Evidence

- `python -m oico.cli.main reproduce` passes.
- `python scripts/check_release.py` passes.
- 21 tests pass, including metric edge cases and installed-package project-root discovery.
- 5 notebooks execute.
- Credential scan passes.
- Documentation and website link check passes.
- Release audit reports no missing required paths and no checksum issues.
- A non-editable wheel built from the release archive passes the full release gate in an isolated environment.
- The release archive has a deterministic SHA-256 sidecar and a machine-verified artifact manifest.
