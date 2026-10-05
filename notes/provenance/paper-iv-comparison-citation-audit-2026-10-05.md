# Paper IV: absolute comparison and rational-fiber citation follow-up

Date: 2026-10-05. Baseline main: `fa53b5fdb51834fe7135d3948ed4a35cd454c68e` (PR #18).

## Scope

This is the focused follow-up requested after the arithmetic mixed-sheaf realization repair. It strengthens the source-to-claim explanation for the actual absolute comparison and replaces the rational-fiber proof with direct rational references and an explicit direction transport. It does not replace the Section 3 architecture, add a hypothesis, change a theorem statement, or re-audit all of the downstream arithmetic/Tannakian/Picard–Vessiot proofs. The earlier dated records remain unchanged. This is an AI-assisted source and argument audit, not independent specialist review or formal verification.

## 1. Absolute normalization: general pairs and the specified period map

The suggested Huber–Müller-Stach Theorem 8.1.9 and Example 8.1.10 were checked in the author-hosted **June 8, 2015 manuscript**, Part II, printed pages 161–162. The theorem extends a cohomology representation together with its specified comparison to singular cohomology. Its final paragraph gives the multiplicative/tensor version. The example explicitly takes algebraic de Rham cohomology and the period isomorphism of Chapter 5. These are not asserted to be the theorem numbers in the published book.

A citation solely to that extension theorem would leave the comparison on geometric generators too compressed. Part I supplies the additional bridge: Theorem 5.3.3 is the smooth affine integration normalization; Lemma 5.5.1 gives the natural smooth complex comparison; Definition 5.5.4 constructs the period isomorphism for arbitrary pairs from compatible smooth proper hypercovers and the relative cone; Lemma 5.5.5 gives well-definedness and compatibility with products and relative long exact sequences. The relevant passages, including their maps, were read directly.

The revised proof of `lem:absolute-dR-comparison` identifies the already-constructed geometric comparison with this map on the hypercover complexes and their common refinements, then takes the designated good-pair cohomology and uses the multiplicative universal property. It does not equate the naive Kahler differential complex of a singular variety with algebraic de Rham cohomology. The actual pair maps, connecting maps, products, and Tate normalization are retained. This does not revive the earlier enhanced cellular-versus-universal comparison problem.

## 2. Rational directional fiber: correct statement and source division

The full author-hosted Fresan–Jossen manuscript was obtained and the relevant pages inspected. Definition 2.3.5 and Proposition 2.3.7 are explicitly rational; Theorem 2.4.11 establishes the convolution tensor structure with its constraints; Theorem 2.8.1 proves that the nearby fiber at infinity is a fiber functor. Corollary 3.2.3 identifies the rational nearby fiber of geometric exponential data with rational rapid-decay cohomology.

The proposed pinpoint **Theorem 2.6.2 is not the tensor-structure theorem**: it computes global monodromy of a convolution, including a fiber tensor-product formula in part (2). Accordingly the revised proof cites Theorem 2.4.11 for the tensor category and Theorem 2.8.1 for the fiber-functor compatibility. No replacement proof of these external theorems is claimed.

The source uses closed half-planes whereas Paper IV uses open half-planes. After avoiding the finite singular set both compute the same eventual local-system sections; the proof records that equivalence. For `r_theta(z)=exp(i theta) z`, the identity `Psi_theta = Psi_0 composed with r_theta^*` follows directly from sections. This rational topological pullback commutes with addition and fixes zero, hence transports the tensor fiber functor. No algebraicity of the rotation, and no motivic pullback by a non-k-defined rotation, is asserted. Eventual section spaces commute with scalar extension.

Corollary 3.2.3 is cited for the **rational topological rapid-decay identification**, not for an algebraic de Rham integration theorem that it does not state. The latter remains the separate actual comparison in `prop:relative-Betti-interface`. The closing paragraph of the normalized tensor/fiber proposition now makes this source division explicit.

The bibliography no longer labels the checked Fresan–Jossen file a “2020 version”. Its cover has no printed version date; the recorded file was accessed on October 5, 2026. It is cited as a book manuscript, not a published book. Its PDF metadata has a creation date of April 11, 2024, which is recorded here only as metadata, not as an asserted edition date.

## 3. Other recommendations checked

Terenzi's *On the functoriality of universal abelian factorizations*, Section 4, was checked beyond the introductory summary: Proposition 4.3 constructs the multi-exact lifted functor; Corollary 4.5 supplies the appropriate compatible version; Proposition 4.6 lifts natural transformations. The existing perverse-concentrated tensor proof uses the required separately exact hypothesis and needs no new modification.

The differential-module component lemma already identifies transfer bimodules, relative de Rham/Spencer complexes, localization and V-filtration, finite Cech constructions, duality, and the operation/cycle maps. Its surrounding input explicitly distinguishes Saito's stated triangulated formalism from the construction-level verification in Paper IV. Another disclaimer sentence would duplicate that qualification, so this lemma is left unchanged. This pass does not claim to have found a single packaged source theorem for the full arithmetic interface.

## 4. Source versions and hashes

All three author-hosted PDFs below were read as sources, not incorporated into the repository. The author-host URLs are the ones in the updated bibliography. The retrieval used a temporary read-only branch workflow; its first attempt encountered author-host certificate hostname errors, and a public-PDF-only fallback retrieved the files without credentials or execution. The temporary source and build helpers are removed before merge.

| Source file | SHA-256 |
| --- | --- |
| Fresan–Jossen, `ExpMot.pdf` (301 pages) | `7da885c162606b3c7a2b377d532e59097e51a6856c7f9ba75071d559d2e5ebf5` |
| Huber–Müller-Stach, Part I, June 8, 2015 | `5d7e91433f2b28ffea8a00f76b5428edca8e9b25a501ba8eeb56564b8294a496` |
| Huber–Müller-Stach, Part II, June 8, 2015 | `cdf0e5bb94fc7d22a36134b61c4d5fead2b515453f9714bf6b527cc3483ce85d` |

## 5. Preservation and validation

The edit script checks that every theorem-like statement and every label is unchanged, and that the full mathematical body from the affine-line quotient through the concluding discussion is byte-identical. Authorship, title, identifier, contact, and the August 2026 manuscript date are preserved. The eight other source/PDF pairs and their manifest records are preserved; the historical repair companion and earlier provenance are not synchronized or rewritten.

The companion `paper-iv-comparison-citation-build-2026-10-05.json` records the actual official build, hashes and preservation checks. The pull request records final-head CI, visual inspection of the updated PDF, helper removal and post-merge validation. Build success checks the artifacts, not the mathematical correctness of the theorem. No release tag, deposit, visibility or repository-setting change is part of this revision.
