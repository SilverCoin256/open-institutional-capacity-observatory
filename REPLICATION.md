# Independent Replication Protocol

Start with the public [reproduction landing page](https://silvercoin256.github.io/open-institutional-capacity-observatory/reproduce/). Use [BREAK_OICO.md](BREAK_OICO.md) when the result or its assumptions appear scientifically wrong.

OICO is seeking independent attempts to reproduce the v1.0 flagship analysis and identify methodological, documentation, packaging, or data-provenance failures.

## Protocol

1. Use a clean machine or temporary environment with Python 3.10, 3.11, or 3.12.
2. Clone the repository and check out tag `v1.1.0`, or download the release archive from [GitHub](https://github.com/SilverCoin256/open-institutional-capacity-observatory/releases/tag/v1.1.0).
3. Run `python -m pip install -e .`.
4. Run `oico reproduce`.
5. Compare the generated files with `replication/reference_manifest.json`.
6. Run `python -m unittest discover -s tests`.

## Expected artifacts

The flagship report should have status `pass`, contain 11 EOIR observations, 10 comparable QAI observations, 8 positive-QAI periods, a peak pending value of 3,925,351, and a peak QAI of 1.580. Exact file checksums are listed in the reference manifest for the tagged release.

## Reporting deviations

Open an issue using the **Independent Reproduction Report** template. Include an identifier if desired, affiliation if desired, operating system, Python version, install route, tag or commit, reproduction status, checksum comparison, deviations, and comments. Do not include credentials or private data.

An independent reproduction is not counted merely because internal CI passes. The project will only record external-validation evidence after a real person outside the author workflow reports a verifiable attempt.
