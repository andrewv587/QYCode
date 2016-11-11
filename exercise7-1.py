#!/usr/bin/python
import math

def increFuncByTaylor(x,t,h):
    et=math.exp(t)
    etx2=et*x**2
    dx=etx2+math.exp(3.0)
    xdxet=x*dx*et
    d2x=etx2+2*xdxet
    d3x=etx2+4*xdxet+2*dx**2*et+2*x*d2x*et
    d4x=etx2+6*xdxet+6*dx**2*et+6*dx*d2x*et+ \
            6*dx**2*et+6*x*d2x*et+2*x*d3x*et
    stepValue=x+h*dx+h**2/2.*d2x+h**3/6.*d3x+ \
            h**4/24.*d4x
    return stepValue

def increFuncByRunge(x,t,h,func):
    K1=func(t,x)
    K2=func(t+h/2.,x+1/2.*K1)
    K3=func(t+h/2.,x+1/2.*K2)
    K4=func(t+h,x+K3)
    stepValue=1/6.*h*(K1+2*K2+2*K3+K4)
    return stepValue



t0=2
x0=4
h=0.5
func=lambda t,x:math.exp(t)*x**2+math.exp(3.)

t=t0
x=x0
while t<5 :
    #x+=increFuncByTaylor(x,t,h)
    x+=increFuncByRunge(x,t,h,func)
    t+=h

print "the final t: ",t
print "the final value: ",x




