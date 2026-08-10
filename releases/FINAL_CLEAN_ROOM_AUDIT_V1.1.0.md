# Final Clean-Room Audit: v1.1.0

Audit date: 2026-08-10

This record covers a fresh extraction of `releases/github/oico-1.1.0.tar.gz` into a directory with spaces in its path, followed by installation into a separate virtual environment. The test was performed outside the working checkout.

## Procedure

1. Extract the versioned source archive into `/tmp/OICO clean room 1.1`.
2. Install the extracted project with isolated build dependencies.
3. Invoke the installed `oico` entry point from the extracted project directory.
4. Run `oico reproduce --full`.

## Observed result

- Installation: pass; built and installed `oico-1.1.0`.
- Data validation: pass, with the documented warning for a source row whose completions are missing.
- Figures: 6 generated.
- Benchmark outputs: 5 generated.
- Study 1: generated across EOIR, USCIS, CFPB, and SEC.
- Release audit: pass; no missing required paths or checksum mismatches.
- Root discovery: pass for both installed `oico` and installed `research` modules when launched outside the source checkout.

## Boundary

This is a clean-room reproducibility test performed by the project author’s environment. It is not an independent reproduction and does not count as external validation. CI remains the authoritative cross-version check for Python 3.10-3.12; this local test additionally exercised Python 3.14.
