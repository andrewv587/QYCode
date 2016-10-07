#!/usr/bin/python

def simpson_int(func,a,b,n):
    h=(b-a)*1./n
    integral=func(a)+func(b)
    for i in range(1,(n+2)/2):
        integral+=4*func(a+h*(2*i-1))
        if i==n/2:
            break
        integral+=2*func(a+h*2*i)
    return integral*h/3

func=lambda x:1-x-4*x**3+2*x**5
n=[4,6,100,1000,10000,1000000]
for i in n:
    value=simpson_int(func,-2,4,i)
    print i,value
