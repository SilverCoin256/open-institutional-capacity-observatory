# Poster Content Draft

## Title

Open Institutional Capacity Observatory: An Auditable Research Package for Public Administrative Workload Traces

## Research question

Can public workload snapshots be transformed into reproducible descriptive evidence of backlog pressure without treating a proxy as institutional capacity?

## Why it matters

Researchers often need to combine public data, provenance, transformations, code, figures, and limitations before they can compare an institution. OICO packages those steps together and makes misuse boundaries part of the artifact.

## Data and design

- Frozen annual EOIR workload snapshot, FY2016-FY2026.
- Primary inference restricted to FY2016-FY2024.
- Pending, received, and completed counts.
- QAI = change in pending / current completions.
- Checksums, schemas, source register, transformation log, tests, and exact output manifest.

## Main result

- Pending: 826,488 in FY2016 to 3,925,351 in FY2024.
- Increase: 4.749435 times.
- Positive QAI: 8 of 8 comparable transitions.
- Peak QAI: 1.579835 in FY2024.
- Alternative normalizations preserve the direction.

## Interpretation

The frozen snapshot shows reported pending workload expanding relative to recorded completions. This is a descriptive workload result. It does not establish institutional failure, staffing inadequacy, legal noncompliance, causality, or AI impact.

## Contribution

The strongest contribution is an open research-software contract: frozen inputs, provenance, transparent computations, reproducible figures, benchmark pilots, executable notebooks, and explicit claims boundaries in one package.

## Limitations

One aggregate institution; inherited source retrieval; no matched case cohorts; no causal design; no independent reproduction; small benchmark samples; later rows excluded from primary inference; external adoption not yet verified.

## Reproduction and validation

Repository: `https://github.com/SilverCoin256/open-institutional-capacity-observatory`

Reproduction: `https://silvercoin256.github.io/open-institutional-capacity-observatory/reproduce/`

Validation invitation: run the frozen release, compare the output hashes, and report agreement or disagreement through the public issue route. A reviewer is encouraged to attack the source comparability and construct validity.

## Status line

Technically release-ready. Scientifically bounded. External validation pending. Not an official ISEF submission or result.
