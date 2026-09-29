#!/usr/bin/env python3
"""One-time typesetting corrections to the newly drafted repair note only."""
from pathlib import Path
import hashlib
import re

p = Path('papers/04-relative-exponential-nori-ayoub/repairs/paper-iv-repair-note.tex')
expected = '9540c6757e6943ee3aef12ec734c96cf51dcc682444dd737486e6705d81174d6'
before = p.read_bytes()
if hashlib.sha256(before).hexdigest() != expected:
    blob = hashlib.sha1(b'blob ' + str(len(before)).encode() + b'\0' + before).hexdigest()
    assert blob == '491ce5f95c5c8ae72acd9356c5bef2bb315c6b1a', blob
    text = before.decode('utf-8')
    text = text.replace('{input}', '{externalinput}').replace(r'\newtheorem{externalinput}[input]', r'\newtheorem{externalinput}[externalinput]')
    text = re.sub(r'\\Vec(?![A-Za-z])', lambda _: r'\VecCat', text)
    text = text.replace(r'\newcommand{\dR}{\mathrm{dR}}', r'\newcommand{\dR}{\mathrm{dR}}' + '\n' + r'\newcommand{\dRB}{\mathrm{dRB}}')
    text = text.replace(r'\Gm_\lambda', r'\Gm')
    start = text.index(r'\paragraph{Frozen baseline and status.}')
    end = text.index(r'\paragraph{Reading contract.}', start)
    text = text[:start] + r'''\paragraph{Frozen baseline and status.}
The repository path, frozen commit, and Paper IV source-blob identifier are,
respectively,
\begin{quote}\small\ttfamily
long-mathematics/exponential-integral-theorem\\
0bb151018dc73c9e48b847fff31fb82fd2cb9072\\
4cc45c6dd428e09cf5db940632106fc394d01393.
\end{quote}
The reference \path{baseline/paper-iv-pre-repair-2026-09-28} points to that
commit. The machine-readable baseline record contains the source and PDF
SHA-256 hashes. This note does not modify the baseline manuscript or its
26-page PDF. Its proofs are submitted for a fresh adversarial audit; they
are not an independently checked certification or an integrated revision.

''' + text[end:]
    text = text.replace(r'\subsection{An explicit equivariant comparison over $\C(S)$}', r'\subsection{An explicit equivariant comparison over \texorpdfstring{$\C(S)$}{C(S)}}')
    assert hashlib.sha256(text.encode()).hexdigest() == expected
    assert re.findall(r'\\label\{([^}]+)\}', text) == re.findall(r'\\label\{([^}]+)\}', before.decode())
    p.write_text(text, encoding='utf-8')
print('Verified corrected note source:', expected)
