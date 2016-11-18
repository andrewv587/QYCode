#!/usr/bin/python
import math
import numpy as np

S=50.
E=50.
r=0.10
T=5./12
singma=0.40
Smin=0
Smax=150

m=1000
n=100

h=(Smax-Smin)*1./n
k=T*1./m

vsT=max(E-S,0)

#v[i][j] maps true v[Smin+i*h][j*k]
v=[[None]*(m+1) for i in range(n+1)]


#initial conditions
for j in range(m+1):
    v[0][j]=E*math.exp(-r*(T-j*k))
    v[n][j]=0

for i in range(n+1):
    v[i][m]=vsT 

#explicit method
for j in range(m,0,-1):
    for i in range(1,n):
        Si=Smin+i*h
        prod1=k*singma**2/2.*(Si*1./h)**2
        prod2=k*r*Si/(2.*h)
        ai=prod1+prod2
        bi=1-2*prod1-k*r
        ci=prod1-prod2
        if i==1:
            v[i][j-1]=bi*v[i][j]+ai*v[i+1][j]+ci*v[i-1][j]
        elif i==n-1:
            v[i][j-1]=ci*v[i-1][j]+bi*v[i][j]+ai*v[i+1][j]
        else:
            v[i][j-1]=ci*v[i-1][j]+bi*v[i][j]+ai*v[i+1][j]


