# Paper IV: geometric-origin bridge and scoped interface-3(b) repair

Date: 2026-10-05. Baseline: `3b587fdfde4992e19745302da1c8e6ec4f9326c0`
(the merged lissity repair, PR #12).

## Scope and verdict

This is an additional source-checked, AI-assisted audit and a targeted repair
of the implication from ordinary Nori geometric input to the smooth-proper
geometric-origin hypothesis in Lam–Litt's rank-one torsion lemma. It is not
independent human peer review or formal verification, and it is not a new
audit of all of Paper IV.

**The missing implication is supplied by `lem:projective-constituents`,
its application in `thm:nearby-geometric`, and
`lem:projective-rank-one`. Interface 3(b) is closed in this scoped review.**
The main rank-one statement is not weakened. The optional sufficient split
criterion now states the requisite constituent condition explicitly. The
proof and its source-hypothesis matches were reviewed again after insertion.
Build and artifact checks are recorded separately in the accompanying
build-verification JSON and the pull request.

Interface 3(a) remains the separate finite-graph/lissity repair in PR #12.
The earlier lissity note correctly left 3(b) open; this entry supersedes
that open status without rewriting the historical note. Neither closure
certifies the algebraic realization/augmentation construction, the
arithmetic exponential kernel, Picard–Vessiot descent, or the entire
period-torsor chain.

## Defect confirmed at the baseline

The old `thm:nearby-geometric` identified an ordinary geometric-origin
category and its subquotient closure using Jacobsen–Terenzi. The subsequent
`cor:rankone-finite` and optional `lem:regular-finite` applied Lam–Litt's
Lemma 3.5 without showing that the particular simple local systems occur
in smooth-proper cohomology on a dense open. A rational structure alone
does not supply the integrality used in the torsion argument.

The Jacobsen–Terenzi pinpoints are accurate comparisons of broad categories;
they are not the omitted smooth-proper realization statement. They are
retained as comparison context and no longer carry this implication.
Lam–Litt's published lemma explicitly says **smooth variety**, so no
restriction to curves or supplementary dimension-reduction argument is
needed. Its published page range, 536–554, was already correct and is
unchanged.

## Sources read and their exact roles

The numbered passages were read in parsed text and the relevant PDF pages
were inspected. Published numbering is used when indicated; accepted
preprint numbering is expressly identified where that was the version
checked. No claim to have checked an unavailable publisher text is made.

| Source and checked location | Input actually used |
| --- | --- |
| Tubach, *On the Nori and Hodge realisations of Voevodsky motives*, accepted [arXiv:2309.11999v4](https://arxiv.org/pdf/2309.11999v4), Theorem 0.1 (p. 4), Corollary 4.19 (p. 44) | Established ordinary Hodge/Betti compatibility and weight-compatible exact Hodge realization; compact smooth generators `f_sharp Q_Y(n)`. The manuscript bibliography now explicitly fixes v4 numbering. The published bibliographic metadata is retained, but published theorem numbering was not independently checked. |
| Ivorra–Morel, *The four operations on perverse motives*, [published JEMS text](https://ems.press/content/serial-article-files/48220), Corollary 3.14 and §3.5 (p. 4232), Corollary 6.16 and Proposition 6.17 (p. 4263), §6.7/Proposition 6.20 (p. 4266) | Betti-compatible perverse-normalized unipotent cycles; strict Nori weight filtration; ordinary intermediate extension and its purity. The weight pieces are taken in the Nori category before realization. |
| Kollár, *Resolution of singularities—Seattle lecture*, [arXiv:math/0508332v3](https://arxiv.org/pdf/math/0508332), Theorems 35–36 (pp. 24–25) | Projective resolution and boundary principalization in characteristic zero, preserving the original smooth open; closed normal-crossings intersections are smooth and projective over the base. |
| Deligne, *Théorie de Hodge II*, [published text](https://www.numdam.org/item/PMIHES_1971__40__5_0.pdf), Proposition 4.2.5 (p. 44), Theorem 4.2.6 (p. 45), Corollary 4.2.8(iii)(b) (p. 47) | Semisimplicity of smooth-projective cohomology local systems and finite tensor order of determinants of complex sub-local systems of algebraic variations. Rank one is the needed special case. |
| Lam–Litt, *Geometric local systems on the projective line minus four points*, [published Compositio text](https://doi.org/10.1112/S0010437X24007620), §1.1 (p. 537), Lemma 3.5 (p. 545) | The generic smooth-proper definition and rank-one torsion. The lemma's statement allows arbitrary smooth varieties. Its integrality hypothesis is supplied by actual family cohomology. |
| Saito, *A young person's guide to mixed Hodge modules*, [arXiv:1605.00435](https://arxiv.org/pdf/1605.00435), §1.2 and Theorem 1.3 (pp. 3–4), (1.1.5) and (2.1.6)–(2.1.7) | Pure strict-support/minimal-extension pieces and quasi-unipotent cycle conventions. The guide points to the original pure-Hodge-module theorems; it is used for the precise formulation, not as a new input specific to this paper. |
| Jacobsen–Terenzi, *A comparison of categories of Nori motivic sheaves*, [arXiv:2509.21476v2](https://arxiv.org/pdf/2509.21476v2), Corollary 5.15 (p. 56), Proposition 5.17 (p. 58) | Directly confirmed comparisons of broad local-system and perverse-sheaf categories. They are contextual, not a substitute for the new bridge. |

## Proof audit: finite generation to actual families

1. A bounded ordinary Nori complex is compact in the Ind category. Compact
   generation gives a **finite thick construction from finitely many**
   smooth generators. Smooth purity gives their usual compact-support
   Betti complexes up to shifts and Tate twists. This does not use the
   manuscript's new de Rham augmentation to prove its own prerequisite.
2. Finite affine-cover/localization reductions allow projective
   compactification of each generator over the base. Resolve and
   principalize the boundary while preserving its smooth open. The
   localization triangle and the alternating resolution of the boundary
   constant sheaf use **closed** intersections of boundary components.
   Those intersections, not open strata or uncompactified cyclic covers,
   are the smooth varieties projective over the base.
3. For the finite list of projective maps from smooth total spaces, remove
   nondominating images and the images of nonsmooth loci. Characteristic-zero
   generic smoothness and properness give one common dense open on which
   these maps are smooth projective.
4. Form the finite set of simple constituents of their cohomology local
   systems. The local systems with only those composition factors are a
   Serre subcategory; complexes with cohomology there form a thick
   subcategory. This explicitly handles arbitrary cones, extensions and
   retracts. They cannot create a new simple constituent outside the list.
5. Semisimplicity is used **only for the smooth-projective generating
   systems**, to turn their simple constituents into direct summands.
   No claim is made that an arbitrary mixed Nori local system splits.
   Family and cohomological degree may depend on the constituent.
6. Finite coefficient extensions are treated by forgetting the field
   action and taking the specified complex idempotent summand. Tate
   twists do not alter the complex monodromy representation. Neither
   operation introduces new simple constituents.

The compact-generation sentence in the existing realization proof now
has the precise Corollary 4.19 reference. This is a cross-reference
clarification, not a new audit or revision of that proof's augmentation
or six-operation exchange maps.

## Proof audit: the exact Fourier sources

The application starts with `gr^W M` **in the Nori category**, then takes
ordinary intermediate extension. Its pure Hodge realization supplies the
polarizable minimal-extension pieces used by Sabbah. Those pieces have
Betti realizations that are summands of a known ordinary Nori realization;
there is no need to lift an arbitrary complex projector motivically.

For proper direct image, the additive derived functor and perverse
cohomology preserve these summands. Perverse direct image is not claimed
to be exact. Each containing perverse cohomology object is an ordinary
Nori object on the base, to which the new bridge applies.

For nearby cycles, the ordinary Nori unipotent-cycle functor is used with
its established Betti comparison and perverse normalization. Every other
geometric eigenvalue is a root of unity. Tensoring on the punctured
infinity chart with the inverse finite-order Kummer character and taking
unipotent cycles gives the desired eigenpart. The Kummer character comes
from a finite étale Artin pushforward after finite cyclotomic coefficient
extension. This argument covers **all** eigenvalues; it does not assume
that unipotent cycles exhaust the Fourier comparison. The Betti eigenvalue
1 is distinguished from Sabbah's differential-module index -1.

`ker N` introduces no new simple constituent. For its infinity-supported
term, `q o i_infinity = id`, so no arbitrary subobject is passed through a
nonexact proper-image functor. Sabbah's two upstream triangles and the
nonunipotent comparison can therefore use the identified containing
objects. Their mathematical assertions are retained unchanged; this
repair checks the ordinary geometric sources fed into them, not a new
proof of Sabbah's transform comparison.

Only finitely many weights, eigenvalues and cohomological degrees are
involved. There is a common open, not an intersection of infinitely many
separately chosen opens. If the finite étale graph-splitting cover has
been retained, exact finite étale direct image of the containing Nori
objects and the unit/trace degree identity return the constituent
containment to the original base. Pullback of a simple local system is
not assumed to remain simple.

## Rank one and the optional criterion

The new torsion lemma invokes Deligne's original determinant theorem and
Lam–Litt's modern formulation only after exhibiting actual smooth
projective cohomology. Its integral lattice is the torsion-free part of
integral family cohomology. A complex rank-one summand is **not** asserted
to inherit a rank-one integral lattice. Dense-open restriction does not
change the monodromy image of an already lisse local system, because the
induced map of fundamental groups is surjective.

The conclusion in the main Fourier corollary remains **finite Betti
monodromy**. It does not turn an irregular algebraic connection into an
Artin connection. The separate arithmetic kernel theorem remains needed.
In the optional split criterion, the factor is already regular singular,
so regular-singular Riemann–Hilbert does identify its finite character
with an Artin connection. Condition (FG2) now explicitly concerns simple
constituents, not the whole possibly mixed system. This criterion is
still optional, not a new hypothesis of the main saturation theorem.

## Preservation and remaining scope

The canonical title, author list, author identifier, contact, manuscript
date, existing 138 labels, lissity proof and fixed-fiber/regular-cycle
normalizations are preserved. Two lemma labels are added. All eight other
manuscript sources/PDF snapshots/manifest entries are preserved, including
the historical repair companion. No historical provenance report is
rewritten. README and live ledgers point to the two distinct scoped
October 5 repairs rather than claiming universal audit coverage.

Independent specialist review of the assembled paper remains valuable,
especially the realization interface and arithmetic/Tannakian chain.
Those topics are outside this additional audit. No release tag, deposit,
visibility change, or claim of independent human review is made here.
