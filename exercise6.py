#!/usr/bin/python

n=4
a=[1]*n
b=a

sum_ab=0.
for i in range(n):
    for j in range(n):
        sum_ab+=a[i]*b[j]

print sum_ab

sum_aplusb=0.
for i in range(n):
    for j in range(n) :
        if(i==j):  continue
        sum_aplusb+=a[i]+b[j]
print sum_aplusb

import numpy as np
a = np.random.random_integers(100, 999, 100)
b = np.random.random_integers(100, 999, 100)
c = np.random.random_integers(100, 999, 100)
total = 0;
i = 0;
while i < 100:
    total = total + a[i] + b[i] * c[i];
    i = i + 1;
output = total;
print output

total=0
for i in range(100):
    total = total + a[i] + b[i] * c[i]
output = total
print output

def secant(func,dfunc,x0,n):
    i=0
    x=x0
    while i<n:
        temp=x-func(x)/dfunc(x)
        if(i<5):
            print i,x,func(x),dfunc(x),temp
        if(abs(temp-x)<1e-10):
            return temp
        i+=1
        x=temp

func=lambda x:x**5+2*x**3+5*x-8
dfunc=lambda x:5*x**4+6*x**2+5
print secant(func,dfunc,0.,100)
        

def secant_true(func,x0,x1,n):

    i=0
    tmp0=x0
    tmp1=x1
    print i,tmp0,func(tmp0)

    while i<n:
        i+=1 
        tmp=tmp1*1.-(tmp1-tmp0)/(func(tmp1)-func(tmp0))*func(tmp1) 
        print i,tmp1,func(tmp1),tmp
        if(abs(tmp-tmp1)<1e-10):
            return tmp
        tmp0=tmp1
        tmp1=tmp

print secant_true(func,0.5,1.5,100)


