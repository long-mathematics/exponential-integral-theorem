# Papers V–VI: proof interfaces, applications, and candidate separation

Integration date: 10 October 2026 (UTC). Manuscript dates retain the repository's explicit month/year convention. Paper V keeps its September 2026 date and records the October revision; VI and the new candidates are dated October 2026.

## Baseline, authority, and preservation

Baseline main: `22d98c4f27e606b5b25fa673c33f9c56c53cc86b` (tree `a4abd16f1e6ce83b2d9d7ef6c2a3858fd348cabb`). The preceding canonical Paper V is archived verbatim in `notes/archives/2026-10-10-paper-v-before-two-level/`:

- Source SHA-256: `161726ecb44f8b06977c290638a594ddc77c169b5cf83e974e161efa23189e24`.
- PDF SHA-256: `bd92cb30c4d406b9246d56eff91217543c2c237d6028f33604e8aa937e088873`.

The canonical V filename is unchanged. The two-author order, Le Blanc identifier, contact, and printed title are preserved. Papers I–IV, their supplements, the structural companion, and existing historical provenance are not edited. Their eight unrelated committed PDF snapshots and manifest records are preserved byte-for-byte. The normal read-only LaTeX workflow is not changed.

The user authorized the mathematical revision, new VI and candidate drafts, README/scripts/PDF updates, and feature-branch pull-request publication. This record is a scoped AI-assisted audit and implementation account, not independent specialist refereeing, a formal proof certificate, or a priority claim. Retained Paper V geometry is invoked at its stated scope rather than claimed to have been re-proved independently here.

## 1. Linear span versus boundary field

The earlier conversational objection to removing (Q) and (F) concerned irreducibility after extension to a boundary field. It does not apply to the linear criterion now stated in V. The map is a differential map over `C(z)` into meromorphic functions modulo the finite **linear differential span** of the actual boundary coordinates. An irreducible source and a nonzero image imply injectivity. No boundary-field scalar extension is used.

Beukers' Theorem 3.2 (printed page 375) lifts every prescribed algebraic linear relation among a closed E-function vector at a nonsingular nonzero algebraic point. It allows redundant coordinates. Theorem 3.2 and Lemma 3.1 were checked in the published primary PDF, including the full-rank specialization of polynomial relation rows. Consequently the combined V boundary/interior vector, whose only possible finite pole is zero, gives the all-nonzero-algebraic-parameter linear theorem.

The amplitude conclusion is precisely membership in the boundary **span** iff the specialized twisted remainder is zero. A nonzero remainder is absolutely transcendental. It is not automatically transcendental over the generated boundary **field**. A zero remainder can have a nonzero boundary integral. These distinctions appear in the theorem, its proof, VI, and the README.

## 2. Positive-domain extremum detection

The detector is deliberately restricted to the usual positive area measure on a compact domain and to strict separation from every specified face image. For a minimum `c<d`, all genuine face functions on the ray `z=-s` are at most polynomial multiples of `exp(-ds)`, whereas an interior positive-area sublevel gives a lower bound of order `exp(-(c+epsilon)s)`.

First omit the artificially adjoined constant 1. This detects the irreducible interior module modulo the genuine boundary span. Restoring 1 adds a differential module of rank at most one, whose intersection with the irreducible interior image of rank at least two is zero. Thus the argument covers extremal critical value zero without a fictitious logarithmic singularity. It does not assert noncancellation for arbitrary signed or complex chains.

## 3. Finite root separation and its open locus

The large-group argument needs distinct ordered root weights `c_i-c_j`, not rational independence of all differences from one base value. V replaces (Q) by (R), while retaining (Q) as a sufficient test. The torus, reductivity, root-line decomposition, and Kummer finite-component arguments were checked with this weaker input. The group proposition is formulated for an irreducible system with entries in `C[z^{-1}]` and simple separated leading spectrum, so it also applies to the direct rank-three example.

The full weighted coefficient family has a nonempty Morse locus: separable univariate Morse phases and a finite avoidance of collisions suffice. On a finite étale critical-point label cover, coefficient variation gives `dc_i(h)=h(P_i)`. Quadratic test polynomials determine an unordered pair of points by its first and second moments, excluding an identically forced additive collision when both exponents are at least three. If one exponent is two, completing the square and a Vandermonde evaluation matrix give the same conclusion. This proves a nonempty Zariski-open (M),(R) locus in the **full** family. It does not prove real-chain observability to be Zariski open, and sparse separable families can fail (R) identically.

The exact rational quintic example verifies the strictness of the weakening: twelve ordered differences are distinct although the three base differences are rationally dependent.

## 4. Boundary disjointness and rank-three application

The intrinsic criterion remains `End^0(H_q)` outside the tensor category generated by the specified faces. The spectral (F) test is retained. A second sufficient test uses the existing reduction of a hypothetical adjoint occurrence to the endomorphisms of **one face's** semisimplified module. A face rank strictly below the interior rank makes the required embedding impossible. Merely comparing the total size of a boundary generating vector would not control its tensor category; that invalid shortcut is not used.

For `q=x^4+y^2+x`, all three literal Stokes certificates were recomputed. The rank-three system has the stated leading matrix and residues `-3/4,-1,-5/4`; every diagonal formal exponent at infinity is `-1`. An invariant rational line is represented by a primitive polynomial vector times `exp(cz)z^lambda`. Comparing zero and infinity forces degree zero and the middle residue line, which is not invariant under the leading matrix. The dual argument excludes a rank-one quotient. This proves irreducibility and then `SL_3`, independently of any inference about ordinary-fibre punctures.

The strict interior minimum on the displayed rational triangle is checked by exact edge inequalities. The quartic critical-value square-difference identity is computed from the Jacobian multiplication matrix. Its three nonzero boundary invariants, versus the zero interior invariant, exclude containment of the six distinct interior differences. Thus the new example supports the full fixed-boundary comparison, not a universal noncoprime theorem.

## 5. Paper VI: limits, normalizations, and arithmetic certificates

The radial limit is proved by exact multinomial/gamma coefficients and dominated summation. The block-radial limit uses gamma concentration near the unique maximum and estimates the **unnormalized** integrand on the complement, including the coordinate boundary. The compact-tail and infinite-tail estimates are explicit; no relative correction is divided by a vanishing top form there.

The odd-degree all-scale family uses an amplitude within V's standard remainder basis. Its absolute Jacobian is four and its slicing constant is `1/[2^{n-1}(n-3)!]`. The elliptic affine map has Jacobian two and slicing constant `1/[2(n-3)!]`. Independent exact simplex monomial moments check both normalizations through dimension nine and total amplitude degree three.

The characteristic-five quotient is an additive twisted quotient, not a quotient algebra. Multiplication by the fifth power of the barycentric form is legitimate because its derivatives vanish in characteristic five. Its exact two-by-two matrix has determinant two. The five initial vectors are checked directly and do not vanish simultaneously at any residue-field value. This proves the all-exponent result; the single algebraic scale `101i` works in every dimension.

Separately, the proved integer recurrence produces all 101 remainder pairs for exponents zero through 100. Exact polynomial gcd calculations give degree zero in each case; recurrence values are independently checked against direct monomial reductions through exponent twelve. This establishes the finite exception-free range through dimension 103, not uniform coprimality for every exponent. A parameter defeating the interior-remainder certificate need not make the integral itself zero.

The complex-parameter argument uses the ideal of all polynomial moment equations and the weak Nullstellensatz on explicitly localized parameter opens. It gives the FC conclusion, not a nonzero limiting period at every transcendental scale. Power closure preserves the angular phase and yields infinitely many nonzero moments. The theorem does not claim eventual nonvanishing for all complex scales or unrestricted FC(n).

## 6. Candidate drafts and excluded promotions

Two unnumbered drafts are explicitly selected by the build and linked in the README:

- `simplex-exponential-periods.tex`: E-function arithmetic/holonomic reductions, coefficient-conjugation argument, effective fixed-phase exceptional sets, the exact positive-amplitude counterexample, and precise open simplex/visibility targets.
- `multicolumn-exponential-periods.tex`: elementary rectangular/square orbit and joint-character ideals, a conditional local-contraction statement, and the missing actual chain/determinant/specialization requirements.

The simplex conjugation argument cites the proof of Beukers' Proposition 4.1 (printed page 377), not a claim that arbitrary field automorphisms commute with analytic integration. Adamczewski–Rivoal's Theorem 2 is used only for fixed-phase effective finite exceptional sets. Holonomic integration and the explicit arithmetic coefficient bounds establish the E-function input; no zero-only singular-locus claim is made for an arbitrary scalar annihilator.

The exact positive polynomial weight integrating to zero against `exp(5it)` obstructs arbitrary-positive-weight induction. It is not a counterexample to unweighted standard-simplex nonvanishing. The older quadratic/cubic triangle manuscript claims are not promoted from context summaries: their full source and relation-row/lattice arguments still need their own audit.

The multicolumn draft does not restore the withdrawn unrestricted endpoint-complete theorem. An abstract orbit calculation is not given an actual geometric realization by terminology. The candidates are not assigned Papers VII/VIII.

## 7. Primary-source checks

- F. Beukers, *A refined version of the Siegel–Shidlovskii theorem*, Ann. of Math. 163 (2006), 369–379: Theorem 1.1 for transcendence degrees; Lemma 3.1 and Theorem 3.2 for prescribed linear lifting; proof of Proposition 4.1 for coefficient-conjugate zeros. [Published PDF](https://annals.math.princeton.edu/wp-content/uploads/annals-v163-n1-p08.pdf).
- B. Adamczewski and T. Rivoal, *Exceptional values of E-functions at algebraic points*, Bull. Lond. Math. Soc. 50 (2018), 697–708, Theorem 2. [Author PDF](https://adamczewski.perso.math.cnrs.fr/E-functions.pdf).
- D. Zeilberger, *A holonomic systems approach to special functions identities*, J. Comput. Appl. Math. 32 (1990), 321–368: holonomic definite integration. [Author-hosted PDF](https://sites.math.rutgers.edu/~zeilberg/mamarimY/Zeilberger_y1991_p321.pdf).
- E. Edo and A. van den Essen, *The Strong Factorial Conjecture*, arXiv:1304.3956, used for the conjecture's formulation and distinction from the stronger consecutive-moment question. [Preprint](https://arxiv.org/abs/1304.3956).

## 8. Reproducibility and publication gate

Run:

```sh
make test
python3 scripts/check_comparison_factorial.py --max-k 100
python3 scripts/check_paper_v.py
make pdf
make check
```

The new checker uses exact symbolic/rational arithmetic; no numerical quadrature or probabilistic polynomial equality tests are used. It does not certify monodromy, analytic continuation, differential Galois arguments, or Beukers' theorem. The test suite retains all previous tests and adds archive preservation, new source/status checks, exact rank-three/characteristic-five/gcd checks, and simplex/radial regressions.

All managed PDFs must compile, match their manifest, have no undefined references/citations or overfull boxes, and have their changed pages visually reviewed. The final ordinary read-only PR check must pass on the exact cleaned head before the authorized squash merge. Temporary preparation helpers and workflow files must be removed. Final build hashes, page counts, test outcomes, and any environment caveats are recorded in the paired build-verification file and PR discussion; a successful build is not a mathematical certification.

### Local validation before the Ubuntu publication build

The local run passed **22 test methods**, the standalone all-exponent/101-gcd exact suite, and the broader elliptic certificate suite. All **12 managed documents** compiled and passed a self-consistent manifest/text check. V has 28 pages, VI 11, the simplex candidate 5, and the multicolumn candidate 4; these four final logs have no overfull/underfull boxes or undefined references/citations. Their fonts are embedded. Every new/changed PDF page was rendered and inspected in contact sheets, with core proof/formula pages also inspected at full-page scale.

After restoring the eight unrelated committed PDFs and their manifest records, the local full snapshot check reaches the unchanged structural companion and reports its known TeX-version text/reference discrepancy. No unrelated source or snapshot is changed to hide this. The final Ubuntu 24.04 build and read-only PR workflow are the authoritative preserved-snapshot gate, and their actual outcomes belong in the final build record and PR discussion.
