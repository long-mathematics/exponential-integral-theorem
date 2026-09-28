#!/usr/bin/env python3
"""Apply the reviewed Paper II changes to the exact audited source snapshot.

Temporary revision helper: removed from the final manuscript pull-request diff.
Every replacement is checked, and theorem numbering and existing labels are kept.
"""
from pathlib import Path
import hashlib
import json
import re

SOURCE = Path('papers/02-compact-polynomial-line-kz/linear-kz-affine-line.tex')
BASE = '093e260aa41a1d71ea6f12b41a0a84ed9c6c1463'
EXPECTED_SHA256 = 'd1397ca7e5ba83374fb15ee31d93b5641498e3e108bec0f0f3d712fcda210889'
original_bytes = SOURCE.read_bytes()
if hashlib.sha256(original_bytes).hexdigest() != EXPECTED_SHA256:
    raise SystemExit('The Paper II source has changed since the audited baseline.')
original = original_bytes.decode('utf-8')
text = original
changes = []


def replace_once(old: str, new: str, description: str) -> None:
    global text
    count = text.count(old)
    if count != 1:
        raise SystemExit(f'{description}: expected one match, found {count}')
    text = text.replace(old, new, 1)
    changes.append(description)


replace_once(
    r'''while the general formal theorem first applies
\cref{lem:twisted-reduction} at $z=1$.
\end{remark}''',
    r'''while the general formal theorem first applies
\cref{lem:twisted-reduction} at $z=1$.

For example, take $q(x)=x(x-1)$, $r(x)=2x^2-x+1$, and
$\Delta=[1]-[0]$.  Then $r=R'+q'R$ with $R=x$, so $s=0$ and
\[
  \int_0^1 r(x)e^{q(x)}\,dx
  =\bigl[xe^{q(x)}\bigr]_0^1=1.
\]
Nevertheless, $I_{q,r,\Delta}(0)=7/6$, so the deformed function is not
identically zero.  The algebraic value at $1$ is entirely an endpoint term;
the reduced transfer theorem cannot be applied to the unreduced function.
\end{remark}''',
    'Add the polynomial-amplitude scope regression example')

replace_once(
    r'''This is the degree-one case of Beukers' complete lifting theorem
\cite[Theorems~1.3 and~3.2]{Beukers}.''',
    r'''This is the linear lifting theorem
\cite[Theorem~3.2 and Lemma~3.1]{Beukers}.  No linear independence
hypothesis on the coordinates is required.''',
    'Specify the linear Beukers reference and dependent-coordinate scope')

replace_once(
    r'''The row
$\boldsymbol\phi$ in \eqref{eq:lifted-relation} belongs to $\Rcal$ and is
regular at $1$, so $v=\boldsymbol\phi(1)\in W$.  Hence the constant row
$v$ belongs to $\Rcal$, and''',
    r'''The row
$\boldsymbol\phi$ in \eqref{eq:lifted-relation} belongs to $\Rcal$ and is
regular at $1$.  Choose a constant matrix $T_W$ whose columns span the
annihilator of $W$.  Then $\boldsymbol\phi(z)T_W=0$, and evaluation at
$1$ gives $vT_W=0$.  Thus $v\in W$.  Hence the constant row
$v$ belongs to $\Rcal$, and''',
    'Make specialization into the constant relation subspace explicit')

replace_once(
    r'''Finally, $F$ has Taylor coefficients in $\Qbar$, and every
$\lambda\in\Lambda$ is algebraic.  Applying any automorphism of
$\C/\Qbar$ coefficientwise to \eqref{eq:F-exp-polynomial} and using the
uniqueness furnished by \cref{lem:distinct-exponentials} shows that every
$p_\lambda$ is fixed.  Hence $p_\lambda\in\Qbar[z]$.''',
    r'''Finally, the coefficients of the $p_\lambda$ are algebraic by a finite
Hermite-interpolation argument.  If every $p_\lambda$ is zero, there is
nothing to prove.  Otherwise choose an integer $\ell\ge1$ such that
$\deg p_\lambda<\ell$ for every $\lambda$, write
\[
  p_\lambda(z)=\sum_{k=0}^{\ell-1}c_{\lambda,k}z^k,
  \qquad h=\ell|\Lambda|,
\]
and differentiate \eqref{eq:F-exp-polynomial} at zero.  For $0\le m<h$,
\[
  F^{(m)}(0)
  =\sum_{\lambda\in\Lambda}\sum_{k=0}^{\ell-1}
    c_{\lambda,k}
    \left.\frac{d^k}{dt^k}t^m\right|_{t=\lambda}.
\]
The coefficient matrix is the transpose of the matrix of the Hermite
jet-evaluation map
\[
  \Qbar[t]_{<h}\longrightarrow
  \bigoplus_{\lambda\in\Lambda}\Qbar^\ell,
  \qquad
  H\longmapsto
  \bigl(H^{(k)}(\lambda)\bigr)_{\lambda,\,0\le k<\ell}.
\]
This map is injective: an element of its kernel is divisible by
$\prod_{\lambda\in\Lambda}(t-\lambda)^\ell$, whose degree is $h$.
Since the source and target both have dimension $h$, the matrix is
invertible over $\Qbar$.  Every $F^{(m)}(0)$ is algebraic, so the unique
solution has $c_{\lambda,k}\in\Qbar$.  Hence
$p_\lambda\in\Qbar[z]$.''',
    'Replace field-automorphism descent by finite Hermite interpolation')

replace_once(
    r'''If $F_1,\ldots,F_N$ are linearly independent over $\Qbar$ as entire
functions and $\beta_1,\ldots,\beta_M$ are distinct, then''',
    r'''Let $F_j=I_{q_j,s_j,\Delta_j}$ satisfy the reduced hypotheses of
\cref{thm:transfer}, and let $\beta_1,\ldots,\beta_M\in\Qbar$ be
distinct.  If $F_1,\ldots,F_N$ are linearly independent over $\Qbar$ as
entire functions, then''',
    'Restate the inherited reduced hypotheses in the independence corollary')

replace_once(
    r'''If $B\subset U(\C)$ is nonempty, connected, and simply connected, and
$\widetilde B$ is a connected component of $\pi^{-1}(B)$, then the''',
    r'''The morphism $\pi$ is finite \'{e}tale over $U$.
If $B\subset U(\C)$ is a nonempty, connected, simply connected open set,
and $\widetilde B$ is a connected component of $\pi^{-1}(B)$, then the''',
    'State the etale property and require an open analytic neighborhood')

replace_once(
    r'''Let $L$ be a
finite Galois extension of $\Qbar(t)$ containing the compositum of the
Galois closures of all the $K_j$, and let $Y$ be the normalization of
$\Aone_t$ in $L$.''',
    r'''Inside a fixed algebraic closure of $\Qbar(t)$, let
$K_j^{\mathrm{gal}}$ be the Galois closure of $K_j/\Qbar(t)$, and take
\[
  L=K_1^{\mathrm{gal}}\cdots K_N^{\mathrm{gal}}
\]
to be their compositum itself.  This is a finite Galois extension of
$\Qbar(t)$.  Let $Y$ be the normalization of $\Aone_t$ in $L$.''',
    'Correct the cover construction to use the exact Galois compositum')

replace_once(
    r'''and a component $\widetilde B_e$ of $\pi^{-1}(B_e)$.  The lift of the
edge interior has a compact closure $\eta_e$ in $Y(\C)$; after a harmless
reparametrization it is a finite piecewise $C^1$ relative one-chain.  Orient
it so that $\pi_*\eta_e=e$.''',
    r'''and a component $\widetilde B_e$ of $\pi^{-1}(B_e)$.  We justify that
the lifted edge defines an admissible relative chain.  Since $\pi$ is
finite, it is proper, so the lift of the edge interior has compact closure
in $\pi^{-1}(\overline e)$.  At a point over an endpoint $t_0$, a local
holomorphic coordinate $u$ gives
\[
  t-t_0=u^r
\]
for the ramification index $r\ge1$.  This model shows that the lift has a
unique limit at each endpoint.  Reparametrizing a terminal straight
segment by an $r$-th power makes its lift $C^1$ up to that endpoint.
Doing this at both ends gives a finite piecewise $C^1$ chain $\eta_e$.
Its endpoints lie in finite fibers over the algebraic vertices of $T$;
since $\pi$ is defined over $\Qbar$, these endpoints belong to
$Y(\Qbar)$.  Thus $[\eta_e]\in H_1^{\mathrm{rel}}(Y)$.  Orient it so
that $\pi_*\eta_e=\overline e$ with the chosen orientation.''',
    'Justify compact lifted edges, power reparametrization, and algebraic boundary')

replace_once(
    r'''Summing over all edges and using
\eqref{eq:edge-decomposition-formal} proves
\eqref{eq:formal-functional-relation}.''',
    r'''Each displayed identity is a separate relative-chain relation, so the
lifts $\eta_e$ may be chosen independently for different edges.  Summing
these identities and using \eqref{eq:edge-decomposition-formal} proves
\eqref{eq:formal-functional-relation}.''',
    'Explain why independently chosen edge lifts suffice')

labels_before = re.findall(r'\\label\{([^}]+)\}', original)
labels_after = re.findall(r'\\label\{([^}]+)\}', text)
assert labels_before == labels_after, 'Existing cross-reference labels changed'
environments = r'\\begin\{(theorem|proposition|lemma|corollary|definition|remark)\}'
assert re.findall(environments, original) == re.findall(environments, text)
for command in ('title', 'author', 'date'):
    before = original.split('\\' + command + '{', 1)[1].split('\n\n', 1)[0]
    after = text.split('\\' + command + '{', 1)[1].split('\n\n', 1)[0]
    assert before == after, f'{command} changed'
for label in ('thm:main', 'thm:transfer'):
    pattern = r'\\begin\{theorem\}.*?\\end\{theorem\}'
    before = next(s for s in re.findall(pattern, original, flags=re.S) if '\\label{' + label + '}' in s)
    after = next(s for s in re.findall(pattern, text, flags=re.S) if '\\label{' + label + '}' in s)
    assert before == after, f'Main statement changed: {label}'
SOURCE.write_text(text, encoding='utf-8')
report = {
    'baseline_commit': BASE,
    'source': str(SOURCE),
    'original_source_sha256': EXPECTED_SHA256,
    'revised_source_sha256': hashlib.sha256(text.encode()).hexdigest(),
    'preserved_labels': len(labels_before),
    'preserved_numbered_environments': len(re.findall(environments, original)),
    'changes': changes,
}
Path('.build').mkdir(exist_ok=True)
Path('.build/paper-ii-audit-validation.json').write_text(json.dumps(report, indent=2) + '\n')

note = f'''# Paper II: audit corrections and clarifications, 2026-09-28

Baseline: commit `{BASE}`; Paper II source blob
`657193696c72967fdfaf7ab9dbd099ec1c24a8af`.

This revision follows the adversarial audit discussed on 2026-09-28.
The audit identified a local error in the auxiliary-cover construction:
an arbitrary larger Galois extension could introduce new ramification.
Choosing the exact compositum corrects that construction. No fatal gap
was found in the main argument; this is not independent peer review or a
formal proof certificate. Historical audit reports are unchanged.

## Changes

- Choose the compositum itself of the polynomial covers' Galois closures,
  rather than an arbitrary containing Galois extension. State the etale
  property over the specified open set, and require analytic neighborhoods
  to be open.
- Prove that lifted closed edges extend to compact piecewise C1 relative
  chains with algebraic boundary, using the local ramification model and
  power reparametrization. Explain that different edges need not lift to
  one global chain on the auxiliary curve.
- Repeat the inherited reduced-degree and algebraic-exponent hypotheses
  explicitly in Corollary 7.6. This corrects its stand-alone wording, not
  the intended scope of the transfer theorem.
- Replace the coefficientwise field-automorphism descent with a finite
  invertible Hermite-interpolation system over the algebraic numbers.
- Explain specialization into the constant relation subspace by its
  constant annihilator; cite Beukers Theorem 3.2 and Lemma 3.1 precisely,
  including applicability to dependent coordinates.
- Add the polynomial-amplitude counterexample to the existing reduction
  remark: its algebraic value is an endpoint term, not a counterexample
  to the reduced transfer theorem.

## Preserved scope

The main injectivity and transfer statements are unchanged, as are all
{len(labels_before)} original cross-reference labels and the ordering of all
{len(re.findall(environments, original))} theorem-like, definition, and remark environments.
No numbered statement is added or removed. Authorship, title, contact
information, and the explicit August 2026 manuscript date are preserved.
The cover lemma and independence corollary have the explicit corrections
described above. Other manuscripts and their committed PDFs are unchanged.

The finite exact-arithmetic experiments from the audit are stress tests,
not a proof certificate for the general theorem.
'''
Path('notes/provenance/paper-ii-audit-clarifications-2026-09-28.md').write_text(note, encoding='utf-8')
print(json.dumps(report, indent=2))
