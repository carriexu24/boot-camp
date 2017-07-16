import time
import numpy

#define Eliminate
def Eliminate(A, b):
    m = len(A[0])
    n = len(A)

    #A should be a square matrix
    if m != n:
        print "You should input a n*n A."
        return StandardError

    #for each column of A
    for i in range(m):

        #set the location of the pivot
        j = i

        #if the pivot == 0, then move to the next row
        while A[j][i] == 0:
            j += 1

            #if in every row the pivot == 0, return an error
            if j == n:
                print "This equation can't be solved."
                return StandardError

        #if the pivot has been moved, change the rows
        if j > i:
            myline = A[i]
            A[i] = A[j]
            A[j] = myline

        #calculate the scaler, and do eliminations
        for t in range(i+1, n):
            scaler = A[t][i] / A[i][i]
            for r in range(m):
                A[t][r] = A[t][r] - scaler * A[i][r]
            b[t] = b[t] - scaler * b[i]

    return (A, b)

#list of matrix size n
n = [100, 200, 300, 400, 500, 600]

#list of time using linalg.solve
timeL = []

#list of time using Eliminate.py
timeE = []

#for each size
for i in n:

    #build a n * n R(e)
    R = numpy.random.rand(i, i)

    #build w
    w = i * [1]

    #record the time using linalg.solve
    time1 = time.clock()
    x = numpy.linalg.solve(R, w)
    time2 = time.clock()
    timeL.append(time2 - time1)

    #record the time using Eliminate.py
    time3 = time.clock()
    Eliminate(R, w)
    time4 = time.clock()
    timeE.append(time4 - time3)

print timeL
print timeE




