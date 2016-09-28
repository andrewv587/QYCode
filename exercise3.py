#!/usr/bin/python

def function1_a(n,m):
    sumi=0
    for i in xrange(1,n+1):
        sumj=0
        for j in xrange(1,m+1):
            sumj+=j
        sumi+=i+sumj
    return sumi

def function1_b(n,m):
    sumi=1
    for i in xrange(1,n+1):
        podj=1
        for j in xrange(1,m+1):
            podj*=i+j
        sumi*=i+podj
    return sumi


def function1_c(n,m):
    sumi=0
    for i in xrange(1,n+1):
        podj=1
        for j in xrange(1,m+1):
            podj*=i+j
        sumi+=podj+i
    return sumi

import numpy as np
def function2(A,b,x0,k):
    """
    caculate x(k+1)=b-Ax(k)+x
    k:iteration number
    example: 
        A=np.array([[1,7,4],[5,2,8],[6,9,3]],dtype=float)
        b=np.array([32,58,63],dtype=float)
        x0=np.array([6.01,2.02,3.0],dtype=float)
    """
    x=x0
    for i in range(k):
        x=b-A.dot(x)+x
    return x

def function3(A,b,x0,k):
    x=x0
    for i in range(b.size):
        x[i]=(b[i]-A[i,:].dot(x))*1./A[i][i]+x[i]
    return x

def function4(A,b,x0,k,w):
    x=x0
    tmp=x0
    for i in range(b.size):
        tmp[i]=(b[i]-A[i,:].dot(x))*1./A[i][i]+x[i]
        x[i]=(1-w)*tmp[i]+w*x[i]
    return x
