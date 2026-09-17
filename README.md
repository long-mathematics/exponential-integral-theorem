# Exponential Integral Theorem

Working research repository for the Exponential Integral Theorem and its compact exponential-period, Kontsevich–Zagier, relative Nori–Ayoub, and polynomial-flag companions.

## Manuscripts

| Paper | Subject | Source |
| --- | --- | --- |
| I | Exponential Integral Theorem | [exponential-integral-theorem.tex](papers/01-exponential-integral-theorem/exponential-integral-theorem.tex) |
| II | Linear Kontsevich–Zagier theorem on the affine line | [linear-kz-affine-line.tex](papers/02-compact-polynomial-line-kz/linear-kz-affine-line.tex) |
| III | Polynomial Kontsevich–Zagier theorem on the affine line | [polynomial-kz-affine-line.tex](papers/03-complete-polynomial-kz/polynomial-kz-affine-line.tex) |
| IV | Relative exponential fixed parts and Nori–Ayoub | [relative-exponential-nori-ayoub.tex](papers/04-relative-exponential-nori-ayoub/relative-exponential-nori-ayoub.tex) |
| V | Polynomial-flag exponential periods | [polynomial-flag-exponential-periods.tex](papers/05-polynomial-flags/polynomial-flag-exponential-periods.tex) |

These are recovered working drafts, not newly certified proofs or publication releases. Paper V's numerical theorem is restricted to its endpoint-complete hypotheses. Paper IV concerns functional periods; numerical specialization is a separate issue.

## Supplements and notes

- [Linear KZ supplement](papers/02-compact-polynomial-line-kz/linear-kz-supplement.tex): alternate presentations and extensions.
- [Polynomial KZ supplement](papers/03-complete-polynomial-kz/polynomial-kz-supplement.tex): quadratic normal forms, tensor-square residues, and entire exponential integrals.
- [EIT structural companion](notes/eit-structural-companion.tex).
- [Draft provenance and original filenames](notes/provenance/draft-import.md).

Historical audit and revision records are kept in `notes/provenance/`; they should not be confused with a fresh verification of the imported sources.

## Building

Each `.tex` file is a standalone document with its own embedded bibliography. A TeX Live installation and `latexmk` are required. For example, from the repository root:

```sh
cd papers/01-exponential-integral-theorem
latexmk -pdf -interaction=nonstopmode -halt-on-error exponential-integral-theorem.tex
```

The same command applies to the other source files in their respective directories. Generated PDFs and build intermediates are not part of this initial source import.

## Working conventions

Use stable descriptive source names; Git records revisions instead of filename suffixes such as `updated`, `definitive`, or `v9`. Keep mathematical edits separate from moves and formatting changes. The original polynomial-flags “Paper IV” is organized here as Paper V.

## License

See [LICENSE](LICENSE).
