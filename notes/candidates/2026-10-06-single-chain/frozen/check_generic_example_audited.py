#!/usr/bin/env python3
"""Exact algebraic certificates for q = x^4 + y^3 + xy - y.

Requires Python 3.10+ and SymPy. Run:
    python check_generic_example_audited.py

All tests use exact rational arithmetic, polynomial identities, finite-field
arithmetic, Sturm root counts, or interval bounds on whole intervals.
No test of a sign at a root is inferred merely from signs at interval endpoints.
These computations certify the explicit example, not the analytic and
monodromy assertions in the generic theorem. No files or repositories are changed.
"""
from __future__ import annotations
from dataclasses import dataclass
import sympy as sp

x, y, z, t = sp.symbols("x y z t")
q = x**4 + y**3 + x*y - y
qx, qy = sp.diff(q, x), sp.diff(q, y)


def check(condition: object, message: str) -> None:
    """Do not use assert: checks remain active under python -O."""
    if not bool(condition):
        raise RuntimeError(message)


def lx(p: sp.Expr) -> sp.Expr:
    return sp.expand(sp.diff(p, x) + z*qx*p)


def ly(p: sp.Expr) -> sp.Expr:
    return sp.expand(sp.diff(p, y) + z*qy*p)


def normal_form(r: sp.Expr) -> tuple[sp.Expr, sp.Expr, sp.Expr]:
    """Weighted reduction, with the entire polynomial Stokes certificate."""
    r = sp.expand(r)
    p = qq = sp.S.Zero
    while True:
        bad = [(mon, c) for mon, c in sp.Poly(r, x, y).terms()
               if mon[0] >= 3 or mon[1] >= 2]
        if not bad:
            return r, sp.expand(p), sp.expand(qq)
        (i, j), c = max(bad, key=lambda term:
                        (3*term[0][0] + 4*term[0][1], term[0]))
        if i >= 3:
            v = c*x**(i-3)*y**j/(4*z)
            p += v
            r = sp.expand(r-lx(v))
        else:
            v = c*x**i*y**(j-2)/(3*z)
            qq += v
            r = sp.expand(r-ly(v))


@dataclass(frozen=True)
class Interval:
    lo: sp.Rational
    hi: sp.Rational

    def __post_init__(self) -> None:
        check(self.lo <= self.hi, "Reversed interval")

    def __add__(self, other: Interval) -> Interval:
        return Interval(self.lo + other.lo, self.hi + other.hi)

    def __mul__(self, other: Interval) -> Interval:
        products = [self.lo*other.lo, self.lo*other.hi,
                    self.hi*other.lo, self.hi*other.hi]
        return Interval(min(products), max(products))


def interval_evaluate(poly: sp.Poly, domain: Interval) -> Interval:
    """Horner enclosure valid at EVERY point of the given rational interval."""
    result = Interval(sp.S.Zero, sp.S.Zero)
    for coefficient in poly.all_coeffs():
        coefficient = sp.Rational(coefficient)
        result = result*domain + Interval(coefficient, coefficient)
    return result


def sturm_variations(poly: sp.Poly, point: sp.Expr) -> int:
    signs = []
    for member in sp.sturm(poly.as_expr(), poly.gen):
        p = sp.Poly(member, poly.gen, domain=sp.QQ)
        if point == sp.oo:
            sign = sp.sign(p.LC())
        elif point == -sp.oo:
            sign = sp.sign(p.LC())*(-1)**p.degree()
        else:
            sign = sp.sign(p.eval(point))
        if sign != 0:
            signs.append(sign)
    return sum(u != v for u, v in zip(signs, signs[1:]))


def sturm_count(poly: sp.Poly, lo: sp.Expr, hi: sp.Expr) -> int:
    for endpoint in (lo, hi):
        if endpoint not in (-sp.oo, sp.oo):
            check(poly.eval(endpoint) != 0, "Sturm interval endpoint is a root")
    return sturm_variations(poly, lo) - sturm_variations(poly, hi)


def main() -> None:
    basis = [1, x, x**2, y, x*y, x**2*y]
    matrix = sp.zeros(6)
    for i, m in enumerate(basis):
        remainder, p, qq = normal_form(q*m)
        check(sp.expand(q*m-remainder-lx(p)-ly(qq)) == 0,
              f"Stokes certificate failed for amplitude {m}")
        rpoly = sp.Poly(remainder, x, y)
        check(all(i <= 2 and j <= 1 for i, j in rpoly.monoms()),
              "Remainder outside the claimed basis")
        for j, amplitude in enumerate(basis):
            matrix[i, j] = rpoly.coeff_monomial(amplitude)
    a0 = matrix.applyfunc(lambda e: sp.limit(e, z, sp.oo))
    a1 = (matrix-a0).applyfunc(lambda e: sp.limit(z*e, z, sp.oo))
    check((matrix-a0-a1/z).applyfunc(sp.simplify) == sp.zeros(6),
          "Connection is not A0+A1/z")
    print("PASS: all six Stokes certificates; connection A=A0+A1/z")

    chi = sp.Poly(1289945088*t**6 - 573308928*t**4 + 83980800*t**3
                  + 83854656*t**2 + 5477429*t - 4197429, t, domain=sp.QQ)
    check(sp.expand(a0.charpoly(t).as_expr()*chi.LC()-chi.as_expr()) == 0,
          "Characteristic polynomial mismatch")
    f = sp.Poly(sp.expand(qx.subs(x, 1-3*y**2)), y, domain=sp.QQ)
    critical_phase = sp.expand(q.subs(x, 1-3*y**2))
    resultant = sp.resultant(f.as_expr(), t-critical_phase, y)
    ratio = sp.cancel(resultant/chi.as_expr())
    check(ratio.is_Rational and ratio != 0, "Resultant mismatch")
    check(sp.gcd(f, f.diff()).degree() == 0, "Repeated critical point")
    hessian = sp.Poly(72*(1-3*y**2)**2*y-1, y, domain=sp.QQ)
    check(hessian == -f.diff(), "Hessian identity H=-f' failed")
    print(f"PASS: characteristic polynomial and critical-value resultant (ratio {ratio})")
    print("PASS: six distinct critical points; H=-f' and gcd(f,f')=1")

    # Rabin's irreducibility criterion for degree 6 over F_5.
    # The prime divisors of 6 are 2 and 3, so the proper-divisor tests
    # required are gcd(t^(5^3)-t, chi)=gcd(t^(5^2)-t, chi)=1.
    bar = sp.Poly(chi.as_expr(), t, modulus=5).monic()
    check(bar.degree() == 6, "Degree dropped modulo 5")
    variable = sp.Poly(t, t, modulus=5)
    power = variable
    for degree in range(1, 7):
        power = (power**5).rem(bar)
        if degree in (2, 3):
            check(sp.gcd(bar, power-variable).degree() == 0,
                  f"Rabin gcd test failed at degree {degree}")
    check((power-variable).rem(bar).is_zero, "Rabin final congruence failed")
    print(f"PASS: irreducible modulo 5 by Rabin's criterion: {bar.as_expr()}")
    print("      Hence chi is irreducible over Q and all six critical values are distinct.")

    for prime, required in [(7, (1, 5)), (31, (1, 2, 3))]:
        reduced = sp.Poly(chi.as_expr(), t, modulus=prime)
        check(reduced.degree() == 6, f"Degree dropped modulo {prime}")
        check(sp.gcd(reduced, reduced.diff()).degree() == 0,
              f"Repeated factor modulo {prime}")
        scalar, factors = reduced.factor_list()
        reconstructed = sp.Poly(scalar, t, modulus=prime)
        for factor, exponent in factors:
            reconstructed *= factor**exponent
            check(factor.is_irreducible, "Finite-field factor is not irreducible")
        check(reconstructed == reduced, "Finite-field factors do not multiply back")
        actual = tuple(sorted(factor.degree() for factor, _ in factors))
        check(actual == required and all(e == 1 for _, e in factors),
              f"Unexpected Frobenius type modulo {prime}")
        print(f"PASS: squarefree Frobenius type modulo {prime}: {actual}")
    print("      These types and irreducibility imply S6; the transposition argument")
    print("      then implies Q-linear independence of the five critical-value differences.")

    intervals = [Interval(sp.Rational(-420, 1000), sp.Rational(-419, 1000)),
                 Interval(sp.Rational(722, 1000), sp.Rational(723, 1000))]
    check(sturm_count(f, -sp.oo, sp.oo) == 2, "Not exactly two real critical points")
    for domain in intervals:
        check(sturm_count(f, domain.lo, domain.hi) == 1,
              "Critical-point interval does not contain exactly one root")
    negative_hessian = interval_evaluate(hessian, intervals[0])
    positive_hessian = interval_evaluate(hessian, intervals[1])
    check(negative_hessian.hi < 0, "Negative root not certified a saddle")
    check(positive_hessian.lo > 0, "Positive root not certified non-saddle")
    print("PASS: exactly two real critical points (Sturm); exactly one saddle")
    print(f"      Saddle y in [{intervals[0].lo}, {intervals[0].hi}]")
    print(f"      Hessian determinant throughout saddle interval: {negative_hessian}")
    print(f"      Hessian determinant throughout other interval: {positive_hessian}")

    # Strict triangle inequalities: y+1>0, -y>0,
    # x-(y+1)/2>0, and (1-y)/2-x>0.
    xv = 1-3*y**2
    inequalities = {"above base": y+1, "below vertex level": -y,
                    "right of left side": xv-(y+1)/2,
                    "left of right side": (1-y)/2-xv}
    for label, expression in inequalities.items():
        bound = interval_evaluate(sp.Poly(expression, y, domain=sp.QQ), intervals[0])
        check(bound.lo > 0, f"Triangle inequality not certified: {label}")
        print(f"PASS: {label}, lower bound {bound.lo}")

    vertices = [(0, -1), (1, -1), (sp.Rational(1, 2), 0)]
    u = sp.symbols("u")
    face_degrees = []
    for start, end in zip(vertices, vertices[1:]+vertices[:1]):
        face = sp.Poly(q.subs({x: start[0]+u*(end[0]-start[0]),
                              y: start[1]+u*(end[1]-start[1])}), u, domain=sp.QQ)
        face_degrees.append(face.degree())
    check(all(d <= 4 for d in face_degrees), "Unexpected face degree")
    print(f"PASS: face degrees {face_degrees}; critical face values have degree <=3")
    print("      Interior critical values have degree 6, so no boundary-level collision.")
    print("ALL EXACT ALGEBRAIC AND GEOMETRIC CERTIFICATES PASSED.")


if __name__ == "__main__":
    main()
