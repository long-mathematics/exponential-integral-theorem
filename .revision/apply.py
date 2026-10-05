#!/usr/bin/env python3
"""Apply the source-checked comparison/fiber clarification to the pinned baseline."""
from pathlib import Path
import hashlib
import os
import re
import subprocess

branch = 'docs/paper-iv-comparison-citations-20261005'
if os.environ.get('GITHUB_REF') and os.environ['GITHUB_REF'] != 'refs/heads/' + branch:
    raise SystemExit('Wrong branch; no changes applied')
p = Path('papers/04-relative-exponential-nori-ayoub/relative-exponential-nori-ayoub.tex')
old = p.read_text()
if hashlib.sha256(p.read_bytes()).hexdigest() != 'f9fc806c0f40eeaf5b7ea8fd838e685ef50d4a504fcc0f73a1e5294e0ac808aa':
    raise SystemExit('Baseline source changed; reconcile first')
s = old

def replace_once(a: str, b: str) -> None:
    global s
    if s.count(a) != 1:
        raise SystemExit('Expected a unique source anchor: ' + a[:100])
    s = s.replace(a, b, 1)

replace_once(r'''For sufficiently large $r$ the half-plane avoids the finite singular
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
arbitrary irregular connection by choosing complex horizontal generators.''',r'''For the positive-real direction this is the rational nearby fiber of
\cite[Definition~2.3.5 and Proposition~2.3.7]{FresanJossenExp}.
The convolution tensor structure and the fiber-functor assertion are
\cite[Theorems~2.4.11 and~2.8.1]{FresanJossenExp}, respectively.
That source uses closed half-planes. For sufficiently large $r$, open
and closed half-planes give the same sections of the local system away
from the finite singular set, hence the same limiting fiber.

Let $r_\theta(z)=e^{i\theta}z$. Pullback by this homeomorphism is a
tensor autoequivalence of the rational topological convolution category:
it commutes with addition and fixes the origin. Since
$\Psi_{\theta,\Q}=\Psi_{0,\Q}\circ r_\theta^*$, the assertion follows
in every direction. This is a topological transport, not a motivic
pullback over $k$. The eventual section spaces also commute with
coefficient extension, giving the stated $k$- and $\C$-valued fibers.
For geometric exponential data the rational fiber identifies naturally
with rational rapid-decay cohomology by
\cite[Corollary~3.2.3]{FresanJossenExp}, with the direction transported
as above. No rational structure on an arbitrary irregular connection
is obtained by choosing complex horizontal generators.''')

replace_once(r'''Finally the absolute nearby-fiber functor is exact, faithful, and tensor,
with the rapid-decay comparison; these are the absolute convolution inputs
of Katz and Fres\'an--Jossen, in the form recalled by
\cite[Corollary~2.17 and Theorem~3.6]{Snodgrass}.''',r'''Finally \cref{lem:rational-directional-fiber} supplies the exact faithful
tensor functor and its rational rapid-decay identification. The absolute
de Rham--rapid-decay comparison is the one used in
\cref{prop:relative-Betti-interface}.''')

replace_once(r'''differential-module component is its algebraic relative de Rham complex,
and the rational component is its relative Betti complex. Their
comparison is algebraic de Rham integration. For a good pair, take the
single designated cohomology group. This identifies its image with the
usual de Rham realization of that Nori generator.''',r'''differential-module component is its algebraic relative de Rham complex,
and the rational component is its relative Betti complex.

To identify the comparison also for a possibly singular good pair
$(X,Y)$, compute these relative complexes on compatible smooth proper
hypercovers $Y_\bullet\to X_\bullet$, using total complexes and the
relative cone. On the smooth terms the comparison is the algebraic de
Rham integration map; the smooth comparison and its integration
normalization are \cite[Lemma~5.5.1 and Theorem~5.3.3]{HuberMullerStach}.
Proper cohomological descent and common refinements identify the
resulting relative map with the period isomorphism for arbitrary pairs
\cite[Definition~5.5.4 and Lemma~5.5.5]{HuberMullerStach}.
The localization and direct-image maps used above are the same maps on
these geometric complexes, so this identifies their comparison, not
just their cohomology spaces. It also retains compatibility with maps
of pairs, products, and the relative long exact sequences. For a good
pair, take its single designated cohomology group. This gives precisely
the usual de Rham realization of that Nori generator.''')

replace_once(r'''on both sides. The universal abelian factorization extends the
identification and its comparison to all absolute Nori objects and
morphisms. The multi-exact product construction gives the tensor
compatibility. Thus the absolute comparison is the specified one.''',r'''on both sides. The universal abelian factorization extends the
identification and its comparison to all absolute Nori objects and
morphisms. More explicitly, the multiplicative universal property of
\cite[Theorem~8.1.9]{HuberMullerStach} extends this specified period
comparison, and Example~8.1.10 there applies it to algebraic de Rham
cohomology. Together with the multi-exact product construction, this
identifies the tensor normalization as well. Thus the absolute
comparison is the specified one.''')

replace_once(r'''J.~Fres\'an and P.~Jossen, \emph{Exponential motives},
preliminary manuscript, 2020 version, with the absolute rapid-decay
comparison used here also recalled in \cite[\S3]{Snodgrass}.''',r'''J.~Fres\'an and P.~Jossen, \emph{Exponential motives},
book manuscript, author-hosted version accessed October~5, 2026.
\url{https://www.jossenpeter.ch/PdfDvi/ExpMot.pdf}.
Pinpoints use that version: Definition~2.3.5, Proposition~2.3.7,
Theorems~2.4.11 and~2.8.1, and Corollary~3.2.3.''')

replace_once(r'\bibitem{HuberWustholz}',r'''\bibitem{HuberMullerStach}
A.~Huber and S.~M\"uller-Stach, \emph{Periods and Nori Motives},
with contributions by B.~Friedrich and J.~von Wangenheim,
Parts~I--II, manuscript of June~8, 2015.
\href{https://home.mathematik.uni-freiburg.de/arithgeom/preprints/buch-alt/partI.pdf}{Part~I};
\href{https://home.mathematik.uni-freiburg.de/arithgeom/preprints/buch-alt/partII.pdf}{Part~II}.
Pinpoints use this dated manuscript: Theorem~5.3.3, Lemma~5.5.1,
Definition~5.5.4, Lemma~5.5.5, Theorem~8.1.9, and Example~8.1.10.

\bibitem{HuberWustholz}''')

# Preserve every statement, label, and the entire downstream proof body.
pattern = r'\\begin\{(theorem|lemma|proposition|corollary|definition|externalinput)\}.*?\\end\{\1\}'
assert re.findall(pattern, old, re.S) == re.findall(pattern, s, re.S)
assert [m.group(0) for m in re.finditer(pattern,old,re.S)] == [m.group(0) for m in re.finditer(pattern,s,re.S)]
assert re.findall(r'\\label\{([^}]+)\}',old) == re.findall(r'\\label\{([^}]+)\}',s)
a = r'\subsection{The affine-line quotient}'
b = r'\begin{thebibliography}'
assert old[old.index(a):old.index(b)] == s[s.index(a):s.index(b)]
for command in ('author', 'title', 'date'):
    assert re.search(r'^\\'+command+r'\{.*', old, re.M).group() == re.search(r'^\\'+command+r'\{.*', s, re.M).group()
p.write_text(s)

note = Path('notes/provenance/paper-iv-comparison-citation-audit-2026-10-05.md')
assert not note.exists()
note.write_text('''# Paper IV: absolute comparison and rational-fiber citation follow-up

Date: 2026-10-05. Baseline main: `fa53b5fdb51834fe7135d3948ed4a35cd454c68e` (PR #18).

## Scope

This is the focused follow-up requested after the arithmetic mixed-sheaf realization repair. It strengthens the source-to-claim explanation for the actual absolute comparison and replaces the rational-fiber proof with direct rational references and an explicit direction transport. It does not replace the Section 3 architecture, add a hypothesis, change a theorem statement, or re-audit all of the downstream arithmetic/Tannakian/Picard–Vessiot proofs. The earlier dated records remain unchanged. This is an AI-assisted source and argument audit, not independent specialist review or formal verification.

## 1. Absolute normalization: general pairs and the specified period map

The suggested Huber–Müller-Stach Theorem 8.1.9 and Example 8.1.10 were checked in the author-hosted **June 8, 2015 manuscript**, Part II, printed pages 161–162. The theorem extends a cohomology representation together with its specified comparison to singular cohomology. Its final paragraph gives the multiplicative/tensor version. The example explicitly takes algebraic de Rham cohomology and the period isomorphism of Chapter 5. These are not asserted to be the theorem numbers in the published book.

A citation solely to that extension theorem would leave the comparison on geometric generators too compressed. Part I supplies the additional bridge: Theorem 5.3.3 is the smooth affine integration normalization; Lemma 5.5.1 gives the natural smooth complex comparison; Definition 5.5.4 constructs the period isomorphism for arbitrary pairs from compatible smooth proper hypercovers and the relative cone; Lemma 5.5.5 gives well-definedness and compatibility with products and relative long exact sequences. The relevant passages, including their maps, were read directly.

The revised proof of `lem:absolute-dR-comparison` identifies the already-constructed geometric comparison with this map on the hypercover complexes and their common refinements, then takes the designated good-pair cohomology and uses the multiplicative universal property. It does not equate the naive Kahler differential complex of a singular variety with algebraic de Rham cohomology. The actual pair maps, connecting maps, products, and Tate normalization are retained. This does not revive the earlier enhanced cellular-versus-universal comparison problem.

## 2. Rational directional fiber: correct statement and source division

The full author-hosted Fresan–Jossen manuscript was obtained and the relevant pages inspected. Definition 2.3.5 and Proposition 2.3.7 are explicitly rational; Theorem 2.4.11 establishes the convolution tensor structure with its constraints; Theorem 2.8.1 proves that the nearby fiber at infinity is a fiber functor. Corollary 3.2.3 identifies the rational nearby fiber of geometric exponential data with rational rapid-decay cohomology.

The proposed pinpoint **Theorem 2.6.2 is not the tensor-structure theorem**: it computes global monodromy of a convolution, including a fiber tensor-product formula in part (2). Accordingly the revised proof cites Theorem 2.4.11 for the tensor category and Theorem 2.8.1 for the fiber-functor compatibility. No replacement proof of these external theorems is claimed.

The source uses closed half-planes whereas Paper IV uses open half-planes. After avoiding the finite singular set both compute the same eventual local-system sections; the proof records that equivalence. For `r_theta(z)=exp(i theta) z`, the identity `Psi_theta = Psi_0 composed with r_theta^*` follows directly from sections. This rational topological pullback commutes with addition and fixes zero, hence transports the tensor fiber functor. No algebraicity of the rotation, and no motivic pullback by a non-k-defined rotation, is asserted. Eventual section spaces commute with scalar extension.

Corollary 3.2.3 is cited for the **rational topological rapid-decay identification**, not for an algebraic de Rham integration theorem that it does not state. The latter remains the separate actual comparison in `prop:relative-Betti-interface`. The closing paragraph of the normalized tensor/fiber proposition now makes this source division explicit.

The bibliography no longer labels the checked Fresan–Jossen file a “2020 version”. Its cover has no printed version date; the recorded file was accessed on October 5, 2026. It is cited as a book manuscript, not a published book. Its PDF metadata has a creation date of April 11, 2024, which is recorded here only as metadata, not as an asserted edition date.

## 3. Other recommendations checked

Terenzi's *On the functoriality of universal abelian factorizations*, Section 4, was checked beyond the introductory summary: Proposition 4.3 constructs the multi-exact lifted functor; Corollary 4.5 supplies the appropriate compatible version; Proposition 4.6 lifts natural transformations. The existing perverse-concentrated tensor proof uses the required separately exact hypothesis and needs no new modification.

The differential-module component lemma already identifies transfer bimodules, relative de Rham/Spencer complexes, localization and V-filtration, finite Cech constructions, duality, and the operation/cycle maps. Its surrounding input explicitly distinguishes Saito's stated triangulated formalism from the construction-level verification in Paper IV. Another disclaimer sentence would duplicate that qualification, so this lemma is left unchanged. This pass does not claim to have found a single packaged source theorem for the full arithmetic interface.

## 4. Source versions and hashes

All three author-hosted PDFs below were read as sources, not incorporated into the repository. The author-host URLs are the ones in the updated bibliography. The retrieval used a temporary read-only branch workflow; its first attempt encountered author-host certificate hostname errors, and a public-PDF-only fallback retrieved the files without credentials or execution. The temporary source and build helpers are removed before merge.

| Source file | SHA-256 |
| --- | --- |
| Fresan–Jossen, `ExpMot.pdf` (301 pages) | `7da885c162606b3c7a2b377d532e59097e51a6856c7f9ba75071d559d2e5ebf5` |
| Huber–Müller-Stach, Part I, June 8, 2015 | `5d7e91433f2b28ffea8a00f76b5428edca8e9b25a501ba8eeb56564b8294a496` |
| Huber–Müller-Stach, Part II, June 8, 2015 | `cdf0e5bb94fc7d22a36134b61c4d5fead2b515453f9714bf6b527cc3483ce85d` |

## 5. Preservation and validation

The edit script checks that every theorem-like statement and every label is unchanged, and that the full mathematical body from the affine-line quotient through the concluding discussion is byte-identical. Authorship, title, identifier, contact, and the August 2026 manuscript date are preserved. The eight other source/PDF pairs and their manifest records are preserved; the historical repair companion and earlier provenance are not synchronized or rewritten.

The companion `paper-iv-comparison-citation-build-2026-10-05.json` records the actual official build, hashes and preservation checks. The pull request records final-head CI, visual inspection of the updated PDF, helper removal and post-merge validation. Build success checks the artifacts, not the mathematical correctness of the theorem. No release tag, deposit, visibility or repository-setting change is part of this revision.
''')

status=Path('notes/repository-status.md')
t=status.read_text()
needle='| [Arithmetic realization build verification](provenance/paper-iv-arithmetic-realization-build-2026-10-05.json) | Official build and preservation hashes for this replacement. |'
assert t.count(needle)==1
t=t.replace(needle,needle+'\n| [Absolute comparison and rational-fiber citation follow-up](provenance/paper-iv-comparison-citation-audit-2026-10-05.md) | Source-checked general-pair integration normalization, direct rational fiber references, and version-specific pinpoints; theorem statements and downstream proofs unchanged. |\n| [Comparison-citation build verification](provenance/paper-iv-comparison-citation-build-2026-10-05.json) | Official snapshot and preservation checks for the focused follow-up. |')
status.write_text(t)
ledger=Path('notes/repairs/paper-iv-repair-ledger.md')
with ledger.open('a') as f:
    f.write('''\n\n## 2026-10-05: absolute-comparison and rational-fiber source follow-up\n\nThe focused [comparison/citation audit](../provenance/paper-iv-comparison-citation-audit-2026-10-05.md) strengthens the absolute-normalization proof for arbitrary good pairs using the dated Huber–Müller-Stach period construction and its multiplicative Nori universal property. The rational directional fiber now cites Fresan–Jossen directly, using Theorem 2.4.11 for convolution and Theorem 2.8.1 for the fiber functor, with explicit topological rotation and scalar extension. Version-specific bibliography details are corrected. The existing Terenzi multi-exact pinpoints were checked in full.\n\nAll theorem statements and labels, the Section 3 realization architecture, and the downstream arithmetic/Tannakian/PV proofs are unchanged. The scope remains that of the preceding repair and its qualifications; this source follow-up is not another whole-paper certification. See the [build record](../provenance/paper-iv-comparison-citation-build-2026-10-05.json) for artifact validation.\n''')
subprocess.run(['git','diff','--check'],check=True)
print('Applied source clarification and three documentation edits; statements, labels, and downstream body preserved.')
