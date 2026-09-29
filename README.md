# Exponential Integral Theorem

Research manuscripts on algebraic exponential integrals, compact exponential periods, Kontsevich–Zagier relations, and relative exponential fixed parts.

Authors: **Christopher D. Long and Antoine-Auguste Le Blanc**. Le Blanc cryptographic author identifier: `b604812530b3535b23d6dbb0f5abe32d1ed1a9de35fb4f7d04d62cff08ea19c8`.

## Read the papers

| Paper | Manuscript | PDF | LaTeX |
| --- | --- | --- | --- |
| I | Algebraic Exponential Integrals: Transcendence and Linear Relations | [Read PDF](output/pdf/exponential-integral-theorem.pdf) | [Source](papers/01-exponential-integral-theorem/exponential-integral-theorem.tex) |
| II | A Linear Kontsevich–Zagier Theorem for Compact Exponential Periods on the Affine Line | [Read PDF](output/pdf/linear-kz-affine-line.pdf) | [Source](papers/02-compact-polynomial-line-kz/linear-kz-affine-line.tex) |
| III | A Polynomial Kontsevich–Zagier Theorem for Compact Exponential Periods on the Affine Line | [Read PDF](output/pdf/polynomial-kz-affine-line.pdf) | [Source](papers/03-complete-polynomial-kz/polynomial-kz-affine-line.tex) |
| IV | Relative Exponential Fixed Parts and Functional Periods: An Exponential Nori–Ayoub Theorem | [Read PDF](output/pdf/relative-exponential-nori-ayoub.pdf) | [Source](papers/04-relative-exponential-nori-ayoub/relative-exponential-nori-ayoub.tex) |
| V | Relative Exponential Periods on Polynomial Flags: Polynomial Boundary Systems and an Elliptic Comparison Theorem | [Read PDF](output/pdf/polynomial-flag-exponential-periods.pdf) | [Source](papers/05-polynomial-flags/polynomial-flag-exponential-periods.tex) |

The PDFs are committed snapshots of the corresponding sources, not expiring build-artifact links. Access follows the repository's visibility.

### Scope and status

These are working research drafts. Their inclusion here and successful compilation are not new mathematical certifications.

- **I:** algebraic-value rigidity and common-polynomial linear relations.
- **II:** formal linear relations for compact affine-line exponential periods.
- **III:** polynomial relations for the tensor-generated affine-line algebra, building on I and II.
- **IV:** relative functional periods and exponential fixed parts. Numerical specialization remains a separate issue.
- **V:** general polynomial-representative boundary systems and an explicit fixed-triangle elliptic theorem: the two basic moments and their values at every nonzero algebraic parameter are algebraically independent over the associated fixed-face fields. Observable single-phase geometry is retained. General multiblock formal completeness remains conditional on actual linear and determinant-line realizations; this is not an unrestricted two-variable theorem.

The polynomial-flags manuscript was historically called “Paper IV”; this repository assigns it **Paper V** and reserves **Paper IV** for Nori–Ayoub. Historical audit filenames retain their original terminology.

## Supplements and notes

| Document | PDF | LaTeX |
| --- | --- | --- |
| Linear KZ: alternate presentations and extensions | [Read PDF](output/pdf/linear-kz-supplement.pdf) | [Source](papers/02-compact-polynomial-line-kz/linear-kz-supplement.tex) |
| Polynomial KZ: quadratic normal forms, tensor-square residues, and entire exponential integrals | [Read PDF](output/pdf/polynomial-kz-supplement.pdf) | [Source](papers/03-complete-polynomial-kz/polynomial-kz-supplement.tex) |
| EIT structural companion | [Read PDF](output/pdf/eit-structural-companion.pdf) | [Source](notes/eit-structural-companion.tex) |

## Build and check

On Debian/Ubuntu, install the build dependencies:

```sh
sudo apt-get install latexmk texlive-latex-extra texlive-fonts-recommended texlive-science lmodern poppler-utils python3 make
```

From the repository root:

```sh
make pdf    # compile all eight documents; refresh PDFs and manifest
make check  # verify hashes, rebuild, compare PDF text, and check README links
make test   # test the build checks
```

Each LaTeX source is standalone and has an embedded bibliography. PDFs live in `output/pdf/`; intermediate files stay in ignored `.build/`. The [manifest](output/pdf/manifest.json) records each source hash, PDF hash, and page count.

The [LaTeX workflow](.github/workflows/latex.yml) runs on pull requests and pushes to `main`. It checks committed snapshots without writing back to the repository and uploads fresh PDFs and logs for inspection.

### Paper V certificates and audit

The [focused audit and revision record](notes/provenance/paper-v-focused-audit-2026-09-29.md) supersedes the earlier Paper V endpoint verdict without changing historical reports. The [repair-session closeout](notes/provenance/repair-session-closeout-2026-09-29.md) records the cross-document dependency check, completed revisions, and the questions deliberately left for future research. The closeout clarifies scope and references; it does not enlarge the audited theorem.

```sh
python3 scripts/paper_v_certificate.py 'x**4 + 2*x*y**2 + 1/3'
python3 scripts/check_paper_v.py  # optional broader exact suite; requires SymPy
```

The certificate routine and its tests use only the Python standard library; `make test` runs them. The broader script writes its results under `.build/`. Neither finite checks nor a successful build constitute a formal proof certificate.

## Provenance and maintenance

- [Recovered drafts and original-to-working filename map](notes/provenance/draft-import.md)
- [Original import validation](notes/provenance/import-validation.md)
- [Repository setup and outstanding research checks](notes/repository-status.md)
- [Contribution and PDF-update workflow](CONTRIBUTING.md)

Historical audit reports are preserved in `notes/provenance/`. Stable filenames identify the working sources; Git records their revisions. Mathematical changes should be separated from editorial and build changes.

## License

[MIT License](LICENSE).
