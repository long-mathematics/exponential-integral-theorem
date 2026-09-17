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

## Remaining mathematical work (not a repository-setup blocker)

1. Reconcile later conversation-only corrections against these exact working sources.
2. Audit the mathematical dependency interfaces from I to II to III, including the moment-connection and differential-Galois arguments.
3. Independently audit the relative Nori–Ayoub hypotheses and the endpoint-complete hypotheses and implementation in Paper V.
4. Review authorship, manuscript dates, external bibliography currency, and release metadata before public or archival publication.

Successful compilation, source hashes, and historical audit reports do not settle these mathematical or publication questions. No new theorem-level verification is claimed by the setup pass.
