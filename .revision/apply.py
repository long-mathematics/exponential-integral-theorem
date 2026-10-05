#!/usr/bin/env python3
"""Apply the audited revision only on its isolated feature branch."""
from pathlib import Path
import hashlib
import os
import re
import subprocess

branch='repair/paper-iv-k-rational-realization-20261005'
if os.environ.get('GITHUB_REF') != 'refs/heads/'+branch:
    raise SystemExit('Wrong branch')
p=Path('papers/04-relative-exponential-nori-ayoub/relative-exponential-nori-ayoub.tex')
old=p.read_text()
if hashlib.sha256(p.read_bytes()).hexdigest() != 'e135bb195254b3e172a264a31ef7352c55c1c2e25ae88b18bb66b7c51b5e9cb5':
    raise SystemExit('Canonical baseline changed; reconcile before applying')
s=old
start=s.index(r'\begin{externalinput}[Ordinary Nori structure and absolute comparison]')
end=s.index(r'\subsection{The affine-line quotient}',start)
s=s[:start]+Path('.revision/realization-a.txt').read_text().lstrip()+Path('.revision/realization-b.txt').read_text()+s[end:]

def change(a,b):
    global s
    if s.count(a)!=1:
        raise SystemExit('Expected one source occurrence: '+a[:100])
    s=s.replace(a,b,1)

change(r'''realization over $k=\overline{\Q}$ is built from the absolute de Rham
augmentation of the Nori algebra and its relative module presentation;
comparison, operation maps, and nonzero exponential realization are retained
in the construction.''',r'''realization over $k=\overline{\Q}$ is constructed through arithmetic mixed
sheaves, their constructible-heart enhancement, and universal Nori hearts.
Perverse-concentrated generators supply the tensor comparison; operation
maps and the actual absolute period normalization are retained.''')
change(r'''we construct the algebraic realization from the absolute Nori de Rham
augmentation, prove its comparison and operation compatibilities, and pass
to the affine-line quotient.''',r'''we construct the algebraic realization through arithmetic mixed sheaves,
verify the enhancement and tensor comparison, fix its absolute period
normalization, and pass to the affine-line quotient.''')
change(r'''The ordinary module presentation
\eqref{eq:nori-module-model} remains available but is not an input to
\eqref{eq:relative-algebraic-realization}.''',r'''The ordinary module presentation
\eqref{eq:nori-module-model} remains available but is not an input to
\eqref{eq:relative-algebraic-realization}. Cellular constructions
\cite{ChoudhuryGallauer,Harrer} are complementary approaches; no
comparison of their enhanced functors is used here.''')

fiber=r'''
\begin{lemma}[The rational directional fiber]\label{lem:rational-directional-fiber}
In the absolute vanishing-cohomology presentation, the directional fiber
has a rational form. For a rational object written $F[1]$, put
\[
 \Psi_{\theta,\Q}(F[1])
   =\varinjlim_{r\to+\infty}\Gamma(e^{i\theta}S_r,F),
 \qquad S_r=\{z\in\C:\operatorname{Re}z>r\}.
\]
Its extension to $\C$ is the directional functor of
\cite[Definition~3.5 and Theorem~3.6]{Snodgrass}. On the rigid
convolution category used here it is an exact faithful tensor fiber
functor over $\Q$; coefficient extension gives the $k$-valued fiber.
\end{lemma}
\begin{proof}
For sufficiently large $r$ the half-plane avoids the finite singular
set. The sections are the fiber of a rational local system on a simply
connected half-plane, so the system stabilizes and commutes with
extension of coefficients. Restriction, external product, addition and
the cohomological maps defining convolution are rational sheaf maps.
They give the rational tensor comparison whose complexification is the
standard directional convolution comparison. Exactness, invertibility
of the tensor maps, their coherence and faithfulness can therefore be
checked after the faithful extension $\Q\subset\C$. The unit is the
rational convolution unit. These are the rational versions of the
absolute convolution construction recalled in \cite[\S3]{Snodgrass}.
For pure exponential geometric data this rational fiber agrees with the
relative-singular-cohomology rational structure on rapid-decay
cohomology, with its integral comparison; see also the introduction of
\cite{Snodgrass}. This does not assign a rational structure to an
arbitrary irregular connection by choosing complex horizontal generators.
\end{proof}

'''
needle=r'\begin{proposition}[Normalized tensor and fiber]'
change(needle,fiber+needle)
change(r'''  =\Psi_\infty\bigl(\rat^{\exp}(i_s^*N[-d])\bigr).''',r'''  =\Psi_\infty\bigl(\rat^{\exp}(i_s^*N[-d])\bigr).'''+r'''
  \quad\text{Here }\Psi_\infty=\Psi_{\theta,\Q}\otimes_\Q k.''')

change(r'''for this cover until the final descent. For the underlying algebraic
regular holonomic module $M$, the characteristic variety at finite $t$
is contained in the zero section and the conormals''',r'''for this cover until the final descent. For the characteristic-variety
argument extend scalars to $\C$ and suppress that extension in the
notation; this is the field of the cited statements in \cite{HTT}.
All input modules and the partial Fourier transform were already defined
over $k$. For the resulting regular holonomic module $M$, the
characteristic variety at finite $t$ is contained in the zero section
and the conormals''')
change(r'''Near infinity put $x=t^{-1}$. By the algebraic logarithmic-lattice
criterion for regular connections \cite[Theorem~5.3.7]{HTT}, choose a
coherent lattice $L$ in $\overline M$, with $L[x^{-1}]=\overline M$,
stable under $x\partial_x$ and the parameter derivations $\partial_{s_j}$.''',r'''Near infinity put $x=t^{-1}$. The logarithmic characterization of
regular connections \cite[Theorem~5.3.7]{HTT} supplies coherent
logarithmically stable submodules containing any chosen finite set of
local meromorphic generators. Taking their finite sum gives a coherent
lattice $L$ with $L[x^{-1}]=\overline M$, stable under
$x\partial_x$ and the parameter derivations $\partial_{s_j}$.''')
change(r'''The proper direct-image characteristic estimate
\cite[Theorem~2.5.1 and Remark~2.5.2]{HTT} now places the characteristic
variety of every cohomology module of $q_+\Ncal$ in the zero section.''',r'''Proper-image coherence is \cite[Theorem~2.5.1]{HTT}; the
characteristic-variety estimate is specifically Remark~2.5.2 there.
That estimate places the characteristic variety of every cohomology
module of $q_+\Ncal$ in the zero section.''')
change(r'''This proves the asserted lissity over $k$, which descends along the
finite etale cover.''',r'''This proves lissity after extension to $\C$. Algebraic base extension
commutes with the transfer complexes computing the transform. Faithful
flatness reflects vanishing of unwanted cohomology and descends
$\Ocal$-coherence and local freeness of the resulting connection.
Thus lissity holds over $k$ and then descends along the finite etale
cover. No logarithmic lattice over $k$ was inferred solely from the
complex-field textbook theorem.''')
change(r'''This uses the established ordinary Betti
realization, not the new algebraic augmentation in
\cref{thm:algebraic-interface}.''',r'''This uses the established ordinary Betti
realization, independently of the algebraic realization construction in
\cref{thm:algebraic-interface}.''')
change(r'''idempotent over $k$; algebraically closed extension does not change finite
etale covers in characteristic zero.''',r'''idempotent over $k$; algebraically closed extension does not change finite
etale covers in characteristic zero, including for nonproper varieties
\cite[Remark~3.3(c)]{MilneEtale}.''')
change(r'''$R_k$, and its solution fiber is the evaluation fiber $\omega_v$, since
$Y(s_0)=I$. Its group is $H_v$.''',r'''$R_k$. Since $Y(s_0)=I$, evaluation at $s_0$ identifies its horizontal
solution fiber with the algebraic evaluation fiber $\omega_v$, naturally
on tensor constructions and their subquotients. Its group is $H_v$.''')
change(r'''Numbering here follows this accepted version, including Theorem~0.1
and Corollary~4.19.''',r'''All pinpoints use arXiv~v4 numbering, including Theorem~4.5,
Corollary~4.8, Proposition~4.16, and Corollary~4.19; the published
numbering differs.''')
change(r'\bibitem{Mostaed}',r'''\bibitem{MilneEtale}
J.~S.~Milne, \emph{Lectures on 'Etale Cohomology}, version~2.21,
March~22, 2013, Remark~3.3(c).
\url{https://www.jmilne.org/math/CourseNotes/LEC.pdf}.

\bibitem{Mostaed}''')
change(r'\bibitem{Tubach}',r'''\bibitem{TerenziFunctoriality}
L.~Terenzi, \emph{On the functoriality of universal abelian factorizations},
\href{https://arxiv.org/abs/2401.13583}{arXiv:2401.13583},
Proposition~4.3, Corollary~4.5, Proposition~4.6, and \S6.

\bibitem{Tubach}''')
# Preserve identity and ensure no reference to a retired augmentation label remains.
for command in ('author','title','date'):
    assert re.search(r'^\\'+command+r'\{.*',old,re.M).group()==re.search(r'^\\'+command+r'\{.*',s,re.M).group()
for label in ('lem:geometric-dR','lem:module-extension','eq:absolute-compatible','eq:deRham-augmentation','eq:abstract-module-formula'):
    assert label not in s,label
p.write_text(s)

readme=Path('README.md')
r=readme.read_text()
needle='**Main results.** The paper constructs the relative exponential Nori category'
assert r.count(needle)==1
r=r.replace(needle,'The algebraic realization is constructed through arithmetic mixed sheaves, with an explicit tensor comparison and absolute period normalization.\n\n'+needle)
readme.write_text(r)

status=Path('notes/repository-status.md')
r=status.read_text()
old_row=next(line for line in r.splitlines() if line.startswith('| Paper IV |'))
new_row='| Paper IV | The canonical manuscript uses the arithmetic mixed-sheaf realization replacement, including its enhancement, tensor and absolute-comparison proofs. The separate October 5 lissity and geometric-origin repairs remain integrated; the realization-to-arithmetic-to-PV chain has the scoped follow-up audit linked below. |'
r=r.replace(old_row,new_row)
needle='- Paper IV interface 3(b): generic smooth-projective realization of the relevant simple constituents and the ensuing rank-one torsion step.'
assert needle in r
r=r.replace(needle,needle+'\n- Paper IV realization follow-up: arithmetic mixed-sheaf transfer, perverse-concentrated tensor comparison, actual absolute normalization, and the downstream arithmetic/Tannakian/PV chain in the dated scoped AI-assisted audit.')
needle="- Paper IV's realization/augmentation interface, arithmetic kernel, Picard–Vessiot descent, and full period-torsor chain were not newly re-audited by the October 5 interface-3 repairs."
assert needle in r
r=r.replace(needle,'- The interface-3 repairs alone did not audit the realization chain. The later realization follow-up replaces the augmentation proof; its new transfer argument and scoped audit are not independent specialist certification.')
needle='| 2026-10-05 | README cleanup'
idx=r.index(needle)
r=r[:idx]+'| 2026-10-05 | Paper IV arithmetic realization replacement | Replace the augmentation-based interface; repair the tensor step, retain actual absolute comparison, and recheck the arithmetic/Tannakian/PV dependency chain. |\n'+r[idx:]
needle='| [Geometric-origin build verification]'
idx=r.index(needle)
r=r[:idx]+'| [Arithmetic realization repair and audit](provenance/paper-iv-arithmetic-realization-repair-2026-10-05.md) | Replaces the earlier realization construction and supersedes its blanket clearance; records the tensor correction and the scoped whole-chain follow-up. |\n| [Arithmetic realization build verification](provenance/paper-iv-arithmetic-realization-build-2026-10-05.json) | Official build and preservation hashes for this replacement. |\n'+r[idx:]
status.write_text(r)
ledger=Path('notes/repairs/paper-iv-repair-ledger.md')
with ledger.open('a') as f:
    f.write('''\n\n## 2026-10-05: arithmetic mixed-sheaf realization replacement\n\nThis follow-up supersedes the earlier augmentation-interface clearance, not the historical files. The canonical source now constructs realization through Saito's arithmetic mixed sheaves and an explicit transfer of Tubach's constructible-heart method. The proposed unary argument for external product was invalid; Terenzi's perverse-concentrated presentation and multi-exact universal factorization replace it. The actual absolute de Rham/integration normalization remains an explicit lemma.\n\nThe scoped audit rechecks operation maps, enhancement, universal-heart kernels, ordinary geometric cycles, the arithmetic rank-one kernel, semi-invariant exactness, normalized PV base change and exact constants. No new numerical theorem or optional global arithmetic strengthening is asserted. Tubach arXiv-v4 pinpoints are retained correctly; the rational directional fiber, finite-etale reference and HTT complex-field descent are explicit. The historical repair companion is not synchronized and is not the current proof source.\n\nSee the [dated repair/audit](../provenance/paper-iv-arithmetic-realization-repair-2026-10-05.md) and [official build record](../provenance/paper-iv-arithmetic-realization-build-2026-10-05.json). This is an AI-assisted proof/source audit, not independent human review or formal verification.\n''')
report=Path('notes/provenance/paper-iv-arithmetic-realization-repair-2026-10-05.md')
assert not report.exists()
report.write_text(Path('.revision/audit.md').read_text())
subprocess.run(['git','diff','--check'],check=True)
print('Applied the audited canonical source and four documentation edits.')
