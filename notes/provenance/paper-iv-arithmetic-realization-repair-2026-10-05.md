# Paper IV: arithmetic mixed-sheaf realization repair

Date: 2026-10-05. Baseline main: `7ce1c249f46a0bffc7fe2b689027c28c259455b5`.

## Scope and disposition

This record supersedes the earlier clearance of the augmentation-based realization interface as requiring only citation cleanup. It does not rewrite the September reports or the October 5 lissity/geometric-origin records. The current repair replaces the construction, rather than treating an unproved enhanced absolute comparison as an external theorem.

The candidate was the attached note *A k-rational realization for Paper IV*, considered together with the competing source audits. The additional audit found a definite error in its treatment of external product, repaired below. The canonical manuscript now contains an explicit arithmetic mixed-sheaf transfer proposition, a universal-heart construction, a separate tensor argument, operation/cycle comparisons, and an absolute normalization lemma. These are proposed and audited mathematical arguments in this revision, not statements attributed verbatim to Tubach or Saito. No unresolved essential objection was identified in this scoped AI-assisted check after the revisions below. This is not independent specialist peer review or formal verification.

The arithmetic kernel, rank-one lifting, semi-invariant normality, normalized-solution base change, and torsor/constant-field descent are retained. Their application now uses the replacement interface. No numerical-specialization theorem, elementary presentation theorem, or global arithmetic strengthening is added.

## 1. The tensor error and its repair

The proposed note placed external product in the same perverse-t-exact argument as unary operations. For arbitrary complexes that would require commuting zeroth perverse cohomology with external product. At a point, `A=Q[1]` and `B=Q[-1]` give zero zeroth cohomology separately but `H^0(A tensor B)=Q`. Thus this was a genuine error.

The revised `lem:perverse-tensor-lift` uses Terenzi's perverse-concentrated diagram `D^0(X)`. Theorem 1.12 of *Tensor structure on perverse Nori motives* identifies its universal abelian factorization with the Nori heart. On this diagram the arithmetic Hodge realization is itself perverse, and external product preserves the concentrated diagram. The geometric tensor map can therefore be lifted using the separately exact universal factorization and its natural transformations, with equal Hodge/Betti Serre kernels. The specific multivariable sources are Terenzi's *On the functoriality of universal abelian factorizations*, Proposition 4.3, Corollary 4.5, Proposition 4.6 and Section 6. The construction does not claim such a lifting for arbitrary biadditive functors.

## 2. The arithmetic target and enhancement

The target is Saito's category of mixed Hodge modules with a model over `k=Qbar` of the filtered algebraic D-module, weight filtration, and polarizations. Saito, *On the formalism of mixed sheaves*, Section 1.8(ii), really defines this category. The remark following it constructs its primitive filtered D-module operations over k. Sections 2-5 construct the derived operations and cycle maps; Proposition 6.15 extends from smooth to separated varieties.

Saito is used as a triangulated mixed-sheaf input. The enhancement is a new transfer proposition in this paper, not a claim that Saito already supplied an infinity-categorical coefficient system. Its proof checks the applicability of Tubach's method:

- smooth purity gives the smooth left adjoint; localization, smooth base change, tensor constraints, affine-line invariance and Tate stability use actual mixed-sheaf maps;
- the constructible t-structure and lisse dualizable objects supply the hypotheses of the Section 2 effacement argument, with the point category already a derived heart;
- exact tensor and pullback on constructible hearts give the enhanced diagram by Theorem 3.3 and Proposition 3.5;
- the rational forgetful comparison is enhanced by the same diagram, and actual adjunction mates give the other exchange maps;
- descent uses the bounded-amplitude/truncated mapping-space argument of Theorem 3.24, not an assertion that Ind-completion commutes with arbitrary limits;
- Drew-Gallauer initiality is applied only after constructing the target coefficient system; rational/etale factorization and constructible six-operation compatibility are separate steps, following Tubach's Theorem 4.5 and Lemma 4.7.

`lem:arithmetic-D-operations` explains why the D-module component preserves the actual operations: transfer modules, Spencer/de Rham complexes, localization and V-filtration, finite Cech constructions, duality, and their maps are defined before complexification. Conservativity detects that an existing map is an isomorphism; it neither creates comparison maps nor detects equality of arbitrary derived morphisms.

## 3. Universal hearts, operation maps, and absolute normalization

`lem:arithmetic-heart` works on the universal abelian envelope. The exact Hodge and Betti extensions have the same Serre kernel because the rational forgetful functor is exact faithful. This is stronger and more precise than checking only zero objects in the original triangulated diagram.

Unary closed direct image, shifted smooth pullback and duality use compatible exact representation diagrams. Tensor product uses the separate concentrated-diagram proof. Adjoint mates, factorization, duality and diagonal pullback supply all six operations. Coherence is checked on constructible hearts, where the realization is faithful, and then enhanced. The composite with Tubach's `Nor*` is identified only after it is a morphism of coefficient systems.

Ordinary geometric nearby cycles retain the logarithm objects, nilpotent endomorphisms, canonical and variation maps, and the finite stabilized kernels/cokernels of the Ivorra-Morel gluing construction. Kummer projectors are used only in the geometric quasi-unipotent sector.

The absolute lemma retains interface item (iv): on good-pair generators, the actual de Rham complex and integration map are identified together with morphisms of pairs, connecting maps, products, and Tate trace. Universal heart factorization extends this identification. An abstract comparison of fiber functors alone is not substituted for the actual period normalization. No enhanced cellular-versus-universal `Nor*` comparison is assumed.

## 4. Source corrections and smaller repairs

- **Tubach numbering:** the original manuscript explicitly used arXiv v4. Its Theorem 4.5, Lemma 4.12, Corollary 4.14, Proposition 4.16 and Corollary 4.19 were correctly numbered for that version. The earlier recommendation to replace these by published Section 6 numbers was mistaken. The version convention is now explicit at first use and in the bibliography.
- **Cellular sources:** Choudhury-Gallauer Proposition 7.12 has genuine model-level/Quillen structure, not just a bare triangulated functor. Harrer Theorem 7.6.5 is a mixed-realization factorization whose earlier conditional dependency is addressed in his thesis. Neither observation by itself supplies the particular enhanced de Rham identification required in the old proof. The old augmentation route is removed from the proof, not declared disproved.
- **Rational Betti fiber:** the directional fiber is explicitly constructed with rational sections at infinity and then extended to k. Its tensor maps are rational convolution maps; complexification checks exactness and faithfulness. Snodgrass Definition 3.5/Theorem 3.6 provide the directional complex formulation, and his introduction recalls the natural rational rapid-decay structure in the pure exponential case. No arbitrary irregular rational structure is being inferred. The suggested Fresan-Jossen Section 2.8 pinpoint was not independently retrieved and is not inserted as a verified pinpoint.
- **Finite etale covers:** Milne, *Lectures on Etale Cohomology*, version 2.21 (2013), Remark 3.3(c), supplies the algebraically closed characteristic-zero base-extension invariance used by the arithmetic kernel, including the nonproper case.
- **HTT:** the characteristic estimate is specifically in Remark 2.5.2; Theorem 2.5.1 supplies proper-image coherence. Theorem 5.3.7 supplies the logarithmic characterization. A finite sum of coherent logarithmically stable submodules gives the lattice needed near infinity. The proof is performed after extension to C, the field of the cited textbook, and lissity descends by faithful flatness; no lattice over Qbar is asserted solely from the complex source.
- **Existing clarifications retained:** the specified Tate morphism and the possibly non-algebraically-closed constant field were already explicit. No redundant paragraphs are added for them. The normalized fundamental matrix/evaluation fiber identification receives one short clarification.

## 5. Downstream checks and adversarial tests

The arithmetic sign remains `E^(-F/N)` when `N omega - dlog(u)=dF`; the finite factor's Nth power has horizontal generator `u^(-1)`. Huber-Wustholz Theorem 9.14 lifts the specified de Rham-Betti morphism. The rank-one lift remains ambient until the fixed-part/twist/image construction returns its semi-invariant subspace to the original subobject-closed category.

The PV argument still first proves comparison over `C(S)` with `P=Yc`, allowing the entries of c outside the actual constant-period field. Its action is `P -> P(c^(-1)hc)`. Period injectivity precedes the localized tensor-product injection and the proof that the smaller field has exactly the constants `F0`. All base derivations are used. No new arithmetic theorem is extracted from formal Stokes grades or from complex differential subobjects.

## 6. Preservation and validation

Only canonical Paper IV, its PDF/manifest record, current navigation/status and this dated audit/build record are intended to change. The historical repair companion, the other eight manuscript sources and PDFs, old provenance, author order/identifier, title/contact, and August 2026 manuscript date are preserved. No repository settings, license, visibility, release tag or archival deposit are changed.

The machine-readable companion `paper-iv-arithmetic-realization-build-2026-10-05.json` records the actual official build commands and preservation hashes. Final-head PR CI, official-artifact visual inspection, helper removal and the merge/post-merge checks are recorded in the pull request. Compilation and finite tests validate artifacts, not the mathematical theorem.
