#!/usr/bin/env python3
"""Apply the Paper I audit clarifications to the audited source, fail closed."""
from pathlib import Path
import hashlib
import re

source = Path('papers/01-exponential-integral-theorem/exponential-integral-theorem.tex')
raw = source.read_bytes()
blob = hashlib.sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest()
if blob != 'ada7aac70a76259095a63dfd3405c80edb4c93fd':
    raise SystemExit('Paper I differs from the audited source; reconcile before applying.')
original = text = raw.decode('utf-8')


def replace(old: str, new: str) -> None:
    global text
    if text.count(old) != 1:
        raise RuntimeError(f'Expected one occurrence of revision anchor: {old[:100]!r}')
    text = text.replace(old, new, 1)


replace(r'''Siegel--Shidlovskii theorem \cite{Beukers}.''', r'''Siegel--Shidlovskii theorem
\cite[Theorem~3.2 and Lemma~3.1]{Beukers}.  No linear independence
hypothesis on the coordinates is required.''')

replace(r'''$k\le n\ell\le nm$.  Since''', r'''$k\le n\ell\le nm$, and the total exponent of $d$ needed for each term
satisfies $\ell+j+k+2\le(n+1)m+j+2$.  Since''')

replace(r'''The map $q$ is finite, hence proper and small.  The small-map form of the
decomposition theorem gives''', r'''The map $q$ is finite, hence proper and small.  The small-map
intermediate-extension identity
\cite[Remark~4.2.4]{deCataldoMigliorini} gives''')

replace(r'''so this perverse sheaf is semisimple
\cite{deCataldoMigliorini}.  Under the Riemann--Hilbert correspondence and''', r'''Intermediate extension preserves direct sums and takes irreducible local
systems to simple perverse sheaves.  Thus the semisimplicity of $\Lcal$
makes this perverse sheaf semisimple.  Under the Riemann--Hilbert
correspondence and''')

replace(r'''\end{equation}
Fourier transformation is an exact equivalence''', r'''\end{equation}
This is the inverse convention to the transform with kernel $e^{t\tau}$
in \cite[\S1.3.b]{SabbahFourier}; our convention corresponds to the
kernel $e^{-t\tau}$.
Fourier transformation is an exact equivalence''')

replace(r'''The generic direct image along the $x$-line is therefore the degree-zero
cohomology of''', r'''In particular,
$\partial_x(p\widehat\delta_q)=(p'-\tau q'p)\widehat\delta_q$:
the relation on the generator induces a minus sign in the differential
on coefficient polynomials.  The generic direct image along the $x$-line
is therefore the degree-zero cohomology of''')

replace(r'''This is the standard algebraic Fourier--Laplace direct-image model; see
\cite{SabbahFourier} for the convention and construction.''', r'''This is the algebraic Fourier--Laplace direct-image construction of
\cite[\S1.3.b]{SabbahFourier}, with the inverse convention fixed in
\eqref{eq:Fourier-convention}.''')

replace(r'''\end{equation}
The classes of $1,x,\ldots,x^{n-2}$ form a basis:''', r'''\end{equation}
The connection descends to this quotient because
\begin{equation}\label{eq:twisted-commutator}
  [\partial_z+q,\partial_x+zq']=q'-q'=0.
\end{equation}
The classes of $1,x,\ldots,x^{n-2}$ form a basis:''')

start = r'''For each $\tau$ with $\lambda_\tau=\lambda$, the operator'''
end = r'''This also proves the asserted block preservation.'''
i, j = text.index(start), text.index(end) + len(end)
replace(text[i:j], r'''Fix $\tau$ with $\lambda_\tau=\lambda$, and write $m=m_\tau$.
Define
\[
  F_{\tau,0}=0,\qquad
  F_{\tau,k}=\Span_\C\{g_{\tau,1},\ldots,g_{\tau,k}\}
  \quad(1\le k\le m).
\]
We claim the explicit flag relation
\begin{equation}\label{eq:local-flag}
  \overline D_\lambda g_{\tau,k}
  +\frac{m+1-k}{m+1}g_{\tau,k}
  \in F_{\tau,k-1}
  \qquad(1\le k\le m).
\end{equation}
To prove it, write $y=x-\tau$ and
$q-\lambda=ay^{m+1}+O(y^{m+2})$, with $a\ne0$.  Euclidean division gives
\[
  \mathsf Dg_{\tau,k}
  =-\left(\frac{q-\lambda}{(x-\tau)^k}\right)',
\]
so
\[
  g_{\tau,k}=(m+1)a y^{m-k}+O(y^{m-k+1}),\qquad
  \mathsf Dg_{\tau,k}=-(m+1-k)a y^{m-k}+O(y^{m-k+1}).
\]
Their combination in \eqref{eq:local-flag} therefore vanishes at $\tau$
to order at least $m-k+1$.  If $\sigma\ne\tau$ has the same critical
value, then $(x-\tau)^{-k}$ is regular at $\sigma$, while $q-\lambda$
vanishes there to order $m_\sigma+1$.  Hence
$\mathsf Dg_{\tau,k}$ vanishes at $\sigma$ to order at least $m_\sigma$,
and its component in that factor of $\C[x]/(q')$ is zero.

Under the Chinese remainder decomposition, $F_{\tau,k-1}$ consists
precisely of the classes supported in the $\tau$-factor and divisible
there by $y^{m-k+1}$.  Projection by $\pi_\lambda$ removes all factors
over other critical values.  The preceding vanishing statements thus
prove \eqref{eq:local-flag}.  In particular, every $F_{\tau,k}$ is
$\overline D_\lambda$-invariant.  On each $F_{\tau,m}$ the matrix in the
ordered basis $g_{\tau,1},\ldots,g_{\tau,m}$ is triangular, with diagonal
\begin{equation}\label{eq:local-spectrum}
  -\frac{m}{m+1},
  -\frac{m-1}{m+1},\ldots,-\frac1{m+1}.
\end{equation}
As $\tau$ ranges over the critical points with value $\lambda$, these
lists give the full spectrum of $\overline D_\lambda$, with
multiplicities.  In particular, all its eigenvalues lie in $(-1,0)$,
including when distinct critical points have the same value and different
ramification indices.''')

replace(r'''decomposition of $\mathsf C$.  Projecting the second identity to a
nonzero $\lambda$-block yields''', r'''decomposition of $\mathsf C$.  Choose a critical value $\lambda$ for
which $Q_{d,\lambda}\ne0$; the value $\lambda=0$ is allowed.
Projecting the second identity to this block yields''')

replace(r'''$W$.  Equation \eqref{eq:lifted} puts $\boldsymbol\phi$ in $\Rcal$, so
its value at $1$ lies in $W$.  Hence the constant row''', r'''$W$.  Equation \eqref{eq:lifted} puts $\boldsymbol\phi$ in $\Rcal$.
Every constant linear form annihilating $W$ therefore annihilates
$\boldsymbol\phi(z)$ identically, and hence also annihilates
$\boldsymbol\phi(1)$.  Thus $\boldsymbol\phi(1)\in W$, without
specializing any rational basis.  Hence the constant row''')

replace(r'''It remains only to descend their coefficients.  The Taylor coefficients of
$U_0$ and all $\lambda\in\Lambda$ lie in $\Qbar$.  Applying any
automorphism of $\C$ fixing $\Qbar$ to \eqref{eq:exp-poly}, and using the
uniqueness of the expansion over $\C(z)$, fixes every $p_\lambda$.
Therefore $p_\lambda\in\Qbar[z]$.''', r'''It remains to show that their coefficients are algebraic.  Choose an
integer $d\ge0$ bounding the degrees of all the $p_\lambda$, write
$p_\lambda(z)=\sum_{k=0}^d a_{\lambda,k}z^k$, and put
$M=(d+1)|\Lambda|$.  Differentiating \eqref{eq:exp-poly} at $0$ gives
\begin{equation}\label{eq:finite-descent}
  U_0^{(m)}(0)
  =\sum_{\lambda\in\Lambda}\sum_{k=0}^d
     a_{\lambda,k}
     \left.\frac{d^k}{dt^k}t^m\right|_{t=\lambda}
  \qquad(0\le m<M).
\end{equation}
The square coefficient matrix has algebraic entries and is invertible.
Indeed, its transpose is the Hermite evaluation map
\[
  \Qbar[t]_{<M}\longrightarrow\Qbar^M,
  \qquad f\longmapsto
  \bigl(f^{(k)}(\lambda)\bigr)_{\lambda\in\Lambda,\,0\le k\le d}.
\]
A polynomial in its kernel is divisible by
$\prod_{\lambda\in\Lambda}(t-\lambda)^{d+1}$, of degree $M$, so must
vanish.  Thus the map is injective and hence invertible.  All derivatives
$U_0^{(m)}(0)$ are algebraic by \eqref{eq:coefficient-formula}; solving
\eqref{eq:finite-descent} yields $a_{\lambda,k}\in\Qbar$.  Therefore
$p_\lambda\in\Qbar[z]$.  This argument uses only finite linear algebra,
not the action of field automorphisms on analytic limits.''')

replace(r'''\section{The moment system}''', r'''\paragraph{Scope of the differential form.}
The fixed form $dx$ is essential.  For $q(x)=x(x-1)$ and
$r(x)=2x^2-x+1$, one has
\[
  r(x)e^{q(x)}=\frac{d}{dx}\bigl(xe^{q(x)}\bigr),
  \qquad \int_0^1 r(x)e^{q(x)}\,dx=1.
\]
Yet the function $\int_0^1 r(x)e^{zq(x)}\,dx$ is not identically zero:
its value at $z=0$ is $7/6$.  Thus \cref{thm:rigidity} does not extend
unchanged to arbitrary polynomial amplitudes.

\section{The moment system}''')

statement_pattern = re.compile(r'\\begin\{(theorem|proposition|lemma|corollary)\}.*?\\end\{\1\}', re.S)
if [m.group() for m in statement_pattern.finditer(original)] != [m.group() for m in statement_pattern.finditer(text)]:
    raise RuntimeError('A theorem, proposition, lemma, or corollary statement changed.')
if original.split(r'\begin{document}')[0] != text.split(r'\begin{document}')[0]:
    raise RuntimeError('Front matter changed.')
labels = re.findall(r'\\label\{([^}]+)\}', text)
if len(labels) != len(set(labels)):
    raise RuntimeError('Duplicate labels.')
if not set(re.findall(r'\\label\{([^}]+)\}', original)).issubset(labels):
    raise RuntimeError('An existing label was removed.')
source.write_text(text, encoding='utf-8')

note = Path('notes/provenance/paper-i-audit-clarifications-2026-09-28.md')
if note.exists():
    raise RuntimeError('Do not overwrite a historical revision note.')
note.write_text('''# Paper I: audit clarifications, 2026-09-28

Baseline: commit `c3b1e3d703c6c9df54a740e8c102608b544c4ec6`;
Paper I source blob `ada7aac70a76259095a63dfd3405c80edb4c93fd`.

This revision follows the adversarial audit discussed on 2026-09-28.
The audit found no fatal gap; this is not independent peer review or a
formal proof certificate. Historical audit reports are left unchanged.

## Changes

- Make the local invariant flag in the compressed-residue calculation
  explicit, including the Chinese remainder argument, vanishing at other
  critical points over the same value, and the resulting full spectrum.
- State that the nonzero leading-coefficient block may lie over the
  critical value zero.
- Replace the compressed Galois-descent paragraph with an explicit finite
  derivative system and an elementary Hermite-interpolation invertibility
  proof.
- State the inverse Fourier convention relative to Sabbah, track the
  induced differential on coefficient polynomials, and display the
  commutator that makes the quotient connection well-defined.
- Cite Beukers, Theorem 3.2 and Lemma 3.1, and de Cataldo--Migliorini,
  Remark 4.2.4, precisely; explain the intermediate-extension step.
- Explain specialization into the constant subspace using its constant
  annihilator, and spell out the denominator exponent bound.
- Add the elementary polynomial-amplitude counterexample to delimit the
  scope of the fixed form dx.

All existing theorem, proposition, lemma, and corollary statements,
all existing cross-reference labels, the author list, the title,
and the explicit August 2026 manuscript date are preserved. The changes
expand proofs and delimit scope; they do not enlarge the theorem.

## Verification protocol

Run `make test`, `make pdf`, and `make check`. Preserve the committed PDFs
and manifest records of the seven unchanged documents. Inspect the
revised Paper I PDF visually before merging. Compilation and regression
checks do not constitute a new mathematical certification.
''', encoding='utf-8')
print(f'Updated {source}: {len(raw)} -> {len(text.encode())} bytes')
print(f'Preserved {len(list(statement_pattern.finditer(original)))} theorem-like statements and all original labels.')
