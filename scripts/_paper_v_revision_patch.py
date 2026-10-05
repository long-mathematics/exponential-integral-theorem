#!/usr/bin/env python3
"""Apply the audited, source-hash-guarded October 5 Paper V revision."""
from pathlib import Path
import hashlib
import re
import sys
ROOT = Path(sys.argv[1]) if len(sys.argv) > 1 else Path('.')
p = ROOT / 'papers/05-polynomial-flags/polynomial-flag-exponential-periods.tex'
s = p.read_text()
assert hashlib.sha256(s.encode()).hexdigest() == '51e93dd691c0b4b593a67941dbd2562c8b4914f7c79221777ca981f4071f988b'
original = s

def change(old, new):
    global s
    assert s.count(old) == 1, (old[:100], s.count(old))
    s = s.replace(old, new)

def section(start, end, new):
    global s
    assert s.count(start) == s.count(end) == 1
    i, j = s.index(start), s.index(end)
    assert i < j
    s = s[:i] + new + s[j:]

change(r'''final formal-period interpretation, which is explicitly local at boundary
denominators known not to vanish.''', r'''localized fixed-chain presentation in
\cref{prop:localized-formal-comparison}. Its functional statement uses the
actual boundary coefficients; its numerical formal interpretation uses
Paper III after specialization, inverting only boundary elements with
nonzero value.''')
change(r'''\cref{thm:intro-single}; Paper III supplies the polynomial formal
interpretation after the actual elliptic comparison.''', r'''\cref{thm:intro-single}; Paper III supplies the specialized boundary-symbol
comparison in \cref{prop:localized-formal-comparison}.''')
section('Algebraic direct image of the rank-one connection', '\nThe monomial two-forms', r'''The polynomial Gauss--Manin complex for $q:\A^2\to\A^1_t$ is
\[
 \bigl(\Omega^{\bullet+2}_{k[x,y]/k}[\partial_t],
             d-dq\wedge\partial_t\bigr),
\]
and its cohomology is holonomic \cite[Proposition~9.1]{Sabbah}.
The Fourier substitution $\partial_t\mapsto-z$, $t\mapsto\partial_z$
turns its differential into $d+z\,dq\wedge$. Fourier transform is exact
on Weyl modules, and localization to $k(z)$ is exact. The degree-zero
cohomology of the localized transformed complex is therefore precisely
$\Hq$, which is finite dimensional over $k(z)$ by holonomicity.
This uses neither cohomological tameness nor the rank and lattice
conclusions stated later in \cite{Sabbah}. In particular, no identification
with a Milnor number is asserted here.
''')
change(r'''The complement is a finite union of open intervals $e$.''', r'''Refine this finite exceptional set if necessary so that the algebraic
relative Gauss--Manin system of the parametrized slices is smooth on its
complement. The remaining real phase set is a finite union of open
intervals $e$. For continuation, the real face intersections are viewed
inside the reduced algebraic divisor cut out by the complexified faces.''')
change(r'''The coarea decomposition of the
finite measure obtained by integrating the polynomial density on the compact
chain shows that the resulting density is integrable across the finitely many
critical and boundary values.''', r'''For a component $\Phi_*[0,1]^2$, apply coarea first on the square to
$q\circ\Phi$ and the signed polynomial density $\Phi^*\Omega$, including
its Jacobian, and then push forward. Summing these formulas retains
orientation and multiplicity; injectivity of $\Phi$ is not required.
Unless $\Phi^*\Omega=0$, the polynomial $q\circ\Phi$ is nonconstant,
and its critical set has measure zero. The coarea decomposition of this
finite measure consequently has an $L^1$ density, including across the
finitely many exceptional values.''')
change(r'''distinct; over their complement the fibres form a smooth proper curve
      family, and the face intersections become a finite \'etale divisor after
      a finite base change;''', r'''distinct; after also deleting the finitely many boundary exceptional
      values, the compactified fibres form a smooth proper curve family
      on the chosen phase base, and the reduced algebraic face intersections
      form a finite \'etale divisor there;''')
change(r'''\end{definition}


\subsection{Bonnet's theorem}''', r'''\end{definition}

The incidences in \textup{(A5)} refer to relative Picard--Lefschetz
transformations of the form \eqref{eq:relative-PL} on this chosen base.
Their action on the relative slice local system is part of the observable
datum. They need not generate its full monodromy: additional face
monodromies are allowed. No splitting of the finite \'etale face divisor
into sections, or preservation of observability under an unspecified
finite cover, is assumed.

\subsection{Bonnet's theorem}''')
change(r'''By \cref{cor:connected-observable}, this is the complete projective
weight-one homology.  The one-place-at-infinity hypothesis identifies this
with $H_1(C_t)$ of the affine fibre.''', r'''Apply the rooted propagation argument to the relative
Picard--Lefschetz transformations in the observable datum. The nonzero
incidence gives one absolute vanishing cycle in this span, and the
connected intersection graph propagates to all of them. Thus the full
relative variation span \emph{contains} the complete projective weight-one
homology; equality with that span is unnecessary. The
one-place-at-infinity hypothesis identifies the absolute homology with
$H_1(C_t)$ of the affine fibre.''')
change(r'''An irreducible complex local system underlying a polarizable complex
variation of Hodge structure carries such a variation uniquely up to tensoring''', r'''On a connected smooth complex algebraic base, an irreducible complex
local system underlying a polarizable complex variation of Hodge structure
carries such a variation uniquely up to tensoring''')
change(r'''formulation in \cite[Theorem~2]{BakkerMatsushita}.''', r'''formulation in \cite[Theorem~3(1), linked author manuscript]{BakkerMatsushita}.
The algebraic base is compactifiable, as required in that formulation.''')
s = s.replace('DeligneHodgeIII', 'DeligneHodgeII')
section(r'''The homomorphism and the Poincar\'e bundle determine''', '\n\\end{proof}\n\n\\begin{corollary}[Complex intertwiners', r'''To realize the rational action by a divisor without assuming sections
of the curve families, work first over the function field $\C(S)$.
After a finite field extension both curves have points. The Abel--Jacobi
maps and the Poincar\'e bundle then give a divisor correspondence inducing
the given Jacobian homomorphism. Push this divisor down from the finite
extension and divide by its degree, and by the integer used above. The
trace of the induced action is the original rational morphism, since
that morphism was already defined over $\C(S)$.
Take the closure of the resulting rational divisor in
$\mathcal C_i\times_S\mathcal C_j$. This total space is smooth, so the
closure is a rational Cartier divisor. Its action on the two $R^1$
local systems agrees with the prescribed map on a dense open base and
therefore everywhere. Thus no global choice of a degree-one divisor or
an unmentioned base change is needed.''')
change(r'''Under the hypotheses of \cref{thm:Hodge-rigidity}, every complex flat
intertwiner is a complex linear combination of rational VHS morphisms and
therefore, by \cref{prop:Jac-correspondence}, of algebraic Jacobian
correspondences.''', r'''Under the hypotheses of \cref{thm:Hodge-rigidity}, every complex flat
intertwiner is a complex linear combination of rational VHS morphisms.
When the variations are the $R^1$ of curve families as in
\cref{prop:Jac-correspondence}, it is consequently a complex linear
combination of algebraic Jacobian correspondences.''')
change(r'''Apply \cref{thm:Hodge-rigidity,prop:Jac-correspondence} to the rational
summands.''', r'''Apply \cref{thm:Hodge-rigidity} to the rational summands, and then
\cref{prop:Jac-correspondence} in the curve-family setting.''')
change(r'''\begin{theorem}[Actual one-column comparison]''', r'''\begin{lemma}[Regular affine cocycles]\label{lem:affine-cocycle}
Let $G$ be an algebraic group over an algebraically closed field $C_0$
of characteristic zero, with reductive identity component, and let $V$
be a finite-dimensional rational representation. Every regular cocycle
$c(gh)=c(g)+g c(h)$ has the form $c(g)=v-gv$ for some $v\in V$.
\end{lemma}
\begin{proof}
Let $g$ act on $V\oplus C_0$ by
$g(w,t)=(gw+t c(g),t)$. Complete reducibility supplies an invariant
lift $(v,1)$ of $1$ in the trivial quotient, giving the assertion.
Complete reducibility here includes disconnected groups: average a
$G^\circ$-equivariant splitting over the finite component group
\cite[Corollary~22.43]{MilneAG}. Equivalently, this is the vanishing of
algebraic $H^1(G,V)$ in \cite[Proposition~15.15]{MilneAG}.
\end{proof}

\begin{theorem}[Actual one-column comparison]''')
change(r'''reductive homogeneous group is a coboundary. Here reductivity follows''', r'''homogeneous group is a coboundary by \cref{lem:affine-cocycle}.
Here reductivity of its identity component follows''')
change(r'''subgroup. Thus
\[
 U=a+Yc,''', r'''subgroup. Explicitly, writing $\sigma(Y)=Yg_\sigma$, the cocycle
can be written $c_\sigma=g_\sigma c-c$; hence $U-Yc$ is fixed. Thus
\[
 U=a+Yc,''')
change(r'''$1/2+\Z$ \cite[Example 1.3.32]{Singer}; an algebraic rank-one twist does''', r'''$1/2+\Z$ \cite[Example~1.3.32, group statement]{Singer}, attributed
there to Kolchin \cite{Kolchin1968}. The change from ordinary to modified
Bessel is the nonzero constant rescaling of the independent variable by
$i$. An algebraic rank-one twist does''')
change(r'''Such factors
are preserved by differential-module isomorphism. This is a contradiction.''', r'''These are the exponential factors of the formal normal form at infinity
\cite[\S1.4, formal fundamental matrix]{Singer}. In the present
unramified, distinct-leading-eigenvalue case, formal diagonalization
reduces the claim to rank one: a nonzero Laurent-series intertwiner
between factors $e^{az}$ and $e^{bz}$ would have logarithmic derivative
$a-b+O(z^{-1})$, whereas a Laurent series has logarithmic derivative
$O(z^{-1})$. Thus it requires $a=b$. The unequal sets of factors cannot
be related by a formal, and hence not by a rational, isomorphism.''')
section(r'''\begin{remark}[Formal period operations]''', r'''\section{Local specialization without a global boundary normal form}''', r'''\begin{proposition}[Localized fixed-chain Stokes and formal comparison]
\label{prop:localized-formal-comparison}
Fix the triangle and phase \eqref{eq:intro-elliptic}, and put
$\Lambda=k[z,z^{-1}]$. Let $R$ be either $K_{\partial,0}$ or $B_\xi$
for $\xi\in k^\times$. Form the commutative $R$-algebra $\mathscr S_R$
on symbols $\mathsf I(r)$, $r\in\Lambda[x,y]$, modulo
$\Lambda$-linearity and the polynomial Stokes relations
\[
 \mathsf I(L_xP+L_yQ)
   =\int_{\partial D}e^{zq}(P\,dy-Q\,dx),
 \qquad P,Q\in\Lambda[x,y].
\]
The right side is a specified element of the actual coefficient ring $R$.
Then realization gives
\[
 \mathscr S_R\simeq R[X_0,X_1]\simeq R[M_0,M_1],
 \qquad X_0\longleftrightarrow\mathsf I(1),\quad
        X_1\longleftrightarrow\mathsf I(x).
\]
For $R=B_\xi$, its fiber at $\xi$ realizes injectively as
$K_{\partial,\xi}[M_0(\xi),M_1(\xi)]$.

There is also a numerical formal-period version: take the subalgebra of
Paper III's formal compact-line algebra generated by the three fixed
faces with phases $\xi p_e$ and their endpoint exponentials, and localize
at elements with nonzero numerical value. Adjoining the fixed-triangle
amplitude symbols, with linearity, multiplication and specialized
polynomial Stokes, gives an injective numerical realization. Thus every
relation in this specified localized fixed-$(D,q)$ amplitude algebra is
generated by the inherited boundary formal relations and those Stokes
reductions.
\end{proposition}
\begin{proof}
Laurent polynomial division \eqref{eq:elliptic-normal} reduces every
symbol to
\[
 a_r\mathsf I(1)+b_r\mathsf I(x)
       +\int_{\partial D}e^{zq}(P_r\,dy-Q_r\,dx).
\]
This also holds for $r\in\Lambda[x,y]$ by $\Lambda$-linearity, so
$R[X_0,X_1]\to\mathscr S_R$ is surjective. Its composite with actual
realization is injective by \cref{thm:elliptic-main}; hence both maps
are isomorphisms. For $B_\xi$, the boundary residue field is
$K_{\partial,\xi}$ by \cref{lem:boundary-dvr}, and
\cref{thm:values} gives injectivity on the polynomial fiber.
All coefficients and Stokes primitives used here are regular at $\xi$.

For the last assertion, Paper III's polynomial formal comparison
\cite[main theorem]{PaperIII} identifies the stated boundary subalgebra
with its numerical image. Localizing at its nonzero elements identifies
its fraction field with $K_{\partial,\xi}$. Apply the same reduction
with $z=\xi$, followed by the algebraic independence in
\cref{thm:values}. The boundary relations are those inherited from
Paper III's category; they are not restricted to proofs using only the
three original faces as intermediate objects.
\end{proof}

The functional assertion above is a presentation over \emph{actual}
boundary coefficients. The numerical formal assertion invokes Paper III
only after specialization. Neither asserts an unlocalized cancellation
theorem for an arbitrary symbol ring, a new generic formal boundary
theorem, or formal completeness for additional chains or primitive blocks.

''')
change(r'''Assume $n\ge2$, and that the reductive homogeneous group of all the blocks
contains the product of their standard special-linear groups. All matrices
are taken in a common no-new-constants Picard--Vessiot extension.''', r'''Assume $n\ge2$ in each block and let
$G\subset\prod_\lambda\GL_{n_\lambda}$ be the joint homogeneous
Galois group. We require
$\prod_\lambda\SL_{n_\lambda}\subset G$, as an independent product,
not merely surjectivity of the separate projections. Its identity
component is reductive: its unipotent radical lies in that product and
is normal under it, and must therefore be trivial. All matrices are
taken in a common no-new-constants Picard--Vessiot extension.''')
section(r'''The translation kernel is an invariant additive subgroup''', '\n\\end{proof}\n\nFor a constant', r'''Let $H$ be the affine Galois group and $T$ the kernel of $H\to G$.
An algebraic subgroup of a vector group in characteristic zero is a
vector subspace. It is stable under $G$ by conjugation. The independent
special-linear factors imply that, in block $\lambda$,
\[
 T_\lambda=C_0^{n_\lambda}\otimes R_\lambda
 \quad\text{for some }R_\lambda\subset C_0^{r_\lambda};
\]
there is no coupling between distinct standard factors. Indeed the
standard modules are pairwise nonisomorphic simple modules for the
product, with scalar endomorphisms, so their isotypic subspaces have
exactly this form. Choose constant column bases adapted to each
$R_\lambda$.

Translations now vary every active column by $Y_\lambda v$
independently. Over a field trivializing the Picard--Vessiot torsor,
the invertible $Y_\lambda$ makes this the full affine space of those
coordinates. The orbit closure is consequently a product of the active
affine spaces with the orbit closure in the remaining coordinates.
Its ideal is extended from the latter coordinates. Faithfully flat
descent of the torsor gives the same statement for relations over $K$.

On the remaining columns, $T$ acts trivially, so their affine cocycle
descends to $G$. By \cref{lem:affine-cocycle} it is a coboundary:
if $\sigma(Y)=Yg_\sigma$, there is a constant matrix $C$ with
$c_\sigma=g_\sigma C-C$. Thus $U-YC=A_0$ is Galois-fixed and has
entries in $K$. Constant column operations put $C$ into a matrix of
independent columns followed by zero columns. The latter give precisely
the affine-linear equations $U_j=(A_0)_j$; no independent column is
removed.''')
change(r'''Let $T_{\det}\subset\Gm^s$ be the determinant image of the joint group and
\[
 L=\{a\in\Z^s:''', r'''Let $m$ be the number of these square blocks and let
$T_{\det}\subset\Gm^m$ be the image of the joint group under their
determinant characters. Put
\[
 L=\{a\in\Z^m:''')
section(r'''After the linear and translation reductions, independent special-linear''', '\n\\end{proof}\n\nNow work over a DVR', r'''Perform \cref{prop:affine-reduction}; the active coordinates are
free and the zero split columns are eliminated. For a remaining split
block of column rank $s<n$, any map between two ordered independent
$s$-frames extends to a general-linear map, whose determinant can be
corrected on a complementary vector. Its special-linear orbit is
therefore the full-rank open subset of $\operatorname{Mat}_{n\times s}$.
For $s=n$, two invertible matrices are in the same special-linear orbit
exactly when their determinants agree. Since the special-linear groups
act independently, the only remaining joint restriction on the open
set of maximal-rank matrices is on the square-block determinants.

That restriction is the translate of $T_{\det}$ by the actual
nonzero determinant tuple. A character $a\in L$ evaluates on this
tuple to $\eta_a$, which lies in $K^\times$ because it is Galois-fixed.
In Laurent determinant coordinates the ideal of the translate is the
character ideal. Its contraction to ordinary polynomial coordinates is
\[
 I_L=(\delta^{a^+}-\eta_a\delta^{a^-}:a\in L)
       \subset K[\delta_1,\ldots,\delta_m].
\]
This is the full partial-character lattice ideal
\cite{EisenbudSturmfels}. One can see the contraction directly by
grouping monomials whose exponent differences lie in $L$; monomials in
different character classes are linearly independent on the translate.
In particular the quotient injects into its localization at
$\delta_1\cdots\delta_m$. All lattice elements, not just an additive
basis, are used here; disconnected determinant images are allowed.

We check that pulling back this ideal to the matrix coordinates gives
the entire orbit closure, without extra components or nilpotents.
The product of determinant maps is free, hence flat, on coordinate
rings by \cref{lem:free-determinant}. Thus the injection into the
Laurent localization stays injective after this base change and after
adjoining the other coordinates. On the determinant-invertible open
set the maps $\GL_n\to\Gm$ are smooth. The translated determinant
subgroup is reduced in characteristic zero, including when it is
disconnected, so its inverse image is reduced. The whole quotient,
which embeds in this reduced localization, is reduced as well, and
the determinant-invertible locus is dense. Requiring full column rank
in the rectangular blocks removes only a proper closed subset in each
free matrix factor. The resulting dense open is exactly the orbit
computed above. Its ideal is therefore the stated pulled-back ideal.

Finally, this orbit computation does determine the relations of the
actual coordinates over $K$. The Picard--Vessiot ring is the coordinate
ring of a torsor \cite[Proposition~1.3.20]{Singer}. After a faithfully
flat extension trivializing that torsor, the coordinate map becomes
the orbit map of the chosen tuple. Its kernel is the orbit-closure
ideal just computed. Faithfully flat descent gives equality of the
original relation ideal with the displayed ideal over $K$, together
with the affine-linear reductions. This is a statement about the
base-changed coordinate map of the torsor, not about evaluation at a
single point of its splitting field.''')
change(r'''\href{https://doi.org/10.1016/j.aim.2025.110554}{doi:10.1016/j.aim.2025.110554}.''', r'''\href{https://doi.org/10.1016/j.aim.2025.110554}{doi:10.1016/j.aim.2025.110554}.
Theorem numbering here refers to the
\href{https://benjamin-bakker.github.io/matsushita.pdf}{author manuscript}
consulted 5 October 2026, Theorem~3(1).''')
change(r'''\emph{Th\'eorie de Hodge. III},
Inst. Hautes \'Etudes Sci. Publ. Math. \textbf{44} (1974), 5--77.''', r'''\emph{Th\'eorie de Hodge. II},
Inst. Hautes \'Etudes Sci. Publ. Math. \textbf{40} (1971), 5--57,
Rappel~(4.4.3).
\href{https://doi.org/10.1007/BF02684692}{doi:10.1007/BF02684692}.''')
change(r'''\bibitem{KontsevichZagier}''', r'''\bibitem{Kolchin1968}E.~R.~Kolchin,
\emph{Algebraic groups and algebraic dependence},
Amer. J. Math. \textbf{90} (1968), 1151--1164.
For the Bessel-group attribution used here, see
\cite[Example~1.3.32 and reference \textnormal{[Kol68]}]{Singer}.

\bibitem{KontsevichZagier}''')
change(r'''\bibitem{PaperIII}''', r'''\bibitem{MilneAG}J.~S.~Milne,
\emph{Algebraic Groups: The Theory of Group Schemes of Finite Type
 over a Field}, Cambridge Studies in Advanced Mathematics, vol.~170,
Cambridge University Press, 2017, Proposition~15.15 and Corollary~22.43.
\href{https://www.jmilne.org/math/Books/iAG2017.pdf}{Author-hosted text}.

\bibitem{PaperIII}''')
change(r'''Preprint \href{https://arxiv.org/abs/math/9805077}{arXiv:math/9805077},
Proposition 9.1, Remarks 9.4, and Corollary 10.2.''', r'''Preprint \href{https://arxiv.org/abs/math/9805077}{arXiv:math/9805077}.
We use Proposition~9.1 of the
\href{https://perso.pages.math.cnrs.fr/users/claude.sabbah/articles/sabbah_bbases.pdf}{author-hosted manuscript};
no result under its subsequent standing tameness assumption is used
for general finiteness.''')
change(r'''and Theorem 1.5.2.''', r'''\S1.4 (formal fundamental matrices), and Theorem~1.5.2.
Only the group statement of Example~1.3.32 is used; the $E$-function
property of the actual compact integrals is proved here separately.''')
# Preservation: all old labels survive; the three principal theorem bodies are exact.
assert set(re.findall(r'\\label\{([^}]+)\}', original)) <= set(re.findall(r'\\label\{([^}]+)\}', s))
for label in ['thm:intro-elliptic','thm:elliptic-main','thm:values','thm:criterion']:
    pat = r'\\label\{' + re.escape(label) + r'\}.*?\\end\{theorem\}'
    assert re.search(pat, original, re.S).group() == re.search(pat, s, re.S).group(), label
assert hashlib.sha256(s.encode()).hexdigest() == 'f3a49ad33b6f58f38e6cbb2d211392d6b4f682b5a7dd8ce2e608097d32c2e655'
p.write_text(s)
print('Revised source SHA256:', hashlib.sha256(s.encode()).hexdigest())
