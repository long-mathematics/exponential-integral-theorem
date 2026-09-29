# Paper IV: separate repair proofs and second-pass audit

Date: 2026-09-29.

Audited repair-note head: `091655c6b95e33b4cce50e914b9c294e96aacce1`.
Frozen canonical baseline: `0bb151018dc73c9e48b847fff31fb82fd2cb9072`.
Audited repair-note source SHA-256: `9540c6757e6943ee3aef12ec734c96cf51dcc682444dd737486e6705d81174d6`.

This is a new audit record, not a replacement of the preceding ledger or verdict. Canonical Paper IV, the first standalone repair-note source/PDF, and the manifest are unchanged. PR #7 should remain draft and unmerged. This second-pass check is not independent human peer review.

## Outcome

The affine-line categorical replacements, fixed-part and lisse-extension arguments, semi-invariant argument, normalized-solution constant extension, and the abstract torsor/constant-field descent have explicit proofs under their stated interfaces. No counterexample to that abstract chain was found.

The audit found a further kernel-shift distinction that must be explicit, and a missing distinction between topological and moderate algebraic nearby cycles. It also strengthens the arithmetic rank-one conclusion from a dense affine open to the entire smooth quasi-projective base, with the prescribed finite Artin factor.

The complete operation-compatible algebraic de Rham realization over the geometric field, together with the matching Betti comparison, is NOT certified as an assembled interface by this audit. The conditional categorical implications must not be advertised as an unconditional audited application merely because that interface is labeled an external input. A heart-level kernel-comparison lemma below reduces part of the remaining work.

## 1. Further normalization correction

Let `K_lambda = (O, d - lambda dt)` be the exponential connection in the holonomic heart. Virk Section 6.6 defines the derived kernel by `L_lambda[1] = K_lambda`. Thus the kernel in the sheaf-compatible formula

`rho_lambda(QA) = p_!(A tensor mu^*L_lambda)`

is `L_lambda = K_lambda[-1]`.

For a graph `i_h:S -> S x A1`, projection formula and `p i_h = id` give the realization of `Q i_h,* 1_S[d]` as `1_S[d] tensor h^*L_lambda`, whose connection is `d - lambda dh`. The correct potential remains `h=f/lambda` for `E^f=(O,d-df)`.

There is an immediate unit countercheck: at a point and the zero graph, `i_0^*L_lambda=k` in degree zero, whereas `i_0^*K_lambda=k[1]`. Omitting the kernel shift changes the output degree. This is a convention correction to insert in the original repair note; its positive graph sign remains correct.

The normalized tensor is `(N star M)[-d]`, the normalized fiber is `i_s^*N[-d]`, and the tensor symmetry must be transported from the unshifted lisse category. Raw derived symmetry has an unwanted parity sign in odd base dimension. Fixed-scale duality also requires potential reflection because Verdier duality changes lambda to minus lambda. A rapid-decay direction should be fixed consistently, rather than suppressing the directional fiber functor.

Source: Virk, arXiv:2605.14904v4, Section 6.6, Proposition 6.8, Theorem 6.13; Snodgrass, arXiv:2608.06005, Definition 3.5 and Theorem 3.6.

## 2. Affine-line, fixed-part, and extension repairs

The actual unit `id -> R pi_* pi^*` is an isomorphism for `pi:X x A1 -> X`: its Betti realization is the affine-line homotopy isomorphism, and the cone is zero by conservativity. Consequently pullback is fully faithful in every derived degree.

This proves extension closure by lifting the connecting morphism of an extension. It proves the derived essential-image statement by induction on perverse truncation triangles, lifting their connecting morphisms by that same full faithfulness. No general claim that every Serre inclusion gives derived full faithfulness is needed.

Faithfulness on the quotient is proved by detecting zero quotient objects, then applying exactness to images of arbitrary quotient morphisms. One does not assume that an arbitrary quotient morphism lifts between prescribed representatives.

The fixed-part evaluation uses algebraic horizontal sections. Their independence over the constants implies independence over the function field: differentiate a shortest rational relation, normalize one coefficient, and use minimality to force all remaining coefficients to be constants. Thus the evaluation image is a trivial subconnection. Exact faithful realization reflects the constant-object isomorphism.

Lisse objects have no boundary-supported subobjects or quotients, so they are the intermediate extensions of their restrictions. Restriction is fully faithful on lisse objects. Extend an invertible lift and its inverse separately; their products restrict to the unit and remain lisse, hence are the unit on the whole base. This repairs the common-open issue without intersecting infinitely many opens.

These proofs pass as formal consequences of the specified operation-compatible realization. Their application still depends on that interface.

## 3. Fourier repair: do not identify different nearby-cycle functors without a bridge

The product representation of `pi_1(S) x Z` proves that a fixed nonzero fiber and the TOPological nearby-cycle local system have isomorphic underlying `pi_1(S)` representations. It does not by itself identify these with moderate algebraic D-module nearby cycles for an arbitrary irregular extension.

Countercheck outside the intended Fourier class: `E^(1/lambda)` has a trivial rank-one analytic local system on the punctured disc, but no regular formal summand at zero and zero moderate nearby cycles. Lissity away from zero therefore does not justify the algebraic nearby-cycle assertion.

For the intended class, insert Sabbah's regular-specialization input explicitly: Proposition 4.1(ii) includes strict specializability and regularity of the kernel along every finite Fourier scale, including zero. Use the regular-specialization comparison and proper-image compatibility before passing from topological fibers to the algebraic cycle object.

The upstream sequences, with `V=psi_(lambda,-1)(F T)` and `W=ker N_lambda`, are

`0 -> i_infinity,+ ker N_t' -> W -> T -> 0`,

`0 -> W -> V -> i_infinity,+ psi_(t',-1) T -> 0`.

Applying derived proper image gives two triangles. In any triangle `A -> B -> C ->`, each perverse cohomology of B is an extension of a quotient of that of A by a subobject of that of C. This yields the desired constituent containment without assuming exactness of proper image.

For the mixed case use the subquotient-closed REALIZED geometric category; do not assume arbitrary Hodge idempotents lift to motivic idempotents. Relevant locations: Sabbah, Monodromy at infinity and Fourier transform II, Proposition 4.1(ii), (5.21)-(5.22); Jacobsen-Terenzi arXiv:2509.21476v1, Corollary 5.15 and Proposition 5.17; Lam-Litt, published Lemma 3.5.

## 4. Strengthened global arithmetic theorem

**Theorem.** Let U over Qbar be smooth connected quasi-projective and L a rank-one algebraic integrable connection with finite Betti monodromy. Let A0 be the finite Artin connection with the same Betti character. Then on ALL of U,

`L is isomorphic to E^f tensor A0`, with `f in O(U)`,

and f is unique modulo constants for this fixed Artin factor.

**Proof.** Remove A0 and call the resulting trivial-monodromy connection L0. On a dense affine open V trivialize its line bundle and write `d+omega`. All periods of omega belong to `2 pi i Z`. The specified Tate-line argument using Huber-Wustholz Theorem 9.14 and the Picard 1-motive gives

`N omega = d log u + dF`, with u a regular unit and F regular on V.

Thus `L0|V = E^(-F/N) tensor A1`, where `A1=(O,d+(1/N)d log u)` has finite order. Both L0 and the exponential factor have trivial Betti monodromy, so A1 has trivial Betti character as well. A finite-order connection with trivial character is algebraically trivial (equivalently, use the trivial character on its finite etale Kummer cover). Hence `L0|V = E^f` for a rational function f on U.

At the generic point of any prime divisor of U, choose a regular frame of L0 and a uniformizer t. The rational isomorphism gives `alpha+d log g=-df` for a regular connection form alpha and a rational multiplier g. A logarithmic derivative has at most a simple normal pole. If f had a pole of order m>0, df would have a nonzero normal term of order m+1, at least two, in characteristic zero. This is impossible. Thus f has no divisorial poles in U and is regular by normality.

The rational horizontal isomorphism is now between two everywhere lisse line connections. Its multiplier has logarithmic derivative regular, so has valuation zero at every prime divisor. Normality extends this isomorphism and its inverse over U. Tensoring back A0 proves the assertion.

For uniqueness, an isomorphism between E^f and E^g gives `d(f-g)=+/-d log h` for a rational h. On a smooth proper compactification, the same pole-order argument excludes all poles of f-g. Hence f-g is constant. End of proof.

This proof eliminates the auxiliary denominator character after removing the original Betti character; that step would be unjustified without trivial monodromy of L0. It depends on the specified established 1-motive theorem, not on the desired relative functional-period theorem. It is a strengthening of the repair note, not a novelty/priority claim.

## 5. The remaining realization interface, narrowed by a proved lemma

**Kernel-comparison lemma.** Suppose a common geometric diagram has universal abelian hull A and supplied exact Betti and algebraic de Rham functors B and D. If their faithful complexifications agree naturally under regular Riemann-Hilbert, then `ker B=ker D`. D therefore descends to an exact faithful functor on `A/ker B`.

**Proof.** Vanishing of an object is reflected by faithful scalar extension. Complex comparison identifies the two vanishing conditions. Exact quotient factorization and zero-object detection give the result. End of proof.

This is a proved heart-level descent statement ONCE the algebraic diagram functor and natural comparison are supplied. It does not construct them from a complex Hodge realization. Compatibility of derived direct image, adjunction, tensor operations, and exponentiation needs the corresponding coherent geometric diagrams or a precise source theorem. That assembly over Qbar is the principal interface not certified by this audit. The published/perprint results of Ivorra-Morel, Terenzi, and Tubach cover substantial parts, but labeling the whole package an external input is not a proof of the package.

## 6. Abstract torsor and constant-field repair

With compatible fibers and the fixed-part/rank-one lifting hypotheses, take algebraic de Rham evaluation at a regular algebraic point s0. The ambient line lift may be outside the original category: after twisting, taking fixed parts, and tensoring back, its image is a subobject of the original object. Hence every differential semi-invariant space is motivic. The line-stabilizer argument gives normality and the exact quotient by the constant subcategory.

Define H_B over Qbar as the kernel of the Betti motivic group map to the constant group. Actual comparison c at s0 conjugates it over C to the differential group H_v. This group identification precedes period injectivity.

Normalize a fundamental solution Y by `Y(s0)=I`. Its multivariable Taylor coefficients are algebraic by the flat-system recursion. A finite collection of algebraic-coefficient series has the same constant relation space after scalar extension: the infinite coefficient rows span a finite-dimensional vector space, so finitely many rows suffice. Clearing rational-function denominators then proves

`R_k tensor_K C(S) = C(S)[Y,det(Y)^(-1)]`.

This is an actual injective base change, not an assumption that all complex differential subobjects were covered by the arithmetic argument. All base derivations are used.

Let A0 be the actual constant-comparison coordinate algebra, F0 its fraction field, `R0=K tensor_k A0`, and `K0=F0(S)`. Let B0 be the relative motivic comparison coordinate algebra. Geometric integrality embeds K0 in E=C(S); its common constants are F0. The exact group sequence makes B0 faithfully flat over R0 and an H_B-torsor algebra.

The actual comparison matrix is `P=Yc`, with c allowed outside F0. Over E its generated algebra equals that generated by Y. Under `Y -> Yh`, one has `P -> P(c^(-1)hc)`. This proves scheme-level equivariance of the evaluation map for the already identified H_B action. Evaluation is a closed immersion of two nonempty torsors under the same group, hence an isomorphism. Consequently

`B0 -> B0 tensor_R0 K0 -> B0 tensor_R0 E = R_E -> meromorphic germs`

is a sequence of injections. The first uses torsion-freeness and the second a field extension. No no-new-constants assertion over F0 is used at this point.

Set `R=B0 tensor_R0 K0` and `L=Frac(R)`. Differential simplicity descends from R_E by faithful flatness. Localizing the previous isomorphism at the nonzero elements of R gives an injection `L tensor_K0 E -> Frac(R_E)`. If b in L is horizontal, its analytic image is a complex constant a in E. Thus `b tensor 1=1 tensor a` in the tensor product itself. The elementary tensor-intersection lemma forces b in K0: otherwise an F-linear functional on the first factor killing 1 and taking b to 1 gives the contradiction 0=1. Since K0 has constants F0, b belongs to F0.

Therefore the actual period-generated fraction field has exactly the constants F0, and R is the claimed Picard-Vessiot algebra. The injection before the intersection lemma is indispensable: for `F=k(z)` and two copies of `F(sqrt(z))`, their multiplication map kills the nonzero tensor `sqrt(z) tensor 1 - 1 tensor sqrt(z)`.

The abstract torsor theorem is now proved under its named group and realization hypotheses. The main remaining application check is the realization interface in Section 5 of this report, not the flatness or tensor-intersection step.

## Separate proof memorandum and checks

A 15-page, 19-proposition/lemma/theorem/corollary memorandum was delivered as a separate conversation artifact, not as an integrated canonical manuscript:

- `paper-iv-separate-proofs-and-audit.tex`: SHA-256 `44eb23c0970d62106dacdfc8922592cadfdb59a7f76e694738ba8f950d3280f5`.
- `paper-iv-separate-proofs-and-audit.pdf`: SHA-256 `a3bde30c2b27e72c39c3ed69fca3d8f710e288f0b5cfc77e2cfb56f14abfbb5b`.
- `repair_checks.py`: SHA-256 `4fd2f92b1a4d18c208c9d036299ac8c356f20281dbc017c7ba9691d3466661e6`.
- `repair_checks.json`: SHA-256 `602292aa2e52bcc84ff5c4e725c4f57b563dea7aecf6c7924935240164f60fef`.

The new memorandum compiled locally without undefined references or overfull boxes. All 15 pages were rendered and inspected; text-bound checks found no content outside the page. Exact symbolic checks passed for 15 graph pullbacks, 3 noncommuting flat gauges, a finite relation matrix, divisorial pole orders 1 through 8, and the omitted-derivation/noninjective-tensor counterchecks. These mechanical checks do not certify the motivic interface.

Only this dated Markdown report is added to the draft branch in this pass. There is no source/PDF/manifest update to the canonical manuscript or to the first repair note, and no merge. The next integration decision must take account of the explicitly unverified realization interface rather than treating this audit as blanket clearance.
