#!/usr/bin/env python3
"""Reconcile the exact initial closeout patch with concurrent Paper IV PR #7."""
from pathlib import Path
import hashlib
root = Path('.')
status=(root/'notes/repository-status.md').read_text()
status=status.replace('for Papers I, II, III,\nand V have been reconciled with the working sources.', 'for Papers I, II, III,\nand V have been reconciled with the working sources. The concurrent Paper IV\nintegration in PR #7 is also retained and reflected in this status.')
status=status.replace('| Paper V | PR #8', '| Paper IV and repair companion | PR #7, `31ea3d09d944` | Canonical realization, fixed-part, and functional-period repairs integrated in the concurrent workstream; its separate audit records the scope and qualifications. |\n| Paper V | PR #8')
status=status.replace('All eight active sources', 'All nine active sources')
status=status.replace('Paper IV\'s relative Nori–Ayoub proof is not\nan input to Paper V\'s actual elliptic independence theorem and is not\nnewly audited or revised in this closeout.', 'Paper IV\'s relative Nori–Ayoub proof is not\nan input to Paper V\'s actual elliptic independence theorem. Its concurrent\n[assembled-proof and integration audit](provenance/paper-iv-assembled-integration-audit-2026-09-29.md)\nand [latest repair-ledger entry](repairs/paper-iv-repair-ledger.md) record\nthat workstream\'s completed repairs; this closeout checks its dependencies\nand preserves its sources and PDFs, rather than repeating that proof audit.')
status=status.replace('The post-merge workflow on the Paper V rewrite baseline passed:', 'The closeout was reconciled onto `31ea3d09d944` after PR #7 added the ninth\nmanuscript. The README links and both Paper IV snapshots are retained.\nThe post-merge workflow on the initial Paper V rewrite baseline passed:')
status=status.replace('The local TeX Live shared-counter reference-label discrepancy on unchanged\nPaper IV is a documented toolchain issue. Its source and committed PDF\nare not changed to mask that difference. Repository Ubuntu 24.04 checks\nremain the reproducible full-snapshot validation environment.', 'The former local TeX Live reference-label discrepancy in canonical Paper IV\nwas resolved by PR #7\'s alias counters. The corresponding known discrepancy\nin the unchanged EIT structural companion remains a separate toolchain\nissue. This closeout does not alter that companion to mask the difference.\nRepository Ubuntu 24.04 checks remain the reproducible full-snapshot\nvalidation environment.')
(root/'notes/repository-status.md').write_text(status)
note=(root/'notes/provenance/repair-session-closeout-2026-09-29.md').read_text()
note=note.replace('Baseline: `1d91e575bbf44904e37b89d9c342c1b409f7e8bb` (merged PR #8).', 'Initial baseline: `1d91e575bbf44904e37b89d9c342c1b409f7e8bb` (merged PR #8).')
anchor='post-merge workflow `36527841497`, job `109274684840`, completed successfully.\n'
note=note.replace(anchor,anchor+'''\nBefore merging the closeout, concurrent PR #7 integrated repaired Paper IV
and added its companion as the ninth active manuscript. The closeout was
therefore reconciled onto `31ea3d09d9447a9dbdaa3bed65dd30e805b17fea`,
with exact verified tree `22535633182cbf4c709d8e7f9cf0e251cdb7b53a`.
The revised Paper IV, its companion, README additions, manifest entries,
and audit/ledger files are preserved. An initial successful eight-document
closeout build (`36530048558`) is superseded as the merge gate by the
reconciled nine-document build and its normal pull-request checks.
''')
note=note.replace('| V | PR #8', '| IV and repair companion | PR #7, `31ea3d09d944` | Concurrent canonical realization, fixed-part, and functional-period repairs; see its separately recorded assembled-proof and integration audit. |\n| V | PR #8')
note=note.replace('All eight active LaTeX sources were checked, together with the README,\nrepository status, and contribution instructions.', 'All nine active LaTeX sources were checked, together with the README,\nrepository status, and contribution instructions. The expanded check includes\nthe repaired canonical Paper IV, its retained companion, and the latest\ndated entry in the Paper IV repair ledger. Earlier dated ledger entries\nand audit memoranda remain historical records.')
note=note.replace('| Paper IV (relative Nori–Ayoub) | No dependence on Paper V. Its arithmetic-specialization limits are separate from its relative functional results. This pass is not a new audit of its proof. |', '| Paper IV (relative Nori–Ayoub), as integrated by PR #7 | No dependence on Paper V. Its abstract and introduction retain the separation between generic functional results and numerical specialization. This pass is not a new audit of its proof. |\n| Paper IV repair companion | Replacement arguments for the pre-repair Paper IV, retained with the canonical integration. No input from Paper V; the generic functional scope does not assert numerical specialization. |')
note=note.replace('the other seven manuscript sources, PDFs, and manifest', 'the other eight manuscript sources, PDFs, and manifest')
note=note.replace('The other seven manuscript sources, PDFs, and manifest', 'The other eight manuscript sources, PDFs, and manifest')
note=note.replace('The README links this note.', 'The README links this note and retains the ninth-document and Paper IV\naudit links introduced concurrently.')
note=note.replace('All\neight sources compiled.', 'All\nnine sources compiled after reconciliation.')
note=note.replace('The local TeX Live discrepancy on Paper IV\'s unchanged shared-counter\nreference labels is retained as a toolchain limitation, not hidden by an\nunrelated manuscript change. No assertion of byte-identical PDF production\nacross different TeX distributions is required by the repository checks.', 'The former local TeX Live discrepancy in canonical Paper IV\'s shared-counter\nreference labels was corrected by PR #7. The corresponding discrepancy\nin the unchanged structural companion remains a toolchain limitation, not\nhidden by an unrelated manuscript change. No assertion of byte-identical\nPDF production across different TeX distributions is required by the\nrepository checks.')
(root/'notes/provenance/repair-session-closeout-2026-09-29.md').write_text(note)
print('Applied reconciled closeout; Paper V source remains unchanged from reviewed candidate.')
