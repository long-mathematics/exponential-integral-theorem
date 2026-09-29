# Repair-session closeout — 2026-09-29

## Scope and closing snapshot

This closes the recorded September 28–29 repair-and-revise session at the
revised scope of Paper V, not at the scope of its withdrawn predecessor.
It is a dependency, presentation, and repository consistency pass; it does
not replace the mathematical audits or add a theorem.

Initial baseline: `1d91e575bbf44904e37b89d9c342c1b409f7e8bb` (merged PR #8).
The downloaded revision archive was verified against the exact Git tree
`edc7ba453df73999c842a02c19ed67e850b7cfd6` before editing. The baseline's
post-merge workflow `36527841497`, job `109274684840`, completed successfully.

Before merging the closeout, concurrent PR #7 integrated repaired Paper IV
and added its companion as the ninth active manuscript. The closeout was
therefore reconciled onto `31ea3d09d9447a9dbdaa3bed65dd30e805b17fea`,
with exact verified tree `22535633182cbf4c709d8e7f9cf0e251cdb7b53a`.
The revised Paper IV, its companion, README additions, manifest entries,
and audit/ledger files are preserved. An initial successful eight-document
closeout build (`36530048558`) is superseded as the merge gate by the
reconciled nine-document build and its normal pull-request checks.

The closing snapshot is the merge commit containing this note, the
editorially updated Paper V source and PDF, their manifest record, and the
README/status reconciliation. Its exact SHA, pull-request CI result, and
post-merge CI result are recorded in the associated pull-request discussion;
using the containing commit avoids embedding a circular self-hash here.
No tag, release, publication, visibility change, or protection change is
part of this closeout.

## Integrated repairs

| Manuscript | Merged repair | Scope of the integrated work |
| --- | --- | --- |
| I | PR #4, `093e260aa41a` | Residue flag, finite Hermite descent, Fourier conventions, and fixed-form scope. |
| II | PR #5, `5c11c2e1cba0` | Exact cover compositum, compact lifted-edge construction, explicit inherited hypotheses, and finite descent. |
| III and supplement | PR #6, `0bb151018dc7` | Spectral gauge, exponential base change, meromorphic correction, differential-system closure, and quartic Laurent proof order. |
| IV and repair companion | PR #7, `31ea3d09d944` | Concurrent canonical realization, fixed-part, and functional-period repairs; see its separately recorded assembled-proof and integration audit. |
| V | PR #8, `1d91e575bbf4` | Actual polynomial Stokes systems, actual one-column criterion, fixed-triangle elliptic functional/numerical comparison, and corrected local numerical fiber. |

The detailed mathematical findings remain in the separate dated revision
notes. The focused Paper V audit supersedes the favorable endpoint verdict
in `paper-v-strengthening-audit.md`; both historical records are preserved.
The old global endpoint assertion is not silently restored by this closeout.

## Cross-document dependency check

All nine active LaTeX sources were checked, together with the README,
repository status, and contribution instructions. The expanded check includes
the repaired canonical Paper IV, its retained companion, and the latest
dated entry in the Paper IV repair ledger. Earlier dated ledger entries
and audit memoranda remain historical records. Companion bibliography
entries, mentions of polynomial flags and endpoint completeness, numerical
specialization claims, and the relevant introduction/scope passages were
reviewed. Historical files under `notes/provenance/` were read as historical
evidence, not treated as current theorem statements.

| Active document | Dependency/scope finding |
| --- | --- |
| Paper I | No input from Paper V or its withdrawn endpoint theorem. |
| Paper II | Uses the Paper I moment package; no input from Paper V. Its actual-curve and reduced-amplitude scope remains explicit. |
| Linear KZ supplement | References the Paper II comparison; no Paper V endpoint dependency. |
| Paper III | Uses Papers I and II for the tensor-generated affine-line algebra; no Paper V dependency. |
| Polynomial KZ supplement | Its compact-line applications refer to Papers I–III; no Paper V endpoint input. |
| Paper IV (relative Nori–Ayoub), as integrated by PR #7 | No dependence on Paper V. Its abstract and introduction retain the separation between generic functional results and numerical specialization. This pass is not a new audit of its proof. |
| Paper IV repair companion | Replacement arguments for the pre-repair Paper IV, retained with the canonical integration. No input from Paper V; the generic functional scope does not assert numerical specialization. |
| Paper V | The actual construction, criterion, and elliptic independence proof do not use companion formal completeness. Paper II interprets the reduced single-phase face relation; Paper III interprets already separated polynomial boundary relations. Paper IV is not an input to the actual elliptic theorem. |
| EIT structural companion | Companion arguments for Paper I; no Paper V endpoint dependence. |

No active claim or dependency was found that requires the withdrawn general
Paper V endpoint theorem. The known historical claim remains only as a
superseded audit statement or in explicit explanations of the correction.
There was therefore no reason to revise an unrelated manuscript or PDF.

## Final editorial changes

Paper V's introduction now states the internal-series dependency boundary
explicitly. The Paper III bibliography entry is normalized to its current
printed title and the repository's companion-preprint style, retaining its
August 2026 manuscript date and September 28 revision reference. Its
explanatory dependency prose is placed in the introduction rather than in
the bibliography.

No theorem, proposition, lemma, corollary, definition, example, remark, or
proof environment is changed. Existing labels, author order, author
identifier, contact email, title, PDF metadata, and the September 2026 date
are preserved. The other eight manuscript sources, PDFs, and manifest
records remain byte-for-byte unchanged. Earlier provenance records remain
byte-for-byte unchanged.

The README links this note and retains the ninth-document and Paper IV
audit links introduced concurrently. The live status page now separates completed
repairs, withdrawn/conditional claims, and future research/review instead
of leaving already completed session tasks on a generic pending list.

## Established scope and excluded extrapolations

The general polynomial-representative construction gives actual
boundary-forced systems; injectivity still requires the comparison
criterion's hypotheses. The concrete elliptic theorem concerns the fixed
phase and fixed triangle, with arbitrary polynomial amplitudes, over the
fields generated by its three fixed faces and their endpoints. It does not
assert independence over the field of all compact polynomial-line periods.
Its numerical algebra is the specialized fiber, not the functional algebra
containing the unspecialized parameter. Its actual independence proof is
separate from the formal interpretation of residual boundary relations.

General isotypic or multiblock geometric completeness, additional-chain
comparison, and determinant-line realization remain separate obligations.
Restoring the withdrawn general theorem is new research, not an unfinished
step required to close the explicitly delimited repair. Independent review,
Lean formalization, and publication are separate stages.

## Validation record and limitations

Local validation in this closeout passed all 11 unit-test methods and the
extended exact suite (81 monomial certificates, both connection and both
Gelfand–Leray certificates, and 42 independent Taylor identities). All
nine sources compiled after reconciliation. Paper V remains 27 pages; every page was rendered
and reviewed, with enlarged inspection of the changed introduction and
bibliography. All 84 existing numbered/definition/remark/proof environments
and all 91 labels were compared byte-for-byte and preserved.

The delivery is required to pass `make test`, `make pdf`, and `make check`
in the repository's Ubuntu 24.04 environment, along with the extended exact
Paper V suite. All changed PDF pages must be rendered and inspected before
merge. Source-environment and label preservation, unchanged-document hashes,
and the six-file delivery boundary are checked against the baseline. Actual
run identifiers and outcomes are recorded in the associated pull request,
including the post-merge check on the closing commit.

The former local TeX Live discrepancy in canonical Paper IV's shared-counter
reference labels was corrected by PR #7. The corresponding discrepancy
in the unchanged structural companion remains a toolchain limitation, not
hidden by an unrelated manuscript change. No assertion of byte-identical
PDF production across different TeX distributions is required by the
repository checks.

This closeout is not independent specialist review, a renewed audit of all
proofs, or a kernel-checked mathematical certification. Successful
compilation and finite regression checks are not substitutes for those.
