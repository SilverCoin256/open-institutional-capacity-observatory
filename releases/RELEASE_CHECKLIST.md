# OICO v1.0.0-rc1 Release Checklist

Review date: 2026-07-01

## Verified Locally

- [x] Version is `1.0.0-rc1` across package and citation metadata.
- [x] Annotated local tag `v1.0.0-rc1` is prepared.
- [x] Data build, validation, benchmark baselines, and six figures reproduce.
- [x] All five notebooks execute.
- [x] Twenty-one tests pass, including metric edge cases and non-editable-install root discovery.
- [x] Documentation and website links pass the repository checker.
- [x] Credential scan reports no high-risk patterns.
- [x] Dataset manifest and top-level artifact manifest verify all listed checksums.
- [x] The release archive is deterministic and has a SHA-256 sidecar.
- [x] A non-editable wheel built from the archive passes the complete release gate in an isolated environment.
- [x] Source-by-source redistribution evidence and caveats are dated and recorded.

## Publication Holds

- [ ] Authenticate GitHub through a fresh secure session; do not reuse the token pasted in chat.
- [ ] Create the intended public repository and add its verified URL to `CITATION.cff` and `codemeta.json`.
- [ ] Push `main` and the annotated `v1.0.0-rc1` tag.
- [ ] Create the GitHub prerelease using `releases/github/RELEASE_NOTES.md` and attach the archive, checksum sidecar, and artifact manifest.
- [ ] Ask an external researcher to run the archive gate and record the independent result.
- [ ] Obtain repository-curator confirmation of `datasets/metadata/license_review.md` before DOI deposit.
- [ ] Mint a DOI only after the archival record exists; then add the real DOI to citation metadata.

## Adoption Evidence

- [ ] Named laboratory use.
- [ ] Professor recommendation.
- [ ] University course link.
- [ ] Published-paper citation.
- [ ] Conference poster or demo built by an external user.

These boxes must only be checked with public or privately auditable evidence. Repository
existence, stars, self-downloads, and self-authored demos do not count as external adoption.
