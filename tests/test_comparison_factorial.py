"""Regression checks for V/VI additions; not a formal proof audit."""
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]

class ComparisonFactorialChecks(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temporary = tempfile.TemporaryDirectory()
        report = Path(cls.temporary.name) / 'checks.json'
        result = subprocess.run([sys.executable,
            str(ROOT / 'scripts/check_comparison_factorial.py'),
            '--max-k', '100', '--output', str(report)],
            cwd=ROOT, capture_output=True, text=True, timeout=180)
        if result.returncode:
            raise RuntimeError(result.stdout + result.stderr)
        cls.report = json.loads(report.read_text())

    @classmethod
    def tearDownClass(cls):
        cls.temporary.cleanup()

    def test_rank_three_and_separation(self):
        self.assertEqual(self.report['weaker_root_separation_example']['distinct_ordered_differences'],12)
        self.assertEqual(len(self.report['noncoprime_rank_three']['literal_stokes_certificates']),3)
        self.assertEqual(len(self.report['noncoprime_boundary_separation']['edges']),3)
        self.assertEqual(len(self.report['rank_three_interior_minimum']['signed_edge_tests']),3)

    def test_all_exponent_certificate_and_finite_range(self):
        self.assertEqual(self.report['elliptic_mod5']['determinant_mod5'],2)
        self.assertEqual(self.report['elliptic_mod5']['initial_vectors_checked'],5)
        finite=self.report['elliptic_finite_coprimality']
        self.assertEqual(finite['number_of_gcds'],101)
        self.assertEqual(finite['range'],[0,100])
        self.assertEqual(finite['maximum_polynomial_degree'],50)
        self.assertTrue(finite['all_gcd_degrees_zero'])

    def test_radial_and_simplex_normalizations(self):
        self.assertEqual(self.report['simplex_affine_jacobians'],{'elliptic':2,'odd_a_absolute':4})
        self.assertEqual(self.report['simplex_monomial_normalizations']['number_checked'],70)
        self.assertGreater(self.report['radial_coefficient_bounds']['cases'],1000)
        self.assertIn('positive_amplitude_counterexample',self.report)

    def test_preserved_pre_revision_snapshot(self):
        archive=ROOT / 'notes/archives/2026-10-10-paper-v-before-two-level'
        for suffix, digest in [
            ('tex','161726ecb44f8b06977c290638a594ddc77c169b5cf83e974e161efa23189e24'),('pdf','bd92cb30c4d406b9246d56eff91217543c2c237d6028f33604e8aa937e088873')]:
            self.assertEqual(hashlib.sha256((archive / ('polynomial-flag-exponential-periods.'+suffix)).read_bytes()).hexdigest(),digest)

    def test_scope_and_source_labels(self):
        v=(ROOT/'papers/05-polynomial-flags/polynomial-flag-exponential-periods.tex').read_text()
        for label in ['thm:linear','prop:linear-criterion','lem:extremum',
                      'prop:root-open','cor:boundary-tests','thm:noncoprime',
                      'thm:main','thm:elliptic-main']:
            self.assertIn('\\label{'+label+'}',v)
        self.assertIn('Neither (R), (Q), nor (F) is required',v)
        self.assertIn('rank at most one',v)
        vi=(ROOT/'papers/06-exponential-factorial-moments/exponential-factorial-moments.tex').read_text()
        for label in ['thm:radial','thm:odd-family','thm:modfive','thm:elliptic-family',
                      'prop:finite','thm:block-limit','thm:complex']:
            self.assertIn('\\label{'+label+'}',vi)
        self.assertIn('No uniform coprimality assertion',vi)
        self.assertIn('not require multicolumn algebraic independence',vi)

    def test_candidate_status_is_explicit(self):
        for folder,stem in [
            ('2026-10-10-simplex-program','simplex-exponential-periods'),
            ('2026-10-10-multicolumn-program','multicolumn-exponential-periods')]:
            text=(ROOT/'notes/candidates'/folder/(stem+'.tex')).read_text()
            self.assertIn('Candidate research draft; not a numbered paper',text)
            self.assertIn('No',text)

if __name__=='__main__':
    unittest.main()
