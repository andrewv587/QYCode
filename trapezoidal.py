#!/usr/bin/python
def trape_int(func,a,b,n):
    h=(b-a)*1./n
    integral=h/2*(func(a)+func(b))
    for i in range(1,n):
        integral+=h*func(a+h*i)
    return integral

func=lambda x:1-x-4*x**3+2*x**5
n=[2,4]
for i in n:
    value=trape_int(func,-2,4,i)
    print i,value
