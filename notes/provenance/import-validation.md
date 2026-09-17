# Import validation

On 2026-09-17, all five selected main manuscripts, both supplements, and the EIT structural companion compiled successfully using TeX Live 2023 and `latexmk -pdf -interaction=nonstopmode -halt-on-error`.

Final logs contained no undefined references, undefined citations, multiply defined labels, or overfull boxes. The Nori–Ayoub draft reported one underfull bibliography line. This was a compilation/log check, not a fresh visual or mathematical audit.

The source SHA-256 hashes below identify the unchanged imported bytes; the organization commit only changes their paths.

| Working path | SHA-256 |
| --- | --- |
| `papers/01-exponential-integral-theorem/exponential-integral-theorem.tex` | `12a787a6b3424da69a802961ba268f00035fa24bdcd3e283b5be7e073e0ca254` |
| `papers/02-compact-polynomial-line-kz/linear-kz-affine-line.tex` | `4a557f3bd8ab93702b02603b973cff06be2fffec699d0b16b30957b1e53f02d9` |
| `papers/03-complete-polynomial-kz/polynomial-kz-affine-line.tex` | `7bb44d707ac87c096169d1e2bd7dc2b8799827ed791ac6a8b4d2c0c2831cf5ec` |
| `papers/04-relative-exponential-nori-ayoub/relative-exponential-nori-ayoub.tex` | `975ddae72e4ecee71c2bdd5f39391440defa0bf912f8e4d2b132349cab4872af` |
| `papers/05-polynomial-flags/polynomial-flag-exponential-periods.tex` | `4bc47cb092d7926c623ced00bd07794da0e7c0cd4fca57e3eab2dc20e1e819e6` |
| `papers/02-compact-polynomial-line-kz/linear-kz-supplement.tex` | `70a2842ffa229edff89e803e9fde736e5f065605cdf013a98d16ed7225803db8` |
| `papers/03-complete-polynomial-kz/polynomial-kz-supplement.tex` | `d81da044877537ecb2b96a74d54e4415a27242ec499929580eab7028c35acbe5` |
| `notes/eit-structural-companion.tex` | `50526b6246ccd1a42680214e36f6cd365e1ec0fe2ed1b032f4c4d6af95364963` |
