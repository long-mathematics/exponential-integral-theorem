import importlib.util
from pathlib import Path
import tempfile
import unittest

spec = importlib.util.spec_from_file_location("build", Path(__file__).resolve().parents[1] / "scripts/build.py")
build = importlib.util.module_from_spec(spec)
spec.loader.exec_module(build)


class BuildChecks(unittest.TestCase):
    def test_author_identifier(self):
        text = (r"\author{Christopher D. Long \and Antoine-Auguste Le Blanc "
                + build.LE_BLANC_ID + "}\n"
                + "pdfauthor={Christopher D. Long; Antoine-Auguste Le Blanc}")
        build.check_authors(text)
        with self.assertRaises(RuntimeError):
            build.check_authors(text.replace(build.LE_BLANC_ID, "wrong"))

    def test_clean_log(self):
        build.check_log("Output written on paper.pdf\nUnderfull \\hbox (badness 1000)")

    def test_bad_logs(self):
        for line in ["! Undefined control sequence.",
                     "LaTeX Warning: There were undefined references.",
                     "LaTeX Warning: Citation `missing' undefined on input line 10.",
                     "LaTeX Warning: Label `a' multiply defined.",
                     "Overfull \\hbox (10pt too wide)"]:
            with self.subTest(line=line), self.assertRaises(RuntimeError):
                build.check_log(line)

    def test_links(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / "paper.tex").touch()
            (root / "README.md").write_text("[source](paper.tex) [site](https://example.com) [heading](#title)")
            build.check_readme_links(root)
            (root / "README.md").write_text("[PDF](missing.pdf)")
            with self.assertRaises(RuntimeError):
                build.check_readme_links(root)

    def test_stale_snapshot(self):
        with tempfile.TemporaryDirectory() as folder:
            source, pdf = Path(folder) / "paper.tex", Path(folder) / "paper.pdf"
            source.write_text("source")
            pdf.write_bytes(b"snapshot")
            record = {"source_sha256": build.digest(source), "pdf_sha256": build.digest(pdf)}
            build.verify_record(record, source, pdf)
            source.write_text("changed")
            with self.assertRaises(RuntimeError):
                build.verify_record(record, source, pdf)
            source.write_text("source")
            pdf.write_bytes(b"changed")
            with self.assertRaises(RuntimeError):
                build.verify_record(record, source, pdf)


if __name__ == "__main__":
    unittest.main()
