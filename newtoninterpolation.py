#!/usr/bin/python

def newton_coef(x,y):
    assert(len(x)==len(y))
    n=len(x)
    a=y
    coef=[[0 for col in range(n+1)] for row in range(n)]
    for i in range(n):
        coef[i][0]=x[i]
        coef[i][1]=y[i]
    for j in range(1,n):
        for i in range(n-1,j-1,-1):
            a[i]=(a[i]-a[i-1])*1./(x[i]-x[i-j])
            coef[i-j][j+1]=a[i]
    print 'xi','f(xi)',[i for i in range(n)]
    for row in range(n):
        print [coef[row][col] for col in range(n+1-row)]
    return a

def newton_intrep(x,y,t):
    a=newton_coef(x,y)
    n=len(x)
    temp=a[n-1]
    for i in range(n-2,-1,-1):
        temp =temp*(t-x[i])+a[i]
    return temp

#x=[1,2,3,-4,5]
#y=[2,48,272,1182,2262]
x=[0,1,2,-1,3]
y=[-1,-1,-1,-7,5]

value=newton_intrep(x,y,-1)
print "polynomial value is:"
print value

