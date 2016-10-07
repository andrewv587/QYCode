#!/usr/bin/python
import numpy as np

def spine_interp(x,y,t):
    '''
    x: np.array(float) sorted
    y: np.array(float)
    t: float
    '''
    assert(x.size==y.size)
    n=x.size
    #construct tridiagon matrix and right hand side
    h=np.diff(x)
    dy=np.diff(y)
    tri_matrix=np.zeros([n,n])
    tri_matrix[0,0]=1
    tri_matrix[n-1,n-1]=1
    for j in range(0,n-2):
        tri_matrix[j+1,j:j+3]=[h[j],2*(h[j]+h[j+1]),h[j+1]]
    dyh=dy/h
    right_side=np.zeros(n)
    right_side[1:-1]=3*np.diff(dyh)
    #cacluate b
    b=np.linalg.solve(tri_matrix,right_side)
    #cacluate a and c
    a=np.diff(b)/(3*h)
    c=dyh-h/3*(2*b[0:-1]+b[1:])
    value = None
    #cacluate f(t)
    for i in range(n-1):
        if x[i]<=t and x[i+1]>=t:
            value=y[i]+c[i]*(t-x[i])+b[i]*(t-x[i])**2+ \
                a[i]*(t-x[i])**3
            return value


x=np.array([0,2,4,7,10,12],float)
y=np.array([20,20,12,7,6,6],float)
value=spine_interp(x,y,1.5)
print value


