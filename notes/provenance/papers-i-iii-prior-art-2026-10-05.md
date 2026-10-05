# Papers I–III: prior-art and citation revision, 5 October 2026

## Scope and baseline

The source baseline is main commit
`3b587fdfde4992e19745302da1c8e6ec4f9326c0`.
This is a focused citation-to-claim and overlap check prompted by the supplied
prior-art handoff and its source documents, not a new full proof audit or an
independent peer review. The revision changes the introductions and references
of Papers I–III, a proof-lineage paragraph immediately before Paper I's
semisimplicity proposition, and the quadratic comparison in Paper III's
supplement. It does not change existing theorem statements, hypotheses,
proof bodies, abstracts, labels, author lists, or manuscript dates.

Paper III's supplement is included because it gives a standalone treatment of
the quadratic model discussed in the newly cited lecture. Paper II's supplement,
Papers IV–V, their repair material, the structural companion, historical audit
records, README, and build configuration are outside this revision. Only the four
corresponding PDF snapshots and their manifest records are refreshed.

## Sources checked and use of each citation

| Source | Passage checked | Use in the revision |
| --- | --- | --- |
| Fresán–Jossen, *Exponential motives*, supplied 301-page preliminary manuscript | Chapter 1 (relative data); Sections 12.5–12.7, especially Proposition 12.7.2 and paragraph 12.7.3 | General relative framework; compact-loop E-functions and the differential-system construction. The bibliography identifies the consulted draft, not a published edition. |
| Jossen, *Special values of E-functions as exponential periods*, May 2018, 11 pages | Sections 2–3, especially Theorem 3.2 | Polynomial-phase deformation, noncompact rapid-decay periods, and the already stated polynomial-relation lifting principle. Historical attribution, not an additional proof input. |
| Fresán–Jossen, *A non-hypergeometric E-function*, Annals of Mathematics 194 (2021), 903–942 | Introduction and Section 5, especially Proposition 5.1; checked against arXiv:2012.11005v2 | Published antecedent for the homogeneous polynomial-phase Fourier–Laplace construction, not merely terminology. |
| Jossen, *Examples around the exponential period conjecture*, CIRM, recorded 20 February 2025 | Supplied transcript: opening attribution; second example and closing arithmetic discussion; official recording metadata | The quadratic marked-point predecessor, presented as joint work in progress with Fresán. It is cited as a recorded lecture, not as a refereed theorem. |
| Delaygue, *A Lindemann–Weierstrass theorem for E-functions*, arXiv:2210.12046v2 / J. Reine Angew. Math. 820 (2025) | Theorems 1.2 and 1.4 | Existing linear-independence comparison retained. No new claim that this linear theorem by itself gives arbitrary algebraic independence. |
| Fischler–Rivoal, *On Siegel's problem for E-functions*, supplied version of 28 April 2022 | Introduction and Section 2 | Considered but not added: peripheral to the present value-rigidity and formal-period claims. |

Stable public locators:

- Jossen 2018: [official Simons meeting page](https://www.simonsfoundation.org/event/periods-and-l-values-of-motives-2018/), linking the [lecture report](https://simonsfoundation.s3.amazonaws.com/share/mps/symposia/2018/pdf/palvom/Report_Jossen.pdf).
- Jossen 2025: [CIRM recording](https://www.carmin.tv/en/video/examples-around-the-exponential-period-conjecture), DOI [10.24350/CIRM.V.20308403](https://doi.org/10.24350/CIRM.V.20308403). The recording date is 20 February; the page's publication date is 7 March 2025.
- Fresán–Jossen 2021: DOI [10.4007/annals.2021.194.3.7](https://doi.org/10.4007/annals.2021.194.3.7), [arXiv v2 full text](https://arxiv.org/html/2012.11005v2).
- Fresán–Jossen book: [author-hosted manuscript locator](http://javier.fresan.perso.math.cnrs.fr/expmot.pdf); the actual text checked was the supplied 301-page PDF. A PDF metadata timestamp is not treated as a publication date.
- Delaygue: [arXiv v2 full text](https://arxiv.org/html/2210.12046v2).

## Corrections to the preliminary overlap assessment

The handoff's description of the 2021 Fresán–Jossen paper as relevant only for
terminology was too narrow: Proposition 5.1 is substantive prior art for the
homogeneous connection. The revised papers cite it accordingly. The all-polynomial
relative arithmetic and relation-classification statements, not the existence of
that Fourier construction, are the contributions emphasized here.

Jossen's 2018 Theorem 3.2 already states lifting of polynomial relations, rather
than only a transcendence-degree equality. The revision does not contrast an
allegedly weaker old specialization theorem with a newly introduced lifting step.

The relative motive framework already permits marked algebraic boundary data.
Likewise, boundary forcing is already present in the quadratic example. The
revision therefore does not claim to introduce relative data or boundary terms.
It distinguishes the uniform arithmetic treatment and formal realization from
the pre-existing construction and examples.

The supplied lecture transcript is automated and visibly imperfect. In
particular, a statement about equal unipotent coordinates must not be copied as
an equality of the unnormalized integrals at opposite endpoints. The manuscript
comparison uses the explicit integral substitution below. No precise matrix
coordinate formula is attributed to the transcript.

The lecturer's comment about more complicated varieties is not evidence that he
attempted and failed to treat arbitrary polynomial phase on the same affine line;
no such claim or quotation has been added.

The optional broad remark on Siegel's problem was not adopted. Its general
negative solution is already the subject of Fresán–Jossen 2021; the present pass
does not settle or formulate a classification of which compact-boundary families
are hypergeometrically generated. The optional generic Gabber–Katz remark was
also omitted: its exact original hypotheses were not verified here, and it is
not needed for this attribution repair or any proof.

## Quadratic normalization and consistency check

Write

\[
F_a(z)=\int_0^a e^{-zx^2}\,dx,
\qquad H_\beta(z)=\int_0^1 e^{\beta z x^2}\,dx.
\]

Then `F_0 = 0`, and substitution gives `F_a = a H_{-a^2}` for nonzero `a`.
Thus `F_{-a} = -F_a`; normalized integrals `F_a/a` coincide when their nonzero
squares coincide. If `r` is the rational rank of the squares of the marked
points and `m` is the number of distinct nonzero squares, the unchanged quadratic
value-independence and Lindemann–Weierstrass theorems in the supplement give

\[
\operatorname{trdeg}_{\overline{\mathbb Q}}
\overline{\mathbb Q}(e^{-a_i^2},F_{a_i}(1):i)=r+m.
\]

The new unnumbered comparison paragraph records this consequence explicitly.
There is no added assertion that adjoining `sqrt(pi)` increases this degree.
This is a consistency check against the compact part of the lecture's example,
not independent evidence for the general theorem of Paper III.

For constant-coefficient functional relations, grouping the Taylor coefficients
by the distinct nonzero squares gives a Vandermonde matrix. Consequently a
relation `sum d_i F_{a_i}=0` requires and is implied by
`sum_{a_i^2=c} d_i a_i=0` for each nonzero square `c`. This independently checks
the sign convention and the count of normalized quadratic directions.

## Validation and boundaries

The local editorial check compares every existing proof, theorem, lemma,
proposition, corollary, definition, and abstract body with the baseline and finds
no changes. Labels and manuscript dates are unchanged. All bibliography entries
in the four edited documents are cited; all citation keys resolve, with no
duplicate bibliography keys.

The 11 repository unit tests passed, and `make pdf` compiled all nine documents
without fatal LaTeX diagnostics. The local `make check`, after restoring unrelated
snapshots, exposed a TeX-distribution-dependent cleveref difference in the
unchanged structural companion (some cross-reference names rendered as
"Theorem" instead of "Lemma" or "Proposition"). That source and PDF are deliberately
not changed here. The final committed snapshots are to be built and verified in
the repository's Ubuntu 24.04 environment; the pull request records its build,
full `make check`, and visual-review results.

This pass does not establish absolute priority against unpublished work, and no
communication with Fresán or Jossen is claimed. It adds no new external theorem
as a dependency. Paper IV's separate repair status is neither reassessed nor
changed.

## Fingerprints of supplied source copies

SHA-256:

```text
Report_Jossen.pdf
5cb6fb4c966c8d81b296d9b5328834bf970c911e3cdccc754d734dac5d545f2c
expmot.pdf
7da885c162606b3c7a2b377d532e59097e51a6856c7f9ba75071d559d2e5ebf5
probsiegel.pdf
0269211e7ef37d349f3ca2069428bef516faacda7bd2d81d610b7be559a67ad6
supplied CIRM transcript
671dd638f059f074350cc50596612d0529c60451512154779c92125976e9b968
```
