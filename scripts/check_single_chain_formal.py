#!/usr/bin/env python3
"""Exact supplemental checks for the single-chain theorem's formal calculations.

These finite rational computations supplement, not replace, the general proof.
The six formal powers are certified by a Vandermonde trace test without
choosing algebraic eigenvectors.
"""
from pathlib import Path
import importlib.util
import sys
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
candidate = ROOT / "notes/candidates/2026-10-06-single-chain/frozen/check_generic_example_audited.py"
spec = importlib.util.spec_from_file_location("example_check", candidate)
if spec is None or spec.loader is None:
    raise RuntimeError(f"Cannot import certificate: {candidate}")
m = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = m
spec.loader.exec_module(m)


def require(test, message):
    if not bool(test):
        raise RuntimeError(message)


def diag(a):
    return sp.diag(*a.diagonal())


basis = [1, m.x, m.x**2, m.y, m.x*m.y, m.x**2*m.y]
a = sp.zeros(6)
for i, amplitude in enumerate(basis):
    r, p, q = m.normal_form(m.q*amplitude)
    require(sp.expand(m.q*amplitude-r-m.lx(p)-m.ly(q)) == 0,
            "Polynomial certificate failed")
    rpoly = sp.Poly(r, m.x, m.y)
    for j, b in enumerate(basis):
        a[i, j] = rpoly.coeff_monomial(b)
a0 = a.applyfunc(lambda e: sp.limit(e, m.z, sp.oo))
a1 = (a-a0).applyfunc(lambda e: sp.limit(m.z*e, m.z, sp.oo))
require((a-a0-a1/m.z).applyfunc(sp.simplify) == sp.zeros(6),
        "Connection has extra terms")
chi = sp.Poly(a0.charpoly(m.t).as_expr(), m.t)
require(sp.gcd(chi, chi.diff()).degree() == 0, "A0 has repeated eigenvalues")
traces = [sp.trace(a0**k * (a1+sp.eye(6))) for k in range(6)]
require(all(t == 0 for t in traces), "Formal-power trace test failed")
print("PASS: A0 has simple spectrum.")
print("PASS: tr(A0^k (A1+I))=0 for k=0,...,5:", traces)
print("By the invertible Vandermonde matrix in the six distinct eigenvalues,")
print("the diagonal of A1 in an eigenbasis of A0 is (-1,-1,-1,-1,-1,-1).")
print("Thus all six formal powers lambda_i equal -1 exactly.")

# Rational simple-spectrum instance with several nonzero higher A_j.
n, order = 3, 8
c = sp.diag(-2, 1, 4)
a_coeff = [c,
           sp.Matrix([[1, 2, -1], [3, -2, 4], [2, 1, 5]]),
           sp.Matrix([[2, 0, 3], [-1, 1, 2], [4, -2, 0]]),
           sp.Matrix([[0, -3, 1], [2, 2, -1], [1, 5, -2]])]
lam = diag(a_coeff[1])
h = [sp.eye(n)] + [sp.zeros(n) for _ in range(order+2)]
for k in range(1, order+2):
    if k >= 2:
        rest = (a_coeff[1]-diag(a_coeff[1]))*(h[k-1]-diag(h[k-1]))
        rest += sum((a_coeff[j]*h[k-j] for j in range(2, min(k, len(a_coeff)-1)+1)), sp.zeros(n))
        for i in range(n):
            h[k-1][i, i] = -rest[i, i]/(k-1)
    rest = sum((a_coeff[j]*h[k-j] for j in range(1, min(k, len(a_coeff)-1)+1)), sp.zeros(n))
    rhs = -(k-1)*h[k-1]-rest+h[k-1]*lam
    require(all(rhs[i, i] == 0 for i in range(n)), "Diagonal recursion inconsistency")
    for i in range(n):
        for j in range(n):
            if i != j:
                h[k][i, j] = rhs[i, j]/(c[i, i]-c[j, j])
for k in range(1, order+1):
    residual = -(k-1)*h[k-1]-(c*h[k]-h[k]*c)
    residual -= sum((a_coeff[j]*h[k-j] for j in range(1, min(k, len(a_coeff)-1)+1)), sp.zeros(n))
    residual += h[k-1]*lam
    require(residual == sp.zeros(n), f"Formal residual nonzero at w^{k}")
print("PASS: exact rational 3x3 recursion, residual coefficients w^1,...,w^8 all zero.")
print("These finite checks supplement, and do not replace, the general induction.")
