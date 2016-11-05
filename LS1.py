#!/usr/bin/python
import numpy as np

x=np.array([1,2,3,4],dtype=float)
y=np.array([0,1,1,2],dtype=float)

assert(x.size==y.size)
n=x.size

sumx=x.sum()
sumy=y.sum()

x_bar=sumx/n
y_bar=sumy/n

a1=(n*np.sum(x*y)-sumx*sumy)/(n*np.sum(x*x)-sumx*sumx)
a0=y_bar-a1*x_bar

print "The straight line is y={0}+{1}*x".format(a0,a1)

