#!/usr/bin/env python3
"""Exact regression checks for the polynomial boundary-system proof.

The proof is in papers/05-polynomial-flags/polynomial-flag-exponential-periods.tex. These checks test displayed
identities and finitely many Taylor coefficients, not the Galois arguments.
Requires Python 3 and SymPy.
"""
from functools import lru_cache
from pathlib import Path
import argparse
import json
import sympy as s

x,y,z,t=s.symbols('x y z t')
q=y*y-x**3+3*x
p=-x**3+x*x+2*x+s.Rational(1,4)
Lx=lambda P:s.diff(P,x)+z*(3-3*x*x)*P
Ly=lambda Q:s.diff(Q,y)+2*z*y*Q
A=s.Matrix([[-s.Rational(5,6)/z,2],[2,-s.Rational(7,6)/z]])


def normal_form(r):
    rem=s.expand(r); P=s.Integer(0); Q=s.Integer(0)
    while s.degree(rem,y)>0:
        py=s.Poly(rem,y); m=py.degree(); c=py.LC()
        v=c*y**(m-1)/(2*z)
        Q+=v; rem=s.expand(rem-Ly(v))
    while s.degree(rem,x)>=2:
        px=s.Poly(rem,x); m=px.degree(); c=px.LC()
        v=-c*x**(m-2)/(3*z)
        P+=v; rem=s.expand(rem-Lx(v))
    return s.expand(rem),s.expand(P),s.expand(Q)

count=0
for i in range(9):
    for j in range(9):
        r=x**i*y**j
        rem,P,Q=normal_form(r)
        assert s.expand(r-rem-Lx(P)-Ly(Q))==0
        assert s.degree(rem,x)<=1 and s.degree(rem,y)<=0
        count+=1

beta=[(x/(3*z),y/(2*z)),((x*x-2)/(3*z),x*y/(2*z))]
for j,(P,Q) in enumerate(beta):
    assert s.expand(q*x**j-sum(A[j,k]*x**k for k in range(2))-Lx(P)-Ly(Q))==0

G=s.Matrix([[-t,2],[-2,t]])/(6*(t*t-4))
R=[(4-t*x-2*x*x)/(6*(t*t-4)),(2*t-2*x-t*x*x)/(6*(t*t-4))]
f=x**3-3*x+t
for j in range(2):
    identity=-x**j-2*f*sum(G[j,k]*x**k for k in range(2))-4*s.diff(R[j],x)*f+2*R[j]*s.diff(f,x)
    assert s.cancel(identity)==0
C=s.Matrix([[0,2],[2,0]])
D=s.diag(-s.Rational(5,6),-s.Rational(7,6))
assert ((t*s.eye(2)-C)*G+D+s.eye(2)).applyfunc(s.cancel)==s.zeros(2)

# Homogeneous scalar equation, directly eliminating the second coordinate.
w=s.Function('w')(z)
y0=w/z
y1=(s.diff(y0,z)+s.Rational(5,6)*y0/z)/2
scalar=s.simplify(s.diff(y1,z)-2*y0+s.Rational(7,6)*y1/z)
assert s.simplify(2*z*scalar-(s.diff(w,z,2)-(4-s.Rational(5,36)/z**2)*w))==0

# Boundary moment connection obtained by Euclidean division.
Cb=s.Matrix([[s.Rational(17,36),s.Rational(14,9)],[s.Rational(28,27),s.Rational(163,108)]])
Db=s.Matrix([[-s.Rational(1,3),0],[s.Rational(1,9),-s.Rational(2,3)]])
H=[x/3-s.Rational(1,9),x*x/3-x/9-s.Rational(14,27)]
for j in range(2):
    assert s.expand(x**j*p-H[j]*s.diff(p,x)-sum(Cb[j,k]*x**k for k in range(2)))==0
    assert s.expand(-s.diff(H[j],x)-sum(Db[j,k]*x**k for k in range(2)))==0
beta_scale=7*s.sqrt(7)/27
center=s.Rational(107,108)
assert s.expand(p.subs(x,s.sqrt(7)*t/3+s.Rational(1,3))-(center+beta_scale*(-t**3+3*t)))==0
roots=s.solve(s.diff(p,x),x)
values=[s.simplify(p.subs(x,r)) for r in roots]
assert s.simplify((values[1]-values[0])**2-(4*beta_scale)**2)==0
assert s.simplify(beta_scale**2-1)!=0

@lru_cache(None)
def area_monomial(i,j):
    if j%2: return s.Integer(0)
    # y integral first, then x=u-1/2: exact beta integrals on the triangle.
    return s.Rational(2,j+1)*sum(s.binomial(i,h)*(-s.Rational(1,2))**(i-h)*s.factorial(h)*s.factorial(j+1)/s.factorial(h+j+2) for h in range(i+1))

def area(poly):
    return sum(c*area_monomial(i,j) for (i,j),c in s.Poly(poly,x,y).terms())

def x_interval(poly):
    return sum(c*(s.Rational(1,2)**(i+1)-(-s.Rational(1,2))**(i+1))/(i+1) for (i,),c in s.Poly(poly,x).terms())

def y_interval(poly):
    return sum(c*s.Rational(1-(-1)**(i+1),i+1) for (i,),c in s.Poly(poly,y).terms())

boundary_checks=0
prevP=s.zeros(2,1); prevQ=s.Integer(0)
N=20
qpower=s.Integer(1); ppower=s.Integer(1); vpower=s.Integer(1)
prev=s.zeros(2,1)
taylor_checks=0
first=[]
for n in range(N+1):
    moment=s.Matrix([area(qpower),area(x*qpower)])
    P=[x_interval(x**j*ppower) for j in range(4)]
    Q=y_interval(vpower)
    Bx=[2*P[j]-(-s.Rational(1,2))**j*Q for j in range(3)]
    By=[P[j]-2*P[j+1] for j in range(2)]
    b=s.Matrix([By[0]/2+Bx[1]/3,By[1]/2+Bx[2]/3-2*Bx[0]/3])
    assert ((n*s.eye(2)-D)*moment-n*C*prev-b)==s.zeros(2,1)
    # Independently integrated coefficients of all three nonexponential face rows.
    currentP=s.Matrix(P[:2])
    ea=(-s.Rational(3,8))**n; eb=s.Rational(11,8)**n
    forcingP=s.Matrix([(eb+5*ea)/18,(-53*eb+41*ea)/108])
    assert (n*s.eye(2)-Db)*currentP-n*Cb*prevP-forcingP==s.zeros(2,1)
    assert (n+s.Rational(1,2))*Q+n*s.Rational(11,8)*prevQ-ea==0
    boundary_checks+=3
    prevP=currentP; prevQ=Q
    if n<5: first.append([str(v) for v in moment])
    taylor_checks+=2
    prev=moment
    qpower=s.expand(qpower*q); ppower=s.expand(ppower*p)
    vpower=s.expand(vpower*(y*y-s.Rational(11,8)))
assert first[0]==['1','-1/6']

# Exact branch and local-neck checks (not numerical continuation).
f0=-x**3+3*x
assert p.subs(x,-s.Rational(1,5))==-s.Rational(51,500)
assert p.subs(x,0)==s.Rational(1,4)
assert p.subs(x,s.Rational(4,5))==s.Rational(989,500)
assert p.subs(x,1)==s.Rational(9,4)
assert p.subs(x,s.Rational(1,2))==s.Rational(11,8)
# p' is concave, so its minimum on [-1/5,1] is at an endpoint.
assert s.diff(p,x).subs(x,-s.Rational(1,5))>0
assert s.diff(p,x).subs(x,1)>0
assert s.diff(p,x,3)==-6
v=s.symbols('v', positive=True)
assert s.expand(f0.subs(x,1-v)-(2-3*v*v+v**3))==0
assert s.limit(s.sqrt(3*v*v-v**3)/(3*(1-(1-v)**2)),v,0,dir='+')==s.sqrt(3)/6
# A single supported fiber cannot be numerically injected before specialization.
pi,delta=s.symbols('pi delta')
gb=s.groebner([pi*(delta-1)],pi,delta)
assert gb.reduce(delta-1)[1]==delta-1
assert gb.reduce(pi*(delta-1))[1]==0
assert (pi*(delta-1)).subs(pi,0)==0
# Stokes multiplier support is not logarithm support.
Nmat=s.zeros(3); Nmat[0,1]=1; Nmat[1,2]=1
Emat=s.eye(3)+Nmat+Nmat**2/2
assert Emat[0,2]==s.Rational(1,2)
assert ((Emat-s.eye(3))-(Emat-s.eye(3))**2/2)[0,2]==0
# The determinant relation is monic in an admissible leading matrix monomial.
aa,bb,cc,dd=s.symbols('aa bb cc dd')
det=aa*dd-bb*cc
gdet=s.groebner([det-delta],aa,bb,cc,dd,domain=s.QQ.poly_ring(delta))
assert gdet.reduce(det-delta)[1]==0

report={
    'normal_form_monomial_certificates':count,
    'top_form_connection_certificates':2,
    'gelfand_leray_certificates':2,
    'fourier_matrix_identity':True,
    'scalar_bessel_identity':True,
    'boundary_euclidean_division_certificates':2,
    'boundary_critical_values':[str(v) for v in values],
    'boundary_scale':str(beta_scale),
    'adjoint_scales_differ':True,
    'independent_triangle_and_face_taylor_identities':taylor_checks,
    'independently_integrated_boundary_system_taylor_identities':boundary_checks,
    'branch_and_neck_exact_checks':10,
    'local_torsion_countermodel_checks':3,
    'stokes_logarithm_countermodel_checks':2,
    'determinant_monic_division_check':True,
    'first_five_moment_derivative_vectors_at_zero':first,
    'status':'All exact checks passed. Finite regression tests do not certify the analytic or Galois proofs.'
}
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--output',type=Path,help='Optional destination for JSON results.')
args=parser.parse_args()
if args.output:
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
