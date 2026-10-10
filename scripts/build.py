#!/usr/bin/env python3
"""Build all standalone manuscripts; check committed PDFs without modifying them."""

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "output/pdf"
MANIFEST = OUTPUT / "manifest.json"
BUILD = ROOT / ".build"
LE_BLANC_ID = "b604812530b3535b23d6dbb0f5abe32d1ed1a9de35fb4f7d04d62cff08ea19c8"
CONTACT_BLOCK = "\n".join((r"\maketitle", "", r"\begin{center}", r"\small",
                           r"\texttt{galizur@gmail.com}", r"\end{center}"))


def check_authors(text):
    author = next((line for line in text.splitlines() if line.startswith(r"\author{")), "")
    compact = author.replace(r"\allowbreak{}", "")
    if ("Christopher D. Long" not in author or "Antoine-Auguste Le Blanc" not in author
            or LE_BLANC_ID not in compact
            or "pdfauthor={Christopher D. Long; Antoine-Auguste Le Blanc}" not in text):
        raise RuntimeError("Author list, Le Blanc identifier, or PDF author metadata is inconsistent")


def check_front_matter(text):
    check_authors(text)
    if "headlamp" in text.lower():
        raise RuntimeError("Removed affiliation remains in manuscript")
    if not text.startswith(r"\documentclass[11pt]{article}") or CONTACT_BLOCK not in text:
        raise RuntimeError("Inconsistent document class or title-page contact block")
    months = "January|February|March|April|May|June|July|August|September|October|November|December"
    if not re.search(r"^\\date\{(?:" + months + r") \d{4}\}$", text, re.M):
        raise RuntimeError("Use an explicit Month YYYY manuscript date")
    title = re.search(r"^\\title\{([^{}]+)\}", text, re.M)
    metadata = re.search(r"pdftitle=\{([^{}]+)\}", text)
    if (not title or not metadata
            or " ".join(title[1].replace(r"\\", " ").split()) != metadata[1]):
        raise RuntimeError("Printed title and PDF title metadata differ")


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def check_log(text):
    patterns = [r"^!", r"LaTeX Warning:.*undefined", r"Citation .* undefined",
                r"Reference .* undefined", r"multiply defined", r"Overfull "]
    errors = [line for line in text.splitlines()
              if any(re.search(pattern, line) for pattern in patterns)]
    if errors:
        raise RuntimeError("Unresolved LaTeX diagnostics:\n" + "\n".join(errors))


def check_readme_links(root):
    text = (root / "README.md").read_text(encoding="utf-8")
    for target in re.findall(r"\]\(([^)]+)\)", text):
        if re.match(r"[a-zA-Z][a-zA-Z0-9+.-]*:", target) or target.startswith("#"):
            continue
        target = target.split("#", 1)[0]
        if not (root / target).exists():
            raise RuntimeError("Broken README link: " + target)


def sources():
    result = sorted((ROOT / "papers").rglob("*.tex"))
    result.append(ROOT / "notes/eit-structural-companion.tex")
    # Explicit opt-in: do not compile historical/frozen candidates recursively.
    result.extend(ROOT / p for p in (
        "notes/candidates/2026-10-10-simplex-program/simplex-exponential-periods.tex",
        "notes/candidates/2026-10-10-multicolumn-program/multicolumn-exponential-periods.tex",
    ))
    names = [p.stem for p in result]
    if len(names) != len(set(names)):
        raise RuntimeError("Duplicate manuscript basenames would overwrite PDFs")
    return result


def pdf_text(path):
    return subprocess.check_output(["pdftotext", "-layout", str(path), "-"],
                                   text=True, encoding="utf-8")


def verify_record(record, source, pdf):
    if record.get("source_sha256") != digest(source):
        raise RuntimeError("Source changed; run make pdf: " + source.name)
    if not pdf.exists() or record.get("pdf_sha256") != digest(pdf):
        raise RuntimeError("Missing or modified PDF; run make pdf: " + pdf.name)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true",
                        help="validate snapshots; do not replace committed PDFs")
    args = parser.parse_args()
    for command in ("latexmk", "pdflatex", "pdftotext", "pdfinfo"):
        if shutil.which(command) is None:
            raise RuntimeError("Missing dependency: " + command)
    inputs = sources()
    for source in inputs:
        check_front_matter(source.read_text(encoding="utf-8"))
    old = {}
    if args.check:
        if not MANIFEST.exists():
            raise RuntimeError("Missing PDF manifest; run make pdf")
        old = {r["source"]: r for r in json.loads(MANIFEST.read_text())["documents"]}
        expected = {str(p.relative_to(ROOT)) for p in inputs}
        if set(old) != expected:
            raise RuntimeError("Manifest/source list mismatch; run make pdf")
        for source in inputs:
            verify_record(old[str(source.relative_to(ROOT))], source,
                          OUTPUT / (source.stem + ".pdf"))
    records = []
    env = dict(os.environ, SOURCE_DATE_EPOCH="1786665600", FORCE_SOURCE_DATE="1",
               TZ="UTC")  # Fixed build timestamp; manuscript dates remain explicit.
    for source in inputs:
        folder = BUILD / source.stem
        folder.mkdir(parents=True, exist_ok=True)
        print("Building " + str(source.relative_to(ROOT)), flush=True)
        command = ["latexmk", "-pdf", "-g", "-interaction=nonstopmode",
                   "-halt-on-error", "-file-line-error", "-latexoption=-no-shell-escape",
                   "-outdir=" + str(folder), source.name]
        result = subprocess.run(command, cwd=source.parent, env=env,
                                capture_output=True, text=True, timeout=180)
        (folder / "build-console.txt").write_text(result.stdout + result.stderr)
        if result.returncode:
            raise RuntimeError("LaTeX failed; see " + str(folder / "build-console.txt"))
        log = (folder / (source.stem + ".log")).read_text(errors="replace")
        check_log(log)
        for line in log.splitlines():
            if "Underfull " in line:
                print("  Nonfatal typography diagnostic: " + line)
        built = folder / (source.stem + ".pdf")
        committed = OUTPUT / built.name
        info = subprocess.check_output(["pdfinfo", str(built)], text=True)
        pages = int(re.search(r"^Pages:\s+(\d+)", info, re.M).group(1))
        if args.check and pdf_text(built) != pdf_text(committed):
            raise RuntimeError("Rebuilt PDF text differs; run make pdf: " + built.name)
        records.append({"source": str(source.relative_to(ROOT)),
                        "source_sha256": digest(source),
                        "pdf": str(committed.relative_to(ROOT)),
                        "pdf_sha256": digest(committed if args.check else built),
                        "pages": pages})
    if not args.check:
        OUTPUT.mkdir(parents=True, exist_ok=True)
        for source in inputs:
            shutil.copyfile(BUILD / source.stem / (source.stem + ".pdf"),
                            OUTPUT / (source.stem + ".pdf"))
        MANIFEST.write_text(json.dumps({"schema_version": 1,
                                       "documents": records}, indent=2) + "\n")
    check_readme_links(ROOT)
    print("Verified %d documents and README links." % len(inputs))


if __name__ == "__main__":
    try:
        main()
    except (RuntimeError, subprocess.SubprocessError, OSError, ValueError) as error:
        print(str(error), file=sys.stderr)
        sys.exit(1)
