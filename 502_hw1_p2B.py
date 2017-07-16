import time
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

    return (A, b)

n = [100, 500, 1000, 5000, 10000]
timeL = []
timeE = []

for i in n:

    #build a n * n array R(e)
    R = numpy.random.rand(i, i)

    #build w
    w = i * [1]

    time1 = time.clock()
    x = numpy.linalg.solve(R, w)
    time2 = time.clock()
    timeL.append(time2 - time1)

    time3 = time.clock()
    Eliminate(R, w)
    time4 = time.clock()
    timeE.append(time4 - time3)

print timeL
print timeE




