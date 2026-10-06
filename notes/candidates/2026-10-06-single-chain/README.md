# Frozen single-chain candidate — 6 October 2026

This directory preserves the latest uploaded candidate for independent audit. It does not replace canonical Paper V and does not change its proof-status ledger.

The audit target is the last of three same-named uploaded TeX revisions, containing the direct formal diagonalization, diagonal local Picard–Vessiot subgroup/Kummer component argument, and intrinsic exponent definition.

## Identity

- Canonical base commit: `d5ae8f9081c7bc34d1622316bd8463482f244395`.
- Original attachment: 750 lines, 42,187 bytes.
- Original attachment SHA-256: `3e0f4f801cee6aec7dce897f44efb76ce08a8a10bc5eebcc6a9235a08314b150`.
- Original Git blob: `2ada1c0e48c01a925ad5f1795feff144753ba700`.
- Repository serialization Git blob: `a7e998233ab4f096cb9bd5f40d641e07ca0dfddf`.

The repository serialization has exactly one additional indentation space before `\chi(t)` on source line 635. This was established by an exact hash comparison; every other byte is identical. The mathematical text is unchanged. The original byte-identical attachment is retained in the accompanying local audit archive. The frozen source is a historical record: its inherited review/status language is not a substitute for the independent audit below.

## Files and scope

- `frozen/generic-single-chain-theorem.tex`: frozen mathematical candidate; do not revise in place.
- `frozen/check_generic_example_audited.py`: strengthened exact example certificate; it does not prove the general analytic theorem.
- `audit.md`: independent audit findings and verified source pinpoints.
- `proof-clarifications.tex`: separate proof supplement, including an elementary stable-lattice replacement for the remaining general formal-normal-form input.

No copyrighted reference PDFs or the raw AGV book excerpt are committed here.

## Standalone checks

Run the exact example certificate with Python and SymPy. Compile the frozen TeX with three `pdflatex -interaction=nonstopmode -halt-on-error` passes in a separate build directory. The independent audit rebuilt an 11-page frozen PDF and inspected its pages. A separate exact calculation also certifies that all six formal powers in the rank-six example are -1, using trace identities and a Vandermonde argument.

These are standalone candidate checks, not a claim that the full canonical repository build was rerun locally. Canonical source files, their managed PDFs, and `output/pdf/manifest.json` are unchanged. A corrected mathematical successor must be kept separate from this frozen record and receive an integration check before promotion into Paper V.
