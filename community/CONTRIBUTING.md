# Contributing

OICO welcomes contributions that improve reproducibility, source provenance, validation, or teaching usefulness.

## Good First Contributions

- Add a source-license clarification.
- Improve a data dictionary entry.
- Add a validation check.
- Reproduce a figure and report the environment.
- Propose a new institution with a source-register draft.

## Contribution Standard

Every data contribution must include:

- source URL
- access date
- license or terms note
- raw snapshot checksum
- transformation explanation
- quality flags
- expected misuse

Every metric contribution must include:

- definition
- mathematical intuition
- assumptions
- limitations
- failure modes
- expected misuse

## Review Workflow

1. Open an issue with the proposed change.
2. Add or update tests and docs.
3. Run `python scripts/check_release.py`.
4. Request review from a maintainer.

## Adoption Claims

Do not add claims of lab use, course adoption, citations, or recommendations unless the evidence names the external lab, course, paper, professor, or conference artifact.
