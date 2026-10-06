"""Exact finite regression tests for the integrated single-chain theorem."""
import hashlib
from pathlib import Path
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
FOLDER = ROOT / 'notes/candidates/2026-10-06-single-chain'


class SingleChainCertificates(unittest.TestCase):
    def run_suite(self, suite, required):
        result = subprocess.run(
            [sys.executable, str(ROOT / 'scripts/check_single_chain.py'), '--suite', suite],
            cwd=ROOT, capture_output=True, text=True, timeout=150)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        for phrase in required:
            self.assertIn(phrase, result.stdout)

    def test_rank_six_example(self):
        self.run_suite('example', [
            'ALL EXACT ALGEBRAIC AND GEOMETRIC CERTIFICATES PASSED.',
            'exactly two real critical points', 'Frobenius type modulo 31'])

    def test_formal_recursion_and_powers(self):
        self.run_suite('formal', [
            'all six formal powers lambda_i equal -1 exactly',
            'residual coefficients w^1,...,w^8 all zero'])

    def test_frozen_source_unchanged(self):
        raw = (FOLDER / 'frozen/generic-single-chain-theorem.tex').read_bytes()
        digest = hashlib.sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest()
        self.assertEqual(digest, 'a7e998233ab4f096cb9bd5f40d641e07ca0dfddf')

    def test_canonical_density_and_metadata_closeout(self):
        source = (ROOT / 'papers/05-polynomial-flags/polynomial-flag-exponential-periods.tex').read_text()
        self.assertIn(r'\label{def:polynomial-chain}', source)
        self.assertIn(r'\label{def:chain-multiplicity}', source)
        self.assertIn(r'\label{lem:phase-density}', source)
        self.assertIn(r'$\rho=\rho_{D,1}, source)
        self.assertIn('Polynomial Chains', source)
        self.assertNotIn('Stokes matrix', source)
        self.assertNotIn('14D07', source)
        self.assertNotIn('14H40', source)
        self.assertIn(r'K_{\partial,0}\subset K_\partial', source)
        # Both Milne pinpoints were independently source-checked and are correct.
        self.assertIn(r'Proposition~15.15', source)
        self.assertIn(r'Corollary~22.43', source)

    def test_successor_has_lattice_proof_and_scope(self):
        source = (FOLDER / 'successor/generic-single-chain-theorem-v2.tex').read_text()
        self.assertIn(r'\label{lem:lattice}', source)
        self.assertIn(r'\label{lem:rankone}', source)
        self.assertIn(r'\label{cor:face-lattice}', source)
        self.assertNotIn(r'\label{lem:exponents}', source)
        self.assertNotIn(r'\Lambda_\infty', source)
        self.assertIn('its failure alone does not imply', source)
        self.assertIn('coefficient module', source)
        self.assertIn('off-diagonal intersection numbers', source)
        self.assertIn('rational', source)


if __name__ == '__main__':
    unittest.main()
, source)
        self.assertIn('Polynomial Chains', source)
        self.assertNotIn('Stokes matrix', source)
        self.assertNotIn('14D07', source)
        self.assertNotIn('14H40', source)
        self.assertIn(r'K_{\\partial,0}\\subset K_\\partial', source)
        # Both Milne pinpoints were independently source-checked and are correct.
        self.assertIn(r'Proposition~15.15', source)
        self.assertIn(r'Corollary~22.43', source)

    def test_successor_has_lattice_proof_and_scope(self):
        source = (FOLDER / 'successor/generic-single-chain-theorem-v2.tex').read_text()
        self.assertIn(r'\label{lem:lattice}', source)
        self.assertIn(r'\label{lem:rankone}', source)
        self.assertIn(r'\label{cor:face-lattice}', source)
        self.assertNotIn(r'\label{lem:exponents}', source)
        self.assertNotIn(r'\Lambda_\infty', source)
        self.assertIn('its failure alone does not imply', source)
        self.assertIn('coefficient module', source)
        self.assertIn('off-diagonal intersection numbers', source)
        self.assertIn('rational', source)


if __name__ == '__main__':
    unittest.main()
