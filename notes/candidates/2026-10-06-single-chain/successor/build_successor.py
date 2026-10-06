#!/usr/bin/env python3
"""Reproduce the corrected successor without modifying the frozen input.

This is a bounded proof revision, not a search for further generalizations.
Run from the repository with --root .; --root may name an isolated worktree.
"""
from __future__ import annotations
import argparse
import hashlib
from pathlib import Path
import re

DIRECTORY = Path('notes/candidates/2026-10-06-single-chain')

def replace_once(text: str, old: str, new: str) -> str:
    if text.count(old) != 1:
        raise RuntimeError(f'Expected one occurrence of {old[:95]!r}; found {text.count(old)}')
    return text.replace(old, new, 1)

GEOMETRY = r'''\emph{Local model and stability.} Write
\[
 f_\epsilon(X,Y)=\alpha X^a+\beta Y^b+
 \sum_{bi+aj<ab}q_{ij}\epsilon^{ab-bi-aj}X^iY^j.
\]
Every exponent of $\epsilon$ is a positive integer, so this is a holomorphic
deformation of $f_0=\alpha X^a+\beta Y^b$. For $\epsilon\ne0$ it equals
$\epsilon^{ab}q(\epsilon^{-b}X,\epsilon^{-a}Y)$; its critical points and values
are $(\epsilon^b x_i,\epsilon^a y_i)$ and $\epsilon^{ab}c_i$.
Choose a Milnor ball $\overline B_r$ for $f_0$, and choose $\eta>0$ so that its
levels $|t|\le2\eta$ are transverse to $\partial B_r$. Compactness and
$C^1$ convergence preserve this transversality for $f_\epsilon$ with
$|t|\le\eta$ when $|\epsilon|$ is sufficiently small. Shrink the parameter disk
so that all critical points lie in $B_{r/2}$ and all critical values have
modulus less than $\eta/2$.

At the fixed value $t_* =\eta$, the family
\[
 \{(\epsilon,X,Y):f_\epsilon(X,Y)=t_*,\ (X,Y)\in\overline B_r\}
 \longrightarrow\{\epsilon:|\epsilon|<\epsilon_0\}
\]
is a proper submersion, including on its boundary. The boundary form of
Ehresmann's theorem therefore identifies its fibres with the Milnor fibre of
$f_0$. This is also the perturbation comparison in \cite[\S2.1,
pp.~29--31]{AGV}. For a fixed small nonzero $\epsilon$, the local proper
submersion over the disk minus the critical values transports this
identification to every regular level there. Put
$S_t=f_\epsilon^{-1}(t)\cap\overline B_r$ and $C_t=f_\epsilon^{-1}(t)$.
By \cite[Theorem~2.1, p.~31]{AGV} a distinguished set of vanishing cycles
$\Delta_1,\ldots,\Delta_\mu$ is a basis of $H_1(S_t;\Z)$.
For a plane-curve singularity the kernel of the intersection form has
dimension $r_0-1$, where $r_0$ is the number of branches
\cite[\S3.6, p.~100]{AGV}. The binomial germ $f_0$ is irreducible, so this
form is nondegenerate; compare also \cite[p.~411, Example~2]{AGV}.

\emph{Compatible local and global transport.} Tameness is preserved by the
fixed nonzero rescaling. Over a relatively compact target neighborhood $U$
whose closure avoids the critical values, $\|\nabla f_\epsilon\|$ is bounded
below: use tameness outside a compact set and compactness inside it.
A bounded horizontal lift of a constant target tangent vector $v\in\C$ is
\[
 V_v=v\,\frac{\overline{\nabla f_\epsilon}}{\|\nabla f_\epsilon\|^2},
 \qquad df_\epsilon(V_v)=v.
\]
Boundary transversality supplies a smooth horizontal lift tangent to
$\partial B_r$. On a compact collar patch it to $V_v$ by a partition of unity.
The patched lift remains horizontal and bounded and is tangent to the sphere.
Its flows exist for the required finite times, preserve the sphere and its two
sides, and yield compatible local trivializations of the pair $(C_t,S_t)$.
This uses both tameness and transversality, following the bounded-lift
construction in \cite[pp.~229--230]{Br}.

Inclusion $j:S_t\hookrightarrow C_t$ preserves intersection numbers. Hence
$j_*v=0$ implies $\langle v,u\rangle=\langle j_*v,j_*u\rangle=0$ for every $u$,
and local nondegeneracy gives $v=0$. The global and local homology groups both
have dimension $\mu$, so $j_*$ is an isomorphism. The compatible transport
above makes it an isomorphism of local systems. The punctured disk contains
all critical values and its inclusion in their complement in $\C$ induces an
isomorphism on fundamental groups. Thus the global intersection form is
nondegenerate and its monodromy is that of this morsification. Rescaling back
to $q$ proves the remaining assertions of (G1).

'''

LATTICES = r'''\paragraph{Stable lattices at infinity.}
Put $R_\infty=\C[[w]]$, $K_\infty=\C((w))$ and
$\delta=d/dz=-w^2d/dw$. A lattice in a differential module over $K_\infty$
is a finite free $R_\infty$-submodule spanning it. A lattice $L$ is stable if
$\partial L\subset L$. Since $\delta(R_\infty)\subset wR_\infty$, its
operator induces a $\C$-linear operator on $L/wL$, called the leading
operator of this stable lattice. In the coefficient-module convention its
matrix for a system $Y'=E(w)Y$ is $E(0)^{\mathsf T}$, which has the same
spectrum as $E(0)$.

\begin{lemma}[Stable lattices and subquotients]\label{lem:lattice}
Let $L\subset M$ be a stable lattice and $N\subset M$ a differential
submodule. Then $L_N=L\cap N$ and $L_{M/N}=\operatorname{im}(L\to M/N)$
are stable lattices, and
\[
 0\longrightarrow L_N/wL_N\longrightarrow L/wL
 \longrightarrow L_{M/N}/wL_{M/N}\longrightarrow0
\]
is exact and compatible with the leading operators. Their characteristic
polynomials therefore multiply. In particular a direct sum of successive
quotients of a differential-module filtration has a stable lattice with the
same leading characteristic polynomial as $L$.
\end{lemma}
\begin{proof}
The intersection is a saturated, finitely generated submodule of $L$:
if $wv\in L\cap N$ and $v\in L$, then $v\in N$ because $N$ is a
$K_\infty$-vector space. The intersection and the quotient are free over the
discrete valuation ring $R_\infty$ and span the desired spaces. Stability
is inherited. Since the quotient is free, reduction modulo $w$ preserves
exactness. Also $\delta(w)=-w^2$, so each leading operator is well-defined
and the sequence intertwines them. Apply this successively to the filtration.
\end{proof}

\begin{lemma}[Detection of a rank-one leading coefficient]\label{lem:rankone}
If a module $M$ with stable lattice $L$ contains a nonzero vector $v$ with
$\partial v=(d+\rho w)v$, $d,\rho\in\C$, then $d$ is an eigenvalue of the
leading operator on $L/wL$.
\end{lemma}
\begin{proof}
The saturated lattice $L\cap K_\infty v$ has a generator $fv$, where
$f=w^m u$ with $u\in R_\infty^\times$. Its coefficient is
\[
 d+\rho w+\frac{\delta f}{f},\qquad
 \frac{\delta f}{f}=-mw-w^2\frac{u_w}{u}\in wR_\infty.
\]
Its leading eigenvalue is therefore $d$. Its reduction injects into $L/wL$
by Lemma~\ref{lem:lattice}.
\end{proof}

\begin{corollary}[A leading-spectrum obstruction]\label{cor:face-lattice}
Suppose $M$ has a stable lattice with leading spectrum $\Sigma$. Let $P$
admit a basis over $K_\infty$ with
$\partial e_i=(c_i+\lambda_iw)e_i$. If
\[
 \End^0(P)\hookrightarrow\End(M^{\rm ss})
\]
is a differential-module embedding, then $c_i-c_j\in\Sigma-\Sigma$ for
all $i\ne j$.
\end{corollary}
\begin{proof}
By Lemma~\ref{lem:lattice}, $M^{\rm ss}$ has a stable lattice $L^{\rm ss}$
with the same leading characteristic polynomial. The lattice
$\End_{R_\infty}(L^{\rm ss})$ is stable; its leading operator is the
commutator with that of $L^{\rm ss}$, with eigenvalues $s-s'$ for
$s,s'\in\Sigma$. The vector $e_i\otimes e_j^*$ is trace-free for $i\ne j$
and has differential coefficient
$c_i-c_j+(\lambda_i-\lambda_j)w$. Its image in the endomorphism module is
nonzero, so Lemma~\ref{lem:rankone} gives the result.

If $M^{\rm ss}$ was taken over $F$ first, extend a composition series from
$F$ to $K_\infty$ and apply the lattice lemma to this filtration. Its
quotients need not remain simple. No assertion that semisimplification
commutes with this extension is used.
\end{proof}

For a face polynomial $p$ of degree $d\ge2$, the one-variable reduction gives
a matrix in $M_{d-1}(k[z^{-1}])$ whose leading matrix is multiplication by
$p$ on $k[s]/(p')$. Thus its stable lattice has as leading spectrum the
critical values of $p$, also when those values repeat. For the interior
module, Lemma~\ref{lem:formal} supplies the diagonal basis required in
Corollary~\ref{cor:face-lattice}. These are all the local facts needed below;
no general formal-normal-form theorem is required.

'''

INPUTS = r'''\section{External inputs and scope}\label{sec:inputs}
The proof uses the following precise external results. The elementary
formal diagonalization and stable-lattice lemmas are proved here; neither
Wasow's formal simplification theorem nor a general formal normal form is
an input.
\begin{enumerate}[leftmargin=2.2em]
\item Broughton \cite{Br}, Definition~3.1, p.~225; Theorem~1.2, p.~219,
 and the curve calculation p.~231; bounded horizontal lifts and local
 triviality, pp.~229--230. Proposition~3.4, p.~228, gives an unused
 Newton-theoretic alternative to our explicit tameness estimate.
\item Arnold--Gusein-Zade--Varchenko \cite{AGV}, \S1.3, p.~26
 (Picard--Lefschetz); \S2.1, pp.~29--31 and Theorem~2.1
 (perturbed fibre and distinguished basis); Theorem~3.3, p.~75
 (connectedness); \S3.6, p.~100 and p.~411, Example~2
 (nondegeneracy). Proposition~\ref{prop:geometry} includes the parameter
 choices and the proper-submersion argument for the perturbation comparison.
 Connectedness can alternatively be read in \cite[Theorem~2, p.~274]{La};
 \cite[Corollary~4, p.~27]{Ga} gives an explicit grid basis, and
 \cite[Theorem~17, Corollary~18]{Eb} explains the general statement.
\item Bonnet \cite[Definitions~1.3--1.4 and Theorem~1.5, p.~375]{Bonnet},
 for polynomial relative exactness; Singer \cite[Theorem~1.5.2]{Singer},
 for the Picard--Vessiot tensor equivalence; Beukers
 \cite[Theorem~1.1, p.~370]{Beukers}, for specialization of
 transcendence degrees.
\item The polynomial boundary-system theorem and actual one-column
 criterion of the pinned version of Paper~V \cite[Theorems~2.1 and~8.2]{PaperV}.
 Its Lemma~11.1 supplies the continuation verification for the elliptic
 triangle. These inputs do not use the present general theorem.
\end{enumerate}

\paragraph{Scope.} The fields here belong to the finitely many fixed faces,
not to all compact line periods. The theorem concerns one actual chain and
one phase. It does not prove a several-chain theorem, a several-phase
comparison, or general formal completeness. Hypothesis (Q) is sufficient;
its failure alone does not imply a smaller differential Galois group.
Genericity of (Q) in class $(W)$ is not established. No such genericity is
needed for the theorem under its explicit hypotheses.
For $\min(a,b)=2$ the face condition must still be checked; for example it
fails on horizontal edges when $q=y^2+f(x)$.

\paragraph{Revision record.} This is a corrected successor to the immutable
6 October candidate. It incorporates the geometric transport details,
the coefficient-module convention, a stable-lattice replacement for the
formal-exponent argument, precise references, and the off-diagonal
stabilization and (Q)-scope corrections. It does not weaken (Q), expand
the class of chains, or introduce a formal-completeness conclusion.
The computational certificates establish the displayed finite example;
they do not prove the general geometric or Galois assertions.
'''

EXTRA_BIB = r'''
\bibitem{Bonnet} P.~Bonnet,
 \emph{Relative exactness modulo a polynomial map and algebraic
 $(\mathbb C^p,+)$-actions}, Bull. Soc. Math. France \textbf{131} (2003),
 no.~3, 373--398. \href{https://doi.org/10.24033/bsmf.2447}{doi:10.24033/bsmf.2447}.
\bibitem{Beukers} F.~Beukers,
 \emph{A refined version of the Siegel--Shidlovskii theorem}, Ann. of Math.
 \textbf{163} (2006), 369--379.
 \href{https://doi.org/10.4007/annals.2006.163.369}{doi:10.4007/annals.2006.163.369}.
\bibitem{Singer} M.~F.~Singer,
 \emph{Introduction to the Galois theory of linear differential equations},
 \href{https://arxiv.org/abs/0712.4124}{arXiv:0712.4124v2}, 2008.
 We use ordinary Picard--Vessiot theory and Theorem~1.5.2, not the
 general formal-normal-form theorem of \S1.4.
\bibitem{PaperV} C.~D.~Long and A.-A.~Le~Blanc,
 \emph{Relative Exponential Periods on Polynomial Flags:
 Polynomial Boundary Systems and an Elliptic Comparison Theorem},
 Paper~V, September 2026; repository snapshot
 \href{https://github.com/long-mathematics/exponential-integral-theorem/tree/d5ae8f9081c7bc34d1622316bd8463482f244395}{d5ae8f90},
 inspected 6 October 2026.
'''

def successor(source: str) -> str:
    # Preserve the frozen byte stream; all edits take place in a new string.
    text = source.replace("\n  \\chi(t)", "\n \\chi(t)")
    text = replace_once(text, 'A generic single-chain comparison theorem',
                        'Single-chain comparison for weighted-plane phases')
    text = text.replace('Candidate statement and proof --- working note for Paper V',
                        'Corrected successor --- working note for Paper V')
    text = text.replace('5 October 2026; revised 6 October 2026', '6 October 2026; corrected successor')
    start = text.index(r'\noindent\fbox')
    end = text.index(r'\section{Statement}', start)
    text = text[:start] + r'''\noindent\textbf{Status.} Corrected successor to the frozen candidate.
The main hypotheses and conclusions are retained, including the continuation
alternative $(S^*)$. The proof includes explicit local/global transport and a
stable-lattice argument in place of general formal-exponent theory.
This working note is separate from canonical Paper V; its exact revision
and checks are recorded alongside it.

''' + text[end:]
    text = replace_once(text, r'\begin{theorem}[Generic single-chain comparison]',
                        r'\begin{theorem}[Single-chain comparison]')
    text = replace_once(text,
        r'be a polynomial two-chain over $k_\R$ satisfying \textup{(F)} and \textup{(S)}. Put',
        r'be a polynomial two-chain over $k_\R$ satisfying \textup{(F)} and either \textup{(S)} or \textup{(S$^*$)} below. Put')
    marker = r'\section{Normal form for the class'
    idx = text.index(marker)
    text = text[:idx] + r'''\paragraph{Differential-module convention.}
For a system $Y'=EY$ we use its coefficient module: a column of basis
elements $e$ satisfies $\partial e=Ee$. Solutions are differential
homomorphisms out of this module, so the solution functor is contravariant.
Its horizontal representation is dual to the solution representation.
The natural trace duality identifies the corresponding endomorphism and
trace-free endomorphism representations. All module embeddings below are
under the covariant horizontal-fibre equivalence with these identifications.

''' + text[idx:]
    start = text.index(r'\emph{Local model.}')
    end = text.index(r'\emph{(G2).}', start)
    text = text[:start] + GEOMETRY + text[end:]
    text = text.replace('intersection numbers only by signs.)',
                        'off-diagonal intersection numbers only by signs; self-intersections may change.)')
    text = text.replace(r'+\sum_{j\ge2}A_jH_{k-j}', r'+\sum_{j=2}^kA_jH_{k-j}')
    # The original begins this clause with 'So', not 'so' in some serializations.
    old = "So\n$\\theta^\\sharp$ is exact along the generic fibres, and by Bonnet's theorem\n(fibres connected and reduced by (G1)) $\\theta^\\sharp=dR+a\\,dq$."
    if old in text:
        text = replace_once(text, old, "So\n$\\theta^\\sharp$ is exact along the generic fibres. The critical locus is finite\nand all fibres are connected and nonempty; these give Bonnet's primitive\nand quasi-fibered hypotheses for a map to the line. Thus\n\\cite[Definitions~1.3--1.4 and Theorem~1.5]{Bonnet} gives\n$\\theta^\\sharp=dR+a\\,dq$.")
    start = text.index(r'\paragraph{Leading exponents.}')
    end = text.index(r'Let $\Bcal$ be the closed homogeneous system', start)
    text = text[:start] + LATTICES + text[end:]
    text = replace_once(text,
        r'''Suppose $G\supseteq\SL_\mu$, $\mu\ge2$, and
$\Lambda(\End^0(A))\supseteq\{(c_i-c_j)z\}_{i\ne j}$. If $\End^0(A)$''',
        r'''Suppose $G\supseteq\SL_\mu$, $\mu\ge2$, and that the interior module
has the formal diagonalization of Lemma~\ref{lem:formal}. If $\End^0(A)$''')
    start = text.index(r"By the Tannakian equivalence $\End^0(A)$ is isomorphic to a")
    end = text.index(r'\end{proof}', start)
    text = text[:start] + r'''Using the covariant horizontal-fibre equivalence and the trace dualities
noted above, this gives a differential-module embedding
\[
 \End^0(A)\hookrightarrow\End(H_{p_e}^{\rm ss}).
\]
For the face module the leading spectrum is the set of critical values of
$p_e$. Corollary~\ref{cor:face-lattice}, after extension to $K_\infty$,
therefore makes every $c_i-c_j$ a difference of two such critical values.
This contradicts (F).
''' + text[end:]
    text = replace_once(text, 'with (F), its hypothesis on $\\Lambda$ holding by Lemma~\\ref{lem:formal};',
                        'with (F) and Lemma~\\ref{lem:formal};')
    # Explain why distributional uniqueness is used, without another general theorem.
    text = replace_once(text,
        'So on such an interval the density $\\rho$ of $I_D(dx\\wedge dy)$ satisfies:',
        'The compactly supported distributions are determined by their Laplace\ntransforms: restrict an identically zero entire transform to the imaginary\naxis and apply Fourier uniqueness. Hence on such an interval the density\n$\\rho$ of $I_D(dx\\wedge dy)$ satisfies:')
    # Explicit arithmetic specialization: the field of all reduced faces is finite.
    old = r'''faces by its one-variable case. Beukers' form of Siegel--Shidlovskii gives
equality of functional and numerical transcendence degrees at every
$\xi\in k^\times$, for the boundary vector and for the combined vector.'''
    new = r'''faces by its one-variable case. Let $d$ be the transcendence degree of
$K_{\partial,0}$ over $k(z)$. Part (ii) gives transcendence degree $d+\mu$
for the combined vector. Beukers' form of Siegel--Shidlovskii
\cite[Theorem~1.1, p.~370]{Beukers}, applied first to the boundary vector
and then to the combined vector, gives the numerical degrees $d$ and
$d+\mu$ at every $\xi\in k^\times$. Their difference is $\mu$.
The one-variable normal forms have only powers of $z$ as denominators, so
these reduced boundary values generate the stated face-value field at
all such $\xi$.'''
    text = replace_once(text, old, new)
    # Tighten the actual S6 implication without appealing to a more general statement.
    text = replace_once(text,
        r''' $2$-transitive Galois group the $\Q$-linear relations among the roots lie in
 $\Q\cdot(1,\dots,1)$, so the differences $c_i-c_1$ are $\Q$-independent.''',
        r''' relation $\sum a_i c_i=0$ with rational $a_i$, applying a transposition
 and subtracting yields $(a_i-a_j)(c_i-c_j)=0$. Thus all $a_i$ are equal;
 a relation among the differences has coefficient sum zero and is trivial.''')
    # Replace the introductory words left over by the preceding substitution.
    text = text.replace('it is $S_6$. For a\n relation', 'it is $S_6$. Given a\n relation')
    start = text.index(r'\section{What is cited, and how each citation was checked}')
    end = text.index(r'\begin{thebibliography}', start)
    text = text[:start] + INPUTS + '\n' + text[end:]
    text = text.replace(r'\begin{thebibliography}{9}', r'\begin{thebibliography}{99}')
    text = replace_once(text, r'\end{thebibliography}', EXTRA_BIB + '\n' + r'\end{thebibliography}')
    text = replace_once(text,
        r"The same statements hold with $k$ replaced by $\C$.",
        r"The same statements hold with $k$ replaced by $\C$, and the reduction and independence arguments also apply after specialization at every $z=\xi\ne0$.")
    text = replace_once(text,
        'every branch of every period of $\\alpha^\\sharp=\\omega^\\sharp/dq$ is a polynomial of\ndegree $<N$, hence single valued:',
        'every branch of every period of $\\alpha^\\sharp=\\omega^\\sharp/dq$ is a polynomial of\ndegree $<N$ (zero when $N=0$), hence single valued:')
    text = replace_once(text,
        'Numerical sanity checks, not part of the proof:',
        r'''For reproducibility, writing $\bar\chi_p$ for the monic reduction modulo $p$,
\begin{align*}
 \bar\chi_5&=t^6-t^4+2t^2-2t+2,\\
 \bar\chi_7&=(t+3)(t^5-3t^4+3t^2+3t+2),\\
 \bar\chi_{31}&=(t-14)(t^2+8t+10)(t^3+6t^2-14t+1).
\end{align*}
The displayed factors modulo $7,31$ are irreducible and squarefree.
Irreducibility modulo $5$ is certified by
\[
 \gcd(\bar\chi_5,t^{5^2}-t)=\gcd(\bar\chi_5,t^{5^3}-t)=1,
 \qquad t^{5^6}\equiv t\pmod{\bar\chi_5}.
\]
All these are exact polynomial computations in the accompanying certificate.
The supplementary exact checks give
$\operatorname{tr}(A_0^k(A_1+I))=0$ for $0\le k\le5$.
Since $A_0$ has simple spectrum, the Vandermonde matrix in its eigenvalues
shows that all six diagonal entries of $A_1$ in its eigenbasis are $-1$.
Thus the six powers in Lemma~\ref{lem:formal} are exactly $-1$.

Numerical sanity checks, not part of the proof:''')

    # Require removal of the old machinery, not just its citation.
    for obsolete in (r'\label{lem:exponents}', r'\Lambda_\infty', r'\Lambda(\End',
                     "by Bonnet's theorem", 'For a\n relation'):
        if obsolete in text:
            raise RuntimeError(f'Unrevised passage: {obsolete}')
    return text


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path('.'))
    args = parser.parse_args()
    folder = args.root / DIRECTORY
    frozen = folder / 'frozen/generic-single-chain-theorem.tex'
    raw = frozen.read_bytes()
    blob = hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
    if blob not in {'2ada1c0e48c01a925ad5f1795feff144753ba700',
                    'a7e998233ab4f096cb9bd5f40d641e07ca0dfddf'}:
        raise RuntimeError('The frozen candidate is not the audited revision')
    out = folder / 'successor/generic-single-chain-theorem-v2.tex'
    out.parent.mkdir(parents=True, exist_ok=True)
    result = successor(raw.decode())
    out.write_text(result, encoding='utf-8')
    if frozen.read_bytes() != raw:
        raise RuntimeError('Frozen source changed')
    print(f'Wrote {out}: {len(result.splitlines())} lines, SHA256 '
          f'{hashlib.sha256(result.encode()).hexdigest()}')

if __name__ == '__main__':
    main()
