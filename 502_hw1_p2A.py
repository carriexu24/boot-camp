import numpy

def Eliminate(A, b):
    m = len(A[0])
    n = len(A)

    if m > n:
        return StandardError

    for i in range(m):
        j = i
        while A[j][i] == 0:
            j += 1
            if j == n:
                print "This equation can't be solved."
                return StandardError

        if j > i:
            myline = A[i]
            A[i] = A[j]
            A[j] = myline

        for t in range(i+1, n):
            scaler = A[t][i] / A[i][i]
            for r in range(m):
                A[t][r] = A[t][r] - scaler * A[i][r]
            #print t
            #print A[t]
            b[t] = b[t] - scaler * b[i]

        print A
        print b

    return (A, b)

A = []
for i in range(10):
    myline = []
    for j in range(10):
        myline.append(10*i+j+1)
    A.append(myline)

#define array v
v = []
for i in range(10):
    v.append(i+1)

#define array b
b = 10*[1]

#build a 10 * 10 array R(e)
R = numpy.random.rand(10, 10)

A1 = [row[:] for row in A]
A2 = [row[:] for row in A]
v1 = v[:]
b1 = b[:]

print Eliminate(A1, b1)
print Eliminate(A2, v1)

