# Recovered manuscript baseline

These sources were recovered from saved research artifacts and selected as working starting points on 2026-09-17. This import is not a new mathematical audit or a publication-readiness certification. The user's separately stored local copies were not byte-compared.

The first import commit preserves the recovered source bytes and original filenames under `drafts/`. The following organization commit moves them to the working paths below without changing manuscript text. Git history preserves the original names. Dates below are artifact dates, not claims about the latest possible work in every conversation or local directory.

| Role | Original filename | Artifact date | Working path |
| --- | --- | --- | --- |
| I: Exponential Integral Theorem | `algebraic_exponential_integrals_streamlined_audited.tex` | 2026-08-13 | `papers/01-exponential-integral-theorem/exponential-integral-theorem.tex` |
| II: linear KZ | `compact_exponential_periods_affine_line_audited.tex` | 2026-08-13 | `papers/02-compact-polynomial-line-kz/linear-kz-affine-line.tex` |
| III: polynomial KZ | `polynomial_kz_affine_line_audited.tex` | 2026-08-13 | `papers/03-complete-polynomial-kz/polynomial-kz-affine-line.tex` |
| IV: relative exponential Nori–Ayoub | `relative_exponential_nori_ayoub_sabbah_integrated_20260814_v9.tex` | 2026-08-14 | `papers/04-relative-exponential-nori-ayoub/relative-exponential-nori-ayoub.tex` |
| V: polynomial flags (historical Paper IV) | `paper_iv_relative_exponential_periods_strengthened.tex` | 2026-08-05 | `papers/05-polynomial-flags/polynomial-flag-exponential-periods.tex` |
| II supplement | `paper_ii_alternate_presentations_and_extensions.tex` | 2026-08-13 | `papers/02-compact-polynomial-line-kz/linear-kz-supplement.tex` |
| III supplement | `paper_iii_retained_results.tex` | 2026-08-13 | `papers/03-complete-polynomial-kz/polynomial-kz-supplement.tex` |
| EIT structural companion | `eit_structural_companion.tex` | 2026-08-13 | `notes/eit-structural-companion.tex` |

## Selection rationale

- Paper I: the full-pass audit identifies this as the expanded, audited successor to the shorter streamlined source. Its audit and stress-test script were recovered from `eit_paper_I_full_audit_bundle.zip`.
- Paper II: the August 13 audit explicitly supersedes `paper_ii_compact_polynomial_line_kz_referee_revision_updated.tex`, aligns the moment-system conventions with Paper I, and retains ancillary constructions separately.
- Paper III: the August 13 audit explicitly reorganizes `paper_iii_complete_polynomial_kz_definitive.tex` into the focused main paper and retained-results supplement. The word “definitive” in the older filename is not a version guarantee.
- Paper IV: v9 is the newest recovered Nori–Ayoub source. A direct v7/v9 diff shows that the changes concern the functional Gamma example and associated introduction, conclusion, and references, not the main theorem's proof.
- Paper V: the strengthened source is the newest recovered polynomial-flags draft. Its numerical claims have the explicitly stated endpoint-complete hypotheses; it must not be described as an unrestricted two-variable theorem.
- The EIT structural companion is retained as a separate note, not silently merged into Paper I.

## Historical audit records

The records in `notes/provenance/` are preserved historical assessments. Statements such as “passed” or “no fatal gap” report those earlier assessments; this import does not independently certify them.

## Follow-up work

- Reconcile companion-paper titles and references, especially the older bibliography in Paper V, against the current I–III sources.
- Reconcile historical paper numbering in manuscript prose. Repository Paper IV is Nori–Ayoub; the polynomial-flags source was historically called Paper IV and is now filed as Paper V.
- Review authorship and publication metadata before release. The Nori–Ayoub source has a different author list from the other four; this import intentionally preserves it.
- Audit the mathematical dependency interfaces separately from mechanical compilation. Later conversation-only corrections may still need integration.
- Other recovered extensions (including Volterra closure and turning-defect notes) are outside this initial import and are not declared superseded.

The existing repository visibility and license are unchanged. No generated PDF is included in this source-only baseline.
