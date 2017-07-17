import time
import numpy

#define Eliminate
def Eliminate(A, b):
    m = len(A[0])
    n = len(A)

    #for each column of A
    for i in range(m):

        #if the pivot == 0, then return an error
        if A[i][i] == 0:
            print "A failure has happened."
            return StandardError

        #calculate the scaler, and do eliminations
        for t in range(i+1, n):
            scaler = A[t][i] / A[i][i]
            for r in range(m):
                A[t][r] = A[t][r] - scaler * A[i][r]
            b[t] = b[t] - scaler * b[i]

        #print the results of each elimination
        #when do Problem 2 B., these two operations should be ignored
        #print A
        #print b

    return (A, b)



#Problem 2 A.

#define A
A = []
for i in range(10):
    myline = []
    for j in range(10):
        myline.append(10*i+j+1)
    A.append(myline)

#define v
v = []
for i in range(10):
    v.append(i+1)

#define b
b = 10*[1]

#build a 10 * 10 R(e)
R = numpy.random.rand(10, 10)

#make copies
A1 = [row[:] for row in A]
A2 = [row[:] for row in A]
v1 = v[:]
b1 = b[:]

print Eliminate(A1, b1)
print Eliminate(A2, v1)


#Problem 2 B.

#list of matrix size n
#I make smaller n because my code is too slow
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




