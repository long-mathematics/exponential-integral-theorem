# Full-pass audit of the streamlined EIT Paper I

## Scope

This audit covered the complete 699-line streamlined draft
`algebraic_exponential_integrals_streamlined.tex`, the rendered nine-page PDF,
and the relevant recent literature.  The proof was checked in the order in
which its dependencies actually run:

1. the moment differential system and the arithmetic growth of its Taylor
   coefficients;
2. Beukers lifting;
3. semisimplicity of the homogeneous Fourier--Laplace connection;
4. rational horizontal-endomorphism rigidity;
5. constant splitting of relation submodules;
6. algebraic value implies exponential polynomial;
7. constant-coefficient annihilation;
8. Cauchy-transform rigidity and the edge-density criterion;
9. the main theorem, relation transfer, and regular-value independence.

The revision produced by this audit is
`algebraic_exponential_integrals_streamlined_audited.tex` and its compiled
PDF.  The revised paper is thirteen pages.  The four-page increase is almost
entirely load-bearing: an explicit denominator certificate, a complete
Fourier--Laplace identification, the localization argument, and the exact
geometric relation theorem that the short draft had only used implicitly.

## Overall verdict

I found no fatal mathematical gap in the proof architecture.  The main
argument survives a slow reconstruction, including degenerate critical
points and coincident critical values.  The previous nine-page version was,
however, too compressed at its two most delicate interfaces:

- the assertion that the homogeneous connection is semisimple; and
- the arithmetic verification that the moments are E-functions.

There was also one literal notation error: the vector `b_0` was used in the
restricted system although it had only been defined for endpoint values.
That is now fixed by using a single set

\[
  \Lambda=\{0\}\cup q(\operatorname{supp}\Delta)
\]

and defining `b_lambda` by an empty-sum convention for every
`lambda in Lambda`.

The revised proof is substantially more audit-ready.  It still uses serious
standard machinery (Riemann--Hilbert, the small-map/decomposition theorem,
and algebraic Fourier--Laplace transformation), so independent checking by a
specialist in D-modules remains advisable.  That is a residual verification
risk, not a currently identified contradiction.

## Corrections and improvements made

### 1. The algebraic parameter remains absorbed in the main theorem

The main theorem is stated only at `z=1`.  For an algebraic
`xi != 0`, one has

\[
  I_{\xi q,\Delta}(z)=I_{q,\Delta}(\xi z),
\]

so no separate theorem parameter is needed.  To preserve the strongest
usable form without cluttering the proof, a corollary now records that every
nonzero `I_{q,Delta}` is purely transcendental and has no nonzero algebraic
zero.  The single-integral and regular-value corollaries may therefore state
the familiar arbitrary-`xi` versions without reintroducing `xi` into the
proof machinery.

### 2. The E-function height argument is now explicit

The earlier statement that a common denominator divides
`B^(m+1) lcm(1,...,nm+j+1)` was plausible but insufficiently demonstrated.
The revised proof fixes one number field and an integer `d` clearing all
input denominators, and uses the concrete common denominator

\[
  \delta_m=d^{(n+1)m+j+2}
  \operatorname{lcm}(1,\ldots,nm+j+1).
\]

For every `ell <= m`, the exact coefficient formula shows that
`delta_m u_{j,ell}` is integral.  Together with a uniform archimedean bound
and `log lcm(1,...,N)=O(N)`, this proves the required joint-height estimate
rather than merely asserting it.

### 3. Semisimplicity is separated from endomorphism rigidity

The former single “constant splitting” proposition bundled three logically
different facts.  They are now split into:

- semisimplicity of the homogeneous moment connection;
- rational horizontal-endomorphism rigidity;
- constant splitting as a short corollary of the first two.

This makes the dependency transparent.  In particular, endomorphism
rigidity alone does not imply that every submodule splits.

### 4. The Fourier--Laplace passage is now derived, not asserted

The revised semisimplicity proof includes:

- the permutation local system over the complement of the critical values;
- Maschke semisimplicity and the trace splitting;
- the small-map identity `Rq_* C[1] = IC(L)`;
- Riemann--Hilbert and proper direct image;
- exact Fourier transformation;
- a proof that every nonzero generic localization of a simple Weyl module is
  irreducible;
- the graph-module equations;
- the relative de Rham complex;
- injectivity of its degree `-1 -> 0` differential by degree comparison;
- the pullback `tau=-z` and the resulting signs;
- identification of the matrix `mathsf C + mathsf D/z` and its dual period
  system.

Sabbah is now cited for the algebraic Fourier--Laplace convention and
direct-image model.  The sign check is internally consistent: the twisted
module corresponds to `e^{-zq}`, and the integrals with `e^{zq}` are
horizontal sections of its dual.

### 5. The local-spectrum proof is retained and clarified

For a critical point `tau` with multiplicity `m_tau`, the basis

\[
  g_{\tau,k}=\frac{q'}{(x-\tau)^k},
  \qquad 1\le k\le m_\tau,
\]

is the Chinese-remainder basis of `C[x]/(q')`.  Multiplication by `q` is
scalar on each local factor because `q-q(tau)` vanishes to order
`m_tau+1`.  The compression of `mathsf D` has diagonal

\[
  -\frac{m_\tau}{m_\tau+1},\ldots,-\frac1{m_\tau+1}.
\]

The no-cross-term assertion for distinct critical points over one critical
value is explicitly justified by the order of vanishing of

\[
  -\left(\frac{q-q(\tau)}{(x-\tau)^k}\right)'.
\]

This handles both degenerate critical points and coincident critical values.

### 6. The exponential-polynomial coefficients are algebraic

The short draft concluded only `p_lambda in C[z]`.  Uniqueness of the
expansion over `C(z)` and Galois descent strengthen this to

\[
  p_\lambda\in\overline{\mathbb Q}[z].
\]

This is a genuine strengthening at no conceptual cost.

### 7. The Cauchy-transform result is stated at its actual strength

The old draft used, but did not formally state, the fact that every edge
density vanishes.  The revision separates a tree-representation lemma and a
theorem proving

\[
  I_{q,\Delta}\equiv0
  \quad\Longleftrightarrow\quad
  \psi_e\equiv0\quad\text{for every open edge }e.
\]

The local jump calculation is written out using logarithms rather than
citing Sokhotski--Plemelj as a black box.  This avoids hidden regularity
assumptions at ramified endpoints and makes clear that the jump is evaluated
only on compact interior subarcs where the density is holomorphic.

### 8. The relation theorem is correctly demoted to a corollary and
strengthened geometrically

Transfer of constant linear relations is a formal consequence of the main
rigidity theorem, so it is now a corollary rather than an independent
headline theorem.  A second corollary gives the exact relation space:
for graph representatives on one common tree,

\[
  a_0+\sum_j a_j I_j(1)=0
\]

if and only if `a_0=0` and

\[
  \sum_j a_j\psi_{j,e}\equiv0
\]

on every open edge.  This is the clean geometric classification already
latent in the proof.

### 9. The linear case is rewritten around the actual primitive

The proof now first records

\[
  I_{q,\Delta}(z)=\frac1{az}
  \sum_\alpha d_\alpha e^{zq(\alpha)}
  \qquad(q(x)=ax+b),
\]

then applies Lindemann--Weierstrass.  The possible collision with the
adjoined `e^0` term is handled explicitly before using the degree-zero
condition.

### 10. Literature positioning and bibliography are corrected

The revision now distinguishes the uniform theorem from:

- Adamczewski--Rivoal’s algorithm for one fixed E-function;
- Bostan--Rivoal--Salvy’s effective minimal-equation/canonical-decomposition
  machinery;
- Delaygue’s singularity-separation criterion;
- the classical hypergeometric monomial subfamily.

The Commelin--Habegger--Huber citation is corrected to arXiv v4 (28 March
2025), to appear in *Annales de l’Institut Fourier*.  The previous
“version of August 11, 2026” entry was unsupported.

## Section-by-section correctness audit

### Definition and path independence: passed

For each fixed `z`, `e^{zq(x)} dx` is an entire one-form on the simply
connected plane, hence exact.  The integral depends only on the boundary
zero-cycle.  Entire dependence on `z` follows from compactness of a chosen
finite chain.

### Residue spectrum: passed

No affine normalization of `q` is needed.  Euclidean division gives
`h_j=x^{j+1}/n+O(x^j)` for every degree-`n` polynomial, so the diagonal of
`D` is `-(j+1)/n`.  The entries are distinct, hence `D` is diagonalizable,
which also validates the use of the spectrum of `ad D` at `z=0`.

### Moment system: passed

The integration-by-parts sign and transpose conventions were checked
independently.  In the algebraic twisted module,

\[
  [q x^j]=[r_j]-\frac1z[h_j'],
\]

whereas the moment column is a horizontal section of the dual, hence the
coefficient matrix is the transpose.

### E-function verification: passed after expansion

Algebraicity, exponential conjugate growth, common denominators, and a
scalar differential equation are all now explicit.  The linear case is
covered separately by the closed formula.

### Beukers lifting: passed

The enlarged vector consists of E-functions and satisfies a homogeneous
system with only a finite pole at `z=0`; therefore `z=1` is an admissible
specialization point.  The linear lifting statement used in the paper is a
direct degree-one specialization of Beukers’ full homogeneous-polynomial
theorem.

### Semisimplicity: passed in outline and substantially strengthened

Every step now has either a proof or an appropriate standard reference.
The main residual risk is conventional rather than conceptual: a D-module
specialist should confirm the precise cohomological/direct-image convention.
The explicit graph calculation removes most of the former ambiguity.

### Endomorphism rigidity: passed

Finite poles are excluded by order comparison.  At zero, the spectrum of
`ad D` lies in `(-1,1)`.  At infinity, the first two polynomial
coefficients, the critical-point basis, and the compressed local spectrum
exclude positive degree.  The argument does not assume simple critical
points or distinct critical values.

### Constant splitting: passed

Semisimplicity supplies a horizontal projector; endomorphism rigidity makes
it constant.  This is exactly where semisimplicity is used.

### Algebraic value to exponential polynomial: passed

The relation rows form a differential submodule.  Constant splitting turns
the value of the lifted polynomial row at `1` into membership of the
constant coordinate row.  Residue nonresonance at zero removes poles from
the rational exponential coefficients.  Galois descent gives algebraic
polynomial coefficients.

### Annihilation and moments: passed

The operator

\[
  \prod_{\lambda\in\Lambda}(\partial_z-\lambda)^N
\]

annihilates every `p_lambda(z)e^{lambda z}` when `N` exceeds all polynomial
degrees, and differentiation under the integral replaces `partial_z` by
multiplication by `q(x)`.  The resulting polynomial `H` is nonzero.

### Cauchy transform and edge densities: passed

The moment expansion is uniformly convergent for large `s`; the complement
of a finite embedded tree is connected; the inverse-branch densities have
integrable ramification singularities; and the local logarithmic jump forces
all densities to vanish away from the finite zero set of `H`, hence
everywhere by analyticity.

### Main theorem and corollaries: passed

The linear and nonlinear cases cover all nonconstant polynomials.  The
single-interval function is nonzero because its value at `z=0` is `B-A`.
The regular-value independence proof correctly isolates one terminal lift
for each support point.

## Symbolic stress tests

The residue matrices and polynomial horizontal-endomorphism equations were
checked symbolically for:

- `q=x^3-3x`;
- `q=x^4` (one degenerate critical point);
- `q=(x^2-1)^2` (coincident critical values);
- `q=x^5-5x^3+4x`;
- `q=7x^4+3x^3-2x+5` (unnormalized).

In every case:

- the residue spectrum was exactly
  `{-1/n,...,-(n-1)/n}`; and
- polynomial horizontal endomorphisms through degree three had the same
  dimension as the constant centralizer `Z(C) intersect Z(D)`.

These calculations are consistency checks, not substitutes for the proof.
The script is included in the audit bundle.

## Assessment of Claude’s comments

### “The mathematics looks sound” — agree, with a qualification

The full proof chain is coherent and survived this audit.  The qualification
is that the former semisimplicity paragraph was not publication-grade; it
was a compressed proof sketch.  The revised version repairs that.  I would
still seek an independent D-module audit before submission.

### “The headline corollary appears new in this generality” — plausible,
not certified

The literature search found the fixed-function algorithms, Delaygue’s
separation theorem, and classical hypergeometric subfamilies, but no exact
uniform theorem for arbitrary polynomial `q` and arbitrary algebraic
zero-cycles.  A finite search cannot certify novelty.  The paper should say
precisely how it differs from known results rather than claim an exhaustive
priority result.

### “This is an application-plus-rigidity paper, not a methodological
breakthrough” — partly subjective

The description “application-plus-rigidity” is fair as positioning.  The
constant-horizontal-endomorphism theorem and its use to make every relation
submodule constant are structural, not merely an application.  Journal-rank
predictions such as “not Annals territory” are opinions, not audit findings.

### “The real contribution is rational horizontal-endomorphism rigidity” —
mostly agree

This is the most distinctive load-bearing structural statement in the
proof.  The local-spectrum argument is explicit, robust under degeneracies,
and reusable.  The hybrid use of semisimple splitting, Beukers lifting, and
Cauchy rigidity is also part of the contribution.  I cannot certify from the
search that the endomorphism theorem has no precursor in a different
language.

### “The H-twisted Cauchy result is a legitimate small extension” — agree

The Cauchy machinery is close to the polynomial moment literature.  Its
precise role here, with the annihilator-produced factor `H` and the
exponential conclusion, is useful but should not be oversold as the main
novelty.

### “The transfer theorem is a formal consequence of Beukers” — disagree

It is a formal consequence of the paper’s algebraic-value rigidity theorem,
so it should indeed be a corollary.  It is **not** a formal consequence of
Beukers alone.  Beukers lifts a constant relation at `z=1` to a
**polynomial-coefficient** functional relation.  The paper’s
semisimplicity-plus-endomorphism-rigidity argument is what converts the
relevant relation submodule into a constant subspace.  Without that step,
one cannot conclude that the original constant coefficients give a
functional relation.

### Adamczewski--Rivoal and Bostan--Rivoal--Salvy overlap — agree

For each fixed explicit E-function, their work makes exceptional algebraic
values algorithmically decidable.  The present theorem is valuable because
it proves uniformly, for an infinite geometric family, that the exceptional
set is empty unless the function vanishes identically.  The revised
introduction now says this explicitly.

### Delaygue comparison — agree in substance, correct some details

Delaygue’s main separation result is Theorem 1.2 in the current version; the
sine-integral application is Proposition 4.4 in Section 4.3.  It requires
pairwise disjoint finite singularity sets for the associated G-series and
transcendence of the individual values.  The fixed-`q` family in this paper
is organized by one common moment connection and need not satisfy such a
separation hypothesis.  The comparison belongs in the introduction and is
now included.

### “The monomial case is classical” — agree, with qualification

The identity with `1F1` places the basic monomial integral from `0` to `A`
in the classical hypergeometric setting.  This is an important overlap to
acknowledge.  It does not cover arbitrary polynomial `q`, arbitrary
zero-cycles, or the exact fixed-`q` relation space.  The revised paper states
the overlap without suggesting that the full theorem was previously known.

### “Semisimplicity is the weakest link” — strongly agree

This was the thinnest passage in the short draft.  It is now expanded and
cited carefully.  Claude’s proposed alternative using a full-rank matrix in
Hermite form is an interesting research direction, but it is not presently
a proof.  The equation

\[
  R'+R(C+D/z)=GR
\]

contains an unknown gauge matrix `G`; the pole and degree comparison for a
horizontal endomorphism does not automatically force the rational row space
of `R` to be constant.  Eliminating semisimplicity would require a new
projective/Grassmannian rigidity theorem.  It should not replace the valid
semisimplicity argument until that theorem is proved.

### The `b_0` notation issue — agree

It was a real defect, though minor and easily repaired.  The revision defines
all `b_lambda` on a single set `Lambda`.

### “The linear paragraph is awkward” — agree

The revision displays the primitive formula first and then gives a short
Lindemann--Weierstrass coefficient argument.

### The Commelin--Habegger--Huber citation — agree

The verifiable current record is arXiv:2007.08280v4, last revised 28 March
2025, to appear in *Annales de l’Institut Fourier*.  The draft’s future-dated
version entry has been removed.

### Pure transcendence and no algebraic zeros — agree

Both are immediate, standardly worded consequences and materially sharpen
the presentation.  They are now stated together in a corollary.  “Purely
transcendental” is the terminology used by Delaygue for an E-function with
no nonzero algebraic argument giving an algebraic value.

### Exact geometric determination of linear relations — agree, but avoid a
stronger claim

The edge-density criterion gives a complete and exact description of the
linear relation space for a fixed polynomial `q`.  This is now a named
corollary.  The paper does **not** yet derive a closed compositional or
second-Ritt classification of all vanishing densities, so it should not
claim that stronger classification without additional work.

## Remaining recommendations before submission

1. Obtain an independent expert check of Proposition 3.1, especially the
   direct-image convention and the identification of the generic
   Fourier--Laplace module.
2. Verify the novelty statement through MathSciNet/zbMATH and direct searches
   under “exponential period functions,” “purely transcendental E-functions,”
   “polynomial exponential integrals,” and Fourier transforms of polynomial
   direct images.
3. Decide whether the exact edge-density relation corollary should be
   promoted in the title or abstract.  It gives the paper a stronger
   classification emphasis than the single-integral corollary alone.
4. Keep the structural companion separate.  Multiplicity-free decomposition,
   the full endomorphism algebra, algorithmic questions, and generalization to
   finite maps of curves are useful research tools but are not needed in this
   base paper.

