# Paper III: audit clarifications, 2026-09-28

Revision baseline: `5c11c2e1cba0b4400006e553056254711c9ba9da`.
The Paper III audit examined `093e260aa41a1d71ea6f12b41a0a84ed9c6c1463`;
its two source files were unchanged at the revision baseline. This revision
preserves the intervening Paper II changes from PR #5.

## Main paper

- Add an explicit simultaneous spectral gauge for all horizontal
  endomorphisms over the finite exponential field. The gauge uses only
  eigenvalue differences already in the exponent subgroup and equals the
  identity at zero.
- Use this gauge and a constant change of basis to split the horizontal
  idempotent. Remove the now-unused appeal and reference to Swan's
  Laurent-ring freeness theorem.
- Present semisimplicity after exponential base change through the normal
  subgroup in the joint Picard--Vessiot group.
- Display the transformed connection and the homogeneous correction after
  pulling it back to the original moment system. Explain its single-valued
  meromorphic behavior at zero before applying the residue exclusion.

## Independent supplement

- Explicitly adjoin all forcing exponentials in the quadratic and Ein
  value proofs, as well as the constant coordinate in the Ein system.
  Distinguish generation of the exponential field from closure of a vector
  under a rational first-order differential system. Spell out the rank and
  transcendence-degree bookkeeping.
- Exclude positive Laurent powers for a non-pure quartic before imposing
  the simple-pole-plus-constant ansatz. Explain why projection to the
  symmetric square retains the unique polar coefficient. The classification
  now refers back to this complete argument rather than supplying it later.

## Scope and preservation

No existing theorem, proposition, lemma, corollary, definition, or remark
statement is changed. One proved spectral-gauge lemma is added to the main
paper. Existing labels, author lists, titles, metadata, and August 2026
manuscript dates are preserved. No hypotheses are weakened and no claimed
class of periods is enlarged. The exact-compositum correction in Paper II
is already present at the baseline, so Paper II is not changed here.
Historical audit reports are left unchanged.

## Validation

The revision procedure checks the source-blob baselines, all existing
numbered-environment statements and labels, and unchanged front matter.
Run `make test`, `make pdf`, and `make check`; preserve the six unchanged
PDF snapshots and their manifest entries. Inspect both revised PDFs before
merging. Actual build, regression, and visual-review results are recorded
in the pull request. These checks are not independent peer review or a
kernel-checked mathematical proof.
