# Repository setup and research status

## September 17, 2026 setup

- Five main manuscripts, two supplements, and the EIT structural companion have stable working names and compiled PDF counterparts.
- The root README links directly to all eight sources and PDFs.
- `make pdf` builds the documents and records source/PDF hashes and page counts. `make check` verifies snapshots and README links; `make test` tests the checker.
- A read-only GitHub Actions workflow builds and checks the manuscripts on pull requests and main-branch pushes. It does not automatically commit generated files.
- Paper V's bibliography now uses the current titles of Papers I–III, and its PDF title metadata matches its full printed title.
- A malformed title line break in the linear KZ supplement has been corrected.
- At the author's explicit request, all eight documents now list Christopher D. Long and Antoine-Auguste Le Blanc. Le Blanc's identifier is copied exactly from Paper IV: `b604812530b3535b23d6dbb0f5abe32d1ed1a9de35fb4f7d04d62cff08ea19c8`. PDF author metadata, companion-paper citations, and singular-author disclosure wording are updated consistently. Mathematical statements, proofs, and original manuscript dates are preserved.
- Historical provenance and audit records are unchanged. Their original-source hashes describe the import, not subsequent editorial changes; the PDF manifest describes the current sources.
- Repository visibility and licensing are unchanged. No branch-protection or account settings are modified by this setup.

## September 29, 2026 Paper V revision

Paper V now uses actual polynomial Stokes boundary systems and includes the explicit elliptic fixed-triangle comparison. Its earlier general endpoint-complete numerical claim has been replaced, not silently retained: numerical maps are defined on specialized fibers and general multiblock formal realization is a separate hypothesis. The current title and manuscript date are intentionally updated; the author list is unchanged. See the [focused audit](provenance/paper-v-focused-audit-2026-09-29.md) for mathematical changes and limitations. The earlier setup and historical audit records remain historical descriptions.

## Remaining mathematical work (not a repository-setup blocker)

1. Reconcile later conversation-only corrections against these exact working sources.
2. Audit the mathematical dependency interfaces from I to II to III, including the moment-connection and differential-Galois arguments.
3. Independently review the relative Nori–Ayoub hypotheses and Paper V's new analytic/differential-Galois proof; establish actual comparison hypotheses for additional chains and multiblock collections before extending its theorem.
4. Review authorship, manuscript dates, external bibliography currency, and release metadata before public or archival publication.

Successful compilation, source hashes, and historical audit reports do not settle these mathematical or publication questions. No new theorem-level verification is claimed by the setup pass.
