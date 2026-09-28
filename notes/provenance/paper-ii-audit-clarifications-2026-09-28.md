# Paper II: audit corrections and clarifications, 2026-09-28

Baseline: commit `093e260aa41a1d71ea6f12b41a0a84ed9c6c1463`; Paper II source blob
`657193696c72967fdfaf7ab9dbd099ec1c24a8af`.

This revision follows the adversarial audit discussed on 2026-09-28.
The audit identified a local error in the auxiliary-cover construction:
an arbitrary larger Galois extension could introduce new ramification.
Choosing the exact compositum corrects that construction. No fatal gap
was found in the main argument; this is not independent peer review or a
formal proof certificate. Historical audit reports are unchanged.

## Changes

- Choose the compositum itself of the polynomial covers' Galois closures,
  rather than an arbitrary containing Galois extension. State the etale
  property over the specified open set, and require analytic neighborhoods
  to be open.
- Prove that lifted closed edges extend to compact piecewise C1 relative
  chains with algebraic boundary, using the local ramification model and
  power reparametrization. Explain that different edges need not lift to
  one global chain on the auxiliary curve.
- Repeat the inherited reduced-degree and algebraic-exponent hypotheses
  explicitly in Corollary 7.6. This corrects its stand-alone wording, not
  the intended scope of the transfer theorem.
- Replace the coefficientwise field-automorphism descent with a finite
  invertible Hermite-interpolation system over the algebraic numbers.
- Explain specialization into the constant relation subspace by its
  constant annihilator; cite Beukers Theorem 3.2 and Lemma 3.1 precisely,
  including applicability to dependent coordinates.
- Add the polynomial-amplitude counterexample to the existing reduction
  remark: its algebraic value is an endpoint term, not a counterexample
  to the reduced transfer theorem.

## Preserved scope

The main injectivity and transfer statements are unchanged, as are all
84 original cross-reference labels and the ordering of all
27 theorem-like, definition, and remark environments.
No numbered statement is added or removed. Authorship, title, contact
information, and the explicit August 2026 manuscript date are preserved.
The cover lemma and independence corollary have the explicit corrections
described above. Other manuscripts and their committed PDFs are unchanged.

The finite exact-arithmetic experiments from the audit are stress tests,
not a proof certificate for the general theorem.

## Build verification

`make test`, `make pdf`, and `make check` passed in the revision build.
The revised Paper II PDF has 19 pages. The other seven
PDF snapshots and their manifest entries were restored byte-for-byte
from the audited baseline before the final check.

Visual review and the normal pull-request check are recorded separately
in the pull request before merge. Compilation and regression checks do
not constitute a mathematical certification.
