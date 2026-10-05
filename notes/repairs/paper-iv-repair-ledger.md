# Paper IV standalone repair ledger

Date: 2026-09-28.

Baseline: `0bb151018dc73c9e48b847fff31fb82fd2cb9072`.
Baseline reference: `baseline/paper-iv-pre-repair-2026-09-28`.
Repair branch: `paper-iv/standalone-repair-note-2026-09-28`.

- [Standalone source](../../papers/04-relative-exponential-nori-ayoub/repairs/paper-iv-repair-note.tex)
- [Standalone PDF](../../output/pdf/paper-iv-repair-note.pdf)
- [Machine-readable baseline](paper-iv-baseline.json)

The baseline Paper IV source/PDF are not revised. This note is a candidate set of replacement proofs, not an integrated revision or an independently checked mathematical certificate. An earlier assessment that all issues are repairable is not an input to this note.

## Status vocabulary

- **Replacement proof drafted:** an explicit argument is supplied in the note and is ready to be attacked.
- **External input:** a published or preprint theorem, or a realization-compatibility interface, is used rather than reproved. Its precise applicability remains a separate audit obligation.
- **Independently audited:** reserved for a future fresh audit with a recorded outcome. No item below has this status merely because the document compiles.
- **Integrated:** reserved for a later revision of the canonical Paper IV. No repair in this branch is integrated.

## Dependency-ordered repair ledger

| ID | Baseline issue | Replacement in note | Dependencies | Present status |
| --- | --- | --- | --- | --- |
| N1 | Graph potential has the wrong sign | Section 1, graph-realization lemma: potential `f/lambda`, explicit pullback connection and sign countercheck | Kernel operator convention and projection formula | Replacement proof drafted |
| N2 | Perverse tensor/fiber shifts omitted | Section 1: `(N star M)[-d]`, unit shifted by `d`, fiber `i_s^*N[-d]`; symmetry constraints transported, homology/cohomology variance separated | Derived convolution and absolute Betti fiber input | Replacement proof drafted; external interface to audit |
| N3 | Same-scale duality asserted too broadly | Section 1: sign-reversed realization duality, potential reflection and base Tate normalization; graph inverse explicit | Virk Theorem 6.13, smooth purity | Replacement convention drafted; interface to audit |
| C1 | Extension closure incorrectly attributed to arbitrary smooth connected fibers | Section 2: actual affine-line adjunction unit and derived full faithfulness, then extension classes | Ordinary coefficient system, conservative Betti, BBD subquotient closure | Replacement proof drafted |
| C2 | General Serre-derived devissage invoked without its needed hypothesis | Section 2: full faithfulness in all degrees followed by truncation induction | C1 | Replacement proof drafted |
| C3 | Quotient-faithfulness proof uses chosen representative morphisms | Section 2: detect zero quotient objects, then images of arbitrary quotient morphisms | Constant reflection and exact quotient functors | Replacement proof drafted |
| F1 | Fixed-part calculation must use algebraic invariants and correct shifts | Section 3: independent algebraic horizontals, actual evaluation map, constant reflection and maximality | N1-N3, C1-C3, direct-image compatibility | Replacement proof drafted |
| F2 | Infinite family of dense opens compressed into one without justification | Section 3: lisse intermediate extension, full faithfulness of restriction, extension of an inverse; object-by-object saturation | Exact realization commuting with intermediate extension | Replacement proof drafted; closure interface to audit |
| G1 | Unipotent constituent argument passes too quickly through proper direct image | Section 4: Sabbah (5.21)-(5.22) before direct image, two derived triangles and perverse cohomology | Sabbah comparison, ordinary geometric-origin category | Replacement proof drafted using stated external inputs |
| G2 | Finite Betti monodromy confused with possible irregular algebraic data | Sections 4-5 keep these conclusions separate; full specified-Tate-line arithmetic kernel proof | Lam-Litt published Lemma 3.5; Huber-Wustholz Theorem 9.14; Picard 1-motive convention | Replacement proof drafted using external arithmetic inputs |
| G3 | Rank-one lift may be only ambient | Sections 5-6: graph plus Artin lift, fixed part after twisting, image back inside the original object | G2, F1-F2 | Replacement proof drafted |
| T1 | Fiber fields and group coordinates insufficiently distinguished | Section 6: algebraic evaluation groups over `k`, Betti kernel over `k`, actual comparison conjugation over `C` | Compatible de Rham and Betti fiber functors | Replacement proof drafted; interface to audit |
| T2 | Complex differential subobjects not automatically covered by an arithmetic proof | Section 7: normalized solution with algebraic Taylor coefficients and finite coefficient-matrix descent | Algebraic regular point, integrability, ordinary PV input | New replacement proof drafted |
| P1 | Actual comparison algebra called PV before proving no new constants | Section 8: work first over `C(S)`, identify group and equivariance explicitly via `P=Yc`, compare two torsors | Sections 6-7 | Replacement proof drafted |
| P2 | Descent to actual period-constant field not proved | Section 8: flat injections, differential simplicity descent, localized tensor-product injection, intersection lemma, exact constants `F0` | P1 and geometric integrality of the base | Replacement proof drafted |
| S1 | Auxiliary split Stokes formulation may conceal a global comparison/descent claim | Section 5 explicitly requires an actual global rank-one comparison and effective descent for the optional route; the main route does not use it | Separate optional hypotheses | Qualified formulation, not an unconditional generalization |

## External interfaces the next auditor must examine

1. The ordinary Nori derived coefficient system and its scalar extension, including an **algebraic de Rham realization over the geometric field** compatible with the exponential construction. A complex Hodge realization alone is not a substitute for this requirement.
2. Absolute rapid-decay Betti realization, its cohomological variance, the tensor unit, and the normalization used in relative lisse fibers.
3. The finite-graph parameterized microlocalization result and its application to all regular geometric representatives under consideration; the pure-to-mixed geometric-origin passage.
4. The exact Picard 1-motive/Tate convention and the specific inclusion lifted by Huber-Wustholz. Merely finding some Tate constituent would not prove the stated identity for the chosen form.
5. Standard Picard-Vessiot results for an integrable system with **all** base derivations, including the evaluation fiber interpretation. Do not replace this with parameterized PV theory where some derivatives are omitted.

## Citation locations fixed or clarified

- Virk: the sign is fixed by the explicit operator in Section 6.7; Theorem 6.13 reverses scale under duality; Proposition 7.2 separates subquotients from extension closure.
- Sabbah, Monodromy at infinity and Fourier transform II: use (5.21)-(5.22) upstream of projective direct image, before the later dimension-specific discussion.
- Sabbah, Cotti-Dubrovin-Guzzetti preprint v3: Appendix B is on preprint pages 12-13; use the locally free localized-module statement immediately before Proposition B.1.
- Lam-Litt: use **published Lemma 3.5** rather than the earlier preprint numbering.
- Huber-Wustholz: Theorem 9.14 is the full-faithfulness/subquotient input.

## Fresh audit protocol

Read the note as a proof attempt, not as a list of accepted fixes. Check each external interface, then follow the numbered arguments in dependency order. In particular, attempt to break the normalized tensor symmetry, the extension of invertibility, the normalized-solution constant-extension lemma, the comparison conjugation, scheme-level equivariance, and the localized tensor-product argument for constants. Record whether an objection invalidates a statement, an application, or only an explanation. Do not silently weaken or preserve the main theorem; report precisely what the replacement proofs establish.

A successful build is recorded separately in the build-verification file and PR. The baseline source/PDF hashes and all eight preexisting manifest entries must remain unchanged. The ninth manifest entry is the standalone note, not a replacement Paper IV.


## 2026-09-29: algebraic interface construction incorporated

The dated second-pass report remains unchanged. The standalone note now supplies the previously outstanding algebraic realization-and-comparison construction, rather than postulating that interface. This is a new proposed proof in the repair note, not a retroactive change to earlier audit verdicts and not a claim of independent certification.

### New dependency chain

1. The ordinary geometric algebraic differential-module coefficient system gives `r_X` over the geometric field, with its regular complex comparison. Its motivic construction checks descent, affine-line invariance, orientation and stability; six-operation compatibility is asserted on the geometric constructible image, not as an automatic consequence of initiality.
2. The absolute mixed-realization construction and Tubach's absolute Nori algebra give the algebraic augmentation `alpha_k: r_k(N_k) -> k` by the counit. Pull it back to every base. This is a de Rham augmentation, not evaluation at an algebraic point of a numerical period algebra.
3. Use Tubach's module description to define `R_dR,X(M) = 1 tensor^L_(r_X(N_X)) r_X(UM)`. The free bar resolution proves the functorial comparison on all module morphisms. Operation exchange maps are their canonical mates, checked on free constructible generators and then on the thick closure.
4. Exactness and faithfulness on the heart follow from the natural complex comparison and faithful scalar extension. They are not automatic properties of an arbitrary derived augmentation. Coefficient-field extension is kept separate from geometric-field extension.
5. The shifted algebraic exponential kernel defines the quotient realization over `k`. Its complexification is Virk's actual formula, so the required support and exactness results descend. A fixed directional absolute rapid-decay fiber supplies the actual comparison at `s0`; horizontal continuation extends it naturally to every object and tensor map.
6. In the Fourier argument, topological nearby cycles and moderate algebraic cycles are distinct until Sabbah's regular-specialization input and proper-image comparison identify them. The two upstream exact sequences are still applied before direct image.

### Updated live status

- N1/N2/N3: positive graph potential retained; the additional derived kernel shift `L_lambda=K_lambda[-1]`, degree-zero unit check, directional fiber, and fixed-scale duality conventions are now explicit.
- C1/C2/C3/F1/F2: previous replacement proofs retained. Their algebraic realization input now points to the construction in Section 2, not an unnamed interface.
- G1/G2: the regular-specialization bridge is stated and proved using Sabbah Proposition 4.1(ii); lissity on the punctured family alone is explicitly rejected, with `E^(1/lambda)` as a countercheck.
- T1/T2/P1/P2: their algebraic and analytic fiber functors are now the ones constructed in Section 2. The existing torsor-and-constant-field proofs are retained and remain subject to a whole-chain fresh audit.
- New I1: absolute-to-relative algebraic realization by the Nori module algebra, counit augmentation, bar comparison, and canonical exchange maps — **replacement proof supplied; internally audited; independent audit pending**.

The separate second-pass global rank-one strengthening is not needed for this focused update; the original dense-open arithmetic theorem in this standalone note remains unchanged. Canonical Paper IV and the other seven baseline documents remain frozen. See the new dated `paper-iv-interface-construction-2026-09-29.md` for the source map and proof audit.


## Canonical integration and closure review, 2026-09-29

The assembled candidate at `cb81b7d` has undergone the requested source-checked proof audit, followed by integration into canonical Paper IV and an integration audit. The recorded main proof has no unresolved essential objection in this pass. This is AI-assisted review, not independent human peer review or formal verification. Earlier ledger entries and reports remain historical.

The augmentation interface, normalized kernel and fibers, actual nearby-cycle bridge, fixed parts, arithmetic lifting, compatible groups, and explicit torsor/constant-field descent are integrated. The optional split criterion now requires an actual rank-one comparison and effective descent; it is not used by the main generic proof. The module-functor uniqueness hypothesis, the two-graph cohomological convention, and the Nilsson-E monodromy wording are explicit.

Canonical Paper IV is 35 pages; the retained repair companion is 26 pages. All 63 old canonical labels and all 75 old note labels remain. Duplicate canonical lemmas have been consolidated with label aliases; numerical theorem numbering is not unchanged. Authorship, titles, contacts, and manuscript dates are preserved.

See [assembled and integration audit](../provenance/paper-iv-assembled-integration-audit-2026-09-29.md) and [build and structural verification](../provenance/paper-iv-integration-build-verification.json). The official revision build passed `make test`, `make pdf`, and `make check` for all nine documents, preserving the seven unaffected snapshots. Final artifact review, normal PR CI, and the merge are recorded in the PR. The frozen baseline branch remains pinned.


## 2026-10-05: finite-graph lissity repair and scoped interface-3 status

This dated correction supersedes the earlier coverage claims for the lissity
application without rewriting the September 28–29 records. At baseline
`d83904db95a9c68834c0949d5e52fe97c28a1613`, canonical `lem:graphs` cited
Sabbah's special eigenvalue-parameter calculation and Douai–Sabbah
Propositions 1.18/1.20 without verifying the needed microlocal-lattice
hypothesis. The September 29 reports did not document that verification.
Their broad closure wording is not evidence that this dependency was checked.

The canonical lemma now has an algebraic compactification and
characteristic-variety proof. It explains why the singular graphs miss
infinity, obtains a logarithmic lattice from regularity of the algebraic
input, proves generation and goodness of the filtration, and separates the
proper characteristic estimate from Fourier exactness. The fixed-scale
identification with `rho_lambda` and the regular-singular nearby-cycle
comparison on the pushed-forward transform are explicit. Douai–Sabbah
Theorem 1.11 and Corollary 1.12 replace the mismatched citation.

**Interface 3 must be read as two components:**

- **3(a), finite-graph/nonzero-scale lissity: repaired and closed in this
  scoped review.** The fixed-fiber identification and the bridge's
  regular-singular comparison are included in the repair. This is an
  AI-assisted proof review, not independent peer review or formal verification.
- **3(b), ordinary geometric-origin application: OPEN for separate audit
  before deposit.** Verify that the category in Jacobsen–Terenzi
  Corollary 5.15 and Proposition 5.17 contains the precise pure/mixed
  subquotients of nearby cycles at infinity used here, and that these
  satisfy the geometric-origin hypothesis of Lam–Litt's published
  Lemma 3.5. This revision neither proves nor disproves that application.

The realization interface, the remaining rank-one/arithmetic chain, and
all of Paper IV are not newly certified by closing 3(a). The historical
repair companion is not synchronized: its lissity argument is superseded
by the canonical proof. See the [dated repair and source-check record](../provenance/paper-iv-lissity-repair-2026-10-05.md).


## 2026-10-05: geometric-origin bridge and interface-3(b) repair

This is the separate follow-up to the lissity repair at main
`3b587fdfde4992e19745302da1c8e6ec4f9326c0` (PR #12). It supersedes the
open **3(b)** status above; the historical October 5 lissity record and
September reports remain unchanged.

- **3(a):** finite-graph/nonzero-scale lissity remains closed by the
  preceding scoped repair; its proof and normalizations are unchanged.
- **3(b):** **repaired and closed in this scoped, source-checked AI-assisted
  review.** `lem:projective-constituents` proves generic smooth-projective
  realization of each simple constituent by compact generation,
  compactification, boundary resolution, and a finite Serre/thick argument.
  `thm:nearby-geometric` identifies the ordinary Nori objects containing
  the pure direct images, all nearby-cycle eigenparts, and nilpotent-kernel
  constituents. `lem:projective-rank-one` then applies Deligne/Lam–Litt
  with the actual family and integral-cohomology hypothesis in place.

The additional audit checked Nori weight pieces before realization,
ordinary perverse-normalized unipotent cycles, finite Kummer twists for
all other eigenvalues, preservation of Betti summands without lifting
complex projectors, and finite étale descent via trace. It neither treats
proper perverse direct image as exact nor claims arbitrary mixed local
systems are smooth-projective summands. The optional split criterion has
the same explicit constituent condition. Jacobsen–Terenzi Corollary 5.15
and Proposition 5.17 were read directly and are now comparison context,
not the missing smooth-proper bridge.

This is not independent human review or formal verification. Closing
3(b) does not newly close the realization/augmentation interface,
arithmetic kernel, Picard–Vessiot descent, or entire period-torsor chain.
See the [dated geometric-origin audit](../provenance/paper-iv-geometric-origin-repair-2026-10-05.md)
and its separate build-verification record. No release/deposit is made.


## 2026-10-05: arithmetic mixed-sheaf realization replacement

This follow-up supersedes the earlier augmentation-interface clearance, not the historical files. The canonical source now constructs realization through Saito's arithmetic mixed sheaves and an explicit transfer of Tubach's constructible-heart method. The proposed unary argument for external product was invalid; Terenzi's perverse-concentrated presentation and multi-exact universal factorization replace it. The actual absolute de Rham/integration normalization remains an explicit lemma.

The scoped audit rechecks operation maps, enhancement, universal-heart kernels, ordinary geometric cycles, the arithmetic rank-one kernel, semi-invariant exactness, normalized PV base change and exact constants. No new numerical theorem or optional global arithmetic strengthening is asserted. Tubach arXiv-v4 pinpoints are retained correctly; the rational directional fiber, finite-etale reference and HTT complex-field descent are explicit. The historical repair companion is not synchronized and is not the current proof source.

See the [dated repair/audit](../provenance/paper-iv-arithmetic-realization-repair-2026-10-05.md) and [official build record](../provenance/paper-iv-arithmetic-realization-build-2026-10-05.json). This is an AI-assisted proof/source audit, not independent human review or formal verification.
