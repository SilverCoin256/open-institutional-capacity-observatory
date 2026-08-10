# External Standards 2026

Audit date: 2026-08-10. This document records standards and project implications; it does not claim certification.

## Research and admissions calibration

- [Official Regeneron ISEF judging criteria](https://www.societyforscience.org/isef/grand-award/criteria/): question, methodology, execution, creativity/potential impact, and presentation/interview. Used only as a research-depth benchmark.
- [ISEF Software Design category](https://www.societyforscience.org/isef/categories-and-subcategories/software-design/): software and information processes may demonstrate, analyze, or control a process or solution. OICO still needs a credible research question and validation.
- [Harvard College admissions](https://college.harvard.edu/admissions): no formula; whole-person consideration including academic accomplishment, contribution, extracurricular distinction, and personal qualities.
- [Yale: What Yale Looks For](https://admissions.yale.edu/what-yale-looks-for): academic potential, intellectual initiative, curiosity, creativity, enterprise, and contribution.
- [Princeton admissions guidance](https://admission.princeton.edu/apply/before-you-apply/helpful-tips): intellectual curiosity, academic excellence, personal and extracurricular accomplishment, contribution, and authentic voice.
- [Penn academic preparation](https://admissions.upenn.edu/how-to-apply/preparing-your-application/academics): balanced preparation and challenge in context.
- [Penn M&T program information](https://admissions.upenn.edu/academics/exploring-academics/specialized-degree-programs): interdisciplinary engineering and business integration. This is a private context for the project's interdisciplinary arc, not a public project claim.

## Research software

- [JOSS submission requirements](https://joss.readthedocs.io/en/latest/submitting.html): open source, public repository, research application, major contribution, and a paper focused on software rather than new research results.
- [JOSS review criteria](https://joss.readthedocs.io/en/latest/review_criteria.html): license, significance, sustained development, documentation, examples, API, tests, community guidance, and AI disclosure. OICO lacks the external-use evidence JOSS considers a strong significance signal; no submission is made.
- [PyPA tool recommendations](https://packaging.python.org/en/latest/guides/tool-recommendations/): use build tooling and prefer Trusted Publishing instead of long-lived upload tokens.
- [GitHub releases](https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases): releases are tag-based and package deployable iterations.
- [Zenodo GitHub integration](https://help.zenodo.org/docs/github/): archive a specific GitHub release to obtain a real DOI; no DOI is claimed without an authenticated deposit.
- [Citation File Format](https://citation-file-format.github.io/): maintain structured citation metadata; `CITATION.cff` is present but has no DOI.
- [Software Heritage saving guidance](https://docs.softwareheritage.org/faq/faq-save.html): public source may be preserved independently; no Software Heritage identifier is claimed.

## Consequences for OICO

The project can satisfy internal software quality gates, but JOSS significance, DOI issuance, PyPI publication, and external adoption remain separate gates. A new release is justified only after Study 1 artifacts, checksums, tests, and documentation pass together.
