#!/usr/bin/env python3
"""One-shot, hash-guarded integration of the audited Paper V successor.

Run in the preparation worktree after build_successor.py. The old canonical
source and PDF are archived verbatim. This script never writes to main and
never changes repository protection, visibility, licenses, or author lists.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess

BASE = 'd5ae8f9081c7bc34d1622316bd8463482f244395'
OLD_BLOB = '8244fc3f9229d74ba3f24f99363a306ad6139a87'
FOLDER = Path('notes/candidates/2026-10-06-single-chain')
CANON = Path('papers/05-polynomial-flags/polynomial-flag-exponential-periods.tex')
ARCHIVE = Path('notes/archives/2026-10-06-paper-v-before-single-chain')
TITLE = 'Relative Exponential Periods on Polynomial Flags: Algebraic Independence over Fixed Boundary Fields'


def unique(text: str, old: str, new: str) -> str:
    if text.count(old) != 1:
        raise RuntimeError(f'Expected one occurrence: {old[:110]!r}, got {text.count(old)}')
    return text.replace(old, new, 1)


def between(text: str, first: str, last: str) -> str:
    a = text.index(first)
    b = text.index(last, a + len(first))
    return text[a:b]


def git_blob(data: bytes) -> str:
    return hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()


ABSTRACT = r'''\begin{abstract}
We construct rational differential systems for compact polynomial-chain
exponential integrals, with polynomial twisted de Rham representatives and
literal Stokes forcing from the fixed faces. For a real algebraic phase
$q=\alpha x^a+\beta y^b+q_<$, where $a,b\ge2$ are coprime and $q_<$ has lower
weighted degree, we prove a single-chain comparison theorem under explicit
Morse, critical-value independence, face-separation, and saddle-or-continuation
hypotheses. The $(a-1)(b-1)$ monomial moments are algebraically independent
over the fixed-face function field, and their values are algebraically
independent over the corresponding face-value field at every nonzero
algebraic parameter. Every polynomial amplitude has a unique Laurent Stokes
remainder; algebraicity of its value over the face-value field is equivalent
to polynomial twisted exactness.

The proof combines global Picard--Lefschetz geometry, a Fourier
order-versus-degree irreducibility argument, direct simple-spectrum formal
diagonalization, and an elementary stable-lattice obstruction to boundary
adjoint factors. An actual one-column criterion converts these facts into
algebraic independence. We verify both the original elliptic triangle and a
rank-six triangle with phase $x^4+y^3+xy-y$. The boundary fields contain only
the specified faces. No genericity assertion, several-chain comparison,
or general formal-completeness theorem is claimed.
\end{abstract}

\medskip
\noindent\textit{2020 Mathematics Subject Classification.}
Primary 11J91; Secondary 11J81, 12H05, 14D07, 14H40, 32S40, 34M35.
\tableofcontents

'''

INTRO = r'''\section{Introduction and main comparison theorem}\label{sec:intro}
We study actual compact integrals and their polynomial Stokes certificates,
not an unspecified completion of a formal period algebra. The basic
polynomial boundary construction is general; the comparison theorem below
verifies its actual-column criterion for a weighted-plane class under
explicit hypotheses. The elliptic and rank-six examples give two complete
applications.

The algebraic changes of variables, linearity, and twisted Stokes identities
used here belong to the exponential Kontsevich--Zagier framework
\cite{KontsevichZagier,CommelinHabeggerHuber}. The conclusions below concern
one actual column over its fixed boundary field. They do not assert a
presentation of all formal exponential-period relations. The functional and
numerical independence proofs do not use the companion formal-comparison
theorems or Paper IV.

\paragraph{Structure and previous version.}
Section~\ref{sec:boundary-construction} constructs actual systems and their
$E$-function coordinates. Section~\ref{sec:criterion} proves the general
one-column criterion. The later sections verify its hypotheses using the
geometry, Fourier irreducibility, and the fixed-face obstruction, and then
specialize at nonzero algebraic parameters. Section~\ref{sec:elliptic-example}
retains the explicit continuation needed for the original triangle.
The pre-integration version \cite{PaperVPrevious}, including its separate
observable-Lefschetz, Hodge, face-lattice, and multicolumn discussions, is
archived unchanged. Those additional discussions are not inputs to the
proof here. The earlier unrestricted endpoint-complete claim remains
withdrawn; it is not restored by this theorem.

\paragraph{Revision.} The 6 October 2026 revision integrates the
source-checked single-chain theorem and its stable-lattice proof. The
manuscript's author list and original month-year date are retained.

'''

ELLIPTIC_END = r'''
\subsection{Verification of the comparison hypotheses}
The phase has $(a,b)=(3,2)$ and its two critical values are $-2,2$.
Thus (M) holds and (Q) is automatic. For a slanted edge put
$\beta=7\sqrt7/27$. The substitution $x=1/3+(\sqrt7/3)s$ gives
\[
 p(x)=\frac{107}{108}+\beta(-s^3+3s).
\]
Its critical values are $107/108\pm2\beta$, so their nonzero differences
are $\pm4\beta$, whereas the interior differences are $\pm4$.
Since $\beta^2=343/729\ne1$, these do not agree. The vertical quadratic
face has only one critical value, so it also satisfies (F).
Lemma~\ref{lem:elliptic-continuation} supplies $(S^*)$, although the saddle
$(1,0)$ lies outside the triangle and (S) fails.

\begin{corollary}[Elliptic functional and numerical comparison]
\label{thm:intro-elliptic}\label{thm:elliptic-main}\label{thm:values}
For this triangle and phase, $M_0,M_1$ are algebraically independent over
$\C(z)(P_0,P_1,Q_0,E_a,E_b)$. At every nonzero algebraic $\xi$, their values
are algebraically independent over the corresponding fixed-face value
field. Every polynomial amplitude has the unique remainder
\eqref{eq:elliptic-normal}, and its value is algebraic over the face-value
field exactly when its specialized polynomial twisted class is zero.
\end{corollary}
\begin{proof}
Apply Theorem~\ref{thm:main}, using the verifications above. The formulas
\eqref{eq:explicit-beta}--\eqref{eq:boundary-field} retain the actual
normalization and the finite generating boundary vector. Thus this is
also a specialization of the general proof, not just an abstract
identification of two homogeneous equations.
\end{proof}
'''

CANONICAL_SCOPE = r'''\section{Scope, dependencies, and verification}\label{sec:scope}
The normal-form theorem is algebraic and the polynomial boundary-system
construction allows arbitrary polynomial phases. Algebraic independence
requires the explicitly stated hypotheses of Theorem~\ref{thm:main},
verified for the two examples above. The result is not contingent on
an unproved genericity conjecture: (Q) is a hypothesis on the specified
critical values, certified in the examples. Its failure alone does not
imply that the homogeneous Galois group is smaller.

All boundary fields are attached to the finitely many fixed faces and
endpoints of the chain. Replacing them by the field of all compact
polynomial-line periods is not an asserted extension. Only one phase and
one actual column are considered. No several-chain or multiblock formal
completeness is inferred. Numerical independence is a statement after
specializing the parameter; it is not injectivity of evaluation on the
unspecialized algebra containing $z-\xi$.

\paragraph{External inputs.}
The geometric proof uses Broughton \cite[Definition~3.1, Theorem~1.2,
pp.~229--231]{Br} and the Picard--Lefschetz, distinguished-basis,
connectedness, and nondegeneracy statements in
\cite[\S1.3; \S2.1; Theorem~3.3; pp.~100, 411]{AGV}.
The needed perturbation and compatible-transport arguments are included
in Proposition~\ref{prop:geometry}. Polynomial relative exactness uses
\cite[Definitions~1.3--1.4, Theorem~1.5]{Bonnet}.
Ordinary Picard--Vessiot theory and its tensor equivalence use
\cite[Theorem~1.5.2]{Singer}, and the complete reducibility in the actual
criterion uses \cite[Proposition~15.15, Corollary~22.43]{MilneAG}.
The general finiteness assertion uses the explicitly identified
Proposition~9.1 of Sabbah \cite{Sabbah}.
Numerical specialization uses \cite[Theorem~1.1]{Beukers} separately for
the boundary and combined vectors. Neither Wasow's formal simplification
nor a general formal-normal-form theorem is needed: the relevant
simple-spectrum and lattice statements are proved in the text.

\paragraph{Computational verification.}
The repository contains the retained exact elliptic-amplitude certificate,
the rank-six polynomial/resultant/Frobenius/Sturm certificate, and exact
checks of the formal recursion and six formal powers. The rank-six
geometric inequalities are certified on whole rational intervals.
These tests verify finite calculations, not the general monodromy or
Galois proofs. Compilation, regression tests, and AI-assisted audits are
not independent specialist refereeing or formal verification.

\paragraph{AI assistance and responsibility.}
OpenAI ChatGPT and Anthropic Claude were used for proof exploration,
drafting, symbolic checks, and adversarial review. They are not authors.
The authors are responsible for the statements, proofs, citations, and
remaining errors.
'''

README_V = '''### Paper V — Single-chain comparison over fixed boundary fields

**Scope.** The polynomial boundary-system construction covers compact polynomial two-chains with algebraic parametrizations. The main comparison theorem treats

$$q=\\alpha x^a+\\beta y^b+q_<,\\qquad \\gcd(a,b)=1,$$

where $q_<$ has lower weighted degree for weights $b,a$. It assumes nondegenerate critical points with distinct values, rational independence of the differences $c_i-c_1$, fixed-face separation, and an interior saddle or the stated continuation alternative.

**Main results.** The $\\mu=(a-1)(b-1)$ moments with amplitudes $x^iy^j$, $0\\le i\\le a-2$, $0\\le j\\le b-2$, are algebraically independent over the complexified fixed-face function field. Their values at every nonzero algebraic parameter are algebraically independent over the corresponding face-value field. Every polynomial amplitude has a unique Laurent Stokes remainder. Algebraicity of its value over the face-value field is equivalent to polynomial twisted exactness.

The original elliptic triangle for $y^2-x^3+3x$ is retained through the continuation hypothesis $(S^*)$. A second, rank-six example uses $x^4+y^3+xy-y$ on the triangle with vertices $(0,-1),(1,-1),(1/2,0)$; its finite algebraic and geometric hypotheses have exact certificates. For straight-edged chains with $\\min(a,b)\\ge3$, face separation is automatic under the critical-value hypothesis.

The proof includes direct simple-spectrum formal diagonalization and a stable-lattice boundary obstruction; it does not require a general formal-normal-form theorem. The fields use **only the specified faces**, not all compact line periods. Genericity of the critical-value hypothesis, multiple chains/phases, and general formal completeness are not claimed. The actual comparison does not depend on Paper IV or the companion formal-comparison theorems.

The [frozen candidate and audit](notes/candidates/2026-10-06-single-chain/README.md), [corrected successor](notes/candidates/2026-10-06-single-chain/successor/generic-single-chain-theorem-v2.tex), and [integration record](notes/provenance/paper-v-single-chain-integration-2026-10-06.md) preserve the proof-development sequence. The [pre-integration manuscript](notes/archives/2026-10-06-paper-v-before-single-chain/polynomial-flag-exponential-periods.tex) and [its PDF](notes/archives/2026-10-06-paper-v-before-single-chain/polynomial-flag-exponential-periods.pdf), including the separate geometric and multicolumn material, are archived unchanged; that material is not used in the new main proof.

'''


def bibliography_entries(text: str) -> dict[str, str]:
    body = text.split(r'\begin{thebibliography}',1)[1]
    body = body[body.index('\n')+1:].split(r'\end{thebibliography}',1)[0]
    matches = list(re.finditer(r'\\bibitem\{([^}]+)\}', body))
    return {m[1]: body[m.start(): matches[i+1].start() if i+1<len(matches) else len(body)].strip()
            for i,m in enumerate(matches)}


def integrate(root: Path) -> None:
    oldbytes=(root/CANON).read_bytes()
    if git_blob(oldbytes) != OLD_BLOB:
        raise RuntimeError('Canonical Paper V is not the audited base; reconcile before integration')
    old=oldbytes.decode()
    revised=(root/FOLDER/'successor/generic-single-chain-theorem-v2.tex').read_text()
    # Freeze the complete previous canonical manuscript, not isolated selected paragraphs.
    archive=root/ARCHIVE
    archive.mkdir(parents=True,exist_ok=True)
    (archive/CANON.name).write_bytes(oldbytes)
    shutil.copyfile(root/'output/pdf/polynomial-flag-exponential-periods.pdf',archive/'polynomial-flag-exponential-periods.pdf')
    preamble=old[:old.index(r'\begin{abstract}')]
    preamble=unique(preamble,
        'pdftitle={Relative Exponential Periods on Polynomial Flags: Polynomial Boundary Systems and an Elliptic Comparison Theorem}',
        'pdftitle={'+TITLE+'}')
    preamble=unique(preamble,
        r'''\title{Relative Exponential Periods on Polynomial Flags:\\
Polynomial Boundary Systems and an Elliptic Comparison Theorem}''',
        r'''\title{Relative Exponential Periods on Polynomial Flags:\\
Algebraic Independence over Fixed Boundary Fields}''')
    extra=r'''\newcommand{\PGL}{\operatorname{PGL}}
\newcommand{\wt}{\operatorname{wt}}
\newcommand{\Bcal}{\mathcal B}
'''
    preamble=unique(preamble,r'\begin{document}',extra+'\n'+r'\begin{document}')

    statement=between(revised,r'\section{Statement}',r'\section{Normal form for the class')
    statement=unique(statement,r'\section{Statement}',INTRO)
    statement=statement.replace('Notation follows\nPaper~V: for', 'For')
    statement=statement.replace('The phase $y^2-x^3+3x$ of Paper~V', 'The elliptic phase $y^2-x^3+3x$')
    statement=unique(statement,
        'over $k_\\R$ in the sense of Paper~V, Definition~3.1: a finite $k$-linear',
        'over $k_\\R$: a finite $k$-linear')
    statement=unique(statement,
        "Paper~V, Lemma~11.1 verifies (S$^*$) for its triangle (the saddle $(1,0)$ lies\noutside the triangle, so (S) itself fails there). With (S$^*$), Theorem\n\\ref{thm:main} contains Paper~V, Theorems~1.1, 12.2 and~13.2: for that datum (F)\nreads $4\\ne\\pm4\\beta$.",
        r'''Lemma~\ref{lem:elliptic-continuation} verifies $(S^*)$ for the original
elliptic triangle: its saddle $(1,0)$ lies outside the triangle, so (S)
itself fails. Section~\ref{sec:elliptic-example} verifies (F) and derives
its functional and numerical comparison from Theorem~\ref{thm:main}.''')
    statement=statement.replace("Variant covering Paper V's triangle", 'The continuation alternative')

    boundary=between(old,r'\section{Polynomial representatives and literal boundary forcing}',
                     r'\section{Polynomial flags and phase densities}')
    boundary=unique(boundary,r'\section{Polynomial representatives and literal boundary forcing}',
                    r'\section{Polynomial representatives and literal boundary forcing}\label{sec:boundary-construction}')
    criterion=between(old,r'\section{An actual-solution comparison criterion}',
                      r'\section{The elliptic polynomial normal form}')
    criterion=unique(criterion,r'\section{An actual-solution comparison criterion}',
                     r'\section{An actual-solution comparison criterion}\label{sec:criterion}')
    core=between(revised,r'\section{Normal form for the class',r'\section{External inputs and scope}')
    core=core.replace('As in Paper~V, Lemma~11.1, the inverse Laplace', 'The inverse Laplace')
    core=unique(core,
        'Paper~V, Theorem~8.2 (the actual one-column criterion) requires:',
        r'The actual one-column criterion, Theorem~\ref{thm:criterion}, requires:')
    core=unique(core,'(Paper~V, Theorem~2.1)',r'(Theorem~\ref{thm:boundary-system})')
    sanity=core.index('Numerical sanity checks, not part of the proof:')
    core=core[:sanity] + r'''The exact checks are run by \texttt{make test}. No numerical quadrature
or asymptotic fitting is used to certify the hypotheses.

'''

    ellipse=between(old,r'\section{The elliptic polynomial normal form}',
                    r'\section{Explicit comparison with elliptic Gauss--Manin periods}')
    ellipse=unique(ellipse,r'\section{The elliptic polynomial normal form}',
                    r'\section{The elliptic triangle and the continuation alternative}\label{sec:elliptic-example}')
    density=between(old,'We verify a nonzero elliptic monodromy variation of this particular germ.',
                    'A power $T_+^m$ fixes the algebraic germ')
    density=unique(density,'We verify a nonzero elliptic monodromy variation of this particular germ.',
                   r'We verify a nonzero elliptic monodromy variation of the actual density germ.')
    ellipse += r'''\subsection{The actual continuation}
On the regular phase fibre $y^2=x^3-3x+t$, the convention
$dq\wedge\alpha=dx\wedge dy$ gives $\alpha=-dx/(2y)$.

\begin{lemma}[Continuation for the elliptic triangle]\label{lem:elliptic-continuation}
The density germ of $M_0$ just to the right of $t=0$ satisfies $(S^*)$.
\end{lemma}
\begin{proof}
''' + density + r'''The variation is a nonzero constant multiple of the required
Gelfand--Leray vanishing period; the common sign is immaterial.
\end{proof}

\begin{remark}
This is continuation of a regular density germ, not a claim that the
original compactly supported density is nonzero outside $q(D)=[-11/8,11/8]$.
\end{remark}
''' + ELLIPTIC_END

    text=preamble+ABSTRACT+statement+boundary+criterion+core+ellipse+CANONICAL_SCOPE
    entries=bibliography_entries(old)
    entries.update(bibliography_entries(revised))
    entries['PaperVPrevious']=entries['PaperV'].replace('{PaperV}','{PaperVPrevious}',1)
    cited=set()
    for m in re.finditer(r'\\cite(?:\[[^\]]*\])*\{([^}]+)\}',text):
        cited.update(k.strip() for k in m[1].split(','))
    missing=cited-set(entries)
    if missing: raise RuntimeError(f'Unresolved bibliography entries {missing}')
    bib='\n\\small\n\\begin{thebibliography}{99}\n\n'+'\n\n'.join(entries[k] for k in sorted(cited))+'\n\n\\end{thebibliography}\n\\end{document}\n'
    text+=bib
    labels=re.findall(r'\\label\{([^}]+)\}',text)
    if len(labels)!=len(set(labels)): raise RuntimeError('Duplicate LaTeX labels')
    references=[]
    for m in re.finditer(r'\\(?:ref|eqref|cref|Cref)\{([^}]+)\}',text):
        references.extend(k.strip() for k in m[1].split(','))
    unresolved=set(references)-set(labels)
    if unresolved: raise RuntimeError(f'Unresolved internal references: {unresolved}')
    old_author=next(line for line in old.splitlines() if line.startswith(r'\author{'))
    if old_author not in text or r'\date{September 2026}' not in text:
        raise RuntimeError('Author list or month-year date changed')
    (root/CANON).write_text(text)

    readme=(root/'README.md').read_text()
    readme=readme.replace('Relative Exponential Periods on Polynomial Flags: Polynomial Boundary Systems and an Elliptic Comparison Theorem',TITLE)
    readme=unique(readme,
        'Paper V constructs two-variable boundary systems and proves an explicit elliptic independence theorem.',
        'Paper V constructs two-variable boundary systems and proves a single-chain algebraic-independence theorem under explicit weighted-phase and boundary hypotheses, with rank-two and rank-six applications.')
    a=readme.index('### Paper V —');b=readme.index('## Status',a)
    readme=readme[:a]+README_V+readme[b:]
    readme=readme.replace('poppler-utils python3 make','poppler-utils python3 python3-sympy make')
    readme=readme.replace('make test   # test the build checks','make test   # build regressions and exact elliptic/rank-six/formal certificates')
    readme=readme.replace('The certificate routine and its tests use only the Python standard library; `make test` runs them.',
        'The elliptic certificate routine uses only the Python standard library. The new rank-six and formal-recursion suites require SymPy; `make test` runs all of them.')
    readme=readme.replace("python3 scripts/check_paper_v.py  # optional broader exact suite; requires SymPy", "python3 scripts/check_paper_v.py  # optional broader exact elliptic suite\npython3 scripts/check_single_chain.py  # rank-six and formal certificates")
    (root/'README.md').write_text(readme)

    status=(root/'notes/repository-status.md').read_text()
    status=re.sub(r'^\| Paper V \|.*\|$',
        '| Paper V | The class-(W) single-chain theorem is integrated under explicit (M), (Q), (F), and (S) or (S*) hypotheses, with functional independence, all-nonzero-algebraic-parameter independence, and polynomial twisted exactness. The elliptic triangle and rank-six triangle are verified applications. The frozen candidate, corrected successor, and pre-integration manuscript are preserved. The older unrestricted endpoint-complete claim remains withdrawn; genericity and general multiblock formal completeness are not claimed. |',status,flags=re.M)
    status=status.replace('- Paper V: the current fixed-triangle elliptic theorem and its actual polynomial boundary-system formulation replace the withdrawn endpoint-complete claim.',
        '- Paper V: the October 6 source-checked class-(W) theorem extends the fixed-triangle actual comparison under explicit hypotheses; it does not reinstate the withdrawn endpoint-complete claim.')
    status=status.replace('- Paper V follow-up: source-checked citations, the fixed-base observable hypothesis, the localized actual/specialized-formal distinction, and the expanded affine-orbit proof are integrated. The principal independence statements are unchanged.',
        '- Paper V: direct formal diagonalization, the diagonal local Picard–Vessiot/Kummer argument, stable-lattice face disjointness, and local/global transport are integrated. The October 5 geometric/formal/multicolumn discussions remain in the unchanged archived manuscript, not in the present main proof.')
    timeline='| 2026-10-06 | Paper V single-chain integration | Freeze the candidate; audit the corrected successor; integrate the weighted-plane comparison and stable-lattice proof, retain both examples, archive the previous manuscript, and add exact regression certificates. |\n'
    status=unique(status,'\n## Detailed records by paper','\n'+timeline+'\n## Detailed records by paper')
    marker='### Paper V\n\n| Record | Purpose |\n| --- | --- |\n'
    addition='| [Single-chain integration audit](provenance/paper-v-single-chain-integration-2026-10-06.md) | Successor and integrated proof audit, explicit scope, preservation, and validation record. |\n| [Frozen candidate and source audit](candidates/2026-10-06-single-chain/README.md) | Immutable source snapshot, geometric pinpoints, exact certificate, and separate proof supplement. |\n| [Pre-integration manuscript](archives/2026-10-06-paper-v-before-single-chain/polynomial-flag-exponential-periods.tex) | Verbatim archive of the previous canonical Paper V and its additional material. |\n'
    status=unique(status,marker,marker+addition)
    (root/'notes/repository-status.md').write_text(status)

    # This is only the dependency installation for the additional exact tests.
    workflow=(root/'.github/workflows/latex.yml').read_text()
    workflow=unique(workflow,'lmodern poppler-utils\n','lmodern poppler-utils python3-sympy\n')
    workflow=unique(workflow,'run: make test','run: PATH=/usr/bin:$PATH make test')
    (root/'.github/workflows/latex.yml').write_text(workflow)

    report={'base_commit':BASE,'archived_source_git_blob':git_blob(oldbytes),
            'successor_sha256':hashlib.sha256(revised.encode()).hexdigest(),
            'integrated_source_sha256':hashlib.sha256(text.encode()).hexdigest(),
            'preserved_author_line':old_author,'preserved_manuscript_date':'September 2026',
            'internal_labels':len(labels),'internal_reference_targets':len(set(references)),
            'unresolved_internal_references':sorted(unresolved),
            'bibliography_keys':sorted(cited),
            'other_canonical_sources':{str(p.relative_to(root)):hashlib.sha256(p.read_bytes()).hexdigest()
                for p in list((root/'papers').rglob('*.tex'))+[root/'notes/eit-structural-companion.tex'] if p!=root/CANON}}
    (root/FOLDER/'successor/integration-manifest.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))


def retain_other_pdfs(root: Path) -> None:
    """Keep the eight unrelated snapshots byte-identical after make pdf."""
    manifest=root/'output/pdf/manifest.json'
    built=json.loads(manifest.read_text())
    name='output/pdf/polynomial-flag-exponential-periods.pdf'
    pdf=(root/name).read_bytes()
    record=next(r for r in built['documents'] if r['source']==str(CANON))
    subprocess.run(['git','restore','--source='+BASE,'--','output/pdf'],cwd=root,check=True)
    baseline=json.loads(manifest.read_text())
    baseline['documents']=[record if r['source']==str(CANON) else r for r in baseline['documents']]
    (root/name).write_bytes(pdf)
    manifest.write_text(json.dumps(baseline,indent=2)+'\n')
    print('Retained unrelated committed PDF snapshots and refreshed only Paper V and its manifest record.')


def main() -> None:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root',type=Path,default=Path('.'))
    parser.add_argument('--retain-other-pdfs',action='store_true')
    args=parser.parse_args()
    root=args.root.resolve()
    if args.retain_other_pdfs: retain_other_pdfs(root)
    else: integrate(root)

if __name__=='__main__': main()
