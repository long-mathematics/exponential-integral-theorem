# Paper V: focused audit and substantive rewrite, 29 September 2026

## Inputs and verdict

Repository baseline: `0bb151018dc73c9e48b847fff31fb82fd2cb9072`, tree
`3f3095804f341bd68359d3e8d9606c45832d05e6`. Original Paper V source blob:
`5bb57fb3d46995e8e753bdc8eea6bdf102e8bf74`.

The new conversation proof was *Polynomial-Representative Boundary Systems
and Actual Comparison for an Elliptic Flag*, dated 29 September 2026.
Its construction, actual one-column criterion, and elliptic application
were audited separately. The old Paper V endpoint argument was not assumed.

**No fatal gap or counterexample was found in the new actual elliptic
comparison.** Several compressed interfaces required expansion, and the
rewrite limits the generic Fourier comparison to the explicitly displayed
Weyl presentation rather than claiming an unproved identification of all
middle-extension lattices. This is an adversarial mathematical review, not
independent peer review or a kernel-checked proof certificate.

The earlier Paper V audit identified genuinely false formulations. Those
formulations are replaced in this revision; they are not said to have
survived unchanged. Historical audit files remain untouched. In particular,
`paper-v-strengthening-audit.md` is a superseded historical verdict, not the
current status of the general endpoint theorem.

## 1. Actual density and monodromy

Let `f(x)=-x^3+3x`, `p(x)=-x^3+x^2+2x+1/4`, and let `c(t)` be the inverse
of `p` beginning in `(-1/5,0)`. The revision proves that `p'` is positive
on `[-1/5,1]`, that `c(2)` lies in `(4/5,1)`, and that the middle inverse
of `f` remains on its regular branch along the entire moving segment for
`0<t<2`. Writing the integral on the fixed interval `[-1,1]` proves
analyticity through the meeting of the two endpoints at `t=11/8`.
This is continuation of a density germ, not continuation of the supported
measure as a nonzero function outside its support.

The local calculation at `(1,0)` gives

    rho(t) = (1/(2 sqrt(3))) log(2-t) + O(1), as t -> 2 from below.

The reversed signed orientation is included. The nodal coordinates
`v=1-x`, `u=v sqrt(3-v)` give `q-2=y^2-u^2`. The local fiber is an annulus;
the endpoints and outer path are unramified and the variation is a nonzero
multiple of its core cycle. This justifies both the nonzero variation and
the fact that the vanishing period is fixed by that local monodromy.

A hypothetical rational linear boundary representation would make a
constant-coefficient differential operator applied to the density algebraic.
Finite monodromy of that algebraic germ would force the same operator to
annihilate the vanishing period. Its continuation towards the other node,
at `t=-2`, is unbounded: a positive integral on an interval has a uniform
lower bound `c integral_delta^b dv/v`. A nonzero constant-coefficient ODE
has entire solutions, giving the contradiction. This proves the nonzero
**actual** quotient needed by the field argument.

A separate numerical diagnostic converges to `1/(2 sqrt(3))`; it is recorded
as a diagnostic, not used as a proof.

## 2. Picard--Vessiot and boundary-field comparison

The coefficient module convention is now explicit: its basis has
`partial e_i=sum_j A_ij e_j`, so `e_i -> U_i mod N` is a differential map.
This is dual to the homogeneous solution representation and has the same
adjoint tensor module.

The proof that differentially finite elements of a Picard--Vessiot field
lie in the Picard--Vessiot ring is expanded using the finite translation
orbit and absence of an invariant polar locus on a torsor. The subsequent
tensor-category inclusion is made explicit using bounded monomials in a
fundamental matrix and inverse determinant. The source is Singer's locally
finite argument and tensor equivalence, not a claim that every meromorphic
function is a Picard--Vessiot tensor object.

The normal-subgroup argument now handles finite components explicitly.
If a normal subgroup's intersection with SL_n is finite central,
commutators with the connected SL_n are trivial, and the subgroup is
scalar. Thus a hidden finite noncentral projective subgroup cannot survive.

For the boundary system, its diagonal factors are a rank-two cubic module
and rank-one quadratic/endpoint modules. The kernel of the action on the
diagonal factors is unipotent. The reductive quotient has one simple
derived factor, detected by that cubic module. A projective quotient
isomorphic to the elliptic PGL_2 would have to agree, up to inner conjugacy,
with the cubic quotient. Agreement on the derived factor forces agreement
on the whole group because the centralizer of PGL_2 in itself is trivial.
The formal adjoint exponential differences are `+/-4` for the elliptic
system and `+/-28 sqrt(7)/27` for the cubic boundary system; they differ.
Rank-one endpoint twists do not alter this projective comparison.

The general actual-column criterion and the concrete functional independence
therefore survive. A further corollary is proved: the elliptic translation
kernel is all of Ga^2. A split nonzero homogeneous correction would be
meromorphic at zero, whereas its first Laurent exponent would have to equal
`-5/6` or `-7/6`, neither of which is an integer. The actual affine group
over the complex boundary field is consequently `Ga^2 semidirect SL_2`.

## 3. Specialization and actual coefficient fields

The five-coordinate boundary vector and the augmented seven-coordinate
system are explicitly closed. Their only possible finite pole is zero.
Beukers' Theorem 1.1 is applied to both systems, and Theorems 1.2--1.3 are
used for prescribed-relation lifting. A finite-linear-algebra scalar-descent
lemma records the passage from complex functional coefficients to algebraic
Taylor coefficients.

The theorem remains valid at **every nonzero algebraic parameter**, over
the value field of the three fixed faces, not the field of all compact line
periods. Polynomial reductions introduce only powers of z in denominators.
At a fixed parameter, algebraicity over the face-value field is equivalent
to specialized twisted polynomial exactness; the proof does not assume a
functional remainder cannot vanish at an isolated parameter.

The general replacement lemma proves `ker(ev_xi:R->C)=(z-xi)R` directly
for a finitely generated algebra of a closed nonsingular E-function vector.
It gives a boundary DVR without assuming global normality. Its residue
field is the boundary-value field. Numerical injectivity is stated only on
the specialized fiber algebra.

## 4. Substantive changes to Paper V

The title is intentionally changed to *Relative Exponential Periods on
Polynomial Flags: Polynomial Boundary Systems and an Elliptic Comparison
Theorem*. The manuscript date is intentionally advanced from August 2026
to September 2026. Authors, author order, Le Blanc identifier, and email
are unchanged. Stable repository filenames are unchanged.

The rewrite:

- installs the general polynomial-representative boundary construction;
- proves the actual one-column criterion and the complete explicit elliptic
  application, including the actual boundary matrices and polynomial
  certificates;
- retains single-phase observable geometry, face lattices, rooted
  Picard--Lefschetz, and the correctly separated rational/complex Hodge
  statements;
- states the disjoint-block result on a fixed common base with the required
  surjectivity and irreducibility hypotheses, rather than silently assuming
  preservation after an unspecified cover;
- removes the asserted automatic general completed compatibility and the
  unsupported general isotypic numerical/formal conclusion;
- replaces the unspecialized numerical algebra, global boundary-normal-form
  dependency, and arithmetic inference from punctual support;
- retains the abstract multicolumn orbit calculation and a unit-normalized
  local flat model in an appendix, explicitly requiring actual geometric
  realization when applied to a formal period category;
- replaces miracle flatness for determinants by an elementary monic-division
  proof of freeness;
- restricts the formal elliptic corollary to the stated localized boundary
  category, rather than inferring an unlocalized cancellation theorem.

The actual elliptic independence proofs do not depend on Paper III. Paper III
is used only to identify the already separated boundary relations with formal
compact-line operations. General multiphase, multiple-chain, and determinant
realizations remain separate hypotheses or future work, not solved by
terminology.

## 5. Reproducible validation and limits

`make test` includes a standard-library exact certificate engine. Its tests
check 121 monomials, the two displayed connection certificates, exactness of
sample primitives, linearity, safe parser rejection, and rational branch
inequalities. The certificate CLI handles rational-coefficient polynomial
amplitudes; the mathematical theorem covers all algebraic coefficients.

`scripts/check_paper_v.py` is a separate SymPy suite verifying 81 monomial
certificates, both top-form identities, both Gelfand--Leray identities, the
Fourier matrix comparison, scalar Bessel reduction, two boundary divisions,
critical-value scales, and 42 independently integrated Taylor identities.
It writes `.build/paper-v-exact-checks.json` and is not a replacement for
the analytic or Galois proofs.

Local TeX Live 2025/dev compiled all eight sources. A subsequent full local
`make check` stopped on the unchanged Paper IV snapshot: that toolchain
labels shared-counter references differently from the committed Ubuntu
build. Paper IV and its PDF were not edited to mask this environment
difference. The repository's Ubuntu 24.04 workflow is the authoritative
full snapshot check; its actual outcome is recorded in the pull request.

The build-and-merge record in the pull request reports the actual final
`make test`, `make pdf`, `make check`, hash, normal CI, and visual-review
results. Other manuscripts/PDF snapshots and historical provenance records
are to remain byte-for-byte unchanged. A successful check or compilation is
not a mathematical certification.

## Primary references checked

- F. Beukers, *A refined version of the Siegel--Shidlovskii theorem*,
  Ann. of Math. 163 (2006), Theorems 1.1--1.3.
- M. F. Singer, *Introduction to the Galois theory of linear differential
  equations*, arXiv:0712.4124v2, Example 1.3.32 (group classification only),
  proof of Proposition 1.3.33, and Theorem 1.5.2.
- C. Sabbah, *Hypergeometric periods for a tame polynomial*,
  arXiv:math/9805077, Proposition 9.1 and Remarks 9.4. Only generic
  finite-dimensionality is used without additional tameness hypotheses.

The homogeneous Bessel solutions themselves are not asserted to be entire
E-functions; that property is proved for the actual compact integrals.
