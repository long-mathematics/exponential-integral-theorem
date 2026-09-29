# Paper IV: assembled-proof and canonical-integration audit

Date: 2026-09-29.

Audited standalone head: `cb81b7d538ffbabd96081d24e8262422dda8052a`.
Frozen canonical baseline: `0bb151018dc73c9e48b847fff31fb82fd2cb9072`.
Baseline reference: `baseline/paper-iv-pre-repair-2026-09-28`.

This report records the requested assembled-proof audit, canonical integration, and integration audit. It supersedes the *current status* of earlier repair records without rewriting their historical findings. The proof audit is source-checked AI-assisted mathematical review, not independent human peer review, a Lean certificate, or a guarantee that no error can remain. No unresolved essential objection was found in the main chain during this pass. The final build, visual comparison, and merge checks are recorded separately in the verification JSON and PR.

## Audited candidate and scope

The candidate is the repository's **augmentation/module-based** 25-page note, not the separate 26-page local mixed-sheaf-hull variant from an earlier conversation artifact. Its input SHA-256 is `a6587462e47aeb6b7d4d243db6404438ff078b02c8728dabd509ba3a11709ee4`.

The canonical mathematical goal remains the generic relative functional theorem over `k=Qbar` at every `lambda in k^*`, after imposing the actual constant exponential-period relations. The revision does not assert a numerical-specialization theorem, an elementary presentation of all motivic relations, or the optional global arithmetic strengthening from the second-pass memorandum. The dense-open arithmetic theorem suffices and is retained.

## 1. Assembled realization construction

### Geometric system, absolute comparison, and augmentation

The audit checked the algebraic geometric differential-module system before the Nori quotient, including transfer maps, affine-line de Rham invariance, Tate stabilization, and the constructible six-operation argument. The construction does not infer all right-adjoint compatibilities merely from initiality. It retains the algebraic ground field before complexification; objectwise choices of algebraic models would not suffice.

The absolute comparison is used as a natural complex-level monoidal comparison with consistent homological variance. Common-refinement cellular complexes are invoked for the absolute construction only; the proof does not assume the unproved relative cellular comparison discussed in Tubach Remark 4.10. Naturality is applied to the actual adjunction counit to obtain the de Rham augmentation. This is not evaluation of unknown numerical periods at an alleged algebraic period point.

The module formula uses Tubach's absolute Nori algebra and its pullbacks. The free-bar resolution checks all module morphisms and action maps, rather than only the values on free objects. One qualification was added in both manuscripts: the uniqueness assertion is **among colimit-preserving r-linear functors with the specified free-module identification**. It is not an assertion about arbitrary functors from a module category.

### Operations and heart properties

The direct-image exchange maps are actual adjunction mates, checked against the augmentation on free compact geometric modules. The class where an exchange map is an equivalence is thick; compact generation extends the verification through cones and retracts. Coherence is supplied by the bar maps and mates, not by an invalid assertion that a conservative derived Betti functor detects equality of arbitrary morphisms.

Perverse t-exactness and heart faithfulness follow from the constructed complex comparison and faithful scalar extension. They are not automatic consequences of derived extension of scalars. Nearby/vanishing-cycle operation maps are treated through the ordinary gluing diagrams, including unipotent logarithmic and finite Kummer packets. Geometric ground-field extension and coefficient-field extension are explicitly different; the latter uses the chosen component of the finite coefficient-field tensor product.

### Sources checked at the relevant locations

| Source | Use checked |
| --- | --- |
| Tubach, arXiv:2309.11999v4, Theorem 4.5, Lemma 4.12, Corollary 4.14, Proposition 4.16 and Section 4.2 | Enhanced realization, absolute Nori algebra, module presentation, constructible operation argument and compact generation. |
| Drew-Gallauer, arXiv:2009.13610v4, Definitions 7.5/7.7 and Theorem 7.14 | Geometric motivic coefficient-system factorization after the required localization/stability checks. |
| Saito, arXiv:math/0611597, Section 1.8(ii) and Sections 2-6 | Arithmetic mixed-sheaf model retaining an algebraic filtered differential module and the ordinary operation constructions; not an identification of all mixed sheaves with Nori motives. |
| Harrer, arXiv:1609.05516, Chapters 4/7, Theorems 7.4.17/7.6.5; Choudhury-Gallauer, arXiv:1410.6104v3, Sections 6-7, Proposition 7.12 | Absolute mixed realizations, complex-level cellular/refinement maps, monoidal construction and variance. |

No main-period injectivity statement is used to construct this interface.

## 2. Normalizations, quotient heart, and fixed parts

The shifted kernel is `L_lambda=K_lambda[-1]`, where the holonomic heart object is `K_lambda=(O,d-lambda dt)`. The zero-graph unit test is in degree zero. Pulling the kernel to a graph gives `d-lambda dh`, so the required potential is `h=f/lambda` for `E^f=(O,d-df)`. Virk Section 6.6, Proposition 6.8, Theorem 6.13, and Theorems 7.5-7.6 were checked for the kernel, multiplicativity, scale-changing duality, exactness, and faithfulness.

Lisse products use `(N star M)[-d]`, the fiber uses `i_s^*N[-d]`, and symmetry is transported from the unshifted category. A rapid-decay direction and cohomological variance are fixed. The comparison with the chosen absolute fiber is the actual integration comparison, continued horizontally; it is not an unrelated isomorphism of abstract fiber functors.

The Serre and derived-image replacements use the actual affine-line adjunction unit and full faithfulness in every degree before lifting extension classes and truncation triangles. Neither smooth connected fibers in general nor a Serre inclusion in general is asserted to suffice.

Fixed parts use **algebraic** horizontal sections. The shortest-rational-relation argument proves their generic independence, and local horizontal uniqueness gives bundle evaluation. Lisse intermediate extension and its fully faithful restriction are used to extend invertible lifts and their inverses. This avoids an intersection of infinitely many dense opens. The constant subcategory's tensor-dual closure is now stated explicitly.

## 3. Fourier and arithmetic chain

The product fundamental-group argument is stated only for topological nearby cycles. A separate regular-specialization bridge uses Sabbah Proposition 4.1(ii) at finite Fourier scale, including zero, before identifying moderate algebraic nearby cycles. The counterexample `E^(1/lambda)` remains to delimit the hypothesis.

The two sequences (5.21)-(5.22) were checked directly in Sabbah's source, before the later dimension-specific argument. Derived proper image gives two triangles. The perverse-cohomology proof is now worded as an explicit short exact sequence: the subobject of the middle cohomology is a quotient of the first cohomology, and its quotient is a subobject of the third. No exactness of proper direct image on the heart is assumed.

For mixed input, the proof uses the realized geometric-origin category rather than assuming arbitrary Hodge idempotents lift motivically. The source reference is sharpened to Jacobsen-Terenzi, arXiv:2509.21476v1, **Corollary 5.15 and Proposition 5.17**, covering both local systems and perverse constituents. Lam-Litt's published Lemma 3.5 gives torsion only for the rank-one Betti constituent; it is not mistaken for finite tensor order of the irregular algebraic connection.

The arithmetic kernel uses the specified Tate line of the chosen form and Huber-Wustholz Theorem 9.14, checked directly, together with the Picard 1-motive convention. It yields the required logarithmic class and finite factor after clearing a boundary divisor. Algebraic affineness supplies the primitive. The graph and Artin lift then has the correct sign. This argument is independent of the relative functional-period conclusion.

### Explicit corrections to secondary statements

1. The optional split criterion now requires an **actual rank-one exponential-times-regular comparison on the cover and effective descent**. Boundary Stokes grades alone are not claimed to supply that global comparison. Its original labels are retained, but its stronger hypothesis is disclosed in the text. The main generic proof does not use this optional route.
2. The two-graph example distinguishes ordinary topological cohomology degrees from perverse direct-image degrees and states the base `s != 0`.
3. The Nilsson-E example distinguishes finite Kummer monodromy from possibly infinite logarithmic unipotent monodromy.
4. The broad whole-absolute-category identification is not used as a new input; the chosen quotient presentation and the actual absolute fiber comparison are sufficient.

## 4. Galois, constant extension, and torsor audit

Rank-one saturation permits an ambient lift. After twisting, taking fixed parts, and tensoring back, the resulting image is a subobject of the original object and therefore lies in the original Tannakian category. The line-stabilizer proof of normality and the constant quotient are valid with these semi-invariant subspaces.

The evaluation differential group is defined over k at an algebraic regular point. The Betti kernel is separately defined over k. The actual comparison c conjugates the complex groups; this precedes period injectivity. The normalized solution Y has algebraic Taylor coefficients. Finite-dimensional row reduction of its coefficient matrix, after clearing rational denominators, proves the injective extension to C(S). This is not a claim that an arithmetic argument already handled every transcendental-coefficient differential subobject.

The actual matrix is `P=Yc`. Its transformation `P -> P(c^{-1}hc)` agrees with the Betti torsor action on universal coordinates, so the map is genuinely equivariant for the same group. The torsor comparison is first made over C(S), where the meromorphic solution field has exactly the complex constants. Flat localization then proves the relative period-map injection.

Only afterward does the proof localize the tensor-product embedding, prove `b tensor 1 = 1 tensor alpha` inside an injective tensor product, and apply the intersection lemma. It yields the exact constant field F0; differential simplicity descends by faithful flatness. The proof uses **all** base derivations and does not separately adjoin the potentially transcendental entries of c to the smaller solution field. The dimension-zero case is stated separately.

## 5. Canonical integration audit

The canonical document was rebuilt around this checked chain, not left with parallel obsolete proofs. The abstract, introductory claims, category definitions, applications, and conclusion were reconciled with it. The main generic KZ statement and the Gamma presentation retain their original scope. The old framework's subsidiary assertions are qualified as described above; no broader hypothesis was silently retained in an introduction.

The title, author order, Le Blanc identifier, email, and **August 2026 canonical date** are preserved. The repair note retains its **September 2026 date**. Canonical theorem counters use aliascnt, correcting the previous toolchain-sensitive reference names without modifying any unrelated manuscript.

All 63 original canonical cross-reference labels are retained, with aliases for consolidated duplicate lemmas; the build record includes the alias map. There are now 136 canonical labels and 57 theorem/lemma/proposition/corollary environments. The old numerical theorem numbering is not claimed to be unchanged. All 75 original standalone-note labels are retained. The revised local PDFs have 35 canonical pages and 26 companion-note pages.

Exact reviewed source output hashes:

- Canonical: `bc652b2f6d9a2e94b945c2a4e42c3f4b2ac9c19e0b060047cc949271cbf218cb`.
- Standalone note: `eac3f84b331389c80e687c5530604dc5399624d64b3fac3a94549c57b9f88236`.

The integration audit checked every preserved label target, all referenced/cited keys, the changed hypotheses and downstream applications, and the complete main dependency chain. No essential mathematical objection remains open in this audit record. This means the recorded repair work is ready for the repository release checks; it is not an assertion of independent peer-review certification.

## 6. Mechanical evidence and remaining release gate

Both exact-arithmetic suites were rerun locally: 120 Gamma packets and 1,645 additional weight relations passed, as did graph-sign, flat-gauge, finite-coefficient, divisorial-pole, and negative tensor/derivation checks. These are limited regression tests, not tests of the motivic construction itself.

The local build-tool tests passed (6/6), and all nine documents compiled. Both changed PDFs passed their front-matter, log, label, hash, and rebuilt-text checks. All 35 canonical and 26 note pages were rendered and reviewed; full-size inspection covered the algebraic interface, cycle bridge, and final torsor/constant argument. No clipping or out-of-page content was found.

The local full-repository `make check` under TeX Live 2025/dev now passes canonical Paper IV (whose reference names are repaired) but stops at the **unchanged structural companion**, due only to the previously known cleveref theorem-name differences from the repository's TeX Live 2023 snapshots. The companion is deliberately not changed. The official Ubuntu 24.04 build must pass all nine documents before merge. The official PDFs must also be checked against the reviewed sources and renders.

The frozen baseline reference must remain unchanged. The seven unaffected canonical source/PDF snapshots and manifest records must be byte-identical. No temporary integration payload or workflow may remain in the final diff. The build-verification record and final PR comment supply the release result, including the exact merged revision; this report alone does not assert that a pending CI run or merge has completed.
