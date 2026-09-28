#!/usr/bin/env python3
"""Apply the Paper III audit revisions to an exact source baseline."""
from pathlib import Path
from collections import Counter
import hashlib
import json
import re

ROOT = Path('.')
MAIN = ROOT / 'papers/03-complete-polynomial-kz/polynomial-kz-affine-line.tex'
SUPP = ROOT / 'papers/03-complete-polynomial-kz/polynomial-kz-supplement.tex'
EXPECTED = {
    MAIN: 'b753c96616dc10207d0c911550cc70c36a1f5bcc',
    SUPP: 'c554482f19d277d11fcab87b42b7d9f11388816c',
}


def blob_sha(raw):
    return hashlib.sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest()


originals = {}
for path, expected in EXPECTED.items():
    raw = path.read_bytes()
    if blob_sha(raw) != expected:
        raise SystemExit(f'{path} differs from the reviewed baseline; reconcile first.')
    originals[path] = raw.decode('utf-8')


def replace(text, old, new):
    if text.count(old) != 1:
        raise RuntimeError(f'Expected one revision anchor: {old[:100]!r}')
    return text.replace(old, new, 1)


main = originals[MAIN]
main = replace(main, r'''Horizontal projectors are Laurent polynomials in the
adjoined exponentials.  A Laurent-polynomial gauge separates the coordinates''', r'''Horizontal projectors are Laurent polynomials in the
adjoined exponentials.  An explicit gauge built from the spectral projectors
of the constant connection matrix separates the coordinates''')

anchor = r'''The appearance of exponential coefficients is necessary.'''
gauge = r'''\begin{lemma}[Explicit simultaneous spectral gauge]
\label{lem:spectral-gauge}
Partition $\Spec(C)$ by
\[
  \alpha\sim\beta\quad\Longleftrightarrow\quad\alpha-\beta\in\Gamma,
\]
and choose a representative $\rho_B$ in every equivalence class $B$.
Let $\pi_\alpha$ be the spectral projector of $C$ at $\alpha$, and set
\begin{equation}\label{eq:spectral-gauge}
  G(z)=\sum_{\alpha\in\Spec(C)}
       e^{(\alpha-\rho_{[\alpha]})z}\pi_\alpha.
\end{equation}
Then $G\in\operatorname{GL}_N(A_\Gamma)$, $G(0)=I$, and every horizontal
endomorphism $P\in M_N(K_\Gamma)$ satisfies
\begin{equation}\label{eq:simultaneous-constant}
  G^{-1}PG=P(0).
\end{equation}
\end{lemma}

\begin{proof}
All exponents in \eqref{eq:spectral-gauge} belong to $\Gamma$.  The
orthogonal spectral projectors give
\[
  G^{-1}(z)=\sum_{\alpha\in\Spec(C)}
           e^{-(\alpha-\rho_{[\alpha]})z}\pi_\alpha,
  \qquad G(0)=G^{-1}(0)=I.
\]
By \cref{thm:endomorphism-normal-form}, the block from $V_\alpha$ to
$V_\beta$ is
\[
  \pi_\beta P(z)\pi_\alpha
  =\begin{cases}
     e^{(\beta-\alpha)z}\pi_\beta P(0)\pi_\alpha,
       &\beta-\alpha\in\Gamma,\\
     0,&\beta-\alpha\notin\Gamma.
   \end{cases}
\]
In the first case $[\alpha]=[\beta]$, so conjugation by $G$ cancels the
exponential factor; in the second case the block is zero.  This proves
\eqref{eq:simultaneous-constant} simultaneously for all $P$.  The
construction uses only differences within $\Gamma$, so no enlargement of
the exponential coefficient ring is needed.
\end{proof}

'''
main = replace(main, anchor, gauge + anchor)

old = r'''Let $L_h/\C(z)$ be a Picard--Vessiot field for the homogeneous system and
let $G$ be its Galois group.  Semisimplicity of the faithful solution
representation implies that $G$ is reductive.  The extension
$K_\Gamma/\C(z)$ is Picard--Vessiot with torus Galois group.  In a common
differential overfield, put
\[
  J=L_h\cap K_\Gamma.
\]
The subgroup of the torus fixing $J$ is normal, so $J/\C(z)$ is itself a
Picard--Vessiot extension.  Therefore
$\operatorname{Gal}(L_h/J)$ is a closed normal subgroup of the reductive
group $G$, hence is reductive in characteristic zero.  The standard
base-change identification
\[
  \operatorname{Gal}(L_hK_\Gamma/K_\Gamma)
  \simeq\operatorname{Gal}(L_h/J)
\]
proves the assertion.  We use the Picard--Vessiot correspondence and
base-change results in \cite[Chapter~1]{vanDerPutSinger}.'''
new = r'''Put $F=\C(z)$, let $L_h/F$ be a Picard--Vessiot field for the
homogeneous system, and let $H_h$ be its Galois group.  Semisimplicity of
the faithful solution representation implies that $H_h$ is reductive.
The extension $K_\Gamma/F$ is Picard--Vessiot with torus group $\mathbf T$.
Choose a joint Picard--Vessiot realization, with no new constants, and
write $L=L_hK_\Gamma$ and $\mathcal G=\operatorname{Gal}(L/F)$.
Restriction gives surjective morphisms
\[
  \mathcal G\longrightarrow H_h,
  \qquad \mathcal G\longrightarrow\mathbf T.
\]
Let $\mathcal N$ be the kernel of the second morphism.  Restriction to
$L_h$ identifies $\mathcal N$ with a closed normal subgroup of $H_h$:
normality follows from the surjectivity of the first morphism, and
injectivity follows because an automorphism fixing both $L_h$ and
$K_\Gamma$ fixes their compositum.  A closed normal subgroup of a
reductive algebraic group in characteristic zero is reductive.
Now $\mathcal N=\operatorname{Gal}(L/K_\Gamma)$ is the
Picard--Vessiot group of the base-changed homogeneous system, so its
solution representation is semisimple.  The restriction and fixed-field
identifications used here are the Picard--Vessiot correspondence of
\cite[Chapter~1]{vanDerPutSinger}.'''
main = replace(main, old, new)

main = replace(main, r'''\cref{thm:endomorphism-normal-form}, $P\in M_N(A_\Gamma)$.  Its image and
kernel in $A_\Gamma^N$ are finitely generated projective modules.  Since
$A_\Gamma$ is a Laurent polynomial ring over a field, Swan's theorem makes
both free \cite{SwanLaurent}.  Choosing bases gives
$S\in\operatorname{GL}_N(A_\Gamma)$ such that''', r'''\cref{thm:endomorphism-normal-form}, $P\in M_N(A_\Gamma)$.
By \cref{lem:spectral-gauge}, $G^{-1}PG=P(0)$.  Since $P(0)$ is a
constant idempotent, choose $S_0\in\operatorname{GL}_N(\C)$ with
\[
  S_0P(0)S_0^{-1}=\operatorname{diag}(0_t,I_{N-t}).
\]
Set $S=S_0G^{-1}\in\operatorname{GL}_N(A_\Gamma)$.  This explicit choice
gives''')

main = replace(main, r'''The matrices
$S$ and $S^{-1}$ are finite Laurent sums of exponential functions and are
invertible at zero.  Hence
$B_0v_0=\mathbf a-\mathbf V_0$ is a single-valued meromorphic homogeneous
solution at zero after returning through $S^{-1}$.  By
\cref{lem:meromorphic-exclusion}, it vanishes.  Therefore''', r'''The matrices $S$ and $S^{-1}$ are entire and invertible at zero.
For the transformed homogeneous connection,
\[
  A_S=(S'+SA)S^{-1}=B'B^{-1}
\]
is block diagonal.  Thus
\[
  h=\binom{B_0v_0}{0},\qquad y=S^{-1}h
\]
satisfy $h'=A_Sh$ and $y'=Ay$.  Moreover,
$B_0v_0=\mathbf a-\mathbf V_0$ is single-valued and meromorphic at zero:
$\mathbf a\in K^t$ is meromorphic there, and $\mathbf V_0$ is entire.
The same is true of $y$, so \cref{lem:meromorphic-exclusion} gives
$y=0$, hence $B_0v_0=0$.  It follows that''')

main = replace(main, r'''\bibitem{SwanLaurent}
R.~G.~Swan,
\emph{Projective modules over Laurent polynomial rings},
Trans. Amer. Math. Soc. \textbf{237} (1978), 111--120.
\href{https://doi.org/10.1090/S0002-9947-1978-0469906-4}{doi:10.1090/S0002-9947-1978-0469906-4}.

''', '')

supp = originals[SUPP]
supp = replace(supp, r'''A proposed algebraic relation over $\mathbb E$ involves only finitely many
exponential values.  Let $\Gamma\subset k$ be generated by their indices and
the $\beta_j$.  Form the $E$-function vector consisting of the $H_{\beta_j}$
and a basis of exponential functions for $\Gamma$.  By
\cref{thm:H-functional}, its functional transcendence degree is
$\operatorname{rank}\Gamma+m$.  Beukers' theorem gives the same
transcendence degree at $z=1$, while \cref{thm:LW} gives transcendence degree
$\operatorname{rank}\Gamma$ for the exponential-value subfield.  The $m$
quadratic values are therefore algebraically independent over that subfield.''', r'''A proposed algebraic relation over $\mathbb E$ involves only finitely many
exponential values.  Let $\Gamma\subset k$ be generated by their indices
and the $\beta_j$, and choose a $\mathbb Z$-basis
$\omega_1,\ldots,\omega_r$ of $\Gamma$.  Form the $E$-function vector
\[
  \bigl(H_{\beta_1},\ldots,H_{\beta_m},
        e^{\omega_1z},\ldots,e^{\omega_rz},
        e^{\beta_1z},\ldots,e^{\beta_mz}\bigr)^{\mathsf T},
\]
omitting repeated coordinates.  It is closed under a first-order system
over $k(z)$: equation \eqref{eq:H-series-ode} supplies the derivatives of
the $H_{\beta_j}$, while each exponential has derivative equal to its
index times itself.  The only possible finite pole is zero.

The forcing exponentials $e^{\beta_jz}$ are Laurent monomials in the
basis exponentials, so adjoining them does not change the generated
field.  Their explicit inclusion is nevertheless needed for the displayed
linear differential system.  By \cref{thm:H-functional}, the functional
transcendence degree is $r+m$.  Beukers' theorem gives the same
transcendence degree at $z=1$.  By \cref{thm:LW}, the exponential-value
subfield $k(e^\lambda:\lambda\in\Gamma)$ has transcendence degree $r$.
The $m$ quadratic values are therefore algebraically independent over this
subfield, which contains the coefficients of the proposed relation.''')

supp = replace(supp, r'''The width of the spectrum in \eqref{eq:quartic-D2} is one.  A pole can only
have order one and, after projection to the symmetric square, its leading
term is the map $E_{0,5}$ from the lowest residue line to the highest.  Write''', r'''Poles away from zero are excluded by pole-order comparison.  The tensor
residue has the same spectrum as \eqref{eq:quartic-D2}, of width one.
Thus a pole at zero can have at most order one, and every rational
horizontal endomorphism is a finite Laurent polynomial.

We first exclude positive Laurent powers, without assuming regularity at
zero.  Since $(a,b)\ne(0,0)$, the critical multiplicities of $q$ are
$1+1+1$ or $2+1$.  Each compressed residue of $\Mcal_q$ therefore has
spectrum in $[-2/3,-1/3]$.  By \cref{lem:tensor-compression}, each
compressed tensor residue has spectrum in $[-4/3,-2/3]$, of width $2/3$.
If $d\ge1$ were the highest Laurent degree, the leading coefficient
would commute with $C^{(2)}$.  On a nonzero eigenspace block, the next
coefficient equation would be
\[
  dQ_{d,\Lambda}=[Q_{d,\Lambda},\overline D^{(2)}_\Lambda].
\]
The commutator on the right has spectrum in $[-2/3,2/3]$, excluding the
positive integer $d$.  This argument uses only the two highest
coefficients and so also applies in the presence of a pole at zero.

If a pole remained, its coefficient would map the lowest residue line to
the highest.  Both extreme lines are one-dimensional and belong to the
symmetric square.  Projection on both sides to this horizontal direct
summand therefore preserves the nonzero polar coefficient.  After scaling
that projection, its leading term is $E_{0,5}$.  With all positive powers
already excluded, write''')

supp = replace(supp, r'''If $q$ is not pure, its critical multiplicities are $1+1+1$ or $2+1$.
The compressed tensor residues then lie in an interval of width less than
one, so positive degree at infinity is excluded exactly as in
\cref{thm:degree23}; \cref{lem:quartic-pole} excludes the only possible pole
at zero.''', r'''For a non-pure quartic, the proof of \cref{lem:quartic-pole} excludes
positive Laurent powers before excluding the only possible pole at zero.
There are no poles away from zero.  The rational horizontal endomorphism
is therefore constant.''')

supp = replace(supp, r'''A relation over $\mathbb E$ involves finitely many exponential values.  Form
the $E$-function vector consisting of the $E_{\alpha_j}$, the constant
function $1$, and exponential functions whose indices generate the finite
coefficient field.  Apply \cref{thm:Ein-functional}, Beukers' transcendence-
degree equality at $z=1$, and \cref{thm:LW}.''', r'''A proposed relation over $\mathbb E$ involves finitely many exponential
values.  Let $\Gamma\subset k$ be generated by their indices and the
$\alpha_j$, and choose a $\mathbb Z$-basis
$\omega_1,\ldots,\omega_r$.  Form the $E$-function vector
\[
  \bigl(1,E_{\alpha_1},\ldots,E_{\alpha_m},
        e^{\omega_1z},\ldots,e^{\omega_rz},
        e^{-\alpha_1z},\ldots,e^{-\alpha_mz}\bigr)^{\mathsf T},
\]
omitting repeated coordinates.  Equation \eqref{eq:Ein-ode}, together
with the differential equations for the constant and exponential
coordinates, makes this a closed first-order system over $k(z)$ with no
finite pole except possibly zero.

The additional forcing exponentials are Laurent monomials in the basis
exponentials and do not enlarge the generated field.  By
\cref{thm:Ein-functional}, the functional transcendence degree is $r+m$;
Beukers' theorem gives the same value at $z=1$.  The exponential-value
subfield has transcendence degree $r$ by \cref{thm:LW}.  Thus the $m$
values $\Ein(\alpha_j)$ are algebraically independent over that subfield,
which contains the coefficients of the proposed relation.''')

statement_re = re.compile(r'\\begin\{(theorem|proposition|lemma|corollary|definition|remark)\}.*?\\end\{\1\}', re.S)
report = {}
for path, revised in ((MAIN, main), (SUPP, supp)):
    original = originals[path]
    before = [m.group() for m in statement_re.finditer(original)]
    after = [m.group() for m in statement_re.finditer(revised)]
    allowed_additions = 1 if path == MAIN else 0
    if Counter(before) - Counter(after) or len(after) != len(before) + allowed_additions:
        raise RuntimeError(f'Existing statement changed or lost in {path}.')
    iterator = iter(after)
    if not all(any(x == old for x in iterator) for old in before):
        raise RuntimeError(f'Statement order changed in {path}.')
    if original.split(r'\begin{document}')[0] != revised.split(r'\begin{document}')[0]:
        raise RuntimeError(f'Front matter changed in {path}.')
    old_labels = re.findall(r'\\label\{([^}]+)\}', original)
    new_labels = re.findall(r'\\label\{([^}]+)\}', revised)
    if not set(old_labels).issubset(new_labels) or len(new_labels) != len(set(new_labels)):
        raise RuntimeError(f'Lost or duplicate label in {path}.')
    path.write_text(revised, encoding='utf-8')
    report[str(path)] = {
        'old_blob': EXPECTED[path], 'new_blob': blob_sha(revised.encode()),
        'preserved_numbered_environments': len(before),
        'added_numbered_environments': allowed_additions,
        'preserved_labels': len(old_labels),
        'added_labels': sorted(set(new_labels) - set(old_labels)),
        'front_matter_unchanged': True,
    }

paper_ii = Path('papers/02-compact-polynomial-line-kz/linear-kz-affine-line.tex')
if 'to be their compositum itself.' not in paper_ii.read_text():
    raise RuntimeError('Expected prior Paper II cover correction is missing.')

note = Path('notes/provenance/paper-iii-audit-clarifications-2026-09-28.md')
if note.exists():
    raise RuntimeError('Do not overwrite historical provenance notes.')
note.write_text('''# Paper III: audit clarifications, 2026-09-28

Revision baseline: `5c11c2e1cba0b4400006e553056254711c9ba9da`.
The Paper III audit examined `093e260aa41a1d71ea6f12b41a0a84ed9c6c1463`;
its two source files were unchanged at the revision baseline. This revision
preserves the intervening Paper II changes from PR #5.

## Main paper

- Add an explicit simultaneous spectral gauge for all horizontal
  endomorphisms over the finite exponential field. The gauge uses only
  eigenvalue differences already in the exponent subgroup and equals the
  identity at zero.
- Use this gauge and a constant change of basis to split the horizontal
  idempotent. Remove the now-unused appeal and reference to Swan's
  Laurent-ring freeness theorem.
- Present semisimplicity after exponential base change through the normal
  subgroup in the joint Picard--Vessiot group.
- Display the transformed connection and the homogeneous correction after
  pulling it back to the original moment system. Explain its single-valued
  meromorphic behavior at zero before applying the residue exclusion.

## Independent supplement

- Explicitly adjoin all forcing exponentials in the quadratic and Ein
  value proofs, as well as the constant coordinate in the Ein system.
  Distinguish generation of the exponential field from closure of a vector
  under a rational first-order differential system. Spell out the rank and
  transcendence-degree bookkeeping.
- Exclude positive Laurent powers for a non-pure quartic before imposing
  the simple-pole-plus-constant ansatz. Explain why projection to the
  symmetric square retains the unique polar coefficient. The classification
  now refers back to this complete argument rather than supplying it later.

## Scope and preservation

No existing theorem, proposition, lemma, corollary, definition, or remark
statement is changed. One proved spectral-gauge lemma is added to the main
paper. Existing labels, author lists, titles, metadata, and August 2026
manuscript dates are preserved. No hypotheses are weakened and no claimed
class of periods is enlarged. The exact-compositum correction in Paper II
is already present at the baseline, so Paper II is not changed here.
Historical audit reports are left unchanged.

## Validation

The revision procedure checks the source-blob baselines, all existing
numbered-environment statements and labels, and unchanged front matter.
Run `make test`, `make pdf`, and `make check`; preserve the six unchanged
PDF snapshots and their manifest entries. Inspect both revised PDFs before
merging. Actual build, regression, and visual-review results are recorded
in the pull request. These checks are not independent peer review or a
kernel-checked mathematical proof.
''', encoding='utf-8')
review = Path('.build/review')
review.mkdir(parents=True, exist_ok=True)
(review / 'preservation-checks.json').write_text(json.dumps(report, indent=2) + '\n')
print(json.dumps(report, indent=2))
