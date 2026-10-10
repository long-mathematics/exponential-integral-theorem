#!/usr/bin/env python3
"""Exact checks for EIT V, VI, and the candidate simplex note.

No numerical quadrature or probabilistic polynomial tests are used.

Dependencies: Python 3.10+ and SymPy.
These tests check finite algebraic identities, not the analytic,
monodromy, differential-Galois, or specialization proofs.
"""
from __future__ import annotations
import argparse
import json
import math
import platform
from functools import lru_cache
from pathlib import Path
import sympy as sp

x, y, h, t, z, c = sp.symbols('x y h t z c')
R = sp.Rational

def mod5(expr: sp.Expr) -> sp.Poly:
    """Reduce a rational-coefficient polynomial in h modulo five."""
    p = sp.Poly(sp.expand(expr), h, domain=sp.QQ)
    terms = {}
    for monom, value in p.terms():
        denominator = int(sp.denom(value))
        if denominator % 5 == 0:
            raise ValueError('Denominator divisible by five')
        terms[monom] = (int(sp.numer(value)) * pow(denominator, -1, 5)) % 5
    return sp.Poly.from_dict(terms, (h,), modulus=5)

@lru_cache(None)
def x_remainder(a: int) -> tuple[sp.Expr, sp.Expr]:
    if a == 0:
        return (sp.Integer(1), sp.Integer(0))
    if a == 1:
        return (sp.Integer(0), sp.Integer(1))
    u = x_remainder(a-2)
    if a == 2:
        return u
    v = x_remainder(a-3)
    return tuple(sp.expand(u[j] + h*R(a-2,3)*v[j]) for j in range(2))

@lru_cache(None)
def y_remainder(b: int) -> sp.Expr:
    if b == 0:
        return sp.Integer(1)
    if b % 2:
        return sp.Integer(0)
    return sp.expand(-h*R(b-1,2)*y_remainder(b-2))

def remainder(expr: sp.Expr) -> tuple[sp.Expr,sp.Expr]:
    out = [sp.Integer(0), sp.Integer(0)]
    for (a,b), coefficient in sp.Poly(sp.expand(expr),x,y).terms():
        u = x_remainder(a)
        v = y_remainder(b)
        for j in range(2):
            out[j] += coefficient*u[j]*v
    return tuple(sp.expand(s) for s in out)

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--max-k', type=int, default=100)
    parser.add_argument('--output', type=Path, default=Path('.build/comparison-factorial-exact.json'))
    args = parser.parse_args()
    if not 1 <= args.max_k <= 1000:
        parser.error('--max-k must lie between 1 and 1000')
    if not __debug__:
        raise RuntimeError('Do not run the exact checker with Python optimization enabled')
    results: dict[str,object] = {
        'python':platform.python_version(), 'sympy':sp.__version__,
        'scope':'Finite exact algebra only; not a proof certificate for analytic claims.'
    }
    # A real (W) phase satisfying separated ordered differences but not (Q).
    p = sp.integrate(5*(x+2)*(x+1)*(x-1)*(x-3),x)
    critical_x = [-2,-1,1,3]
    values = [p.subs(x,a) for a in critical_x]
    differences = [values[i]-values[j] for i in range(4) for j in range(4) if i!=j]
    assert len(set(differences)) == 12
    assert all(sp.diff(p,x,2).subs(x,a) != 0 for a in critical_x)
    results['weaker_root_separation_example'] = {
        'p':str(sp.expand(p)), 'critical_values':[str(v) for v in values],
        'distinct_ordered_differences':len(set(differences)),
        'Q_fails':'Four rational critical values have three rationally dependent differences.'
    }
    # The noncoprime rank-three phase and literal polynomial certificates.
    q = x**4 + y**2 + x
    A0 = sp.Matrix([[0,R(3,4),0],[0,0,R(3,4)],[-R(3,16),0,0]])
    A1 = sp.diag(-R(3,4),-1,-R(5,4))
    A = A0 + A1/z
    basis = sp.Matrix([1,x,x**2])
    certificates = []
    for j in range(3):
        P = x**(j+1)/(4*z) + (R(3,16)/z if j == 2 else 0)
        Q = y*x**j/(2*z)
        LxP = sp.diff(P,x) + z*sp.diff(q,x)*P
        LyQ = sp.diff(Q,y) + z*sp.diff(q,y)*Q
        assert sp.expand(q*basis[j] - (A*basis)[j] - LxP - LyQ) == 0
        certificates.append({'amplitude':str(basis[j]),'P':str(P),'Q':str(Q)})
    assert sp.expand(A0.charpoly(c).as_expr()) == c**3 + R(27,256)
    assert sp.trace(A0*A1) == 0 and sp.trace(A0**2*A1) == 0
    assert sp.trace(A1)/3 == -1
    middle = sp.Matrix([0,1,0])
    assert A0*middle != sp.zeros(3,1)
    assert (A0*middle)[0] != 0 and (A0.T*middle)[2] != 0
    results['noncoprime_rank_three'] = {
        'phase':str(q), 'A0':str(A0), 'residue':str(A1),
        'critical_polynomial':str(A0.charpoly(c).as_expr()),
        'formal_residue_each_eigenline':'-1',
        'literal_stokes_certificates':certificates
    }
    # A noncoprime triangle with boundary adjoint spectra separated exactly.
    aa,bb,cc = sp.symbols('aa bb cc')
    quartic = x**4+aa*x**2+bb*x+cc
    multiplication=sp.zeros(3)
    for j in range(3):
        reduced=sp.rem(quartic*x**j,sp.diff(quartic,x),x)
        for i in range(3):
            multiplication[i,j]=sp.expand(reduced).coeff(x,i)
    difference_square_sum=sp.factor(6*sp.trace(multiplication**2)-2*sp.trace(multiplication)**2)
    assert difference_square_sum == aa*(aa**3-27*bb**2)/4
    vertices=[(-sp.Integer(1),-sp.Integer(1)),(sp.Integer(0),-R(1,2)),(-R(1,2),sp.Integer(1))]
    edge_checks=[]
    for j in range(3):
        P,Q=vertices[j],vertices[(j+1)%3]
        slope=(Q[1]-P[1])/(Q[0]-P[0])
        intercept=P[1]-slope*P[0]
        value=sp.factor(difference_square_sum.subs({aa:slope**2,bb:1+2*slope*intercept,cc:intercept**2}))
        assert value != 0
        edge_checks.append({'slope':str(slope),'intercept':str(intercept),'sum_squared_ordered_differences':str(value)})
    assert 6*sp.trace(A0**2)-2*sp.trace(A0)**2 == 0
    results['noncoprime_boundary_separation']={
        'triangle':[list(map(str,P)) for P in vertices],
        'interior_difference_square_sum':0,
        'quartic_difference_square_sum':str(difference_square_sum),
        'edges':edge_checks,
        'interpretation':'Each edge has at most six ordered critical differences; containing all six distinct interior differences would force equality and the same square sum, impossible.'}
    # Independent normal-form calculation of the characteristic-five certificate.
    ell = (1-2*x-2*y)/4
    matrix = sp.Matrix.hstack(sp.Matrix(remainder(ell**5)),sp.Matrix(remainder(x*ell**5)))
    expected = sp.Matrix([[h-1,2*h**2+2],[2,-h-1]])
    assert all(mod5(matrix[i,j]-expected[i,j]).is_zero for i in range(2) for j in range(2))
    assert mod5(expected.det()-2).is_zero
    initials = [[1,0],[-1,2],[-2*h,1],[2*h+2,-2*h-1],[2*h**2+h+1,2*h]]
    for k in range(5):
        v = remainder(ell**k)
        assert all(mod5(v[j]-initials[k][j]).is_zero for j in range(2))
    assert mod5(initials[3][0]+initials[3][1]-1).is_zero
    assert mod5(initials[4][0]+(2-h)*initials[4][1]-1).is_zero
    results['elliptic_mod5'] = {'matrix':str(expected),'determinant_mod5':2,
        'initial_vectors_checked':5,'direct_reduction_used':True}
    # Integer recurrence and its finite coprimality range.
    W = [(sp.Poly(1,t,domain=sp.ZZ),sp.Poly(0,t,domain=sp.ZZ)),
         (sp.Poly(1,t,domain=sp.ZZ),sp.Poly(-2,t,domain=sp.ZZ))]
    for k in range(args.max_k-1):
        coords=[]
        for j in range(2):
            value=2*W[k+1][j] + sp.Poly(3-6*(2*k+1)*t,t)*W[k][j]
            if k>=1:
                value += sp.Poly(4*k*t,t)*W[k-1][j]
            if k>=2:
                value -= sp.Poly(36*k*(k-1)*t**2,t)*W[k-2][j]
            coords.append(value)
        W.append(tuple(coords))
    gcd_degrees=[]
    for k, coords in enumerate(W):
        degree=int(sp.gcd(coords[0],coords[1]).degree())
        assert degree == 0, f'Common factor at k={k}'
        gcd_degrees.append(degree)
        if k <= min(12,args.max_k):
            v = remainder(ell**k)
            for j in range(2):
                assert sp.Poly(4**k*v[j].subs(h,3*t),t,domain=sp.ZZ) == coords[j]
    results['elliptic_finite_coprimality'] = {
        'range':[0,args.max_k], 'number_of_gcds':len(gcd_degrees),
        'all_gcd_degrees_zero':True,'direct_reduction_comparison_range':[0,min(12,args.max_k)],
        'maximum_polynomial_degree':max(int(p.degree()) for pair in W for p in pair if not p.is_zero)
    }
    # Positive polynomial amplitude does not imply nonzero oscillatory period.
    g = t**2*(1-t)**2
    amp = sp.expand(sp.diff(g,t,2)+25*g)
    positive_form=25*((t-R(1,2))**2-R(1,100))**2+R(14,25)
    assert sp.expand(amp-positive_form)==0
    for endpoint in [0,1]:
        assert g.subs(t,endpoint)==0 and sp.diff(g,t).subs(t,endpoint)==0
    primitive=(sp.diff(g,t)-5*sp.I*g)*sp.exp(5*sp.I*t)
    assert sp.simplify(sp.diff(primitive,t)-amp*sp.exp(5*sp.I*t))==0
    results['positive_amplitude_counterexample']={
        'amplitude':str(amp),'positive_form':str(positive_form),
        'integral_against_exp_5it':'0 (checked exact primitive with zero endpoints)'}
    # Two affine changes used in the simplex constructions.
    u,v=sp.symbols('u v')
    assert sp.Matrix([u-R(1,2),u+2*v-1]).jacobian([u,v]).det()==2
    assert sp.Matrix([2*(1-u-v),v-u]).jacobian([u,v]).det()==-4
    results['simplex_affine_jacobians']={'elliptic':2,'odd_a_absolute':4}

    # Simplex monomial moments validate both Jacobians and slicing factors.
    def triangle_moment(expr: sp.Expr) -> sp.Expr:
        total = sp.Integer(0)
        for (i,j), coefficient in sp.Poly(sp.expand(expr),u,v).terms():
            total += coefficient*R(math.factorial(i)*math.factorial(j),
                                   math.factorial(i+j+2))
        return total

    moment_count=0
    for n in range(3,10):
        kk=n-3
        for i in range(4):
            for j in range(4-i):
                expected_moment=R(math.factorial(i)*math.factorial(j),
                                  math.factorial(n-1+i+j))
                sliced=triangle_moment(u**i*v**j*(1-u-v)**kk)/math.factorial(kk)
                assert sliced == expected_moment
                # Pull the triangular weighted moments back to the standard triangle.
                elliptic=2*triangle_moment(u**i*v**j*(1-u-v)**kk)
                assert elliptic/(2*math.factorial(kk)) == expected_moment
                odd=4*triangle_moment(u**i*v**j*(2*(1-u-v))**kk)
                assert odd/(2**(n-1)*math.factorial(kk)) == expected_moment
                moment_count += 1
    results['simplex_monomial_normalizations'] = {
        'dimensions':[3,9], 'number_checked':moment_count,
        'amplitude_total_degree_at_most':3,
        'comparison':'Exact monomial factorial moments, both affine pullbacks and slicing constants.'}

    # Check the exact radial coefficient bound, including D=1 and small m.
    from itertools import product
    radial_count=0
    for dimension in range(1,5):
        for degree in range(1,5):
            for m in range(1,6):
                for ks in product(range(m+1),repeat=degree):
                    K=sum(ks)
                    if K>m:
                        continue
                    J=sum((index+1)*value for index,value in enumerate(ks))
                    coeff=R(math.factorial(m),math.factorial(m-K))*R(
                        math.factorial(degree*m-J+dimension-1),
                        math.factorial(degree*m+dimension-1))
                    assert 0 <= coeff <= 1
                    radial_count += 1
    results['radial_coefficient_bounds'] = {
        'cases':radial_count, 'dimension_range':[1,4],
        'degree_range':[1,4], 'moment_range':[1,5],
        'scope':'Finite exact regression for the bound proved uniformly in Paper VI.'}

    # The edge geometry used by the rank-three example has the correct orientation.
    edges=[]
    for j in range(3):
        P,Q=vertices[j],vertices[(j+1)%3]
        # At x=-r,y=0, verify positivity for all r in [1/2,3/4].
        rr=sp.symbols('rr')
        signed=(Q[0]-P[0])*(-P[1])-(Q[1]-P[1])*(-rr-P[0])
        assert signed.subs(rr,R(1,2)) >= 0 and signed.subs(rr,R(3,4)) >= 0
        assert signed.subs(rr,R(5,8)) > 0
        edges.append(str(sp.expand(signed)))
    assert R(1,2)**3 < R(1,4) < R(3,4)**3
    results['rank_three_interior_minimum']={
        'signed_edge_tests':edges,'interval_for_4_to_minus_one_third':["1/2","3/4"],
        'interpretation':'r=4^(-1/3) is strictly inside the interval; all three edge tests are positive there.'}

    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(results,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(results,indent=2))

if __name__=='__main__':
    main()
