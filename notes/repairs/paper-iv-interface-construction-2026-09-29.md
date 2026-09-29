# Paper IV: algebraic realization interface constructed; conventions incorporated

Date: 2026-09-29.

Prior repair-branch head: `b2fd02cba7ad6794ccca49b890f72ab1af27cb6c`.
Prior standalone-note source SHA-256: `9540c6757e6943ee3aef12ec734c96cf51dcc682444dd737486e6705d81174d6`.
Frozen canonical baseline: `0bb151018dc73c9e48b847fff31fb82fd2cb9072`.

This revision supplies the algebraic realization-and-comparison construction that the second-pass report left open, and incorporates that report's kernel and nearby-cycle corrections into the standalone note. The canonical Paper IV and all other canonical sources/PDFs are unchanged. Historical reports retain their original verdicts. PR #7 remains draft; this is not integration into canonical Paper IV or independent peer-review certification.

## The construction replacing the missing interface

The former broad external-input paragraph is narrowed to established ordinary Nori structure and **absolute** mixed realizations. The relative functor is now constructed in the note.

Write `N_X=a_X^*N_k` for Tubach's Nori algebra and identify derived Nori motives with `N_X`-modules in etale motives. Let `r_X` be the ordinary algebraic geometric differential-module realization over `k=Qbar`. From the known absolute Nori de Rham fiber `d_k`, define

`alpha_k: r_k(N_k) = d_k(Nor_k^* Nor_k,* 1) -> d_k(1)=k`

by the adjunction counit. Pull this algebra map to X and set

`R_dR,X(M) = 1 tensor^L_(r_X(N_X)) r_X(UM)`.

The map alpha is a de Rham augmentation, not evaluation of unknown numerical periods at an algebraic point. The note proves the module-extension lemma by the augmented free bar resolution; this checks the maps and augmentation, not just the images of free objects. The absolute complex comparison identifies the two augmentations, so the bar construction gives a natural comparison on all module morphisms.

The canonical operation exchange maps are their adjunction mates. On free compact modules they are the established geometric exchange maps. Compact modules form the thick closure of free geometric compact modules; exactness, cones, and retracts prove the exchange isomorphisms on the constructible category. Coherence comes from relative tensor associativity, the bar maps, and adjunction mates, not from an incorrect claim that a conservative derived Betti functor detects equality of morphisms. The heart's t-exactness and faithfulness are proved using the actual complex comparison and faithful field extension.

The absolute complex comparison is used in its homological convention (Choudhury-Gallauer); Harrer's cohomological construction is dualized on rigid geometric motives when used. The proof invokes common-refinement cellular complexes only for the **absolute** assertion. It does not assert the relative cellular-filtration comparison discussed as problematic in Tubach Remark 4.10.

The same algebraic functor, followed by the shifted exponential kernel and algebraic direct image, defines the nonzero-scale realization over k. At an algebraic regular point its normalized restriction is the absolute de Rham fiber with the chosen directional rapid-decay comparison. Unique horizontal continuation makes that comparison natural and tensor-compatible on the entire lisse category and identifies it with elementary rapid-decay period functions. Thus the later `P=Yc` argument uses the matching fiber functors actually constructed here.

## Kernel and nearby-cycle corrections

- The holonomic heart object is `K_lambda=(O,d-lambda dt)`; the derived kernel is `L_lambda=K_lambda[-1]`. The zero-graph check is `i0^*L_lambda=k` in degree zero. The positive graph potential remains `f/lambda` for `E^f=(O,d-df)`.
- The directional nearby-fiber functor is fixed consistently with the dual pairing `exp(-lambda t)`. The lisse tensor/fiber shifts and the scale reversal under Verdier duality are retained explicitly.
- The product `pi1(S) x Z` argument is now stated only for **topological** nearby cycles. A separate proposition uses regular specialization of the Fourier kernel along every finite Fourier scale, including zero, followed by proper-image compatibility, to identify moderate algebraic cycles with that topological local system.
- The counterexample `E^(1/lambda)` is included to rule out the invalid lissity-only inference. The two upstream Sabbah sequences continue to be applied before derived proper image.

## Source map and dependency audit

| Input | Exact use in the revised note |
| --- | --- |
| Tubach, arXiv:2309.11999v4, Lemma 4.12, Corollary 4.14, Proposition 4.16 | The Nori algebra is absolute; derived Nori motives are its modules. The construction does **not** claim that arbitrary mixed Hodge modules have the same absolute-algebra property. |
| Tubach, Theorem 4.5 and proof | The geometric constructible six-operation argument. Initiality alone does not automatically imply all right-adjoint compatibilities. |
| Drew-Gallauer, arXiv:2009.13610v4, Definitions 7.5/7.7 and Theorem 7.14 | The geometric motivic coefficient construction after the algebraic descent, affine-line, orientation, and stability checks. |
| Saito, arXiv:math/0611597, Section 1.8(ii), Sections 2-6 | An explicit ordinary mixed-sheaf model retains the algebraic filtered differential module over the ground field. This is not identified with the entire Nori category. |
| Harrer, arXiv:1609.05516, Chapters 4/7, Theorems 7.4.17/7.6.5 | The absolute cellular and mixed-realization construction, including the algebraic de Rham component and actual comparison. |
| Choudhury-Gallauer, arXiv:1410.6104v3, Sections 6-7, Propositions 7.1/7.12 | Complex/model-level homological realization and its monoidal coherent construction; no claim that a bare triangulated functor automatically has an enhancement. |
| Virk, arXiv:2605.14904v4, Section 6.6, Propositions 6.4/6.8, Theorems 6.13/7.5/7.6, Appendix B | Derived kernel, multiplicativity, support comparison, scale-changing duality, exactness and faithfulness after complexification. |
| Sabbah, Monodromy at infinity and Fourier transform II, Proposition 4.1(ii), Proposition 5.8, Corollary 5.20, (5.21)-(5.22) | Regular specialization at finite Fourier scale and the actual upstream comparison maps and exact sequences. No assertion of global regularity of the Fourier output. |
| Snodgrass, arXiv:2608.06005, Definition 3.5 and Theorem 3.6; absolute rapid-decay comparison of Fresan-Jossen/Hien | A specified directional Betti fiber and its comparison with the algebraic exponential de Rham realization. |

### Internal adversarial checks of the new assembly

1. **Objectwise descent is insufficient.** The construction instead supplies one algebra map and a bar formula on all module morphisms. Comparison must identify the augmentation as well as the objects.
2. **Derived extension of scalars need not be t-exact in general.** For the dual-number augmentation, higher Tor terms survive. The note therefore obtains t-exactness from its actual complex comparison, not from the tensor formula by itself.
3. **Six-operation maps cannot be inferred merely from object identities.** The proof identifies their canonical mates on free modules and uses the existing source-operation maps before extending through cones and retracts.
4. **Unknown periods are not set algebraic.** The augmentation is produced from the absolute de Rham functor and the counit. The actual comparison c may have transcendental entries; it is used only after complexification.
5. **Geometric and coefficient field extensions are different.** The finite coefficient-field projector and its exactness are described separately from k-to-C descent.
6. **Punctured lissity is insufficient for algebraic nearby cycles.** The regular-specialization comparison is inserted explicitly, and the irregular exponential counterexample is retained.
7. **No circular dependence on the functional theorem.** Algebraic realization, comparison, and operation compatibility are constructed before fixed parts, Galois exactness, normalized solutions, and the torsor argument. No numerical or functional period injectivity is used in the augmentation construction.

## Scope and proof status

The interface obligation is discharged by the explicit construction and its proofs **in the revised argument**, using the named standard inputs above. This status does not mean that a separate reviewer has checked the newly assembled proof. A fresh whole-chain audit must examine the new Section 2 together with the retained fixed-part, rank-one, Galois, and torsor arguments before integration into canonical Paper IV.

The prior 61 labels are retained; new labels are added for the interface and cycle comparison. Title, authors, author identifier, contact information, and September 2026 note date are unchanged. The earlier dense-open arithmetic theorem is unchanged: the separate second-pass global strengthening is not needed for this focused revision. No new arithmetic specialization theorem or elementary presentation theorem is claimed.

Mechanical validation is recorded separately in `paper-iv-note-build-verification.json` and the draft PR. The eight original manuscript snapshots and their manifest records are preserved byte-for-byte. A local full-repository check still encounters the already recorded TeX-toolchain-dependent reference-name difference in unchanged canonical Paper IV; the normal repository CI is checked separately. This limitation is not repaired by changing the frozen manuscript.
