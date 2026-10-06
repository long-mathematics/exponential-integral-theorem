# Paper V single-chain publication — 6 October 2026

## Exact prepared revision

This publication uses the checked integration tree `7115d12131ed7d20214e90465a0983cec9ba6f2c`, prepared in GitHub Actions run `37446965266` and preserved as commit `aee6a1d00cad97152f356fc3354598e2c8488da4`. The locally delivered integration archive was reconstructed as a Git tree; its tree ID matched that value exactly. The preceding preparation run completed the manuscript checks but failed at its subsequent push, so that historical run must not be described as an overall green workflow.

Publication is a fast-forward addition to feature branch `revision/paper-v-single-chain-2026-10-06`, starting at `80ce82b42e3329793f2c6ac98390f46f1fbbe313`, not a direct push to main. Main was independently checked at `d5ae8f9081c7bc34d1622316bd8463482f244395` before publication. No author list, manuscript date, visibility, license, or repository protection setting is changed.

The only changes to the checked integration tree are removal of the obsolete `successor/prepare-trigger.txt` and addition of this publication record. The temporary preparation workflow remains absent. The existing `LaTeX` workflow has `contents: read`; its only previously prepared changes install `python3-sympy` and use the system Python for the test command. There is no workflow write permission or self-modifying preparation job in the published tree.

## Identity and preservation checks

- Canonical Paper V source SHA-256: `600a12bc83ee64a12c43311df34fe354e94fddb6672bb800364c913692431796`.
- Its managed 21-page PDF SHA-256: `a98b59aa13b84b5c567b9cffce6afb034290fac22db17a62706cca5a99545c05`.
- Archived previous Paper V source Git blob: `8244fc3f9229d74ba3f24f99363a306ad6139a87`.
- Frozen candidate source Git blob: `a7e998233ab4f096cb9bd5f40d641e07ca0dfddf`.

All nine source/PDF pairs were checked against their committed manifest hashes again before publication. All 15 `make test` tests passed again locally, including the exact elliptic, rank-six, formal-recursion, and frozen-source tests. The prior integration record and build JSON retain the all-nine Ubuntu `make test`, `make pdf`, and `make check` evidence and the preservation checks for the eight unrelated source/PDF pairs. The previously recorded local TeX cross-reference-rendering discrepancy in the untouched structural companion is not silently treated as a local full-build pass.

The 12-page successor, 21-page integrated manuscript, prior complete manuscript archive, frozen candidate, proof supplement, and exact scripts remain in their established paths. No further mathematical revision has been made during publication. The stated Morse, critical-value independence, face-separation, and saddle-or-continuation hypotheses remain. The previously withdrawn unrestricted endpoint-complete claim is not restored; genericity and general formal completeness are not claimed.

## Review and merge boundary

The ordinary pull-request LaTeX workflow must pass on the final proposed tree before squash merge. Inspect the complete main-to-feature diff, confirm that only the intended Paper V source and PDF pair changed among the canonical documents, and retain all historical audit records. The PR's checks and merge metadata provide the authoritative final publication outcome; this pre-merge record does not claim that future checks or the merge have already happened.

Earlier audit notes describing assembly or merge as pending record their state at the time and are deliberately not rewritten. Successful builds and AI-assisted proof audits are not independent specialist refereeing or formal verification.
