#!/usr/bin/python
import numpy as np

x=np.array([-2,-1,0,1,2],dtype=float)
y=np.array([2,1,1,1,2],dtype=float)

assert(x.size==y.size)
n=x.size

x2=x*x
x3=x2*x
x4=x3*x

sumx=np.sum(x)
sumx2=np.sum(x2)
sumx3=np.sum(x3)
sumx4=np.sum(x4)

A=np.array([[n,sumx,sumx2],[sumx,sumx2,sumx3], \
        [sumx2,sumx3,sumx4]])

b=np.array([np.sum(y),np.sum(x*y),np.sum(x2*y)])


av=np.linalg.solve(A,b)

print "The straight line is y={0}+{1}*x+{2}" \
        .format(av[0],av[1],av[2])

