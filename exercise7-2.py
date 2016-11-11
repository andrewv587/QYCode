#!/usr/bin/python
import math

h=0.1
k=0.005
n=int((1-0)*1./h)+1
m=10
#u[i][j] maps true u[i+1][j]
u=[[None]*m for i in range(n-1)]
for i in range(n-1):
    u[i][0]=math.sin(math.pi*h*(i+1))

#explicit finite differ method
omega=k*1./h**2
omega2=1-2*omega
for j in range(0,m-1):
    for i in range(n-1):
        if i==0:
            u[i][j+1]=omega2*u[i][j]+omega*u[i+1][j]
        elif i==n-2:
            u[i][j+1]=omega2*u[i][j]+omega*u[i-1][j]
        else:
            u[i][j+1]=omega*u[i-1][j]+omega2*u[i][j]+omega*u[i+1][j]

#crank-nicolson method
import numpy as np
s=h**2*1.0/k
r=2+s
tri_matrix=np.zeros([n-1,m])

for i in range(n-1):
    if i==0:
        tri_matrix[i,i:i+2]=[r,-1]
    elif i==n-2:
        tri_matrix[i,i-1:i+1]=[-1,r]
    else:
        tri_matrix[i,i-1:i+2]=[-1,r,-1]
for j in range(0,m-1):
    right_side=np.array(u[:][j])
    left_side=np.linalg.solve(tri_matrix,right_side)
    u[:][j+1]=left_side.tolist()
    






