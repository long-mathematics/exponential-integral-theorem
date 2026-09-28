# Paper I: audit clarifications, 2026-09-28

Baseline: commit `c3b1e3d703c6c9df54a740e8c102608b544c4ec6`;
Paper I source blob `ada7aac70a76259095a63dfd3405c80edb4c93fd`.

This revision follows the adversarial audit discussed on 2026-09-28.
The audit found no fatal gap; this is not independent peer review or a
formal proof certificate. Historical audit reports are left unchanged.

## Changes

- Make the local invariant flag in the compressed-residue calculation
  explicit, including the Chinese remainder argument, vanishing at other
  critical points over the same value, and the resulting full spectrum.
- State that the nonzero leading-coefficient block may lie over the
  critical value zero.
- Replace the compressed Galois-descent paragraph with an explicit finite
  derivative system and an elementary Hermite-interpolation invertibility
  proof.
- State the inverse Fourier convention relative to Sabbah, track the
  induced differential on coefficient polynomials, and display the
  commutator that makes the quotient connection well-defined.
- Cite Beukers, Theorem 3.2 and Lemma 3.1, and de Cataldo--Migliorini,
  Remark 4.2.4, precisely; explain the intermediate-extension step.
- Explain specialization into the constant subspace using its constant
  annihilator, and spell out the denominator exponent bound.
- Add the elementary polynomial-amplitude counterexample to delimit the
  scope of the fixed form dx.

All existing theorem, proposition, lemma, and corollary statements,
all existing cross-reference labels, the author list, the title,
and the explicit August 2026 manuscript date are preserved. The changes
expand proofs and delimit scope; they do not enlarge the theorem.

## Verification protocol

Run `make test`, `make pdf`, and `make check`. Preserve the committed PDFs
and manifest records of the seven unchanged documents. Inspect the
revised Paper I PDF visually before merging. Compilation and regression
checks do not constitute a new mathematical certification.
