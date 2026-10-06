# Repository history and status

This page is the single entry point for the repository's revision history, mathematical audit records, repair notes, and current review boundaries. The root [README](../README.md) describes the papers as they stand now; this page explains how that state was reached.

## Current snapshot

| Area | Current status |
| --- | --- |
| Paper I | Current theorem and proof retained. September proof audit/clarifications are integrated; October 5 prior-art and citation revisions are integrated. |
| Paper II | Current linear Kontsevich–Zagier theorem retained. September audit/repair is integrated; October 5 prior-art framing and references are integrated. |
| Paper III | Current polynomial Kontsevich–Zagier theorem and supplement retained. September audit/repair is integrated; October 5 prior-art framing and the normalized quadratic comparison are integrated. |
| Paper IV | The canonical manuscript uses the arithmetic mixed-sheaf realization replacement, including its enhancement, tensor and absolute-comparison proofs. The separate October 5 lissity and geometric-origin repairs remain integrated; the realization-to-arithmetic-to-PV chain has the scoped follow-up audit linked below. |
| Paper V | The class-(W) single-chain theorem is integrated under explicit (M), (Q), (F), and (S) or (S*) hypotheses, with functional independence, all-nonzero-algebraic-parameter independence, and polynomial twisted exactness. The elliptic triangle and rank-six triangle are verified applications. The frozen candidate, corrected successor, and pre-integration manuscript are preserved. The older unrestricted endpoint-complete claim remains withdrawn; genericity and general multiblock formal completeness are not claimed. |
| Build | make test, make pdf, and make check are the repository validation entry points. The committed PDF manifest records current source/PDF hashes and page counts. |

The current manuscripts are working research drafts. Successful compilation, finite computational checks, and scoped AI-assisted audits are not independent peer review or formal verification.

## Current review boundaries and follow-up

### Closed in the recorded scoped reviews

- Papers I–III: the September proof-audit revisions recorded below are integrated.
- Papers I–III: the October 5 prior-art/citation pass is integrated, including the Fresán–Jossen/Jossen overlap and the corrected quadratic normalization.
- Paper IV interface 3(a): finite-graph/nonzero-scale lissity, fixed-scale restriction, and the regular-singular nearby-cycle bridge.
- Paper IV interface 3(b): generic smooth-projective realization of the relevant simple constituents and the ensuing rank-one torsion step.
- Paper IV realization follow-up: arithmetic mixed-sheaf transfer, perverse-concentrated tensor comparison, actual absolute normalization, and the downstream arithmetic/Tannakian/PV chain in the dated scoped AI-assisted audit.
- Paper V: the October 6 source-checked class-(W) theorem extends the fixed-triangle actual comparison under explicit hypotheses; it does not reinstate the withdrawn endpoint-complete claim.
- Paper V: direct formal diagonalization, the diagonal local Picard–Vessiot/Kummer argument, stable-lattice face disjointness, and local/global transport are integrated. The October 6 follow-up also defines chain multiplicity and phase density explicitly, including non-injective parametrizations, and closes the associated expository gap. The October 5 geometric/formal/multicolumn discussions remain in the unchanged archived manuscript, not in the present main proof.

### Not claimed by those closures

- No record here is an independent specialist referee report.
- The interface-3 repairs alone did not audit the realization chain. The later realization follow-up replaces the augmentation proof; its new transfer argument and scoped audit are not independent specialist certification.
- The Papers I–III prior-art pass does not establish absolute priority against unpublished work.
- Paper V does not prove unrestricted two-variable or general multiblock formal completeness.

### Useful pre-deposit follow-up

- A concise note to Javier Fresán and Peter Jossen about the general polynomial marked-point theorems would be useful for checking possible unpublished overlap after the February 2025 talk. The current manuscripts already use bounded priority language, so this is a scholarly priority check rather than a logical dependency of the proofs.
- Independent specialist review remains especially valuable for the full Paper IV realization-to-arithmetic-to-Picard–Vessiot chain.

## Timeline

The table gives the high-level flow. Detailed records are linked in the next section.

| Date | Change | Result |
| --- | --- | --- |
| 2026-09-17 | Repository setup and import | Five main manuscripts, supplements, structural companion, build scripts, committed PDFs, and provenance records organized under stable paths. |
| 2026-09-28 | Papers I–III audits | Focused proof audits and clarification passes produced the current repaired versions of Papers I–III. |
| 2026-09-29 | Paper IV integration | The relative algebraic realization, fixed-part, rank-one lifting, Galois exactness, and functional-period repairs were integrated into canonical Paper IV. |
| 2026-09-29 | Paper V rewrite and repair closeout | The unsupported general endpoint-complete claim was removed; actual polynomial boundary systems and the explicit elliptic comparison became the canonical result. Cross-document dependencies were rechecked. |
| 2026-10-01 | Editorial compression | Redundant bookkeeping in Papers I–II was removed without changing mathematical statements. |
| 2026-10-05 | Paper IV lissity repair | A direct algebraic characteristic-variety argument replaced the earlier mismatched finite-graph citation route; interface 3(a) was closed in the scoped review. |
| 2026-10-05 | Paper IV geometric-origin repair | The smooth-projective bridge and rank-one torsion hypothesis were made explicit; interface 3(b) was closed in the scoped review. |
| 2026-10-05 | Papers I–III prior-art revision | Fresán–Jossen/Jossen prior art was incorporated and the quadratic normalization/count was checked and recorded. |
| 2026-10-05 | Paper IV arithmetic realization replacement | Replace the augmentation-based interface; repair the tensor step, retain actual absolute comparison, and recheck the arithmetic/Tannakian/PV dependency chain. |
| 2026-10-05 | README cleanup | The root README was converted to a current-results guide; historical repair narrative was moved out of the front page and remains here and in provenance records. |
| 2026-10-05 | Paper V audit follow-up | Clarify the actual relative-monodromy hypothesis and localized formal comparison; expand the affine-orbit proof and correct version-specific references without weakening the elliptic independence statements. |

| 2026-10-06 | Paper V single-chain integration | Freeze the candidate; audit the corrected successor; integrate the weighted-plane comparison and stable-lattice proof, retain both examples, archive the previous manuscript, and add exact regression certificates. |
| 2026-10-06 | Paper V density and front-matter closeout | Define polynomial-chain multiplicity and phase densities, clarify scalar-field transcendence bookkeeping, rename the current paper from polynomial flags to polynomial chains, and recheck the Sabbah and Milne pinpoints. |

## Detailed records by paper

### Papers I–III

| Record | Purpose |
| --- | --- |
| [Paper I audit](provenance/paper-i-audit.md) | Original focused proof audit of Paper I. |
| [Paper I audit clarifications](provenance/paper-i-audit-clarifications-2026-09-28.md) | Clarifications and incorporated repairs following that audit. |
| [Paper II audit](provenance/paper-ii-audit.md) | Focused audit of the linear Kontsevich–Zagier manuscript. |
| [Paper II audit clarifications](provenance/paper-ii-audit-clarifications-2026-09-28.md) | Corrections and clarifications integrated into Paper II. |
| [Paper III audit](provenance/paper-iii-audit.md) | Focused audit of the polynomial Kontsevich–Zagier manuscript. |
| [Paper III audit clarifications](provenance/paper-iii-audit-clarifications-2026-09-28.md) | Corrections and clarifications integrated into Paper III and its supplement. |
| [Papers I–III prior-art and citation revision](provenance/papers-i-iii-prior-art-2026-10-05.md) | Source-to-claim comparison with Fresán–Jossen, Jossen, Delaygue, and related E-function literature; includes the quadratic normalization consistency check. |

### Paper IV

Read the Paper IV records chronologically. Later dated records supersede earlier open/closed status statements without rewriting the historical files.

| Record | Purpose / present interpretation |
| --- | --- |
| [Standalone repair ledger](repairs/paper-iv-repair-ledger.md) | Dependency-ordered record of the original repair program. Early entries are historical and are superseded where later records say so. |
| [Interface-construction note](repairs/paper-iv-interface-construction-2026-09-29.md) | Construction of the algebraic realization/comparison interface used in the repaired proof. |
| [Second-pass audit](repairs/paper-iv-second-pass-audit-2026-09-29.md) | Audit of the standalone repaired proof before canonical integration. |
| [Assembled and integration audit](provenance/paper-iv-assembled-integration-audit-2026-09-29.md) | Canonical integration audit for the September Paper IV repair. |
| [Lissity repair and source check](provenance/paper-iv-lissity-repair-2026-10-05.md) | Replaces the earlier finite-graph microlocalization application with the algebraic characteristic-variety proof; closes interface 3(a) in the scoped review. |
| [Geometric-origin repair and source check](provenance/paper-iv-geometric-origin-repair-2026-10-05.md) | Supplies the generic smooth-projective constituent bridge and rank-one torsion input; supersedes the open interface 3(b) status in the lissity record. |
| [Arithmetic realization repair and audit](provenance/paper-iv-arithmetic-realization-repair-2026-10-05.md) | Replaces the earlier realization construction and supersedes its blanket clearance; records the tensor correction and the scoped whole-chain follow-up. |
| [Arithmetic realization build verification](provenance/paper-iv-arithmetic-realization-build-2026-10-05.json) | Official build and preservation hashes for this replacement. |
| [Absolute comparison and rational-fiber citation follow-up](provenance/paper-iv-comparison-citation-audit-2026-10-05.md) | Source-checked general-pair integration normalization, direct rational fiber references, and version-specific pinpoints; theorem statements and downstream proofs unchanged. |
| [Comparison-citation build verification](provenance/paper-iv-comparison-citation-build-2026-10-05.json) | Official snapshot and preservation checks for the focused follow-up. |
| [Geometric-origin build verification](provenance/paper-iv-geometric-origin-build-verification-2026-10-05.json) | Machine-readable build and preservation record for the final October 5 repair. |

The retained [Paper IV repair companion](../papers/04-relative-exponential-nori-ayoub/repairs/paper-iv-repair-note.tex) is historical proof-development material. Canonical claims should be read from the main Paper IV source, not inferred from superseded wording in the companion.

### Paper V

| Record | Purpose |
| --- | --- |
| [Density/front-matter closeout](provenance/paper-v-density-closeout-2026-10-06.md) | Defines the phase-density and multiplicity conventions, records scalar-field bookkeeping, metadata cleanup, and independent Sabbah/Milne pinpoint checks. |
| [Single-chain integration audit](provenance/paper-v-single-chain-integration-2026-10-06.md) | Successor and integrated proof audit, explicit scope, preservation, and validation record. |
| [Frozen candidate and source audit](candidates/2026-10-06-single-chain/README.md) | Immutable source snapshot, geometric pinpoints, exact certificate, and separate proof supplement. |
| [Pre-integration manuscript](archives/2026-10-06-paper-v-before-single-chain/polynomial-flag-exponential-periods.tex) | Verbatim archive of the previous canonical Paper V and its additional material. |
| [Strengthening audit](provenance/paper-v-strengthening-audit.md) | Historical record of the earlier strengthening program. |
| [Focused audit and revision record](provenance/paper-v-focused-audit-2026-09-29.md) | Records the replacement of the unsupported endpoint-complete theorem by actual boundary systems and the explicit elliptic theorem. |
| [Repair-session closeout](provenance/repair-session-closeout-2026-09-29.md) | Cross-document dependency review and final scope of the September repair session. |
| [October 5 audit follow-up](provenance/paper-v-audit-followup-2026-10-05.md) | Additional audit of the proposed clarifications, source-to-claim checks, and precise actual versus specialized formal scope. |
| [Follow-up build verification](provenance/paper-v-audit-followup-build-2026-10-05.json) | Official build, snapshot preservation, and reproducible rendering fingerprints. |

## Repository and import history

| Record | Purpose |
| --- | --- |
| [Draft import map](provenance/draft-import.md) | Maps recovered/original filenames to the stable repository paths. |
| [Import validation](provenance/import-validation.md) | Records validation of the initial imported sources and snapshots. |
| [Contribution and PDF-update workflow](../CONTRIBUTING.md) | Current maintenance procedure for source and PDF changes. |
| [PDF manifest](../output/pdf/manifest.json) | Current source/PDF hashes and page counts. |

## How to interpret historical status statements

The provenance directory is intentionally append-only in spirit: older reports are preserved as records of what was believed or checked at that time. Therefore:

1. Prefer **Current snapshot** and **Current review boundaries and follow-up** above for present status.
2. For a specific issue, follow the dated records in chronological order.
3. A later repair may supersede an earlier statement that an interface was open, without altering the earlier file.
4. Build success and source hashes establish reproducibility and preservation, not mathematical correctness.
5. Git history remains the authoritative record of exact line-by-line changes and pull-request merges.

## Build and validation model

- make test runs the repository's finite regression tests.
- make pdf builds the manuscript suite and refreshes generated snapshots and the manifest.
- make check rebuilds and checks committed PDF text, hashes, manifest consistency, and README links.
- The read-only GitHub Actions workflow runs these checks on pull requests and pushes to main.
- Historical machine-readable verification files remain in notes/provenance/ and notes/repairs/.

No release tag, archival deposit, or independent human certification is implied by this status page.
