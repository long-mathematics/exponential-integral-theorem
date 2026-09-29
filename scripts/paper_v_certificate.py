#!/usr/bin/env python3
"""Exact elliptic Stokes certificates over Q[z,z^-1,x,y], standard library only.

Usage: python3 scripts/paper_v_certificate.py 'x**4 + 2*x*y**2 + 1/3'
The input is a polynomial in x,y with rational coefficients. Output gives
r=a(z)+b(z)*x+L_x(P)+L_y(Q), with beta=P*dy-Q*dx. A separate exact
substitution verifies the certificate before anything is returned.
"""
from __future__ import annotations
import argparse
import ast
from dataclasses import dataclass
from fractions import Fraction
import json
from typing import Mapping

Exponent = tuple[int, int, int]  # x, y, z; only z may have negative powers

@dataclass(frozen=True)
class Polynomial:
    terms: Mapping[Exponent, Fraction]

    def __post_init__(self) -> None:
        clean = {e: Fraction(c) for e, c in self.terms.items() if c}
        if any(len(e) != 3 or not all(isinstance(n, int) for n in e)
               or e[0] < 0 or e[1] < 0 for e in clean):
            raise ValueError('Invalid Laurent-polynomial exponent.')
        object.__setattr__(self, 'terms', clean)

    @staticmethod
    def monomial(e: Exponent, c: Fraction | int = 1) -> Polynomial:
        return Polynomial({e: Fraction(c)})

    def __add__(self, other: Polynomial) -> Polynomial:
        d = dict(self.terms)
        for e, c in other.terms.items():
            d[e] = d.get(e, Fraction(0)) + c
        return Polynomial(d)

    def __neg__(self) -> Polynomial:
        return Polynomial({e: -c for e, c in self.terms.items()})

    def __sub__(self, other: Polynomial) -> Polynomial:
        return self + (-other)

    def __mul__(self, other: Polynomial) -> Polynomial:
        d: dict[Exponent, Fraction] = {}
        for e, c in self.terms.items():
            for f, v in other.terms.items():
                g = tuple(e[i] + f[i] for i in range(3))
                d[g] = d.get(g, Fraction(0)) + c*v
        return Polynomial(d)

    def power(self, n: int) -> Polynomial:
        if n < 0:
            raise ValueError('Input amplitudes must be polynomial.')
        a, b = ONE, self
        while n:
            if n & 1:
                a = a*b
            b = b*b
            n //= 2
        return a

    def derivative(self, axis: int) -> Polynomial:
        d = {}
        for e, c in self.terms.items():
            if e[axis]:
                f = list(e)
                f[axis] -= 1
                d[tuple(f)] = c*e[axis]
        return Polynomial(d)

    def to_json(self) -> list[dict]:
        return [{'powers': list(e), 'coefficient': str(c)}
                for e, c in sorted(self.terms.items())]

ZERO = Polynomial({})
ONE = Polynomial.monomial((0,0,0))
X = Polynomial.monomial((1,0,0))
Y = Polynomial.monomial((0,1,0))
Z = Polynomial.monomial((0,0,1))
THREE = Polynomial.monomial((0,0,0),3)
TWO = Polynomial.monomial((0,0,0),2)

def lx(p: Polynomial) -> Polynomial:
    return p.derivative(0) + THREE*Z*(ONE-X*X)*p

def ly(p: Polynomial) -> Polynomial:
    return p.derivative(1) + TWO*Z*Y*p

def reduce_amplitude(r: Polynomial) -> tuple[Polynomial,Polynomial,Polynomial,Polynomial]:
    """Return a,b,P,Q and verify r=a+b*x+L_x P+L_y Q exactly."""
    rem, p, q = r, ZERO, ZERO
    while any(e[1] for e in rem.terms):
        degree = max(e[1] for e in rem.terms)
        v = Polynomial({(i, j-1, k-1): c/2
                        for (i,j,k),c in rem.terms.items() if j == degree})
        q = q+v
        rem = rem-ly(v)
    while any(e[0] >= 2 for e in rem.terms):
        degree = max(e[0] for e in rem.terms)
        v = Polynomial({(i-2, j, k-1): -c/3
                        for (i,j,k),c in rem.terms.items() if i == degree})
        p = p+v
        rem = rem-lx(v)
    a = Polynomial({e:c for e,c in rem.terms.items() if e[0] == 0})
    b = Polynomial({(0,j,k):c for (i,j,k),c in rem.terms.items() if i == 1})
    if r != a+b*X+lx(p)+ly(q):
        raise ArithmeticError('Certificate verification failed.')
    return a,b,p,q

def parse_amplitude(text: str) -> Polynomial:
    """Parse only integer/rational polynomial arithmetic; never evaluate Python."""
    def walk(n: ast.AST) -> Polynomial:
        if isinstance(n,ast.Constant) and type(n.value) is int:
            return Polynomial.monomial((0,0,0),n.value)
        if isinstance(n,ast.Name) and n.id in ('x','y'):
            return X if n.id == 'x' else Y
        if isinstance(n,ast.UnaryOp) and isinstance(n.op,(ast.UAdd,ast.USub)):
            v = walk(n.operand)
            return -v if isinstance(n.op,ast.USub) else v
        if isinstance(n,ast.BinOp):
            if isinstance(n.op,ast.Pow):
                if not isinstance(n.right,ast.Constant) or type(n.right.value) is not int:
                    raise ValueError('Powers must be nonnegative integers.')
                if not 0 <= n.right.value <= 200:
                    raise ValueError('Powers must lie between 0 and 200.')
                return walk(n.left).power(n.right.value)
            a,b = walk(n.left),walk(n.right)
            if isinstance(n.op,ast.Add): return a+b
            if isinstance(n.op,ast.Sub): return a-b
            if isinstance(n.op,ast.Mult): return a*b
            if isinstance(n.op,ast.Div):
                if set(b.terms) != {(0,0,0)}:
                    raise ValueError('Divide only by a nonzero rational constant.')
                return a*Polynomial.monomial((0,0,0),1/b.terms[(0,0,0)])
        raise ValueError('Use x, y, integer constants, +, -, *, /, and ** only.')
    try:
        return walk(ast.parse(text,mode='eval').body)
    except (SyntaxError,ZeroDivisionError) as exc:
        raise ValueError(str(exc)) from exc

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('amplitude')
    args = parser.parse_args()
    try:
        r = parse_amplitude(args.amplitude)
        a,b,p,q = reduce_amplitude(r)
    except (ValueError,ArithmeticError) as exc:
        parser.error(str(exc))
    print(json.dumps({'ring':'Q[z,z^-1,x,y]',
        'identity':'r = a + b*x + L_x(P) + L_y(Q)',
        'one_form':'P dy - Q dx', 'verified':True,
        **{k:v.to_json() for k,v in [('r',r),('a',a),('b',b),('P',p),('Q',q)]}},indent=2))

if __name__ == '__main__':
    main()
