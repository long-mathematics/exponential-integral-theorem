# Independent audit — 6 October 2026

## Target and verdict

The target is the last of the three uploaded candidate revisions, containing the direct formal diagonalization, diagonal local Picard–Vessiot subgroup/Kummer argument, and intrinsic exponent definition. See README.md for exact identities and the single indentation-byte difference in the repository serialization. Canonical Paper V is unchanged.

The three requested geometric source checks pass. The latest direct formal-diagonalization proof, required-torus inclusion, and Kummer component argument are sound. The intrinsic exponent argument is sound under the coefficient-module/contravariant-solution convention of Paper V; that convention should be explicit in the note. No false principal theorem or unrepairable proof step was found.

The supplied `proof-clarifications.tex` expands the geometric interfaces and proves a simpler stable-lattice replacement for the face-exponent argument. This replacement removes even the remaining general formal-normal-form citation. It is separate from the frozen source and does not silently revise it.

## Broughton

Source: S. A. Broughton, *Milnor numbers and the topology of polynomial hypersurfaces*, Invent. Math. 92 (1988), 217–241. The uploaded whole-volume scan was inspected directly at the relevant pages; its indexed text is largely page placeholders. Printed page p is PDF page p+7, one-based.

- Definition 3.1, p.225: gradient norm bounded away from zero outside a compact neighborhood of the critical points.
- Theorem 1.2, p.219: a tame fibre has the homotopy type of a bouquet of mu−mu^c spheres of the fibre's complex dimension.
- The proof on p.231 explicitly gives H_1(F_c;Z)=Z^(mu−mu^c) for curves. A regular fibre has rank mu.
- The bounded horizontal-vector-field construction on pp.229–230 supplies the fibration statement. It is unnumbered, but it is justified by the adjoining construction, not merely asserted without argument.
- Proposition 3.4 is on p.228. Convenience and nondegeneracy with respect to the Newton boundary at infinity imply tameness; the definition of that Newton boundary is on p.227.

The candidate's weighted estimate is valid. With R=max(|x|^(1/b),|y|^(1/a)), normalized coordinates X=x/R^b,Y=y/R^a, at least one of a alpha X^(a−1), b beta Y^(b−1) is uniformly bounded away from zero. The lower-weight terms are uniformly negligible after the indicated componentwise rescaling. Thus the gradient norm tends to infinity, stronger than the cited definition. The normal-form lemma identifies the total Milnor number with (a−1)(b−1).

## Gabrielov, Lazzeri, and connectedness

Gabrielov's Russian Corollary 4, printed p.27 / PDF page10, was checked against its page image. It gives the claimed distinguished grid basis for a morsification of a sum of powers. Its neighboring intersection entries are +/-1. The connected-grid description is correct.

The general input is AGV II, Theorem3.3, printed p.75: connectedness for any distinguished basis, also for a weakly distinguished basis. The excerpt includes its derivation from Theorem3.4, pp.76–77. Lazzeri's Theorem2, p.274 / PDF page7, gives the equivalent assertion that every nontrivial partition has a nonzero cross-intersection. Ebeling's 2019 survey, Corollary18, p.23, corroborates it. The proof can therefore use its own morsification's basis, without Gabrielov's explicit grid or a separate change-of-morsification argument.

Qualify the stabilization sentence: it preserves **off-diagonal** intersection numbers up to signs. Self-intersections can change from zero to +/-2 when parity changes. Ebeling Theorem13, p.19, states the off-diagonal formula. Only off-diagonal nonvanishing is used here.

This does not assert irreducibility of a single classical monodromy operator. The candidate validly proves irreducibility of the full group from connectedness, nondegeneracy, and transvections.

## Milnor-fibre stability and local/global comparison

The AGV source supplied here is raw OCR, not the original page images. Clear prose and surrounding references were checked; garbled formulas were not silently accepted. Ebeling and the original Lazzeri/Gabrielov scans provide independent corroboration where relevant.

Verified AGV pinpoints: Section1.3 p.26 (Picard–Lefschetz); Section2.1 pp.29–31, especially p.30 (small perturbed regular levels diffeomorphic to the Milnor fibre); Theorem2.1 p.31 (distinguished basis); p.100 (kernel dimension r−1 for any plane-curve singularity); p.411 Example2 (coprime powers give nondegenerate form). The OCR misreads the basis-theorem heading as '1.1'; the subsequent references and Ebeling Theorem3 identify it as AGV Theorem2.1.

Write epsilon=1/lambda. Then f_epsilon=alpha X^a+beta Y^b+sum q_ij epsilon^(ab−bi−aj)X^iY^j is a holomorphic deformation, since all epsilon exponents are positive integers. Fix a Milnor ball and target disk with a transversality margin. Compactness and C^1 convergence preserve boundary transversality. Scaling explicitly places every critical point and value in the smaller ball/disk. At a fixed outer regular value, a proper submersion including its boundary over the parameter interval gives the Milnor-fibre diffeomorphism by Ehresmann. This supplies the short proof behind the textbook's 'easy to show'.

For compatibility of global and local transport, cite tameness as well as sphere transversality. Transversality at a compact sphere alone does not control nonproper infinity. Bounded global horizontal lifts from tameness can be patched on a compact collar to lifts tangent to the sphere; complete flows give pair trivializations. The supplement writes this out.

Inclusion then preserves the intersection form. Local nondegeneracy gives injection on H_1; Broughton's global rank equals the local rank mu, so this is an isomorphism of local systems. The punctured disk contains all critical values and induces an isomorphism on fundamental groups. The remaining connectedness/transvection argument is valid.

## Formal diagonalization and the group

The recursion in Lemma4.1 is correct. At order1 the diagonal equation determines Lambda=diag(A1), and the off-diagonal equation determines H1 off the diagonal. At order k>=2, the diagonal terms involving diag(A1) cancel, determining diag(H_(k−1)) by division by −(k−1); division by c_i−c_j then gives H_k off the diagonal. This is a formal induction, with no convergence claim. Bound the sum j>=2 by k or define negative-index H to be zero.

In Proposition4.2, a character trivial on the diagonal local PV group means u^n lies in C((w)). Its logarithmic derivative has zero constant term, forcing sum n_i c_i=0. This proves that the local group **contains** the required connected torus with character lattice sum Z c_i; it need not equal the entire local diagonal group. This inclusion is all that the root argument needs.

The component proof is also valid. The algebraic global PV subextension is unramified on C*, hence Kummer. Its intersection with C((w)) is C(z), by integral valuation. The local diagonal group surjects onto the component group and preserves the coordinate blocks. Irreducibility leaves one block and forces SL_mu. No formal-monodromy generator or Stokes calculation is used.

## Exponents, Wasow, and the replacement proof

The newest exponent definition and lowest-order comparisons work, including repeated leading eigenvalues. The quotient-solution injection uses coefficient modules: solutions are differential homomorphisms **out of** the module. With horizontal-section conventions its variance would be reversed. State this convention explicitly.

Singer's arXiv:0712.4124, p.27, explicitly states the commuting ramified formal fundamental matrix phi(t)x^L exp Q(1/t). Definition1.4.5 on p.29 explains the normal form. Choose the commuting ramified form; the optional later unramified presentation need not retain commutation. After x=w=1/z, the sign of the arbitrary constant regular-part matrix is absorbed by renaming it. Singer states the existence theorem without proof there and refers to van der Put–Singer, Chapter3.

For Wasow, the accessible contents locate Section11, 'Formal Simplification', but the needed theorem statement was not accessible. No precise theorem number was independently verified and none should be cited from recollection. This is not a mathematical blocker: the candidate proves simple-spectrum diagonalization directly.

Moreover, the proof supplement removes the remaining general formal theorem from face disjointness. Stable C[[w]] lattices descend to subquotients by intersection/image. Saturation makes reduction modulo w exact, so residue spectra survive passage to a composition-factor direct sum. Endomorphism residues have difference spectra. A rank-one line with coefficient d+rho w forces d into the ambient residue spectrum because f'/f has zero constant term for f in C((w))*. Apply this to the interior adjoint lines and the semisimplified face lattice. It gives exactly the required critical-value difference obstruction, without formal normal forms, ramification, or exponential-factor separation.

## Remaining chain, computation, and promotion boundary

Normal forms, period injectivity, the Fourier degree-versus-order argument, the Lie-algebra single-face step, the saddle lemma, Paper V's actual one-column criterion, and specialization were checked again; no further defect was found. Bonnet Definitions1.3–1.4/Theorem1.5 (p.375) match finite critical locus and connected nonempty fibres. Beukers Theorem1.1 (p.370) applies to both the boundary and combined E-function vectors, with no nonzero finite singularity. Subtracting transcendence degrees yields the relative numerical statement.

The strengthened example script passes. An additional exact trace check gives tr(A0^k(A1+I))=0 for k=0,...,5; simple spectrum and a Vandermonde argument prove all six formal powers equal -1 exactly. A rational 3x3 recursion test through order8 also passes. These checks supplement, not replace, the general proofs.

The frozen source compiles to11 pages after three pdflatex passes, with no unresolved references/citations or overfull boxes in the final log; its pages were inspected. These standalone checks do not claim a local rerun of the full canonical make test/pdf/check suite.

Before promotion: add the explicit convention and geometric details; qualify off-diagonal stabilization; add complete Singer/Bonnet/Beukers bibliography; choose either the accurately cited general normal form or the stable-lattice replacement; retain(S*) for the original triangle; and keep genericity of(Q), all-line-period fields, several chains, and general formal completeness outside the claims. No principal theorem hypothesis or conclusion needs changing. Preserve the frozen source and create a separately identified corrected successor.
