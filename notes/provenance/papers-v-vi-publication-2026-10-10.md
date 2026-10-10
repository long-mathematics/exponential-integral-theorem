# Papers V–VI: publication preparation and official PDF review

Date: 10 October 2026 (UTC).

## Checked snapshot

Baseline main is `22d98c4f27e606b5b25fa673c33f9c56c53cc86b`. The Ubuntu preparation run [38023587678](https://github.com/long-mathematics/exponential-integral-theorem/actions/runs/38023587678), job `114129599204`, completed successfully and committed the checked manuscripts at `1fd1d1b5cf1c2c9bac74fb39e723ce624b093725` (tree `1c5c95508e53a2e2e2878b9f28906952ba59f3ec`). Its trigger was `cf26f2dd0170ea955183e5cc22beefa1c3b06d62`.

The run verified the source payload before applying it, passed all 22 test methods, ran the extended comparison/factorial certificates through exponent 100 and the existing extended elliptic suite, compiled all 12 managed documents, restored the eight unrelated PDF snapshots and manifest entries byte-for-byte, and passed the complete `make check` including README links. The machine-readable record is [papers-v-vi-build-verification-2026-10-10.json](papers-v-vi-build-verification-2026-10-10.json); the mathematical scope and primary-reference review are in [the integration audit](papers-v-vi-audit-2026-10-10.md).

The downloaded checked-build artifact was independently unpacked. All 13 planned text-source hashes matched the audited payload; all 12 source/PDF manifest pairs matched the actual files. All eight unrelated manuscript/PDF manifest records and committed PDFs matched baseline. Paper V's preceding source and PDF are archived verbatim.

## Official PDFs

| Document | Pages | SHA-256 of committed PDF |
| --- | --- | --- |
| Paper V, polynomial-flag-exponential-periods.pdf | 28 | `9c69990246e7c364e2b79d6a275df58b6b0896d224b7081d18c5a593e57d6169` |
| Paper VI, exponential-factorial-moments.pdf | 11 | `e9371cd9803dbeea202b8efc5c7e543374857c78aa6f65172b5781958e0e98aa` |
| Simplex candidate, simplex-exponential-periods.pdf | 5 | `3af4899986d2c3c41462db5c24da16deeb7c62dc0cd6021f4a6a7e2900b23b26` |
| Multicolumn candidate, multicolumn-exponential-periods.pdf | 4 | `fa6d08be9f67d73acadbf28799ea4c0c853e7ce9b48b5901be26fe2cf117ab48` |

All 48 locally compiled pages were rendered and inspected, with the new linear, Zariski-open, rank-three, characteristic-five, and block-radial arguments also reviewed at full-page scale. PyMuPDF 1.26.7 comparisons of per-page text and 108-dpi RGB hashes establish exact rendered parity between the local reviewed and official PDFs for all 28 pages of V, all 11 pages of VI, and all four pages of the multicolumn candidate.

The simplex candidate is a documented exception to full environment parity. Its official pages 2, 3, and 5 correctly print cross-references as **Conjecture 1.1**, whereas the local TeX distribution labeled those same references **Theorem 1.1**. These are the only extracted-text differences; official pages 1 and 4 also have identical rendered hashes. The three differing official pages were separately rendered at full-page scale and visually inspected. The official conjecture labels are correct, the body explicitly identifies the statement as a conjecture, and no open claim is promoted. No source change was needed. Consequently this record does not claim all-four-document pixel identity across TeX environments.

The separate local full-snapshot mismatch in the untouched structural companion is preserved as an environment caveat in the integration audit. The successful Ubuntu check includes that preserved snapshot; it was not edited to conceal the mismatch.

## Final-tree and merge boundaries

This publication-preparation commit removes the temporary preparation workflow and its five source-transfer chunks. It adds only this record beyond the successfully built source/PDF snapshot. The normal `.github/workflows/latex.yml` remains unchanged and read-only; no repository settings, visibility, licensing, or protection rules are changed. No temporary preparation files are intended for the final main tree.

The ordinary pull-request workflow on the exact clean head remains a distinct merge gate. The actual PR number, final head, merge commit, and post-merge CI result are to be recorded in the PR discussion, not predicted here. The user authorized feature-branch publication and squash merge after checks.

The manuscripts remain working research drafts. This is a scoped AI-assisted mathematical/source review, finite exact verification, and build/render inspection, not independent specialist peer review or formal verification. The two unnumbered candidates retain their explicit open/conditional status.
