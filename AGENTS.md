# Repository instructions

- Treat `papers/` and `notes/eit-structural-companion.tex` as the canonical manuscript sources. Do not rename them merely to encode a version.
- For source changes, run `make test`, `make pdf`, and `make check`. Inspect changed PDF pages visually. Include updated PDFs and `output/pdf/manifest.json` in the same pull request.
- Keep purely editorial/build work separate from mathematical changes. Never silently change author lists, theorem hypotheses, proof status, or manuscript dates during cleanup.
- Preserve `notes/provenance/` as historical records. Add a new dated note for new findings instead of rewriting old audit verdicts.
- Use feature branches and pull requests. Do not bypass required checks or change visibility, licensing, or protection settings without an explicit request.
- Paper IV means relative exponential Nori–Ayoub; Paper V means polynomial flags (historically called Paper IV).
