#/usr/bin/python

def diagonalSolver(A,b):
    """
    cacaluate Ax=b
    input:A diagonal square matrix
        b vector
    output:x=inv(A)*b
    usage:
        A=[[1,0,0],[0,2,0],[0,0,3]]
        b=[6,4,9]
        x=diagonalSolver(A,b)
        result x=[6.0,2.0,3.0]
    """
    n=len(A)
    assert(n==len(b))
    x=[None]*n
    for i in xrange(n):
        x[i] =  b[i]/(A[i][i]*1.0)
    return x

def upperTriSolver(A,b):
    """
    cacaluate Ax=b
    input:A upper triangular square matrix
        b vector
    output:x=inv(A)*b
    usage:
        A=[[1,4,6],[0,2,7],[0,0,3]]
        b=[32,25,9]
        x=upperTriSolver(A,b)
        result x=[6.0,2.0,3.0]
    """
    n=len(A)
    assert(n==len(b))
    x=[None]*n
    for i in xrange(n-1,-1,-1):
        tmp=b[i]
        for j in xrange(i+1,n):
            tmp=tmp-A[i][j]*x[j]
        x[i]=tmp/(A[i][i]*1.0)
    return x

def lowerTriSolver(A,b):
    """
    cacaluate Ax=b
    input:A lower triangular square matrix
        b vector
    output:x=inv(A)*b
    usage:
        A=[[1,0,0],[5,2,0],[6,9,3]]
        b=[6,34,63]
        x=lowerTriSolver(A,b)
        result x=[6.0,2.0,3.0]
    """
    n=len(A)
    assert(n==len(b))
    x=[None]*n
    for i in xrange(0,n):
        tmp=b[i]
        for j in xrange(0,i):
            tmp=tmp-A[i][j]*x[j]
        x[i]=tmp/(A[i][i]*1.0)
    return x

def matrixSolver(A,b):
    """
    cacaluate Ax=b
    input:A square matrix
        b vector
    caution: A must be full rank
        this function will change A,b
    output:x=inv(A)*b
    usage:
        A=[[1,7,4],[5,2,8],[6,9,3]]
        b=[32,58,63]
        x=matrixSolver(A,b)
        result x=[6.0,2.0,3.0]
    """
    n=len(A)
    assert(n==len(b))
    #make A become upper triangular matrix
    #by using forward elimination
    for i in xrange(0,n):
        #normalize first row
        factor=A[i][i]*1.0
        A[i][i:n]=[A[i][k]/factor for k in xrange(i,n)]
        b[i]=b[i]/factor
        for j in xrange(i+1,n):
            factor0=A[j][i]/A[i][i]
            A[j][i:n]=[A[j][k]/factor0-A[i][k] for k in xrange(i,n)]
            b[j]=b[j]/factor0-b[i]
    #solve Ax=b(A upper matrix)
    x=[None]*n
    for i in xrange(n-1,-1,-1):
        tmp=b[i]
        for j in xrange(i+1,n):
            tmp=tmp-A[i][j]*x[j]
        x[i]=tmp/(A[i][i]*1.0)
    return x


