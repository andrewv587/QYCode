#!/usr/bin/python
import math

def richard_extra(func,x,n,h):
    d=[[None for col in range(n+1)] for row in range(n+1)]
    for i in range(0,n+1):
        d[i][0]=1./(2*h)*(func(x+h)-func(x-h))
        h/=2.
    for j in range(1,n+1):
        for i in range(j,n+1):
            d[i][j]=d[i][j-1]+1./(4**j-1)*(d[i][j-1]-d[i-1][j-1])
    #print d
    return d[n][n]


func=lambda x:math.cos(x)
x=math.pi/4
h=math.pi/3
n=3
value=richard_extra(func,x,n,h)
print value
