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

## September 29, 2026 repair-session closeout

The recorded September 28–29 repair recommendations for Papers I, II, III,
and V have been reconciled with the working sources. The concurrent Paper IV
integration in PR #7 is also retained and reflected in this status. This completes the
specified repair session, not an independent certification of every paper.
The [closeout record](provenance/repair-session-closeout-2026-09-29.md)
identifies the exact revision baseline, the dependency review, and the
closing-snapshot convention.

### Completed repairs and checks

| Work | Integrated revision | Current disposition |
| --- | --- | --- |
| Paper I | PR #4, `093e260aa41a` | Compressed-residue flag, finite descent, Fourier convention, and scope clarifications integrated. |
| Paper II | PR #5, `5c11c2e1cba0` | Exact-compositum cover correction, compact lifted edges, inherited hypotheses, and descent clarifications integrated. |
| Paper III and supplement | PR #6, `0bb151018dc7` | Explicit spectral gauge, base-change and correction arguments, closed value systems, and quartic proof order integrated. |
| Paper IV and repair companion | PR #7, `31ea3d09d944` | Canonical realization, fixed-part, and functional-period repairs integrated in the concurrent workstream; its separate audit records the scope and qualifications. |
| Paper V | PR #8, `1d91e575bbf4` | Actual polynomial boundary systems and the explicit elliptic comparison replace the unsupported general endpoint assertion. |
| Cross-document closeout | Revision containing the linked closeout record | All nine active sources and current scope notes checked for reliance on the withdrawn Paper V theorem; none found. Paper V now explicitly records its internal-series dependencies. |

The earlier generic tasks to reconcile this session's conversation-only
corrections and review the I–II–III interfaces are completed to the extent
of the recorded audits and merged repairs. They are not claims of
independent specialist review. Paper IV's relative Nori–Ayoub proof is not
an input to Paper V's actual elliptic independence theorem. Its concurrent
[assembled-proof and integration audit](provenance/paper-iv-assembled-integration-audit-2026-09-29.md)
and [latest repair-ledger entry](repairs/paper-iv-repair-ledger.md) record
that workstream's completed repairs; this closeout checks its dependencies
and preserves its sources and PDFs, rather than repeating that proof audit.

The closeout was reconciled onto `31ea3d09d944` after PR #7 added the ninth
manuscript. The README links and both Paper IV snapshots are retained.
The post-merge workflow on the initial Paper V rewrite baseline passed: run
`36527841497`, job `109274684840`. Validation of the closing revision,
including its final commit and post-merge run, is recorded in that
revision's pull request. No release tag or archival publication is implied.

### Deliberately withdrawn or conditional

The old general endpoint-complete numerical theorem is not a remaining
repair task disguised as a proved result. Its unsupported geometric
application was withdrawn. The current manuscript proves the fixed
elliptic triangle result over its associated fixed-face fields and uses
the specialized numerical fiber. The abstract multicolumn comparison
requires its stated generic-ideal, realization, and local-flatness
hypotheses. These are not automatic consequences of observability.

### Separate research and review

Uniform families, additional chains, higher-rank or multiblock actual
comparison, isotypic compatibility, and determinant-line realization are
future mathematical work. Independent specialist review (including the
relative Nori–Ayoub arguments), full formalization, and publication
metadata/bibliography review are separate verification and dissemination
stages. They are not prerequisites for closing this scoped repair.

The former local TeX Live reference-label discrepancy in canonical Paper IV
was resolved by PR #7's alias counters. The corresponding known discrepancy
in the unchanged EIT structural companion remains a separate toolchain
issue. This closeout does not alter that companion to mask the difference.
Repository Ubuntu 24.04 checks remain the reproducible full-snapshot
validation environment.

Historical provenance remains unchanged. Build success, hashes, and finite
regression tests do not establish a new mathematical proof certificate.
