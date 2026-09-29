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
