# Paper IV: algebraic lissity repair and audit-scope correction

Date: 2026-10-05. Baseline: `d83904db95a9c68834c0949d5e52fe97c28a1613`.
Canonical source: `papers/04-relative-exponential-nori-ayoub/relative-exponential-nori-ayoub.tex`.
Pull request: #12, targeting `main`.

## Scope and disposition

The finite-graph/nonzero-scale lissity argument in `lem:graphs` is repaired.
The fixed-scale identification in `lem:fiber-nearby` and the regular-singular
comparison in `prop:regular-cycle-bridge` are made explicit. This is a scoped
AI-assisted mathematical review of those steps, prompted by Claude's supplied
objection and checked against the actual baseline source. It is not an
independent referee report, formal verification, or a certification of all of
Paper IV.

The September 28 ledger's **interface 3 has two parts**. Only **3(a),
finite-graph/nonzero-scale lissity**, is closed here. **3(b), the
Jacobsen–Terenzi/Lam–Litt ordinary geometric-origin application, remains OPEN
for a separate audit before deposit.** This status is an outstanding
hypothesis/application check, not a counterexample or an assertion that the
cited results are false. The realization interface and the remaining
arithmetic/rank-one chain are not newly audited in this revision.

## What was wrong with the previous application

At the baseline, `lem:graphs` invoked Sabbah's Appendix B in the special
Cotti–Dubrovin–Guzzetti eigenvalue-parameter setting and Douai–Sabbah
Propositions 1.18/1.20. The proof did not verify the microlocal-lattice local
freeness hypothesis required by that route for its own parameter-dependent
input. The right general analytic result is Douai–Sabbah Theorem 1.11 and
Corollary 1.12, whose numbering is unchanged in the published version.

The September 28 ledger expressly identified the finite-graph application as
an external interface to check. Neither September 29 report documents the
missing hypothesis verification; the assembled report's source table omits
both of the references used by the old lissity proof. Accordingly, broad
closure wording in those reports must not be read as verification of this
application. The original reports are preserved byte-for-byte. This dated
addendum, the live ledger, and the repository status correct the current
coverage without rewriting history.

## Replacement proof and internal checks

1. **Finite graphs and infinity.** Shrink the base so the dominating
   singular multisections are finite etale, then split them on a common
   cover. Their regular graph functions define closed graphs in
   `S x P1`, disjoint from infinity. The meromorphic extension of the input
   is therefore a meromorphic connection near infinity. Its regularity
   follows from preservation of *algebraic* regular holonomicity by the
   open direct image, not merely from analytic regularity at finite `t`.
   No additional regular-at-infinity hypothesis is imposed.
2. **Algebraic lattice and sign.** Use a coherent algebraic logarithmic
   lattice stable under `x d/dx` and the parameter derivations, where
   `x=1/t`. Local freeness of the lattice is not required by the argument.
   With the manuscript's unchanged kernel `d-d(lambda t)`, the formal
   generator satisfies `d_lambda e=-e/x` and `d_x e=lambda e/x^2`.
   Local generators of the lattice are pulled back independently of
   `lambda`, so repeated `d_lambda` generates every pole order in `x`.
3. **Good filtration.** Define `F_p=D_{<=p}(L e)`. Coherent generation
   proves exhaustiveness and goodness. The operators `x d_lambda`,
   `x d_x+lambda d_lambda`, and `d_s` preserve `F_0`. The commutator
   identity shows that each preserves every `F_p`; hence its degree-one
   symbol annihilates the associated graded module. At infinity the
   resulting equations leave only the normal `dx` covector when
   `lambda` is invertible.
4. **Proper estimate and degree.** Compactify in `t` before invoking
   the proper characteristic estimate. Neither a finite-graph conormal
   nor the infinity conormal has a nonzero covector annihilating the
   `t`-fiber tangent. Every direct-image cohomology module consequently
   has zero-section characteristic variety and is a connection.
   Concentration in degree zero is established *separately* by the
   relative Weyl-algebra Fourier isomorphism and exact localization.
   Lissity descends along the finite etale cover. This proof is algebraic
   over the geometric ground field and does not rely on analytic
   coherence implying algebraic coherence.
5. **Actual fixed fiber.** The scale slice is noncharacteristic for the
   source and transform. Differential-module base change for that closed
   slice, followed by noncharacteristic restriction and the already
   established forget-supports isomorphism, identifies the fiber with
   `rho_lambda(Q_S A)`. Normalized restriction is `i_lambda^*[-1]` in
   the manuscript's perverse convention and plain bundle restriction
   for a connection. The restricted shifted kernel is exactly
   `L_lambda=K_lambda[-1]`; no extra shift or scale reversal is inserted.
6. **Regular-singular bridge.** The bridge is now proved on the
   pushed-forward transform. Douai–Sabbah Theorem 1.11(1) gives analytic
   regularity at finite Fourier scale. The theorem's disc-times-base
   setting is local: after restricting to a sufficiently small relatively
   compact analytic neighborhood in the base, the finite graphs fit
   in one disc. Regularity of the input at infinity was already proved.
   Together with punctured lissity, this makes the localized transform
   regular singular along `lambda=0`. The classical logarithmic model
   identifies moderate and topological nearby cycles with the stated
   perverse shift. The residue description also explains compatibility
   with the base connection. Mixed regular input is covered directly;
   purity is not used to establish this comparison.

The exponential countercheck `E^(1/lambda)` is retained: lissity on the
punctured family alone does not supply the bridge. Sabbah's kernel notation
and the distinction between regular specialization in `lambda` and possible
irregularity in `t'=0` are retained for the subsequent ordinary-cycle
comparison. The two-triangle and geometric-origin proofs are not replaced.

## Source-to-claim checks

The published source locations below were checked as text and, for the
principal theorem statements/formulas, in rendered pages. Page numbers are
printed source pages, not PDF indices.

| Source location | Claim used and hypothesis check |
| --- | --- |
| Hotta–Takeuchi–Tanisaki, Theorem 6.1.5(ii), p. 162 | Algebraic open direct image preserves regular holonomicity. This concerns algebraic regularity, including boundary behavior. |
| Hotta–Takeuchi–Tanisaki, Theorem 5.3.7, p. 155 | Algebraic regular connections admit coherent logarithmically stable lattices. Only a coherent generating lattice is used. |
| Hotta–Takeuchi–Tanisaki, Theorem 2.5.1 and Remark 2.5.2, pp. 69–70 | Proper direct-image coherence and the characteristic estimate. The projection used in the repair is projective. |
| Hotta–Takeuchi–Tanisaki, Proposition 2.2.5, p. 61 | Zero-section characteristic variety characterizes coherent connections. Fourier exactness is an additional argument, not a consequence of this criterion. |
| Hotta–Takeuchi–Tanisaki, Theorem 1.7.3, p. 54, and Theorem 2.4.6, p. 67 | Base change and one-degree noncharacteristic restriction. Here the base-change map is a closed scale slice and all varieties in the square are smooth. |
| Douai–Sabbah, Theorem 1.11(1), p. 1063 | Regularity of the analytified partial transform at finite scale for regular input including infinity. The local disc condition is explained in the bridge. |
| Douai–Sabbah, Theorem 1.11(2) and Corollary 1.12, p. 1063 | Correct analytic alternative to the direct lissity proof. The noncharacteristic condition is checked from `a(dt-du_i)`. This is not the primary algebraic proof. |
| Deligne, Chapter II, Proposition 5.4 and Remark 5.5(ii), pp. 94–96; Section 6 | Logarithmic extension/model and classical comparison. The manuscript spells out the local residue computation for nearby cycles; it does not attribute an irregular nearby-cycle theorem to Deligne. |
| Sabbah, *Monodromy at infinity and Fourier transform II*, Proposition 4.1(ii), Proposition 5.8 and Corollary 5.20 | Existing finite-scale kernel specializability and projective cycle-comparison context retained. The new bridge does not assume a general de Rham comparison for an arbitrary irregular kernel. |

Primary texts: [HTT](https://ananddeopurkar.org/seminars/mhm/hottaetal.pdf),
[Douai–Sabbah, published article](https://www.numdam.org/item/10.5802/aif.1974.pdf),
[Deligne](https://publications.ias.edu/sites/default/files/Number9.pdf), and
[Sabbah](https://perso.pages.math.cnrs.fr/users/claude.sabbah/articles/sabbah_Fourier-twistor.pdf).

The unused Sabbah Cotti–Dubrovin–Guzzetti bibliography entry is removed from
the canonical source. Deligne's regular-singular monograph is added, and
the Douai–Sabbah entry now points to Theorem 1.11/Corollary 1.12. The
historical companion's bibliography is not rewritten.

## Remaining audit: interface 3(b)

Check the exact definition and coefficient-field conventions for ordinary
geometric origin in Jacobsen–Terenzi Corollary 5.15 and Proposition 5.17,
including closure under the precise nearby-cycle, proper-image,
perverse-cohomology, and subquotient operations used in
`thm:nearby-geometric`. Then check the resulting rank-one constituent
against the geometric-origin hypothesis of Lam–Litt's published Lemma 3.5.
The pure-to-mixed passage and the treatment of geometric rather than
arbitrary Hodge constituents must be verified together. This audit must
not be replaced by assuming that any Hodge direct summand is motivic.

The present revision closes neither this application check nor the
realization interface. No stronger global arithmetic assertion is imported
from the repair companion or an earlier memorandum.

## Build and preservation record

The final local `make test` passed all 11 tests and `make pdf` compiled
all nine documents without unresolved citations/references, duplicate
labels, or overfull boxes. The revised canonical PDF is 36 pages.
After restoring the eight unaffected committed snapshots, local
`make check` verified the first eight documents and then reported the
already documented structural-companion PDF-text discrepancy in this
local TeX environment. That unrelated source and PDF were not changed.

The authoritative Ubuntu 24.04 rebuild, full `make check`, preservation
checks, and source/PDF hashes are recorded in the
[build-verification record](paper-iv-lissity-build-verification-2026-10-05.json).
The normal read-only LaTeX PR workflow remains the merge gate. A temporary
feature-branch build helper is removed before merging; no workflow or
repository-setting change is part of the final repair. Build success is
not mathematical certification. Final artifact inspection and the normal
PR CI result are recorded in PR #12.

All preexisting canonical LaTeX labels, authors, identifiers, contacts,
titles, and manuscript dates are preserved. The other eight manuscript
sources/PDFs and their manifest records, including the historical Paper IV
repair companion, are kept unchanged. New equation labels identify the
infinity characteristic bound and normalized fixed-fiber comparison.
