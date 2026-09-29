"""Exact, dependency-free regression tests for Paper V's polynomial identities."""
import sys
from pathlib import Path
import unittest
from fractions import Fraction as F
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from paper_v_certificate import Polynomial as P, ZERO,ONE,X,Y,Z,lx,ly,reduce_amplitude,parse_amplitude

class PaperVCertificates(unittest.TestCase):
    def test_monomial_certificates(self):
        for i in range(11):
            for j in range(11):
                with self.subTest(i=i,j=j):
                    r=P.monomial((i,j,0))
                    a,b,p,q=reduce_amplitude(r)
                    self.assertEqual(r,a+b*X+lx(p)+ly(q))
                    self.assertTrue(all(e[:2]==(0,0) for c in (a,b) for e in c.terms))

    def test_displayed_connection_certificates(self):
        zinv=P.monomial((0,0,-1))
        phase=Y*Y-X.power(3)+P.monomial((1,0,0),3)
        p0=P.monomial((1,0,-1),F(1,3)); q0=P.monomial((0,1,-1),F(1,2))
        p1=P.monomial((2,0,-1),F(1,3))-P.monomial((0,0,-1),F(2,3))
        q1=P.monomial((1,1,-1),F(1,2))
        self.assertEqual(phase,P.monomial((0,0,-1),-F(5,6))+P.monomial((1,0,0),2)+lx(p0)+ly(q0))
        self.assertEqual(phase*X,P.monomial((0,0,0),2)-P.monomial((1,0,-1),F(7,6))+lx(p1)+ly(q1))

    def test_linearity_and_primitives(self):
        r=parse_amplitude('x**4 + 2*x*y**2 + 1/3')
        a,b,p,q=reduce_amplitude(r)
        self.assertEqual(a,ONE+P.monomial((0,0,0),F(1,3)))
        self.assertEqual(b,P.monomial((0,0,-1),-F(1,3)))
        for primitive in (ONE,X,Y,X*Y,X.power(3)+Y.power(4)):
            for differential in (lx,ly):
                a,b,_,_=reduce_amplitude(differential(primitive))
                self.assertEqual((a,b),(ZERO,ZERO))

    def test_safe_input(self):
        for text in ['1/x','1/0','x**(-2)','sin(x)',"__import__('os')",'0.5*x','z']:
            with self.subTest(text=text),self.assertRaises(ValueError):
                parse_amplitude(text)

    def test_boundary_geometry_inequalities(self):
        p=lambda x:-x**3+x*x+2*x+F(1,4)
        self.assertLess(p(-F(1,5)),0)
        self.assertGreater(p(0),0)
        self.assertLess(p(F(4,5)),2)
        self.assertGreater(p(1),2)
        self.assertEqual(p(F(1,2)),F(11,8))
        self.assertEqual(p(-F(1,2)),-F(3,8))
        # p' is concave and positive at both endpoints of [-1/5,1].
        dp=lambda x:-3*x*x+2*x+2
        self.assertGreater(min(dp(-F(1,5)),dp(1)),0)

if __name__=='__main__': unittest.main()
